# mistertribs - experiment 1
# https://www.youtube.com/watch?v=viu0RwhgEls

var.ch = var([0, 2], 8)

p1.reset() >> blip(var.ch)

p1.fmod = 1
p1.oct = 6
p1.dur = PDur(3, 8)
p1.oct = 5

p2.reset() >> karp(
    P[var.ch, 4, 6, 7],
    oct = 6,
    dur = .25,
)

p2.every(6, 'mirror')

d1.reset() >> play('X ')

d2.reset() >> play(
    '---(-[--])',
    sample = PRand(3)[:16],
)

p1.vib = 12

p3.reset() >> swell(
    P[var.ch, 4, 6, 9] + (0, 4),
    dur = 8,
    oct = 3,
)

d3.reset() >> play(
    '#',
    dur = 32,
)

b2.reset() >> sawbass(
    var.ch,
    dur = PDur(5, 8),
)

b2.bits = 6
b2.shape = .25
b2.chop = 160
b2.chop = 160 * PRand([0, 2, 4])[:10]

p1.degree = var.ch + P[(0, 2), (2, 4)]
p1.dur = PSum(5, 8).loop(3) | P[.25, .25, .25, .25]
p1.every(8, 'stutter', 2, dur=4, oct=6)

p2.every(12, 'offadd', 4)

d4.reset() >> play(
    'o',
    dur = .25,
    amp = var([0, 2], [28, 4]),
)

d4.amp = var([0, 1], [28, 4])

p1.vib = [12, 12, 0]

b2.stop()

p3.pan = (-1, 1)

var.ch = var([0, -1, 2, -2], [16, 8, 16, 8])

b2.reset() >> sawbass(
    var.ch,
    dur = PDur(5, 8),
    bits = 6,
    shape = 0,
    oct = 5,
    chop = 160 * PRand([0, 2, 4])[:10],
)

b2.bits = 7
b2.bits = 5
b2.shape = 1
b2.shape = .2
b2.verb = 1

Group(d1, d2, d3).stop()

d4.stop()
b2.stop()
nextBar(Clock.clear)

