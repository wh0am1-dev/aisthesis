"""
  Ryan Kirkbride - Jamming 000:
  https://www.youtube.com/watch?v=3NDQOKGx0dM

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

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

p1 >> pluck()
p1 >> pluck(dur=PDur(3,8),)
p1 >> pluck(dur=PDur(3,8),sus=2,coarse=4,)
p1 >> pluck(dur=PDur(3,8),sus=2,coarse=4,room=.1,)
p1 >> pluck([0,4],dur=PDur(3,8),sus=2,coarse=4,room=.1,)
p1 >> pluck([0,[4,6,7]],dur=PDur(3,8),sus=2,coarse=4,room=.1,)

d1 >> play("x-")

p2 >> donk((0,9))
p2 >> donk((0,9),dur=PDur(3,8),)
p2 >> donk((0,9),dur=PDur(3,8),pan=PStep(5,P*(-1,1)),)
p2 >> donk((0,9),dur=PDur(3,8),pan=PStep(5,P*(-1,1)),rate=PWhite(20),)
p2 >> donk(var([0,5],8) + (0,9),dur=PDur(3,8),pan=PStep(5,P*(-1,1)),rate=PWhite(20),)
p2 >> donk(var([0,5],8) + (0,9),dur=PDur(3,8),pan=PStep(5,P*(-1,1)),rate=PWhite(20),) + var([0,1],[7,1])
p2 >> donk(var([0,5],8) + (0,9),dur=PDur(3,8),pan=PStep(5,P*(-1,1)),rate=PWhite(20),oct=6,) + var([0,1],[7,1])
p2 >> donk(var([0,5],8) + (0,9),dur=PDur(3,8),pan=PStep(5,P*(-1,1)),rate=PWhite(20),oct=6,sus=1,) + var([0,1],[7,1])

p1 >> pluck([0,[4,6,7]],dur=PDur(3,8),sus=2,coarse=4,room=.1,hpf=linvar([0,1000],16),)
p1 >> pluck([0,[4,6,7]],dur=PDur(3,8),sus=2,coarse=4,room=.1,hpf=linvar([0,1000],16),hpr=linvar([0.1,1],12),)

d2 >> play("  u ")

b1 >> bass(var([0,-2,0,3],8),)
b1 >> bass(var([0,-2,0,3],8),dur=PRand([1,1/2]),)

Master().amplify = var([1,0],[28,4])

b1 >> bass(var([0,-2,0,3],8),dur=PRand([1,1/2]),shape=0.2,)

d3 >> play("#",dur=32,)

b1 >> bass(var([0,-2,0,3],8),dur=PRand([1,1/2]),shape=PWhite(0,1),)
b1 >> bass(var([0,-2,0,3],8),dur=PRand([1,1/2]),shape=PWhite(0.2,1),)

Master().amplify = 1

p2.only()

d2 >> play("  u ")

d1 >> play("x-")

b1 >> bass(var([0,-2,0,3],8),dur=PRand([1,1/2]),shape=PWhite(0.2,1),)

p1 >> pluck([0,[4,6,7]],dur=PDur(3,8),sus=2,coarse=4,room=.1,hpf=linvar([0,1000],16),hpr=linvar([0.1,1],12),)

Group(p1,d1,d2).only()

d2.stop()

d1.stop()

nextBar(Clock.clear)

