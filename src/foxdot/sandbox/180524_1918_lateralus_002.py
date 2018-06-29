Scale.default = "chromatic"
Root.default = 2
Clock.bpm = 120

drp = [0, 7, 12, 17, 21, 26]
std = [0, 5, 10, 15, 19, 24]

p1 >> play(
    "<Vs><  n >",
    sample = 2,
).every(5, "stutter", 2, dur=3)

p2 >> play(
    "{  ppP[pP][Pp]}",
    sample = PRand(5),
    rate = PRand([0.5, 1, 2]),
)

a1 >> karp(
    oct = PRand([4, 5, 6]),
    dur = 1/4,
    hpf = linvar([1000, 2000], 16),
    hpr = linvar([0.1, 1], 20)
)

a2 >> ambi(
    [0, 5, 3],
    dur = [8, 4, 4],
    oct = 4,
) + (0, 7, 12)

b1 >> bass(
    var([0, 5, 3], [8, 4, 4]),
    dur = PDur(var([3, 5]), 8),
    delay = (0, 0.25),
).spread().every(3, "offadd", 7)

Group(b1, a1, p2).solo()

p3 >> play(
    P["  h "].layer("mirror"),
    shape = 0.5,
    chop = 4,
    rate = PRand([1, 2, 4]),
    slide = 1,
)

a3 >> piano(
    [0, 5, 3],
    dur = [8, 4, 4],
    oct = 4,
    delay = (0, 0.25, 0.75),
) + (0, 7, 12)

p4 >> play(
    P["VnOn"].amen(),
)

