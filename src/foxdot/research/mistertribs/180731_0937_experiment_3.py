# mistertribs - experiment 3
# https://youtu.be/AyRlEI8FLfE

import math
Scale.default.set([12*math.log2(i) for i in [1,9/8,4/3,3/2,16/9]])
Root.default = 0
Clock.bpm = 120

~x1 >> klank((0,5,8), oct=3)

~d1 >> play('V   ', dur=1, amp=.3, room=1, mix=.5, fmod=1)
~d1 >> play('V   ', dur=2, amp=.3, room=1, mix=.5, fmod=1)

~d2 >> play('k', amp=.02, sample=1, delay=(0,PWhite(0,.1)))

~d1 >> play('V   ', dur=2, amp=.2, room=1, mix=.5, fmod=1)

var.ch = var([0,3,2,4], 8)

~b1 >> bass(var.ch, dur=8, amp=.5, oct=4)
~b1 >> bass(var.ch+(0,5), dur=8, amp=.5, oct=4, pan=(-1,1))

~m1 >> marimba(P[3,var.ch,2,4], amp=.5, dur=.25, pan=linvar([-1,1],32))
~m1 >> marimba(P[3,var.ch,2,4], amp=.5, dur=.5, pan=linvar([-1,1],32))

~d1 >> play('V   [-V]', dur=2, amp=.2, room=1, mix=.5, fmod=1)
~d1 >> play('V   [   V]', dur=2, amp=.2, room=1, mix=.5, fmod=1)
~d1 >> play('V   ( [   V])', dur=2, amp=.2, room=1, mix=.5, fmod=1)

~d2 >> play('k', amp=.02, sample=1, delay=(0,PWhite(0,.1)), rate=(1,PWhite(.9,1.1)))

~v1 >> viola([0,var.ch,4,2], dur=P[2,8,6,4], amp=.5, room=1, mix=.2, blur=1.2)
~v1 >> viola([0,var.ch,4,2], dur=P[2,8,6,4], amp=linvar([.5,.8],24), room=1, mix=.2, blur=1.2)

~m1 >> marimba(P[3,var.ch,2,4], amp=.5, dur=.5, pan=linvar([-1,1],32)).every(12, 'amen')

~x1 >> klank((0,5,8), oct=3, formant=linvar([0,1],8))

m1.stop()

~d3 >> donk(P[5,4,3,2,3,2,1,0], oct=4, dur=.5, amp=.4, pan=(-1,1))
~d3 >> donk(P[5,4,3,2,3,2,1,0], oct=4, dur=.5, amp=.3, pan=(-1,1))
~d3 >> donk(P[5,4,3,2,3,2,1,0], oct=4, dur=.5, amp=.3, pan=(-1,1), room=.3, mix=.4)

~d1 >> play('V   ( [   V])', dur=2, amp=.2, room=1, mix=.5, fmod=1, rate=[1,1.5,2])
~d1 >> play('V   ( [---V] [pppX])', dur=2, amp=.2, room=1, mix=.5, fmod=1, rate=[1,1.5,2])
~d1 >> play('V   ( [---V] [pppX])', dur=1, amp=.2, room=1, mix=.5, fmod=1, rate=[1,1.5,2])
~d1 >> play('V   ( [---V] [pppX])', dur=1, amp=.4, room=1, mix=.5, fmod=1, rate=[1,1.5,2])

~v1 >> viola([0,var.ch,4,2], dur=P[2,8,6,4], amp=linvar([.5,.8],24), room=1, mix=.2, blur=1.2).every(20, 'offadd', 3)

# he missed it... D:
# ~m1 >> marimba(P[3,var.ch,2,4], amp=.5, dur=.5, pan=linvar([-1,1],32)).every(12, 'amen').every(8, 'mirror')

~b2 >> sawbass(b1.degree+P[3,0,5,2], dur=PDur(5,8), amp=.4, hpf=linvar([0,4000],20), oct=4)

~k1 >> karp(PWalk()+(0,var([2,3,4],4)), dur=.25, amp=linvar([.2,.6],12))

# modulo 5 => 5 notes in the scale ! :)
~m1 >> marimba((P[3,0,2,4]+var.ch)%5+[(0,2),(0,2),(0,3)], amp=.5, dur=PDur(3,8), pan=linvar([-1,1],32)).every(12, 'amen').every(8, 'mirror')

var.ch = var([1,4,0,5], [12,8,6,8])

nextBar(lambda: d_all.stop())
nextBar(lambda: v1.stop())
nextBar(lambda: m1.stop())
nextBar(lambda: x1.stop())

### > block <
~d1 >> play('V   ( [---V] [pppX])', dur=1, amp=.4, room=1, mix=.5, fmod=1, rate=[1,1.5,2])
~d2 >> play('k', amp=.02, sample=1, delay=(0,PWhite(0,.1)), rate=(1,PWhite(.9,1.1)))
~d3 >> donk(P[5,4,3,2,3,2,1,0], oct=4, dur=.5, amp=.3, pan=(-1,1), room=.3, mix=.4)
###

nextBar(lambda: k1.stop())
Clock.clear()
