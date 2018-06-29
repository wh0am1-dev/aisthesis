Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 120

p1.reset() >> play(
    "<Vs><  n >",
    formant = 0,
    pan = 0,
).every(3, "stutter", 2, dur=1)

b1.reset() >> sawbass(
    var([0, 5, 3, 4], 4),
    dur = PDur(3, 8),
    oct = 4,
    formant = 0.5,
    hpf = 1000,
    pan = (-1, 1),
    delay = (0, 0.25, 0.5),
) + (0, 7, 5)

