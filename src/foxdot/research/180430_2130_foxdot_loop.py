"""
  Ryan Kirkbride - FoxDot loop:
  https://www.youtube.com/watch?v=jfjAOZnTwAM

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

p1 >> loop("foxdot",P[:16],)
p1 >> loop("foxdot",0,)
p1 >> loop("foxdot",0,dur=PDur(3,8),)
p1 >> loop("foxdot",0,dur=PDur(3,8)|2,)
p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],)

d1 >> play("x-",)

p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),)
p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),)
p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),)

d1 >> play("<V-><  O >",)

p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),rate=1/2,)
p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),rate=1,)
p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),rate=-1,)
p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),rate=-2,)
p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),rate=-1,)
p1 >> loop("foxdot",P[1:9],dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),rate=-1,)
p1 >> loop("foxdot",0,dur=PDur(3,8)|[0.5,1.5],pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),rate=1,)

Root.default = -2
Scale.default = Scale.minor

b1 >> bass()
b1 >> bass(var([0,-1],[3,1]),)
b1 >> bass(var([0,-1],[3,1]),dur=PDur(5,12),)
b1 >> bass(var([0,-1],[3,1]),dur=PDur(5,12),shape=0.5,)
b1 >> bass(var([0,-1],[3,1]),dur=PDur(5,12),shape=0.5,fmod=(0,1),)

#### > run block <
d1 >> play(P["(V )( V)O "].amen(),)
d2 >> play("----",)
#### > run block <

k1 >> klank(9,)
k1 >> klank(var([9,6,7]),rate=P[4:24].stutter(2),)

d2 >> play("----",) + 2
d2 >> play("----",dur=1/4,) + 2

b2 >> dirt([0,7],)
b2 >> dirt([0,[7,P*(6,7)]],)
b2 >> dirt([0,[7,P*(6,7)]],shape=0.5,)
b2 >> dirt([0,[7,P*(6,7)]],shape=0.5,dur=PDur(3,8),)
b2 >> dirt([0,[7,P*(6,7)]],shape=0.5,dur=PDur(3,8),sus=1,)

p1.solo()
nextBar(lambda: p1.solo(0))
p1 >> loop("foxdot",P[:16],dur=1,pshift=(0,0.1),pan=(-1,1),formant=var([0,4],[12,4]),rate=1,)

d2.stop()
d1.stop()
b1.stop()
b2.stop()

nextBar(Clock.clear)

