Scale.default = Scale.chromatic
Root.default = 2
Clock.bpm = 100

t = [0, 7, 12, 17, 21, 26]

a1.reset() >> star(
    [(t[0],t[1],t[2],t[3]+2,t[4]+3,[t[5]+2,t[5]+1])],
    dur = 8,
    sus = 12,
    oct = 3,
    coarse = 0,
    room = 1,
    mix = 0.8,
)

a2.reset() >> prophet(
    [P*(t[0],t[1],t[2],t[3]+2), t[3]+3, t[4]+2, t[4]+3, t[4]+2, t[3]+3, (t[0],[t[3]+2,t[3]+7])],
    dur = [0.5]*6 + [5],
    sus = a2.dur,
    dist = 0.1,
    oct = 6,
)

b1.reset() >> bass(
    0,
    oct = 5,
    dur = PDur(var([3,5], 8), 8)
).every(4, "offadd", [3,5,7])

p1.reset() >> play(
    "{ ppP[pP][Pp]}",
    sample = PRand(7),
    rate = PRand([0.5, 1, 2]),
    dur = 0.5,
)

p2.reset() >> play(
    P["<Vs><  (nO) >"],
    sample = 2,
).every(5, "stutter", 4, dur=3)

p3.reset() >> play(
    "funky",
    rate = PRand([0.5,1,2]),
    dur = 0.25,
    amp = PWhite(0, 1),
)

p4.reset() >> play(
    "----",
    dur = 0.25
).every(4, "stutter", 4, dur=0.5)

p5.reset() >> play(
    "  h  h h"
)

