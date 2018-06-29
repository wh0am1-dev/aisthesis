# boudoir - meutre de feutre homeoteleute
# https://www.youtube.com/watch?v=fKhNcCht9n4
# https://gist.github.com/jf-parent/83de1aadb2a218b50c93fd734030bd76

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

def opening():
    print('opening')
    p3.reset() >> ripple(
        P[(0, 1)],
        dur = 8,
        sus = 6,
        lpf = 800,
        formant = [0, 1],
        room = 1,
        mix = 1,
        tremolo = 4,
    ).after(30, 'stop')
    p5.reset() >> swell(
        [0, 8],
        dur = 8,
        sus = 10,
        formant = [0, 1],
        mix = 1,
        delay = 10,
        amp = .6,
    )

def main1():
    print('main1')
    p6.reset() >> lazer(
        [0, [(2, 3), (5, 6)]],
        dur = 4,
        formant = 3,
        lpf = 800,
        tremolo = var([0, 3], 4),
        amp = .4,
    ).after(90, 'stop')
    b4.reset() >> play(
        '^ ^^ ^^^ ^^^^',
        amp = .8,
    ).after(90, 'stop')
    b5.reset() >> play(
        'gA[gg]{A }[ggg]{[AA] }',
        amp = .8,
    ).after(90, 'stop')

def perc():
    print('perc')
    b1.reset() >> play(
        '-x',
    )
    b2.reset() >> play(
        'k kk',
        amp = .4,
    )
    b3.reset() >> play(
        'I',
        sample = P[1, 0],
        dur = 4,
        amp = 1.2,
    )
    p4.reset() >> donk(
        [0],
        dur = 2,
        tremolo = 4,
        pan = [-1, 1],
        oct = var([6, 7], 4),
        formant = 2,
        amp = .6,
    )

def main2():
    print('main2')
    p2.reset() >> sawbass(
        P[(0, 1), [(1, 2), (2, 3)], [(4, 5), (5, 6)], (1, 2)],
        lpf = 1000,
        amp = linvar([0, .2, .6, 1], [60, 10, 10, 99999]),
        oct = var([5, 6], 16),
        formant = var([0, 1, 2], 8),
        tremolo = linvar([0, 4], 16),
    ).every(
        2,
        'offadd',
        2,
    ).after(120, 'stop')

def final():
    print('final')
    p1.reset() >> pulse(
        P[(0, 1), (2, 3), [(4, 5), (5, 6), (6, 7)], (3, 4)] & P[(0, 1, 2)],
        dur = var([1, 2], [16, 4]),
        tremolo = var([0, 2], [32, 12]),
        oct = var([4, 5, 6], 32),
        formant = var([0, 1, 2], 4),
        vib = linvar([0, 3], 64),
        room = var([0, 1], [64, 6]),
        mix = 1,
        amp = linvar([0, .2, .6, 1], [200, 10, 10, 360]),
        lpf = 400,
    ).every(
        2,
        'offadd',
        9,
    ).after(20, 'stop')
    p1.solo()

Clock.set_time(0)

Clock.future(0, opening)
Clock.future(30, perc)
Clock.future(45, main2)
Clock.future(160, main1)
Clock.future(280, main2)
Clock.future(420, final)
