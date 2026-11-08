import os
exec(open(os.path.join(os.path.dirname(__file__),'header.py')).read())
for directory in ['stl','plates','renders']:
 os.makedirs(os.path.join(OUT,directory),exist_ok=True)
for folder in ['stl','plates','renders']:os.makedirs(os.path.join(OUT,folder),exist_ok=True)
mounts=[(x-81.5,66-y) for x,y in p['pcb_mount_holes']]
def custom_thread(name,r,pitch,depth,height,z=0,clearance=0):
 N=64;layers=math.ceil(height/.1);vs=[];fs=[]
 for j in range(layers+1):
  zz=height*j/layers
  for i in range(N):
   a=2*math.pi*i/N;t=(zz-pitch*a/(2*math.pi))%pitch
   f=max(0,min(1,(pitch*.45-abs(t-pitch/2))/(pitch*.32)))
   rr=r-depth+depth*f+clearance;vs.append((rr*math.cos(a),rr*math.sin(a),zz+z))
 fs=[tuple(reversed(range(N))),tuple(layers*N+i for i in range(N))]+[(j*N+i,j*N+(i+1)%N,(j+1)*N+(i+1)%N,(j+1)*N+i) for j in range(layers) for i in range(N)]
 return mesh(name,vs,fs)
print('BUILD BASE',flush=True)
base=rounded('01 SLIM BASE',X,Y,R,0,H)
cav=rounded('cavity',X-2*W,Y-2*W,R-W,W,H+2)
for x,y in centers:boolean(cav,cyl('closure column',x,y,1,6.4,H+3))
boolean(base,cav)
for x,y in centers:tapped(base,x,y,H-12,12)
# Universal XY shoes. Square guides provide +/-2.2 mm movement.
for x,y in mounts:
 q=rounded('mount clearance',10.6,10.6,1.8,-1,6);q.location.x=x;q.location.y=y;boolean(base,q)
 for sx in [-1,1]:boolean(base,cube('shoe guide',(x+sx*10.8,y,2.9),(1.2,22.8,1.4)),'UNION')
 for sy in [-1,1]:boolean(base,cube('shoe guide',(x,y+sy*10.8,2.9),(20.8,1.2,1.4)),'UNION')
# Low inlet and high outlet windows, opaque baffles with five mm upper air gap.
for side in [-1,1]:
 for y in range(-45,46,9):
  for row,z in enumerate([6.0,27.4]):
   width=2.8;height=12.6;lean=3.2 if row==0 else -3.2
   poly=[(y,z),(y-width/2,z+width/2),(y+lean-width/2,z+height-width/2),(y+lean,z+height),(y+lean+width/2,z+height-width/2),(y+width/2,z+width/2)]
   q=prism_y('chevron ventilation',poly,side*X/2-5,side*X/2+5);q.rotation_euler[2]=math.pi/2;boolean(base,q)
 boolean(base,cube('opaque baffle',(side*89.8,0,21.5),(1.2,104,38.6)),'UNION') # top40.8
 for y in [-52,52]:boolean(base,cube('baffle return',(side*91.8,y,21.5),(5.2,1.2,38.6)),'UNION')
# Teardrop holes avoid horizontal ceilings, two ports on each opposite face.
for side in [-1,1]:
 for x in p['cable_x']:
  r=(p['cable_diameter']+.6)/2;poly=[(x+r*math.cos(math.radians(a)),31+r*math.sin(math.radians(a))) for a in [135+i*270/48 for i in range(49)]]+[(x,31+r*math.sqrt(2))]
  boolean(base,prism_y('cable port',poly,min(side*(Y/2-5),side*(Y/2+2)),max(side*(Y/2-5),side*(Y/2+2))))
# Subtle long flutes on the cable faces stop below the ports.
for side in [-1,1]:
 for x in range(-76,77,8):
  q=prism_y('flute',[(x-.6,5),(x+.6,5),(x+.6,23),(x,23.6),(x-.6,23)],min(side*(Y/2-.35),side*(Y/2+1)),max(side*(Y/2-.35),side*(Y/2+1)))
  boolean(base,q)
print('BUILD SLIMED LID',flush=True)
# Hollow-free 45-degree saddle braces and deep threaded cable-clamp posts.
for side in [-1,1]:
 q=prism_y('cable saddle',[(68,25),(80.8,25),(80.8,12.2)],-7,7)
 q.rotation_euler[2]=math.pi/2
 if side<0:q.rotation_euler[2]=-math.pi/2
 boolean(base,q,'UNION')
 for x in [-11,11]:
  boolean(base,cyl('clamp post',x,side*73,2.2,4.5,22.6),'UNION')
  q=custom_thread('clamp post thread',3,1.2,.3,17.2,8,.20);q.location.x=x;q.location.y=side*73;boolean(base,q)
  boolean(base,cyl('clamp lead in',x,side*73,24.2,3.3,1.2))
# Four interior floor pockets retain a full-thickness central cross and mounting margins.
for x in [-27.5,27.5]:
 for y in [-30,30]:
  q=rounded('weight relief',53,58,3,1.6,1.0);q.location.x=x;q.location.y=y;boolean(base,q)
lid=rounded('02 SLIM LID exterior up',X,Y,R,0,1.6)
# Continuous architectural rim integrates the flush screw pockets into the lid.
frame=rounded('raised perimeter',X,Y,R,1.4,1.6)
boolean(frame,rounded('open central panel',178,128,5,1.3,2.0))
boolean(lid,frame,'UNION')
# 20 solid hyperbolic surface tiles: 1.2 mm physical relief, smooth curved saddle.
for col in range(5):
 for row in range(4):
  n=16;size=27.2;x0=-71+col*28.7;y0=-56.65+row*28.7;vs=[];fs=[]
  for j in range(n+1):
   for i in range(n+1):
    u=i/n;v=j/n
    if (row+col)%2:u=1-u
    # smooth curved transition through cubic ease; rotated saddle pattern.
    a=u*u*(3-2*u);b=v*v*(3-2*v);h=1.2*(a+b-2*a*b)
    vs.append((x0+size*i/n,y0+size*j/n,1.6+h))
  for j in range(n):
   for i in range(n):
    a=j*(n+1)+i;fs.append((a,a+1,a+n+2,a+n+1))
  boundary=list(range(n+1))+[j*(n+1)+n for j in range(1,n+1)]+[n*(n+1)+i for i in range(n-1,-1,-1)]+[j*(n+1) for j in range(n-1,0,-1)]
  off=len(vs)
  vs.extend([(vs[i][0],vs[i][1],1.4) for i in boundary])
  fs.append(tuple(reversed([off+i for i in range(len(boundary))])))
  for k,a in enumerate(boundary):fs.append((a,off+k,off+(k+1)%len(boundary),boundary[(k+1)%len(boundary)]))
  boolean(lid,mesh('slimed tile',vs,fs),'UNION')
for x,y in centers:
 boolean(lid,cyl('recess island',x,y,1.6,8.6,1.4),'UNION')
 boolean(lid,cyl('shaft hole',x,y,-1,5.6,10))
 boolean(lid,cyl('head pocket',x,y,1.6,7.4,5))
 bpy.ops.mesh.primitive_cone_add(vertices=64,radius1=5.4,radius2=7.4,depth=2.0,location=(x,y,.6));boolean(lid,bpy.context.object)
closure=cyl('03 CLOSURE SCREW x4',0,0,0,7,1.2)
bpy.ops.mesh.primitive_cone_add(vertices=64,radius1=7,radius2=5,depth=2.2,location=(0,0,2.1));boolean(closure,bpy.context.object,'UNION')
boolean(closure,th('closure thread',0,0,3.0,10.0),'UNION');boolean(closure,cube('driver slot',(0,0,-.1),(10,2,1.4)))
print('BUILD ADJUSTABLE MOUNTS',flush=True)
shoe=cube('04 XY MOUNT x4',(0,0,.7),(16,16,1.4))
boolean(shoe,cyl('PCB support',0,0,1.2,4.5,2.2),'UNION') # PCB plane at local3.4/global5.8
boolean(shoe,custom_thread('PCB stud T3.2',1.6,1.2,.3,6.2,3.2),'UNION')
boolean(shoe,custom_thread('bottom lock bore',3,1.2,.3,2.6,-.1,.20))
boolean(shoe,cyl('thread entrance',0,0,-1,3.3,1.2))
lock=cyl('05 MOUNT LOCK FOOT x4',0,0,0,11,1.2,64)
boolean(lock,custom_thread('T6 lock stem',3,1.2,.3,4.8,1.0),'UNION');boolean(lock,cube('lock driver slot',(0,0,-.1),(10,2,1.4)))
nut=cyl('06 PCB NUT x4',0,0,0,4.4,2.8,6)
boolean(nut,custom_thread('PCB internal T3.2',1.6,1.2,.3,4,-.6,.18))
# Internal entry chamfer within a 0.4 mm single-layer increment.
boolean(nut,cyl('nut entry',0,0,-1,1.9,1.3))
clamp=rounded('07 CABLE CLAMP x2 print flat side down',34,10,3,0,3)
for x in [-11,11]:boolean(clamp,cyl('clamp hole',x,0,-1,3.5,6))
# Broad rounded ribs: 1.2 mm radius, 0.3 mm above the clamp face.
for y in [-3,0,3]:
 q=cyl('rounded grip ridge',0,0,-6,1.2,12)
 q.rotation_euler[1]=math.pi/2;q.location=(0,y,2.1)
 boolean(clamp,q,'UNION')
clampscrew=cyl('08 CABLE CLAMP SCREW x4',0,0,0,5.5,2,64)
boolean(clampscrew,custom_thread('clamp screw thread',3,1.2,.3,21.6,1.8),'UNION')
boolean(clampscrew,cube('clamp screw drive',(0,0,-.1),(7,1.8,2.0)))
parts=[base,lid,closure,shoe,lock,nut,clamp,clampscrew];report={}
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT,'checkpoint.blend'))
for o in parts:
 bm=bmesh.new();bm.from_mesh(o.data)
 print(o.name,'initial',sum(not e.is_manifold for e in bm.edges),flush=True)
 bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=.00001)
 bmesh.ops.dissolve_degenerate(bm,edges=list(bm.edges),dist=.00001)
 boundary=[e for e in bm.edges if e.is_boundary]
 if boundary:bmesh.ops.holes_fill(bm,edges=boundary,sides=12)
 bmesh.ops.triangulate(bm,faces=list(bm.faces));bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces))
 bad=sum(not e.is_manifold for e in bm.edges)
 report[o.name]={'nonmanifold_edges':bad,'volume_mm3':round(abs(bm.calc_volume()),2)}
 print(o.name,'final',bad,flush=True)
 assert bad==0,(o.name,bad)
 bm.to_mesh(o.data);bm.free();o.data.update()
json.dump(report,open(os.path.join(OUT,'mesh_checks.json'),'w'),indent=2)
exec(open(os.path.join(os.path.dirname(__file__),'export.py')).read())
