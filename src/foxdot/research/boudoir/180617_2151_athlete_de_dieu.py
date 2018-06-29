# boudoir - athlete de dieu
# https://www.youtube.com/watch?v=pWNQy00kqX0
# https://gist.github.com/jf-parent/c0d50ee96632218de09b57602ce483fb

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

def opening():
    print('opening')
    p1.reset() >> quin(
        P[(0, 2, 4), (4, 6, 8), (0, 2, 4), (1, 3, 5), (5, 7, 9)] & P[(0, 1, 2)],
        dur = 2,
        sus = 4,
        mix = linvar([0, 1], 8),
        room = 1,
        amp = .6,
        lpf = linvar([600, 1200], 4),
    ).every(
        4,
        'stutter',
    ).after(420, 'stop')

def phase1():
    print('phase1')
    p2.reset() >> bell(
        P[(0, 4, 8), (1, 3, 5), (0, 3, 7)],
        dur = 2,
        amp = linvar([1.2, 1.6], 8),
        room = 1,
        mix = linvar([0, 1], 16),
    ).after(30, 'stop')
    p3.reset() >> viola(
        P[(0, 1, 3), (8, 6, 7)] & P[(1, 5, 7)],
        dur = 12,
        sus = var([8, 10], 8),
        oct = var([4, 5], 8),
        room = 1,
        mix = 1,
        amp = .8,
    ).after(30, 'stop')

def perc():
    print('perc')
    p4.reset() >> play(
        '-x',
        dur = var([1, 2, 4], 8),
        amp = .8,
    ).after(30, 'stop')

def acme1():
    print('acme1')
    p5.reset() >> donk(
        P[(0, 4, 8), (1, 3, 5), (0, 3, 7)],
        dur = var([1, 2, 4], 8),
        amp = linvar([.2, 1.2], 8),
        mix = 1,
    ).after(60, 'stop')
    p6.reset() >> dub(
        P[(1, 2, 3)],
        dur = 2,
        room = 1,
        mix = 1,
        vib = 2,
        amp = .6,
    ).after(60, 'stop')
    p6.stop()

def perc2():
    print('perc2')
    p7.reset() >> play(
        ' L LL LLL',
        amp = linvar([.2, 1], 60),
    ).after(90, 'stop')
    p8.reset() >> play(
        '[ww][gg][kk][ggg][WW][WW][wWm][wWm]',
        amp = linvar([.2, 1], 90),
        vib = linvar([0, 2], 32),
        room = 1,
        mix = linvar([0, .4], 32),
    ).after(70, 'stop')

# Clock.set_time(0)
Clock.future(0, opening)
Clock.future(30, phase1)
Clock.future(45, perc)
Clock.future(60, acme1)
Clock.future(140, perc2)
Clock.future(260, perc2)
Clock.future(360, phase1)

