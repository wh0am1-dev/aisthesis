# mistertribs - Experiment 7
# https://www.youtube.com/watch?v=EYxLZAhHwjI

Scale.default.set(P[0:13], tuning=Tuning.bohlen_pierce)
Root.default = 0
Clock.bpm = 120

var.ch = var(P[(0, 3), (0, 8), (-2, 3), (3, 8)], 16)

p1.reset() >> blip()

p1.oct = 3
p1.degree = var.ch
p1.dur = .25
p1.amp = linvar([0, 1], 8)
p1.delay = (0, linvar([0, .25], [16, 0]))
p1.room = .3
p1.mix = linvar([.1, .8], 12)

b1.reset() >> klank(
    p1.pitch[0],
    dur = 4,
    oct = 3,
    amp = .5,
)

b1.sus = 2
b1.oct = [3, 4]

a1.reset() >> ambi(
    p1.pitch[P[0, 1]],
    dur = 8,
    oct = 2,
    amp = .25,
)

a1.amplify = var([0, 1], 64)
a1.amp = .5

b2.reset() >> bass(
    p1.pitch[0],
    dur = P[8, rest(8)],
    oct = 3,
    amp = .5,
)

b2.shape = .2
b2 >> dbass()
b2.dur = P[12, rest(4)]
b2.amplify = a1.amplify

s1 >> space(
    var.ch[0] + [0, 7, 5],
    dur = [2, 1, 1],
    amp = .4,
    oct = 4,
)

s1.dur = [8, 4, 2, 2]
s1.amp = linvar([0, .4], 20)
s1.every(12, 'offadd', 3)
s1.degree = var.ch[0] + [0, 4, 7]
s1.degree = (var.ch[0] + P[0, 4, 7]) % 13

Group(b1, a1).stop()

b2.degree = p1.pitch[1]

s1.stop()

b2.amp = .35
b2.stop()

nextBar(Clock.clear)

