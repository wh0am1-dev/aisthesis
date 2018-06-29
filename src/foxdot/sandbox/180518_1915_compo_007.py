Scale.default = "minor"
Root.default = 0
Clock.bpm = 120

p1 >> play(
    P["<V   >< t >"],
    lpf = 0,
    shape = 0,
    pan = 0,
).every(
    5,
    "stutter",
    4,
    dur = 3,
)

p2 >> play(
    "[--]",
    hpf = linvar([5000, 10000], 12),
    hpr = linvar([0.1, 1], 20),
).every(4, "stutter", 3, dur = 4)

b1 >> bell(
    PRand(10),
    dur = PRand([4, 6]),
    sus = 6,
    chop = 4,
    amp = 1,
)

b2 >> bass(
    b1.degree,
    dur = PDur(5, 8),
    coarse = 0,
    chop = 2
).every(8, "reverse")

# ================================

a1 >> ambi(
    [0, 2, P*(4, 6, 5), [7, 10]],
    dur = 4,
    pan = linvar([-1, 1], 16),
    oct = 4,
) + (0, 3, 5)

