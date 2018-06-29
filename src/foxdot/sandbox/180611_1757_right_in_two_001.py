Scale.default = Scale.chromatic
Root.default = 2
Clock.bpm = 110

t = [0, 7, 12, 17, 21, 26]

var.base = P[t[0], t[0]+8, t[0]+5, t[0]+10]
var.dur  = P[   3,      3,      3,       2]

a1.reset() >> klank(
    var.base + (0, 7, 12),
    dur = var.dur,
    sus = var.dur - 1,
    oct = 4,
)

a2.reset() >> ambi(
    var.base + (0, 24),
    dur = var.dur,
    sus = var.dur + 1,
    oct = 3,
    tremolo = 1,
)

Group(a1, a2, p1).only()

p1.reset() >> play(
    "{ ppP[pP][Pp]}",
    amp = PWhite(0.5, 1),
    sample = PRand(7),
    rate = PRand([0.5, 1, 2]),
    room = 0.5,
    mix = 0.5,
)

p2.reset() >> play(
    "  V  V  V V",
    dur = 1,
    lpf = linvar([500, 1500], 22),
    lpr = linvar([0.1, 1], 11),
)

p3.reset() >> play(
    "H  H  H  H ",
    amp = 0.5,
    hpf = linvar([2000, 3000], 22),
    hpr = linvar([0.1, 1], 11),
)

b1.reset() >> bass(
    var(var.base, var.dur),
    dur = PDur(4, 11),
    oct = 5,
    shape = 0.125,
).every(11, "offadd", 7)

