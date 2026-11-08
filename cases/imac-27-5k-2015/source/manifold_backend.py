# Robust CSG backend used with Blender 4.2's bundled Python.
import sys
sys.path.insert(0,os.path.join(ROOT,'source','vendor'))
import manifold3d as mf
import numpy as np
from mathutils import Matrix
_csg_cache={}
_csg_id=0

def as_manifold(o):
 global _csg_id
 bpy.context.view_layer.update()
 matrix=tuple(v for row in o.matrix_world for v in row)
 key=o.get('_csg_id')
 if key in _csg_cache and _csg_cache[key][2]!=o.as_pointer():key=None
 if key in _csg_cache and _csg_cache[key][0]==matrix:return _csg_cache[key][1]
 me=o.data;me.calc_loop_triangles()
 vs=np.empty(len(me.vertices)*3,dtype=np.float32);me.vertices.foreach_get('co',vs);vs=vs.reshape((-1,3))
 mm=np.array(o.matrix_world,dtype=np.float32);vs=vs@mm[:3,:3].T+mm[:3,3]
 fs=np.empty(len(me.loop_triangles)*3,dtype=np.int32);me.loop_triangles.foreach_get('vertices',fs);fs=fs.reshape((-1,3)).astype(np.uint32)
 m=mf.Manifold(mf.Mesh(np.ascontiguousarray(vs),np.ascontiguousarray(fs)))
 assert str(m.status())=='Error.NoError',(o.name,m.status())
 if key is None:_csg_id+=1;key=_csg_id;o['_csg_id']=key
 _csg_cache[key]=(matrix,m,o.as_pointer());return m

def boolean(o,c,op='DIFFERENCE'):
 a=as_manifold(o);b=as_manifold(c)
 result=a-b if op=='DIFFERENCE' else a+b if op=='UNION' else a^b
 assert str(result.status())=='Error.NoError',(o.name,result.status())
 out=result.to_mesh();new=bpy.data.meshes.new(o.name+' solid');new.from_pydata(out.vert_properties[:,:3].tolist(),[],out.tri_verts.tolist());new.update();old=o.data;o.data=new;o.matrix_world=Matrix.Identity(4)
 if old.users==0:bpy.data.meshes.remove(old)
 bpy.context.view_layer.update();matrix=tuple(v for row in o.matrix_world for v in row);_csg_cache[o['_csg_id']]=(matrix,result,o.as_pointer())
 ck=c.get('_csg_id');_csg_cache.pop(ck,None);bpy.data.objects.remove(c,do_unlink=True)
