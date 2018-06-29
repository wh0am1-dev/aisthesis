"""
  Ryan Kirkbride - Love coding weird noises to dance to:
  https://www.youtube.com/watch?v=Qc_8Pm2t-84

  How to:
  - Run the statements line by line (alt+enter),
    go to the next one whenever you feel like
  - The "#### > run block <" blocks should be
    executed atomically (ctrl+enter)
  - If you want to fast-forward through the song,
    just execute the blocks atomically (ctrl+enter)
    from the beginning, so you don't have to go
    through every variation of each instrument
  - Enjoy ! :+1:
"""

p1 >> pads(dur=8,) + (P*(0,4))
p1 >> pads(dur=8,) + (P*(0,4,4.5))
p1 >> pads(dur=8,) + (P*(0,4,4.5,3.5))
p1 >> pads(dur=8,) + (P*(0,4,4.5,2.5))
p1 >> pads(dur=8,) + (P*(0,4,4.5,0.5))
p1 >> pads(dur=8,room=1,) + (P*(0,4,4.5,0.5))
p1 >> pads(dur=8,room=1,chop=320) + (P*(0,4,4.5,0.5))
p1 >> pads(dur=8,room=1,chop=320,coarse=16) + (P*(0,4,4.5,0.5))

d1 >> play("x ",)

d2 >> play("[ii]", amp=linvar([0,1,0],[2,0]),)
d2 >> play("[ii]", amp=linvar([0,1,0],[2,0,2]),)
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),)
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,)
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,rate=4,)
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,rate=1,)
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,rate=1,crush=4,)
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,rate=2,crush=4,)
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,rate=2,crush=4,room=0.5,)
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,rate=2,crush=4,room=0.5,pan=[-1,1],)

d1 >> play("x-",)
d1 >> play("xn",)
d1 >> play("xn",sample=[0,PRand(5)],)
d1 >> play("xn",sample=[0,PRand(7)],)
d1 >> play("xn",sample=[0,PRand(7)],).every(6,"stutter",4,dur=3)

b1 >> bass(dur=8,)
b1 >> bass([0,0.5],dur=4,)
b1 >> bass([0,0.5],dur=4,oct=4,)
b1 >> bass([0,0.5],dur=4,oct=3,)
b1 >> bass([0,0.5],dur=4,oct=3,shape=1,)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=-1,)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3]),)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3]),coarse=16,)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3]),coarse=PRand([4,8,16]),)

d3 >> play("  u ")

b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3,-4,2]),coarse=PRand([4,8,16]),)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3,-4,2]),coarse=PRand([4,8,16,32]),)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3,-4,2]),coarse=PRand([4,8,16,32,0]),)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3,-4,2]),coarse=PRand([4,8,16,32,0,64]),)

d3 >> play(Pvar(["  u ","  u u"],8),dur=PDur(var([4,5],8),8),)
d3 >> play(Pvar(["  u ","  u u"],8),dur=PDur(var([4,5],16),8),)

d1 >> play("xn",sample=[0,PRand(7)],).every(6,"stutter",4,dur=3).every(8,"amen")

Master().lpf = var([0,200],[28,4])

p1 >> pads(dur=8,room=1,chop=320,coarse=16) + (P*(0,4,4.5,[0.5,5]))

Root.default = var([0,2],64)

Master().lpf = var([0,100],[28,4])
Master().lpf = var([0,1000],[28,4])
Master().lpr = linvar([0.1,1])

b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3,-4,2]),coarse=PRand([4,8,16,32,0,64,13]),)
b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3,-4,2]),coarse=PRand([4,8,16,32,0,64])*PRand([1,1.5]),)

c1 >> play("#",dur=8,)
c1 >> play("#",dur=8,bits=4,)
c1 >> play("#",dur=8,bits=4,cut=1/2,)
c1 >> play("#",dur=8,bits=4,cut=1/2,room=1,)
c1 >> play("#",dur=8,bits=4,cut=1/4,room=1,)
c1 >> play("#",dur=8,bits=4,cut=1/4,room=1,crush=1,)
c1 >> play("#",dur=8,bits=4,cut=1/4,room=1,crush=1,shape=0.5,)
c1 >> play("#",dur=8,bits=4,cut=1/4,room=1,crush=1,shape=0.5,pan=[-1,1],)
c1 >> play("#",dur=8,bits=4,cut=1/4,room=1,crush=1,shape=0.5,pan=[-1,1],slide=-1,)
c1 >> play("#",dur=P[8:12],bits=4,cut=1/4,room=1,crush=1,shape=0.5,pan=[-1,1],slide=-1,)
c1.solo()
c1 >> play("#",dur=P[8:12],bits=4,cut=1/4,room=1,crush=8,shape=0.5,pan=[-1,1],slide=-1,chop=320,)

d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,rate=2,crush=4,room=0.5,pan=[-1,1],)

d1 >> play("xn",sample=[0,PRand(7)],).every(6,"stutter",4,dur=3).every(8,"amen")

c1 >> play("#",dur=P[8:12],bits=4,cut=1/4,room=1,crush=8,shape=0.5,pan=[-1,1],slide=-1,chop=320,rate=2,)
c1 >> play("#",dur=P[8:12],bits=4,cut=1/4,room=1,crush=8,shape=0.5,pan=[-1,1],slide=-1,chop=320,rate=PRand(8),)

b1 >> bass([0,0.5],dur=4,oct=3,shape=2,slide=PRand([-1,0,-2,-3,-4,2]),coarse=PRand([4,8,16,32,0,64])*PRand([1,1.5]),)

d3 >> play(Pvar(["  u ","  u u"],8),dur=PDur(var([4,5],16),8),)

p1 >> pads(dur=8,room=1,chop=320,coarse=16) + (P*(0,4,4.5,[0.5,5]))

c1 >> play("#",dur=P[8:12],bits=4,cut=1/4,room=1,crush=8,shape=0.5,pan=[-1,1],slide=-1,chop=320,rate=PRand(8)*10,)
c1 >> play("#",dur=P[8:12],bits=4,cut=1/4,room=1,crush=8,shape=0.5,pan=[-1,1],slide=-1,chop=320,rate=PRand(8)+10,)

s1 >> saw(PWhite(32),dur=1/4,)
s1 >> saw(PWhite(32),dur=1/6,)
s1 >> pulse(PWhite(32),dur=1/6,)
s1 >> pulse(PWhite(32),dur=1/6,fmod=10,)
s1 >> pulse(PWhite(32),dur=1/6,fmod=10,oct=4,)

Group(s1, b1).only()

s1 >> pulse(PWhite(32)[:8],dur=1/4,fmod=10,oct=4,)

d4 >> play("funky",rate=10,)
d4 >> play("funky",rate=10,dur=1/4,)
d4 >> play("funky",rate=4,dur=1/4,)
d4 >> play("funky",rate=4*PRand([1,1.5]),dur=1/4,)
d4 >> play("funky",rate=4*PRand([1,1.5,1.25]),dur=1/4,)
d4 >> play("funky",rate=4*PRand([1,1.5,1.25]),dur=1/4,pan=PStep(6,P*(-1,1)),)

#### > run block <
d1 >> play("xn",sample=[0,PRand(7)],).every(6,"stutter",4,dur=3).every(8,"amen")
d2 >> play("[oo]", amp=linvar([0,1,0],[2,0,2]),bits=4,rate=2,crush=4,room=0.5,pan=[-1,1],)
d3 >> play(Pvar(["  u ","  u u"],8),dur=PDur(var([4,5],16),8),)
b1.stop()
#### > run block <

s1 >> pulse(PWhite(32)[:8],dur=1/4,fmod=10,oct=3,)
s1 >> pulse(PWhite(32)[:8],dur=1/4,fmod=10,oct=3,) + var([0,(0,4)],[12,4])
s1 >> pulse(PWhite(32)[:8],dur=1/4,fmod=10,oct=4,) + var([0,(0,4)],[12,4])

Root.default = 0

c1 >> play("#",dur=P[8:12],bits=4,cut=1/4,room=1,crush=8,shape=0.5,pan=[-1,1],slide=-1,chop=320,rate=PRand(8)+10,)

d4 >> play("<funky><  m>",rate=4*PRand([1,1.5,1.25]),dur=1/4,pan=PStep(6,P*(-1,1)),)
d4 >> play("<funky><  w>",rate=4*PRand([1,1.5,1.25]),dur=1/4,pan=PStep(6,P*(-1,1)),)
d4 >> play("<funky><  (mw)l>",rate=4*PRand([1,1.5,1.25]),dur=1/4,pan=PStep(6,P*(-1,1)),)
d4 >> play("<funky><  (ew)l>",rate=4*PRand([1,1.5,1.25]),dur=1/4,pan=PStep(6,P*(-1,1)),)
d4 >> play("<funky><  (+t)l>",rate=4*PRand([1,1.5,1.25]),dur=1/4,pan=PStep(6,P*(-1,1)),)
d4 >> play("<funky><  (+q)l>",rate=4*PRand([1,1.5,1.25]),dur=1/4,pan=PStep(6,P*(-1,1)),)

p1 >> pads(dur=8,room=1,chop=320,coarse=16) + (P*(0,4,4.5,[0.5,5]))

s1.every(8,"degrade")
s1.stop()

d3 >> play("*",sample=2,dur=1/4,amp=PRand(2)[:16],)
d3 >> play("*",sample=2,dur=1/4,amp=PRand(2)[:16],pan=[-1,1],)
d3 >> play("*",sample=2,dur=1/4,amp=PRand(2)[:16],pan=[-1,0,1],)
d3 >> play("*",sample=2,dur=1/4,amp=PRand(2)[:16],pan=[-1,0,1],rate=var([1,2]))

d1 >> play("Vn",sample=[0,PRand(7)],).every(6,"stutter",4,dur=3).every(8,"amen")
d1 >> play("<Vn><  u >",sample=[0,PRand(7)],).every(6,"stutter",4,dur=3).every(8,"amen")

p1 >> pads(dur=8,room=1,chop=320,coarse=16,lpf=linvar([500,1000],24),) + (P*(0,4,4.5,[0.5,5]))
p1 >> pads(dur=8,room=1,chop=320,coarse=16,lpf=linvar([500,1000],24),lpr=linvar([0.1,1],14),) + (P*(0,4,4.5,[0.5,5]))
p1 >> pads(dur=8,room=1,chop=320,coarse=16,lpf=linvar([500,800],24),lpr=linvar([0.1,1],14),) + (P*(0,4,4.5,[0.5,5]))
p1 >> pads(dur=8,room=1,chop=320,coarse=16,lpf=linvar([400,800],24),lpr=linvar([0.1,1],14),) + (P*(0,4,4.5,[0.5,5]))
p1 >> pluck(dur=8,room=1,chop=320,coarse=16,lpf=linvar([400,800],24),lpr=linvar([0.1,1],14),) + (P*(0,4,4.5,[0.5,5]))

d_all.amplify = var([1,0],[28,4])

p2 >> blip(dur=12,)
p2 >> blip(dur=12,fmod=10,)
p2 >> blip(dur=12,fmod=4,)
p2 >> blip(dur=12,fmod=4,vib=12,)
p2 >> blip(dur=12,fmod=4,vib=12,slide=-1,oct=7,)
p2 >> blip(dur=12,fmod=4,vib=12,slide=-1,oct=7,pan=P*(-1,0,1),)
p2 >> blip(dur=12,fmod=4,vib=12,slide=-1,oct=7,pan=P+(-1,0,1),sus=4,)
p2 >> blip(dur=12,fmod=4,vib=12,slide=-1,oct=7,pan=P+(-1,0,1),sus=4,bits=8,crush=8,)
p2 >> blip(dur=12,fmod=4,vib=12,slide=-1,oct=7,pan=P+(-1,0,1),sus=4,bits=8,crush=8,) + (0,9)
p2 >> blip(dur=12,fmod=4,vib=12,slide=-1,oct=7,pan=P+(-1,0,1),sus=4,bits=8,crush=8,) + (0,2)

d_all.stop()

# p2 >> blip(dur=12,fmod=4,vib=12,slide=(-1,-2,-3),oct=7,pan=P+(-1,0,1),sus=4,bits=8,crush=8,) + (0,2)
# p2 >> blip(dur=12,fmod=4,vib=12,slide=-1,oct=7,pan=P+(-1,0,1),sus=4,bits=8,crush=8,) + (0,2)
# DefaultServer.freeAllNodes()

d1 >> play("n",dur=1/4,sample=PRand(7),)
d1 >> play("n",dur=1/4,sample=PRand(7),pan=PWhite(-1,1),)
d1 >> play("n",dur=1/4,sample=PRand(7)+PStep(7,P*(0,1)),pan=PWhite(-1,1),)

d2 >> play("(X )( X)O ",)
d2 >> play("(X )( X)O ",rate=(0.9,1),pan=(-1,1),)
d2 >> play("(X )( X)O ",rate=(0.9,1),pan=(-1,1),).every(6,"stutter")
d2 >> play("(X )( X)O ",rate=(0.9,1),pan=(-1,1),).every(6,"stutter",n=4,dur=3)
d2 >> play("<s><(X )( X)O >",rate=(0.9,1),pan=(-1,1),).every(6,"stutter",n=4,dur=3)
d2 >> play("< s><(X )( X)O >",rate=(0.9,1),pan=(-1,1),).every(6,"stutter",n=4,dur=3)

d_all.lpf = 500
d_all.lpf = 0

d3 >> play("[oo]",amp=linvar([0,1],[32,0]),)

d4 >> play("#",dur=32,)

nextBar(Clock.clear())
