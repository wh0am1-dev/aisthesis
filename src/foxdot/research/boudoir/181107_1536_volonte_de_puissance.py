# boudoir - volonte de puissance
# https://www.youtube.com/watch?v=LO5vJ2VGvsE
# https://gist.github.com/jf-parent/911571068aff0e61142ca847f0a62e19

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

# def dreamscape1():
p1 >> sinepad(
  [-2,(-4,4)],
  dur=8,
  sus=10,
  formant=.3,
  room=1,
  mix=[0,1],
)

# def dreamscape2():
p2 >> spark(
  [(2,-2,-4),0],
  dur=8,
  sus=10,
  formant=[0,1,2],
  oct=4,
  room=1,
  mix=1,
  verb=linvar([0,.2],16),
)

# def dreamscape4():
p3 >> space(
  [1,((-2,-4),2)],
  dur=10,
  sus=12,
  formant=linvar([0,2],16),
  amp=.3,
)

# def back2():
p4 >> pasha(
  [(-2,0),(2,4)],
  dur=4,
  amp=.8,
  sus=5,
  formant=[1,2],
  room=1,
  mix=var([0,1],[16,4]),
)

# def back3():
p5 >> play(
  '-b',
  amp=linvar([0,.4],32),
)

# def back4():
p3 >> play(
  'gg ggg ggggg ',
  amp=.2,
)
