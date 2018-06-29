Scale.default = Scale.chromatic
Root.default = 2
Clock.bpm = 120

t = [0, 7, 12, 17, 21, 26]

def s():
    print(SynthDefs)

p1.reset() >> play(
    P["X  X XX "],
    lpf = 800,
)

p2.reset() >> play(
    P["  O   O "],
    lpf = 800,
)

p3.reset() >> play(
    P["x n([--] )o n( [--])"].amen(),
    hpf = linvar([1000, 4000], 16),
    hpr = linvar([0.1, 1], 20),
    formant = [0, 1]
)

p4.reset() >> play(
    "<Vn><  h >",
    hpf = linvar([1000, 2000], 16),
    hpr = linvar([0.1, 1], 20)
).every(
    5,
    "stutter",
    4,
    dur = 3
)

a1.reset() >> ambi(
    [7, 0, 5, 0, 3],
    dur = [4, 4, 4, 4, 8],
    sus = [4, 4, 4, 4, 8],
    oct = 3,
    amp = 0.25
) + (0, 12, 24)

a2.reset() >> pads(
    [7, 0, 5, 0, 3],
    dur = [4, 4, 4, 4, 8],
    sus = [4, 4, 4, 4, 8],
    oct = 3,
    chop = [6, 6, 6, 6, 12],
    delay = (0, 1, 2),
    dist = 0.02
) + (0, 7, 12)

b1.reset() >> bass(
    var([7, 0, 5, 0, 3], [4, 4, 4, 4, 8]),
    dur = PDur(3, 8),
    oct = 4,
    delay = (0, 0.25),
    formant = (0, 1),
    lpf = 200,
    amp = 0.75
) + (0, 12)

k1.reset() >> keys(
    P[
        t[0], t[1], t[2],
        t[0], t[1], t[2],
        t[0], t[1]
    ] + P[
        var([7, 0, 5, 0, 3, 3], 4),
        var([7, 0, 5, 0, 3, 3], 4),
        0,
        var([7, 0, 5, 0, 3, 3], 4),
        var([7, 0, 5, 0, 3, 3], 4),
        0,
        var([7, 0, 5, 0, 3, 3], 4),
        var([7, 0, 5, 0, 3, 3], 4)
    ],
    dur = 0.5,
    echo = 0,
    amp = 0.5,
    formant = linvar([0, 1], 6),
    delay = (0, 0.5, 0.25)
) + (0, 7, 12)

