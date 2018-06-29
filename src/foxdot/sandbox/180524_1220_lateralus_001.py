Scale.default = "chromatic"
Root.default = 2
Clock.bpm = 120

drp = [0, 7, 12, 17, 21, 26]
std = [0, 5, 10, 15, 19, 24]

d1 >> play("<X x n  [--]>")

d2 >> play("(   [II]) I ")

d3 >> play(
    "funky",
    dur = 1/2,
    sample = PRand(5),
    pan = (-1, 1),
    amp = 0.5,
    rate = PRand([0.25, 0.5, 1])
)

a1 >> ambi(
    var([drp[0], drp[0]+5, drp[0]+3], [8,4,4]),
    oct = 4,
) + (0, 7, 12)

p1 >> pluck(
    P[drp[0], drp[1], const(drp[2]+7)].loop(2) | P[drp[0], const(drp[2]+7)],
    oct = 4,
    dur = 1/2,
    sus = 1,
    shape = 1,
    room = 0.75,
    mix = 0.5,
    coarse = 4,
    hpf = linvar([500, 1000], 16),
    hpr = linvar([0.1, 1], 16),
    lpf = 800,
) + var([0,3,5], [8,4,4])

p2 >> piano(
    var([drp[0], drp[0]+5, drp[0]+3], [8,4,4]),
    oct = 4,
    delay = (0, 0.25, 0.5, 0.75)
) + (0, 7, 12, 7)

k1 >> karp(
    var([drp[0], drp[0]+5, drp[0]+3], [8,4,4]),
    dur = 1/4,
    oct = PRand([5, 6, 7])
)

print(SynthDefs)

