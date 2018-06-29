Scale.default = Scale.chromatic
Root.default = 2
Clock.bpm = 120

a1.reset() >> ambi(
    P[0, 8, 5, 10],
    dur = [3, 3, 3, 2],
    oct = 4,
    coarse = [12,12,12,8],
    lpf = 1000,
    hpf =  800,
) + (0, [5, 7, 5, 7], 12)

p1.reset() >> pluck(
    P[0, 8, 5, 10],
    dur = [3, 3, 3, 2],
    sus = p1.dur,
    formant = 0.25,
    oct = 4,
    chop = P[16, 16, 16, 12] * 0.5,
    delay = (0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75),
    amp = 0.5
) + (0, 7, 12, 0, 12, 7, 0, [5, 7, 5, 7])

d1.reset() >> play(
    P["X  X  X  X "] &
    P["-- -- -- -[  --]"],
    dur = 1
)

d2.reset() >> play(
    P["{  ppP[pP][Pp]}"],
    sample = PRand(7),
    rate = PRand([0.5, 1, 2]),
    coarse = PRand([1, 2, 4, 8]),
    amp = 0.5,
    room = 0.5,
    mix = 0.5,
)

