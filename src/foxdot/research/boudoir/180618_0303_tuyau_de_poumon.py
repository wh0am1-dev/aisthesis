# boudoir - tuyau de poumon
# https://www.youtube.com/watch?v=JdjdVPwlVfE
# https://gist.github.com/jf-parent/a9960737d0567ea4b4bce303a7af4e39

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

var.chords = [(0, 1, 2), (1, 4, 5), (2, 6, 7), (0, 1, 3)]

p1.reset() >> nylon(
    var.chords,
    dur = 4,
    sus = 5,
    lpf = 2000,
    vib = linvar([0, 1], 16),
    amp = linvar([.6, 1.2], [16, 32]),
)

p2.reset() >> pulse(
    var.chords,
    dur = var([4, 2, PDur(3, 8)], [64, 32, 16]),
    vib = var([0, 1], 4),
    amp = linvar([.6, 1.2], [16, 32]),
    oct = var([4, 5, 6], 16),
    lpf = 1000,
).every(
    8,
    'stutter',
)

p5.reset() >> play(
    '.g...gg',
    dur = var([1, 2], [16, 8]),
    amp = var([.2, .6], [32, 8]),
)

p4.reset() >> razz(
    [(0, 1), (1, 5), (1, 5), (6, 7, 8, 9), (1, 5)],
    dur = 2,
    sus = 3,
    oct = var([4, 5, 6], [16, 16, 32]),
    vib = linvar([0, 2, 5], 16),
    lpf = 1200,
    pan = (-1, 1),
    amp = linvar([.6, 1.2], [32, 16]),
)

p6.reset() >> play(
    '3141',
    sample = var([0, 1, 2, 3, 4, 5], 1),
    dur = var([2, 4, 8], [16, 8, 4]),
    amp=.1,
)

p7.reset() >> play(
    '[VVXX]...VV...XX',
    dur = 1,
    amp = .7,
    lpf = 2000
)

