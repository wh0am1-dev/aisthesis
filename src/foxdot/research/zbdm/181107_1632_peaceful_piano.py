# zbdm - peaceful piano
# https://www.youtube.com/watch?v=rzPS4hRF1BU

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 80

p1 >> piano(P[0,2,5,4])
p1.degree = P[0,2,5,4].stutter(2)
p1.dur = var([.5,1], [6,2])
p1.room = 1
p1.mix = .2
p1.oct = (3,[4,5])
p1.degree = P[0,2,5,4].stutter(2) + [0,0,0,7]

var.cho = var([0,-2,-4,-3], 8)

p1.degree = P[var.cho,2,5,4].stutter(2) + [0,0,0,7]

p2 >> piano([6,2,4,0], dur=2)

p1.degree = P[var.cho,[2,6],5,4].stutter(2) + [0,0,0,7]
p1.amp = PWhite(.6, 1.2)

p2.amp = PWhite(.7, 1.4)
p2.penta().spread()

p1.lpf = 900
p1.lpf = var([900,4800], 24)

p2.amp = PWhite(.7, 1.2)

p1.lpf = var([900,8800], 24)

p2.room = 1
p2.mix = .2
p2.oct = 6

p1.lpf = 0

k1 >> klank(dur=8)

b1 >> bass(var.cho, dur=8, amp=.7)

d1 >> play('x[::][xx]=', crush=8)
d1.every(4, 'amen')
d1.often('stutter', Cycle([2,4,12]))

b1.degree = var.cho + var([0,PRand(7)], [6,2])
b1.dur = PDur(5, 8)

k1.degree = (var.cho,2,4)

p2.degree = [6,2,PRand(4),0]
p2.degree = P[6,2,PRand(4),0].offlayer('shuffle', .75)

k1.spread()

d2 >> play('#', rate=[-.5,.25], dur=8, drive=.1, lpf=1500)
d2.spread()

k1.degree = (var.cho,2,[4,8])
k1.oct = (5,6)
k1.amp = .2; k1.drive = .1

b1.dur = PDur(var([5,7], [6,2]), 8)

d2.drive = .05

d_all.stop()
b1.stop()
p1.stop()
Clock.clear()
