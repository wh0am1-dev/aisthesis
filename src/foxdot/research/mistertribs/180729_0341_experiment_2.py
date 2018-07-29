# mistertribs - experiment 2
# https://youtu.be/jZTu6qttvMU

Scale.default = Scale.minor
Root.default = 0
Clock.bpm = 105

~b1 >> bass(dur=8, oct=4)

###
b1.room = 1
b1.shape = PWhite(1)
###

~d1 >> play('V  [ -]', dur=2, room=1, mix=.5)

~k1 >> karp([0,3,6,10], dur=.25, sus=.5, echo=.5, amp=var([0,1],[15,1]), oct=7)

###
k1.room = 1
k1.mix = .5
###

###
b1.fmod = 1
b1.pan = (-1,1)
###

b1.lpf=linvar([0,4000],30)

~s1 >> soprano(dur=8, sus=8, amp=[0,1])

s1.degree = var([0,-2,-3],8)
s1.oct = 6

k1.amp = var([0,1.5],[15,1])

b1.degree = s1.degree

###
~k2 >> karp([0,2,4,7], dur=1/3, sus=.5, echo=.5, amp=var([0,1.5],[5,1]), oct=7, room=1, mix=.5)
k1.every(16, 'reverse')
###

###
s1.degree = (0,4,7)+var([0,-2,-3],8)
s1.oct = (5,6)
###

b1.dur = PRand([16,8,12,4])
b1.amp = .8

~b2 >> blip(PWhite(4), dur=PWhite(.1), amp=linvar([0,1,0,0],[6,2,0,0]))

b2.shape = linvar([0,1],12)
b2.dur = PWhite(.3)/var([1,2,3],1)

###
b2.bits = 6
b2.room = .5
b2.mix = linvar([0,1],18)
###

~d2 >> play('#', dur=32, sus=8, chop=64, bits=4)

d1.chop = [128,64,0]

b1.stop()

d1.degree = 'V[-X]o[-=n-]'
d1.dur = 1
d1.fmod = 1
d1.slide = 3

s1.amp = .75
s1.slide = PWhite(-1,1)

~s1 >> soprano((0,4,7)+var([0,-2,-3],8), dur=8, sus=8, amp=[0,.75], oct=(5,6), slide=PWhite(-1,1))

~b1 >> bass(s1.degree, dur=PRand([16,8,12,4]), fmod=1, oct=4, room=1, shape=PWhite(1), pan=(-1,1), lpf=linvar([0,4000],30), amp=.8)

b2.stop()
s1.stop()
d1.stop()

~b2 >> blip(PWhite(4), dur=PWhite(.3)/var([1,2,3],1), amp=linvar([0,1,0,0],[6,2,0,0]), shape=linvar([0,1],12))

b1.stop()
Clock.clear()
