Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

~p1 >> play(
    P['V '],
    amp = .5,
    sample = 2,
    lpf = 400,
).every(5, 'stutter', 4, dur=3, cycle=8)

~p2 >> play(
    ' (nnnnnn[nn]n)',
    amp = .5,
)

~p3 >> play(
    P['  o   (OOO[OO]) '],
    amp = .5,
)

~p4 >> play(
    'funky',
    amp = .5,
    dur = .5,
    sample = PRand(4),
    rate = PRand([.5, 1, 2]),
)

~p5 >> play(
    "{ ppP[pP][Pp]}",
    amp = .5,
    sample = PRand(7),
    rate = PRand([.25, .5, 1, 2, 4]),
)

~s1 >> prophet(
    P[0, [P*(2, 1), 1], 3, [5, P*(5, 4)]],
    amp = 1,
    chop = 0,
)

~s2 >> pluck(
    P[0, 3, 0, 5] + (0, 1, 5),
    amp = 1,
    dur = 4,
    sus = 8,
    room = .5,
    mix = .5,
    vib = 12,
).every(8, 'offadd', 7)

~b1 >> space(
    [0, 3, 0, 5],
    dur = PDur(3, 8),
    oct = 4,
)

~b2 >> glass(
    [0, 3, 0, 5],
    dur = PDur(3, 8),
    oct = 4,
)
