import os
exec(open(os.path.join(os.path.dirname(__file__),'header.py')).read())
for directory in ['stl','plates','renders']:
 os.makedirs(os.path.join(OUT,directory),exist_ok=True)
centers=[(x,y) for x in [-43,43] for y in [-62,62]]
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
base=rounded('01_NEGRU_body_x1',X,Y,R,0,H)
boolean(base,rounded('cavity',X-4.8,Y-4.8,R-2.4,1.8,H+1))
# Four corner columns, attached to floor. They sit beyond the PSU ends.
for x,y in centers:
 boolean(base,cyl('closure tower',x,y,1.6,5.5,H-1.6),'UNION');bore(base,x,y,H-15,16)
# Demo bays. No fabricated PCB mounting-hole coordinates.
# Solid mechanical separator: not a certified electrical insulation barrier.
boolean(base,cube('converter divider',(18.5,0,14),(1.6,58,24.8)),'UNION')
# Flat platforms preserve five mm below component envelope; supports need actual PCB holes.
for x,y,w,l in [(-16.5,0,65,110),(36,0,30,50)]:
 boolean(base,cube('demo platform',(x,y,2.4),(w,l,1.6)),'UNION')
# Opposed cable ports, 12.6 mm teardrop; input and output are single holes.
for side in [-1,1]:
 r=6.3;poly=[(r*math.cos(math.radians(a)),22+r*math.sin(math.radians(a))) for a in [135+i*270/48 for i in range(49)]]+[(0,22+r*math.sqrt(2))]
 boolean(base,prism_y('port',poly,min(side*76,side*82),max(side*76,side*82)))
 boolean(base,cube('cable saddle',(0,side*72.2,8.8),(14,9,14.4)),'UNION') # top16
 for x in [-11,11]:
  boolean(base,cyl('clamp tower',x,side*72.2,1.6,4.5,14.4),'UNION');bore(base,x,side*72.2,2.4,15)
# Cap prints exterior face on bed, skirt growing upward. Solid weather-facing face.
lid=rounded('02_VERDE_solar_cap_x1',X+4,Y+4,R+2,0,2.8)
skirt=rounded('cap skirt',X+4,Y+4,R+2,2.6,5.2)
boolean(skirt,rounded('skirt cavity',X+.8,Y+.8,R+.4,2.4,6))
boolean(lid,skirt,'UNION')
# Sun motif engraved 0.4 mm, 1.2 mm-wide short bridging roofs.
ring=cyl('sun ring',0,0,-.1,13,0.5,96)
boolean(ring,cyl('ring core',0,0,-.2,11.8,.8,96));boolean(lid,ring)
for i in range(32):
 a=2*math.pi*i/32
 end=min(49/max(abs(math.cos(a)),.01),64/max(abs(math.sin(a)),.01))
 pts=[(r*math.cos(a+delta),r*math.sin(a+delta)) for r,delta in [(17,-.022),(end,-.009),(end,.009),(17,.022)]]
 q=prism_z('sun ray',pts,.5);q.location.z=-.1;boolean(lid,q)
for x,y in centers:
 boolean(lid,cyl('closure shaft',x,y,-1,3.4,6));boolean(lid,cyl('recess',x,y,-.1,5.3,2.1))
closure=screw('03_VERDE_closure_x4',14)
clamp=rounded('04_VERDE_cable_clamp_x2',34,8.8,3,0,3)
for x in [-11,11]:boolean(clamp,cyl('clearance',x,0,-1,3.5,6))
for y in [-2.8,0,2.8]:
 q=cyl('rounded ridge',0,0,-6,1.2,12);q.rotation_euler[1]=math.pi/2;q.location=(0,y,2.1);boolean(clamp,q,'UNION')
clampscrew=screw('05_NEGRU_clamp_screw_x4',22)
parts=[base,lid,closure,clamp,clampscrew]
report={}
for o in parts:
 bm=bmesh.new();bm.from_mesh(o.data);bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=.00001);bmesh.ops.triangulate(bm,faces=list(bm.faces));bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bad=sum(not e.is_manifold for e in bm.edges);assert not bad,(o.name,bad);report[o.name]={'nonmanifold_edges':bad,'volume_mm3':abs(bm.calc_volume())};bm.to_mesh(o.data);bm.free()
json.dump(report,open(os.path.join(OUT,'mesh_checks.json'),'w'),indent=2)
exec(open(os.path.join(os.path.dirname(__file__),'export.py')).read())
