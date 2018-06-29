"""
  Ryan Kirkbride - Noodling around:
  https://www.youtube.com/watch?v=CXrkq7u69vU

  How to:
  - Run the statements line by line (alt+enter),
    go to the next one whenever you feel like
  - The "#### > run block <" blocks should be
    executed together (ctrl+enter)
  - If you want to fast-forward through the song,
    just execute the blocks together (ctrl+enter)
    from the beginning, so you don't have to go
    through every variation of each instrument
  - Enjoy ! :+1:
"""

Scale.default = Scale.minor
Root.default = -4
Clock.bpm = 136

d1 >> play(P["x---o---"],)
d1 >> play(P["x---o---"].layer("mirror"),pan=(-1,1),)
d1 >> play(P["x--(-[--])o---"].layer("mirror"),pan=(-1,1),)
d1 >> play(P["x--(-[--])o--(-=)"].layer("mirror"),pan=(-1,1),)
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),)
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,)
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),)

d2 >> play(PZip("Vs","  n "),sample=1,)
d2 >> play(PZip("Vs","  n "),sample=2,)
d2 >> play(PZip("Vs","  n "),sample=2,).every(3,"stutter")
d2 >> play(PZip("Vs","  n "),sample=2,).every(3,"stutter",dur=1)
d2 >> play(PZip("Vs","  n "),sample=2,hpf=var([0,4000],[28,4]),).every(3,"stutter",dur=1)

b1 >> dirt(var([0,2,-1,3]),)
b1 >> dirt(var([0,2,-1,3]),dur=PDur(3,8),)
b1 >> dirt(var([0,2,-1,3]),dur=PDur(3,8),bits=4,)
b1 >> dirt(var([0,2,-1,3]),dur=PDur(3,8),bits=4,lpf=80,)
b1 >> dirt(var([0,2,-1,3]),dur=PDur(3,8),bits=4,lpf=80,fmod=(0,1),)

k1 >> karp()
k1 >> karp(oct=6,)
k1 >> karp(dur=1/4,oct=6,)
k1 >> karp(dur=1/4,oct=var([6,7]),)
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1/2,)
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1,)
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1,) + var([0,-1,1,0])
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1,rate=P[:32],) + var([0,-1,1,0])
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1,rate=P[:32]*(1,2),) + var([0,-1,1,0])
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1,rate=P[:32]*(1,2),delay=(0,1/8),) + var([0,-1,1,0])
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1,rate=P[:32]*(1,2),delay=(0,1/8),lpf=linvar([400,5000],12),) + var([0,-1,1,0])
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1,rate=P[:32]*(1,2),delay=(0,1/8),lpf=linvar([400,5000],12),pan=linvar([-1,1],8),) + var([0,-1,1,0])
k1 >> karp(dur=1/4,oct=var([6,7]),sus=1,rate=P[:32]*(1,2),delay=(0,1/8),lpf=linvar([400,5000],12),pan=linvar([-1,1],8),) + var([0,-1,1,-7])

d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),).every(5,"stutter",4,pan=[-1,1])
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),).every(5,"stutter",4,pan=[-1,1],rate=4)

p1 >> blip([0,4,7,9],)
p1 >> blip([0,4,7,9],oct=6,)
p1 >> blip([0,4,7,9],oct=6,sus=2,)
p1 >> blip([0,4,7,9],oct=6,sus=2,dur=1/2,)
p1 >> blip([var([0,-1,1,0]),4,7,9],oct=6,sus=2,dur=1/2,)
p1 >> blip([var([0,-1,1,0]),4,[7,10],9],oct=6,sus=2,dur=1/2,)
p1 >> blip([var([0,-1,1,0]),4,[7,10],9],oct=7,sus=2,dur=1/2,)
p1 >> blip([var([0,-1,1,0]),4,[7,10],9],oct=(6,7),sus=2,dur=1/2,)

d3 >> play("[--]")

p1 >> blip([var([0,-1,1,0]),4,[7,10],9],oct=(6,7),sus=2,dur=PDur(5,8),)
p1 >> blip([var([0,-1,1,0]),4,[7,10],9],oct=(6,7),sus=2,dur=PDur(5,8),chop=4)
p1 >> blip([var([0,-1,1,0]),4,[7,10],9],oct=(6),sus=2,dur=PDur(5,8),chop=4)

d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),).every(5,"stutter",0,pan=[-1,1],rate=4)

k1.stop()

d2.solo()

Scale.default = "major"

s1 >> swell((0,2,4,const(6)),dur=4,)
s1 >> swell((0,2,4,const(6)),dur=4,) + var([0,1],8)
s1 >> swell((0,2,4,const(6)),dur=4,) + var([0,-1],8)
s1 >> swell((0,2,4,const(6)),dur=4,) + var([0,1],8)

Scale.default = Pvar([Scale.major,Scale.minor],16)

s1 >> swell((0,2,4,const(6)),dur=4,) + var([0,[1,-1]],8)
s1.solo()

b1 >> dirt(var([0,[1,-1]],8),dur=PDur(3,8),bits=4,lpf=80,fmod=(0,1),)
b1 >> dirt(var([0,[1,-1]],8),dur=PDur(3,8),bits=0,lpf=80,fmod=(0,1),)
b1 >> dirt(var([0,[1,-1]],8),dur=PDur(3,8),bits=0,lpf=0,fmod=(0,1),)
b1 >> bass(var([0,[1,-1]],8),dur=PDur(3,8),bits=0,lpf=0,fmod=(0,1),)
b1 >> bass(var([0,[1,-1]],8),dur=PDur(3,8),bits=0,lpf=0,fmod=(0,0),)

b1 >> bass(var([0,[1,-1]],8),dur=PDur(3,8),bits=0,lpf=0,) + [0,4,const(7)]
b1 >> bass(var([0,[1,-1]],8),dur=PDur(5,8),bits=0,lpf=0,) + [0,4,const(7)]
b1 >> bass(var([0,[1,-1]],8),dur=PDur(5,12),bits=0,lpf=0,) + [0,4,const(7)]

d2 >> play(PZip("Vs","  n "),sample=2,hpf=var([0,4000],[28,4]),).every(3,"stutter",dur=1)

d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),)

k2 >> karp([0,7,6,4,2],)
k2 >> karp([0,7,6,4,2],sus=2,)
k2 >> karp([0,7,6,4,2],sus=2,dur=PDur(5,8),chop=4,)
k2 >> karp([0,7,6,4,2],sus=2,dur=PDur(5,8),chop=4,oct=7,)
k2 >> karp(P[var([0,1],8),7,6,4,2],sus=2,dur=PDur(5,8),chop=4,oct=7,)
k2 >> karp(P[var([0,1],8),7,6,4,2].layer("mirror"),sus=2,dur=PDur(5,8),chop=4,oct=7,)
k2 >> karp(P[var([0,1],8),7,6,4,2].layer("mirror"),sus=2,dur=PDur(5,8),chop=4,oct=7,delay=(0,0.25),)
k2.solo()

b1 >> bass(var([0,[1,-1]],8),dur=PDur(5,12),bits=0,lpf=0,) + [0,4,const(7)]

d2 >> play(PZip("Vs","  D "),sample=0,hpf=var([0,4000],[28,4]),).every(3,"stutter",dur=1)
d2 >> play(PZip("Vs","  D D"),dur=PDur(5,8),sample=0,hpf=var([0,4000],[28,4]),).every(3,"stutter",dur=1)
d2 >> play(PZip("Vs","  i i"),dur=PDur(5,8),sample=0,hpf=var([0,4000],[28,4]),).every(3,"stutter",dur=1)

s1 >> swell((0,2,4,const(6)),dur=4,) + var([0,[1,-1]],8)

d3 >> play("[--]")

d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),)
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),chop=32,)
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),chop=32,bits=4,)
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),chop=32,bits=4,slide=PStep(5,-1),)
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sample=-1,rate=var([1,4],[28,4]),chop=8,bits=4,slide=PStep(5,-1),)
d1 >> play(P["x--(-[--])o--o(-=)-"].layer("mirror"),pan=(-1,1),dur=PDur(5,8),sus=1,sample=-1,rate=var([1,4],[28,4]),chop=8,bits=4,slide=PStep(5,-1),)

k2.solo()
k2.solo(0)

p1.stop()

Group(k2, s1, d2, d3).only()

Group(s1, d3).stop()

nextBar(Clock.clear)

