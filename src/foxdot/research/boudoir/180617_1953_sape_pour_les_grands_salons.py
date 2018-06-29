# boudoir - sape pour les grands salons
# https://www.youtube.com/watch?v=wOtZcsUrhNo
# https://gist.github.com/jf-parent/752a7eab8b52a9e69fb5d27ddf1804f0

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

def start1():
    print('start1')
    p1.reset() >> fuzz(
        P[:4],
        dur = 4,
        sus = 6,
        echo = 2,
        vib = linvar([0, 2], 12),
        oct = 4,
        room = 1,
        mix = 1,
        lpf = 800,
        pan = (-1, 1),
        amp = .4,
    ).after(220, 'stop')

def main1():
    print('main1')
    p2.reset() >> spark(
        P[-4, 8] | P[2, 8] | P[-2, 6] | P[5, 8] | P[(0, 1, 2, 4)],
        dur = [1, 1, 1, 2, 2],
        chop = var([0, 1], 24),
        mix = linvar([0, 1], 16),
        room = 1,
        formant = .3,
        oct = 4,
        vib = .2,
        amp = 1.2,
    ).every(
        8,
        'offadd',
        12,
    ).after(120, 'stop')

def main2():
    print('main2')
    p3.reset() >> pulse(
        P[(1, 2), (2, 3), (4, 5), (8), (4, 5), (2, 3)],
        dur = [1, 1, 1, 4, 1, 1],
        sus = [1, 1, 1, 4, 1, 1],
        oct = var([4, 5], 12),
        formant = linvar([0, 1], 48),
        mix = var([0, 1], 24),
        room = 1,
        vib = [0, 0, 0, 1, 0, 0],
    ).after(45, 'stop')

def main3():
    print('main3')
    p4.reset() >> bell(
        [(5, 3), (1, 2), (7, 8), (2, 3)],
        oct = var([4, 5], 16),
        amp = .4,
    ).every(
        4,
        'offadd',
        12,
    ).after(180, 'stop')

def perc1():
    print('perc1')
    b1.reset() >> play(
        '-x',
        sample = var([0, 1], 4),
        amp = .3,
    ).after(180, 'stop')

def perc2():
    print('perc2')
    b2.reset() >> play(
        't g gg I II',
        sample = 1,
        amp = .5,
    ).after(120, 'stop')
    b3.reset() >> play(
        '(x)([xx][^^][x^][^^^] )',
        sample = 2,
        amp = .5,
    ).after(120, 'stop')

def end2():
    print('end2')
    p5.reset() >> glass(
        P[-2:8],
        dur = 12,
        formant = 1,
        oct = 4,
        room = 1,
        mix = 1,
        blur = 1,
        lpf = 1600,
        amp = linvar([1, 1.4], 120),
    ).after(120, 'stop')

# Clock.set_time(0)
Clock.future(0, start1)
Clock.future(25, perc1)
Clock.future(30, perc2)
Clock.future(45, main1)
Clock.future(80, main3)
Clock.future(150, main2)
Clock.future(200, main1)
Clock.future(320, end2)

