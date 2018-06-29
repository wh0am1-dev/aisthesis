Scale.default = "chromatic"
Root.default = 4
Clock.bpm = 120

tune = [0, 5, 10, 15, 19, 24]

p1.reset() >> play(
    P["V n([--] )O n( [--])"].amen(),
    sample = 3,
    rate = PRand([0.5, 1, 2]),
)

p2.reset() >> play(
    P["{  ppP[pP][Pp]}"],
    sample = PRand(7),
    rate = PRand([0.5, 1, 2]),
)

a1.reset() >> ambi(
    [0, 5, 3],
    dur = [16, 8, 8],
    sus = [16, 8, 8],
    oct = 4,
    coarse = [16, 16, 12],
    chop = [64, 32, 24],
    lpf = 400,
) + (0, 7, 12)

b1.reset() >> bass(
    var([0, 5, 3], [16, 8, 8]),
    dur = PDur(var([3, 5]), 8),
    oct = 4,
    delay = (0, 0.25),
    sus = P(0.125, 0.25) * 1,
    formant = 1
) + (0, 12)

k1.reset() >> keys(
    [0, 5, [3, P*(7, 8)]],
    formant = 1,
    dist = 0.01,
    dur = PDur(var([3, 5], 8), 8),
    echo = var([0.5, 1], 8),
)

