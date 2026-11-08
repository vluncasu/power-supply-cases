import bpy, math, json, os, struct, bmesh, zipfile
from mathutils import Vector
from xml.etree.ElementTree import Element, SubElement, tostring
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'final')
p=json.load(open(os.path.join(ROOT,'source/parameters_v2.json')))
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
X,Y,R,W,H,LH=[p[k] for k in ['outer_x','outer_y','corner_radius','wall','base_height','lid_height']]
centers=[(sx*(X/2-11),sy*(Y/2-11)) for sx in [-1,1] for sy in [-1,1]]
def mesh(name,verts,faces):
 m=bpy.data.meshes.new(name); m.from_pydata(verts,[],faces); m.update(); o=bpy.data.objects.new(name,m); bpy.context.collection.objects.link(o)
 bm=bmesh.new(); bm.from_mesh(m); bmesh.ops.recalc_face_normals(bm,faces=bm.faces); bm.to_mesh(m); bm.free(); return o
def rounded(name,x,y,r,z,h):
 pts=[]
 for cx,cy,start in [(x/2-r,y/2-r,0),(-x/2+r,y/2-r,90),(-x/2+r,-y/2+r,180),(x/2-r,-y/2+r,270)]:
  for i in range(17):
   a=math.radians(start+i*90/16); pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
 n=len(pts); v=[(a,b,z+c) for c in [0,h] for a,b in pts]
 return mesh(name,v,[tuple(reversed(range(n))),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)])
def cube(name,loc,dim):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=name; o.dimensions=dim; bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); return o
def cyl(name,x,y,z,r,h,n=64):
 bpy.ops.mesh.primitive_cylinder_add(vertices=n,radius=r,depth=h,location=(x,y,z+h/2)); o=bpy.context.object;o.name=name;return o
def boolean(o,c,op='DIFFERENCE'):
 bpy.context.view_layer.objects.active=o; mod=o.modifiers.new('precision','BOOLEAN'); mod.operation=op; mod.solver='EXACT'; mod.object=c; bpy.ops.object.modifier_apply(modifier=mod.name); bpy.data.objects.remove(c,do_unlink=True)
def thread(name,x,y,z,height,clearance=0):
 # Trapezoidal custom printed thread. Flanks: 0.8 mm radial over 0.9 mm axial.
 N=80; nz=math.ceil(height/0.15); pitch=p['screw_pitch'];depth=p['thread_depth'];vs=[]
 for j in range(nz+1):
  zz=height*j/nz
  for i in range(N):
   a=2*math.pi*i/N; t=(zz-pitch*a/(2*math.pi))%pitch
   d=abs(t-pitch/2); f=max(0,min(1,(1.2-d)/0.9))
   rr=5-depth+depth*f+clearance
   vs.append((x+rr*math.cos(a),y+rr*math.sin(a),z+zz))
 fs=[tuple(reversed(range(N))),tuple(nz*N+i for i in range(N))]
 fs += [(j*N+i,j*N+(i+1)%N,(j+1)*N+(i+1)%N,(j+1)*N+i) for j in range(nz) for i in range(N)]
 return mesh(name,vs,fs)
def cablecut(o,zc):
 for x in p['cable_x']:
  c=cyl('cable bore',0,0,-W-2,(p['cable_diameter']/2+p['cable_clearance_radial']),2*W+4)
  c.rotation_euler[0]=math.pi/2; c.location=Vector((x,Y/2-W/2,zc)); boolean(o,c)
def vent(x,y,z,width=3,height=20):
 # Vertical slot with 45-degree closing roof.
 poly=[(x-width/2,z),(x+width/2,z),(x+width/2,z+height-width/2),(x,z+height),(x-width/2,z+height-width/2)]
 vs=[(a,y+d,b) for d in [-5,5] for a,b in poly];n=5
 return mesh('roofed ventilation',vs,[tuple(reversed(range(n))),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)])
