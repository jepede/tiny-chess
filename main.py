import json,os,sys,urllib.error,urllib.request
ENV_URL=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("MAKEFUN_ENV_URL is not set")
def post(path,body):
 req=urllib.request.Request(ENV_URL+path,data=json.dumps(body).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(req) as res:
   return json.load(res)
 except urllib.error.HTTPError as e:
  sys.exit(f"{path}:HTTP {e.code} {e.read().decode(errors='replace')}")
V=(0,100,356,359,500,962,20000)
D=((),(-10,),(-21,-19,-12,-8,8,12,19,21),(-11,-9,9,11),(-10,-1,1,10),(-11,-10,-9,-1,1,9,10,11),(-11,-10,-9,-1,1,9,10,11))
def F(f):
 f=f.split();b=[99]*120;i=21
 for x in f[0]:
  if x=='/':i+=2
  elif x.isdigit():
   for _ in range(int(x)):b[i]=0;i+=1
  else:b[i]=' PNBRQK'.index(x.upper())*(1 if x.isupper() else -1);i+=1
 c={i for x,i in zip('KQkq',(98,91,28,21)) if x in f[2]}
 e=f[3];e=0 if e=='-' else ord(e[0])+4-10*int(e[1])
 p=b,c,e
 return R(p) if f[1]=='b' else p
def R(p):
 b,c,e=p
 return [-x for x in b[::-1]],{119-x for x in c},119-e if e else 0
def A(b,k,s=1):
 for p in range(1,7):
  for d in D[p] if p!=1 else (-10*s-1,-10*s+1):
   j=k+d
   while abs(b[j])!=99:
    if b[j]:
     if b[j]==-p*s:return True
     break
    if p in (1,2,6):break
    j+=d
 return False
def G(p,q=0):
 b,c,e=p
 for i,v in enumerate(b):
  if not 0<v<7:continue
  if v==1:
   for j in (i-10,i-20,i-11,i-9):
    if j==i-10 and b[j]==0 or j==i-20 and i>80 and b[i-10]==b[j]==0 or j in (i-11,i-9) and (-7<b[j]<0 or j==e):
     for u in (2,3,4,5) if j<30 else (0,):yield i,j,u
  else:
   for d in D[v]:
    j=i+d
    while abs(b[j])!=99 and b[j]<=0:
     if b[j] or not q:yield i,j,0
     if b[j] or v in (2,6):break
     j+=d
   if v==6 and not q and c&{91,98} and not A(b,i):
    for r in (91,98):
     d=1 if r>i else -1
     if r in c and b[r]==4 and not any(b[i+d:r:d]) and not A(b,i+d):yield i,i+2*d,0
def M(p,m):
 b,c,e=p;i,j,u=m;b=b[:];v=b[i];b[j]=u or v;b[i]=0;c=c-{i,j}
 if v==6:
  c=c-{91,98}
  if abs(i-j)==2:
   r=91 if j<i else 98;b[(i+j)//2]=b[r];b[r]=0
 if v==1 and j==e:b[j+10]=0
 return R((b,c,i-10 if v==1 and i-j==20 else 0))
def E(b):
 z=0;ph=sum(abs(x) in (4,5) for x in b)
 for i,p in enumerate(b):
  if 0<abs(p)<7:
   j=i if p>0 else 119-i;r=j//10-2;f=j%10-1;t=abs(p);x=abs(2*f-7)+abs(2*r-7)
   v=V[t]+((6-r)*9-abs(2*f-7)*2 if t==1 else x*(0,0,-4,-2,0,-1,5 if ph>2 else -5)[t]+(6-r)*2*(t==4))
   z+=v if p>0 else -v
 return z
N=0;T={}
def S(p,d,a,z,h=0):
 global N
 N+=1
 if N>18000:raise TimeoutError
 b,c,e=p;k=tuple(b),frozenset(c),e
 o=T.get(k);t=o[2] if o else None
 if o and o[0]>=d and (o[3]==0 or o[3]==1 and o[1]>=z or o[3]==-1 and o[1]<=a):return o[1]
 f=A(b,b.index(6));w=a
 if d<=0 and not f:
  v=E(b)
  if v>=z:return v
  a=max(a,v)
 if h>80:return E(b)
 if h and d>2 and not f and any(1<x<6 for x in b) and -S(R((b,c,0)),d-3,-z,1-z,h+1)>=z:return z
 l=sorted(G(p,d<=0 and not f),key=lambda m: (m==t)*100000+V[abs(b[m[1]])]*10-b[m[0]]+m[2]*100,reverse=True)
 n=0;v0=-30000
 for m in l:
  if d<=0 and not f and not b[m[1]] and m[1]!=e and not m[2]:continue
  q=M(p,m)
  if A(q[0],q[0].index(-6),-1):continue
  n+=1
  v=-S(q,d-1,-z,-a,h+1)
  if v>v0:v0=v;t=m
  if v>a:a=v
  if a>=z:
   break
 if not n:
  if f:return -29000+h
  if d>0:return 0
 if d>0:T[k]=d,a,t,1 if a>=z else -1 if a<=w else 0
 return a
def U(m,bl):
 i,j,u=m
 if bl:i,j=119-i,119-j
 return ''.join(chr(96+x%10)+str(10-x//10) for x in (i,j))+(' pnbrqk'[u] if u else '')
def choose(fen,legal):
 global N,T
 p=F(fen);N=0;T={};bl=fen.split()[1]=='b';mv=min(legal)
 for d in range(1,10):
  try:
   S(p,d,-30000,30000);m=U(T[tuple(p[0]),frozenset(p[1]),p[2]][2],bl)
   if m in legal:mv=m
  except TimeoutError:break
 return mv
while True:
 g=post("/game",{})
 if g["status"]=="done":
  break
 while g["status"]=="your_move":
  g=post("/move",{"game":g["game"],"move":choose(g["fen"],g["legal_moves"])})
 print(f"game {g['game']}:{g['outcome']} by {g['reason']}",file=sys.stderr)
print(f"done:{g.get('wins')} won,{g.get('draws')} drawn,{g.get('losses')} lost",file=sys.stderr)
