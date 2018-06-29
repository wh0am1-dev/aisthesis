# boudoir - solivagant
# https://www.youtube.com/watch?v=-zKUM_FhIOs
# https://gist.github.com/jf-parent/28871f89d06f1fd01724e43a1992ee4d

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

p1.reset() >> glass(
    P[0, 3, 0, 3] & P[5, 6, 7, 8],
    oct = var([3, 4, 5, 2], [8, 8, 4, 4]),
    pan = var([-1, 1], 4),
    amp = .8,
)

p2.reset() >> star(
    P[[1, 2], [2, 3], [3, 4]] & P[5],
    dur = 4,
    vib = 4,
    oct = var([4, 5], [4, 16]),
    sus = 6,
    fmod = var([0, 1, 2], 4),
    amp = var([.6, .8, 1], 8),
)

p3.reset() >> play(
    '[Ex][gg]',
    dur = var([2, 1], [64, 8]),
    sample = 1,
    amp = .6,
)

p4.reset() >> razz(
    P[0, 1],
    dur = var([2, 4], 4),
    sus = 4,
    vib = var([0, 1], 4),
    amp = var([.6, .8, 1], 8),
)

p5.reset() >> play(
    'g',
    sample = var([0, 1], [2, 4]),
    amp = .4,
)

p6.reset() >> play(
    '[tT]',
    dur = var([2, 1], [8, 8]),
)

p7.reset() >> bell(
    P[0, 1],
    amp = var([.8, 1, 1.2], 8),
)

