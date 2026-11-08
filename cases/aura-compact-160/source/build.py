import os
exec(open(os.path.join(os.path.dirname(__file__),'header.py')).read())
for directory in ['stl','plates','renders']:
 os.makedirs(os.path.join(OUT,directory),exist_ok=True)
centers=[(x,y) for x in [-44,44] for y in [-64,64]]
def ct(name,height,z=0,clearance=0):
 N=48;nz=math.ceil(height/.12);vs=[];pitch=1.6;depth=.45
 for j in range(nz+1):
  zz=height*j/nz
  for i in range(N):
   a=2*math.pi*i/N;t=(zz-pitch*a/(2*math.pi))%pitch;f=max(0,min(1,(pitch*.46-abs(t-pitch/2))/(pitch*.34)));r=3-depth+depth*f+clearance
   vs.append((r*math.cos(a),r*math.sin(a),z+zz))
 fs=[tuple(reversed(range(N))),tuple(nz*N+i for i in range(N))]+[(j*N+i,j*N+(i+1)%N,(j+1)*N+(i+1)%N,(j+1)*N+i) for j in range(nz) for i in range(N)]
 return mesh(name,vs,fs)
def bore(o,x,y,z,h):
 q=ct('tap',h,z,.25);q.location.x=x;q.location.y=y;boolean(o,q)
def screw(name,length):
 q=cyl(name,0,0,0,5,2);boolean(q,ct('stem',length,1.8),'UNION');boolean(q,cube('slot',(0,0,0),(7,1.6,1.4)));return q
base=rounded('01_BLACK_body_x1',X,Y,R,0,H)
boolean(base,rounded('cavity',X-4.8,Y-4.8,R-2.4,1.8,H+1))
# Four corner columns, attached to floor. They sit beyond the PSU ends.
for x,y in centers:
 boolean(base,cyl('closure tower',x,y,1.6,5.5,H-1.6),'UNION');bore(base,x,y,H-15,16)
# Metal housing rests on four pads. Stops capture its 58.02 x 86 envelope.
for x in [-46,46]:
 for y in [-53,49]:
  boolean(base,cube('support',(x,y,2.3),(8,8,1.4)),'UNION')
for side in [-1,1]:
 for y in [-49,45]:boolean(base,cube('lateral stop',(side*52.4,y,4.5),(2,9,5.8)),'UNION')
 for x in [-45,45]:boolean(base,cube('end stop',(x,-2+side*57.4,4.5),(10,2,5.8)),'UNION')
# Leaf-like slanted side intakes, 45-degree roofs; upper exits are in lid.
for side in [-1,1]:
 for y in range(-48,49,8):
  poly=[(y-1.4,7),(y+1.4,7),(y+5.4,21.6),(y+4,23),(y+2.6,21.6)]
  q=prism_y('leaf vent',poly,side*X/2-4,side*X/2+4);q.rotation_euler[2]=math.pi/2;boolean(base,q)
# Opposed cable ports, 12.6 mm teardrop; input and output are single holes.
for side in [-1,1]:
 r=6.3;poly=[(r*math.cos(math.radians(a)),22+r*math.sin(math.radians(a))) for a in [135+i*270/48 for i in range(49)]]+[(0,22+r*math.sqrt(2))]
 boolean(base,prism_y('port',poly,min(side*76,side*82),max(side*76,side*82)))
 boolean(base,cube('cable saddle',(0,side*72.2,8.8),(14,9,14.4)),'UNION') # top16
 for x in [-11,11]:
  boolean(base,cyl('clamp tower',x,side*72.2,1.6,4.5,14.4),'UNION');bore(base,x,side*72.2,2.4,15)
# DC routing guide along one side, does not cross metal envelope.
for y in [-23,0,23]:
 boolean(base,cube('routing guide',(53.8,y-2,4),(1.2,3,4.8)),'UNION')
# Lid prints outside face on bed. All locator/retention features grow upward.
lid=rounded('02_WHITE_wave_lid_x1',X,Y,R,0,2.8)
# flowing narrow apertures: serpentine field, length follows a leaf envelope.
for col in range(-6,7):
 x0=col*6.8;length=105-abs(col)*4;pts=[]
 for i in range(41):
  y=-length/2+length*i/40;x=x0+2.1*math.sin(y/15+col*.35);pts.append((x,y))
 poly=[(x-1.15,y) for x,y in pts]+[(x+1.15,y) for x,y in reversed(pts)]
 q=prism_z('wave aperture',poly,5);q.location.z=-1;boolean(lid,q)
# Top shadow grooves at both ends, 0.6 deep, short bridges only.
for sy in [-1,1]:
 for j in range(3):
  q=rounded('end flute',37-j*7,1.2,.6,-.1,.7);q.location.y=sy*(61+j*4);boolean(lid,q)
for x,y in centers:
 boolean(lid,cyl('shaft',x,y,-1,3.4,6));boolean(lid,cyl('recess',x,y,-.1,5.3,2.1))
# Two adjustable metal-housing hold-down screws, independent of guessed mounting holes.
for x in [-48,48]:
 boolean(lid,cyl('hold down boss',x,2,2.6,6.5,4.8),'UNION');bore(lid,x,2,-.2,7.8);boolean(lid,cyl('adjuster head recess',x,2,-.1,5.3,4.2))
# locator tabs outside metal housing
for x in [-58,58]:
 for y in [-26,26]:boolean(lid,cube('locator',(x,y,4.3),(1.2,8,3.4)),'UNION')
closure=screw('03_WHITE_closure_x4',14)
clamp=rounded('04_WHITE_cable_clamp_x2',34,8.8,3,0,3)
for x in [-11,11]:boolean(clamp,cyl('clearance',x,0,-1,3.5,6))
for y in [-2.8,0,2.8]:
 q=cyl('rounded ridge',0,0,-6,1.2,12);q.rotation_euler[1]=math.pi/2;q.location=(0,y,2.1);boolean(clamp,q,'UNION')
clampscrew=screw('05_BLACK_clamp_screw_x4',21)
pressure=screw("06_WHITE_housing_pressure_x2",8)
parts=[base,lid,closure,clamp,clampscrew,pressure]
report={}
for o in parts:
 bm=bmesh.new();bm.from_mesh(o.data);bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=.00001);bmesh.ops.triangulate(bm,faces=list(bm.faces));bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bad=sum(not e.is_manifold for e in bm.edges);assert not bad,(o.name,bad);report[o.name]={'nonmanifold_edges':bad,'volume_mm3':abs(bm.calc_volume())};bm.to_mesh(o.data);bm.free()
json.dump(report,open(os.path.join(OUT,'mesh_checks.json'),'w'),indent=2)
exec(open(os.path.join(os.path.dirname(__file__),'export.py')).read())
