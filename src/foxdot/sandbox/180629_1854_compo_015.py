Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

# t = [0, 7, 12, 17, 21, 26]
var.ch = P[0, 2]

~p1 >> play(
    'Vn([www] )( [tt])',
    dur = 2,
)

~p2 >> play(
    ' [(ab)(md)] ([ff][kkk])'
)

~p3 >> play(
    '<Vn><  h >',
).spread().every(16, 'stutter', 4, dur=3)

~a1 >> ambi(
    var.ch + (0, [3, 5, 1, 8]),
    dur = 4,
    oct = 4,
    vib = .2,
    coarse = 6,
)

~a2 >> prophet(
    var.ch + [0, -2, P*(6, 7), 4],
    pan = (-1, 1),
    amp = 1.5,
).every(6, 'offadd', 7, cycle=8)

~b1 >> sawbass(
    var.ch,
    dur = PDur(3, 8) * 2,
    formant = 1,
).spread().every(6, 'offadd', 5, cycle=8)
