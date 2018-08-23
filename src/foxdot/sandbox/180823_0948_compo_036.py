Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 120

var.ch = var(P[1,5,0,3],8)

~p1 >> play('m', amp=.8, dur=PDur(3,8), rate=[1,(1,2)])

~p2 >> play('-', amp=.5, dur=2, hpf=2000, hpr=linvar([.1,1],16), sample=1).often('stutter', 4, dur=3).every(8, 'sample.offadd', 1)

~p3 >> play('{ ppP[pP][Pp]}', amp=.8, dur=.5, sample=PRand(7), rate=PRand([.5,1,2]))

~p4 >> play('V', amp=.8, dur=1)

~p5 >> play('#', amp=1.2, dur=16, drive=.1, chop=128, formant=1)

~s1 >> glass(var.ch+(0,5,12), amp=1, dur=8, coarse=8)

~s2 >> piano(var.ch+(0,[5,5,3,7],12), amp=1, dur=8, delay=(0,.25,.5))

Group(p1, p2, p3).stop()

p4.lpf = linvar([4000,10],[32,0])
p4.stop()

s2.stop()

~s3 >> saw(var.ch+PWalk(), amp=PRand([0,.8])[:24], dur=PDur(3,8), scale=Scale.minor, oct=PRand([4,5,6])[:32], drive=.05, room=1, mix=.5).spread()
~s3 >> saw(var.ch+PWalk(), amp=PRand([0,.8])[:20], dur=PDur(5,8), scale=Scale.minor, oct=PRand([4,5,6])[:32], drive=.05, room=1, mix=.5).spread()
~s3 >> saw(var.ch+PWalk(), amp=PRand([0,.8])[:64], dur=.25, scale=Scale.minor, oct=PRand([4,5,6])[:32], drive=.05, room=1, mix=.5).spread()

~p4 >> play('V', amp=.5, dur=1, room=1, lpf=1200).every(7, 'stutter', cycle=16)

~p6 >> play('n', amp=.5, dur=1, delay=.5, room=1, hpf=linvar([2000,4000],16), hpr=.1)

s1.oct = 4
s1.formant = 1

~p3 >> play('{ ppP[pP][Pp]}', amp=.5, dur=.5, sample=PRand(7), rate=PRand([.5,1,2]), room=1, mix=.25)

Group(p6, s3).stop()

~s2 >> piano(var.ch+([12,0],[5,5,3,7],[0,12]), amp=1, dur=8, delay=(0,.25,.5), room=1, mix=.5, drive=.05, chop=32, echo=[1,2,1,4])

Group(p3, s1).stop()

Clock.clear()
