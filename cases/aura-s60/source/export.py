def triangles(o):
 me=o.data.copy();me.transform(o.matrix_world);me.calc_loop_triangles();v=[tuple(q.co) for q in me.vertices];f=[tuple(t.vertices) for t in me.loop_triangles];bpy.data.meshes.remove(me);return v,f

def save_stl(o,path):
 v,fs=triangles(o)
 with open(path,'wb') as f:
  f.write(b'ARC 300 V2 adjustable mechanical design'.ljust(80,b' '));f.write(struct.pack('<I',len(fs)))
  for face in fs:
   a,b,c=[Vector(v[i]) for i in face];n=(b-a).cross(c-a).normalized();f.write(struct.pack('<12fH',*n,*a,*b,*c,0))
for o in parts:save_stl(o,os.path.join(OUT,'stl',o.name.replace(' ','_')+'.stl'))

def three_mf(filename,items):
 ns='http://schemas.microsoft.com/3dmanufacturing/core/2015/02';root=Element('model',{'unit':'millimeter','xml:lang':'en-US','xmlns':ns});res=SubElement(root,'resources');build=SubElement(root,'build')
 for k,(o,px,py) in enumerate(items,1):
  v,fs=triangles(o);obj=SubElement(res,'object',{'id':str(k),'type':'model','name':o.name});m=SubElement(obj,'mesh');vv=SubElement(m,'vertices');tt=SubElement(m,'triangles')
  for a in v:SubElement(vv,'vertex',dict(zip(['x','y','z'],[str(a[0]+px),str(a[1]+py),str(a[2])])))
  for f in fs:SubElement(tt,'triangle',dict(zip(['v1','v2','v3'],map(str,f))))
  SubElement(build,'item',{'objectid':str(k)})
 with zipfile.ZipFile(os.path.join(OUT,'plates',filename),'w',zipfile.ZIP_DEFLATED) as z:
  z.writestr('[Content_Types].xml','<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
  z.writestr('_rels/.rels','<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Target="/3D/3dmodel.model" Id="rel0" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
  z.writestr('3D/3dmodel.model',tostring(root,encoding='utf-8',xml_declaration=True))
