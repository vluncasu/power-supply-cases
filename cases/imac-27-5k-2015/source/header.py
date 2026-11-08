import os
exec(open(os.path.join(os.path.dirname(__file__),'cad_utils.py')).read())
exec(open(os.path.join(os.path.dirname(__file__),'manifold_backend.py')).read())
centers=[(sx*48,sy*74) for sx in [-1,1] for sy in [-1,1]]
def th(name,x,y,z,height,radius=5,clearance=0):
 N=64;nz=math.ceil(height/.18);pitch=3;depth=.8;vs=[]
 for j in range(nz+1):
  zz=height*j/nz
  for i in range(N):
   a=2*math.pi*i/N;t=(zz-pitch*a/(2*math.pi))%pitch;f=max(0,min(1,(1.2-abs(t-1.5))/.9));rr=radius-depth+depth*f+clearance
   vs.append((x+rr*math.cos(a),y+rr*math.sin(a),z+zz))
 fs=[tuple(reversed(range(N))),tuple(nz*N+i for i in range(N))]+[(j*N+i,j*N+(i+1)%N,(j+1)*N+(i+1)%N,(j+1)*N+i) for j in range(nz) for i in range(N)]
 return mesh(name,vs,fs)
def tapped(o,x,y,z,h,r=5):
 boolean(o,th('thread bore',x,y,z,h+.8,r,.35))
 boolean(o,cyl('lead in',x,y,z+h-1.4,r+.4,2.4))
def bolt(name,length):
 o=cyl(name,0,0,0,8.5,4,6);boolean(o,th('printed thread',0,0,3.8,length+.2),'UNION');return o

def prism_y(name,poly,ya,yb):
 n=len(poly);vs=[(x,y,z) for y in [ya,yb] for x,z in poly]
 return mesh(name,vs,[tuple(reversed(range(n))),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)])
def prism_z(name,poly,height):
 n=len(poly);vs=[(x,y,z) for z in [0,height] for x,y in poly]
 return mesh(name,vs,[tuple(reversed(range(n))),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)])
def slotted(o,x,y,z,h,length=20):
 c=rounded('slot',11.2,length+11.2,5.6,z,h);c.location.x=x;c.location.y=y;boolean(o,c)
def half(o,name,side):
 q=o.copy();q.data=o.data.copy();bpy.context.collection.objects.link(q);q.name=name
 boolean(q,cube('split plane',(side*50.05,0,30),(100,150,100)),'INTERSECT');return q

def mark(stage):print(stage,flush=True)
