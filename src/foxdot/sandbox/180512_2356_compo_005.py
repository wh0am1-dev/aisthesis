Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 100

p1pat = [[0, 1, 2], P+(1, 2, [4, 6]), P/([2, 1], 4), P+(7, [6, 8], [5, 2, 6], 4)]
p1.reset() >> glass(
    p1pat,
    dur = PDur(5, 8) * 4 | 4,
    sus = [3, 4, 6, [4, 1]],
    oct = [(4, 5), 5, P/(4, 5)],
    amp = linvar([0.8, 1], 12),
    lpf = 0,
    hpf = 0,
) + var([0, 1], 8)

a1.reset() >> ambi(
    var([0, 1], 8),
    oct = 5,
    fmod = (0, 1),
    pan = (-1, 1),
    amp = 1.0,
) + (0, var([2, 4], 16))

k1.reset() >> klank(
    lpf = linvar([4000, 200], 16),
    rate = P[4:24].stutter(2),
    amp = 0.6,
) + var([0, 1, 2, 3], 8)

d1.reset() >> play(
    "X - - (-X)(X[--])",
    bits = 16,
).every(5, "stutter", 3, dur = 1)

x1.reset() >> play("(x )(-[-x]-)")
x2.reset() >> play("  ((  [ p])(p[pp][p ])) ")
x3.reset() >> play("m  m  m ").every(3, "stutter", 3, dur = 1)

d2.reset() >> play(
    "funky",
    dur = .25,
    amp = PWhite(0.25, 0.5),
    pan = PWalk(-1, 1),
    sample = PRand(5),
    rate = PRand([1.0, 2.0, 4.0]),
    delay = 0,
)

d3.reset() >> play(
    "this is nice",
    rate = 11,
    dur = 1,
    pan = PWhite(-1, 1),
    lpf = 6000,
).every(50, "stutter", var([2, 4]), pan=[-1, 1])

d4 >> play(
    "  ( ( I))I( [II])",
    dur = 1,
    rate = (0.9, 1),
    pan = 0,
    room = 1,
    amp = 0.5,
    hpf = 4000,
)

charmpat = []

s1 >> charm(
    p1.degree,
    coarse = 0.7,
    dur = 0.25,
    lpf = 600
)



s3 >> noise([0], amp = 0.6, dur = 8, sus = 4, attack = 0.1)

print(SynthDefs)
