# boudoir - karate commando
# https://www.youtube.com/watch?v=OPWOPIhAgrg
# https://gist.github.com/jf-parent/19bd98dcc2bf60a3fe941b98ed47fff8

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

def opening():
    print('opening')
    p2.reset() >> pads(
        P[0, 1],
        dur = 4,
        oct = [4, 5],
        vib = .2,
        amp = [.6, .8],
        room = .5,
        mix = .5,
    ).after(250, 'stop')
    p3.reset() >> fuzz(
        P[0:4],
        dur = 4,
        lpf = 1200,
        room = 10,
        mix = 10,
        oct = 4,
        vib = 0,
        verb = 2,
        amp = .4,
    ).after(250, 'stop')
    p4.reset() >> pluck(
        P[0, 2, 4, 6, (6, 7), 4, 2],
        dur = 2,
        room = 10,
        mix = 10,
        verb = 2,
        amp = 1.2,
        lpf = [1000, 1400],
        sus = 6,
        oct = [4, 5],
        pan = (-1, 1),
    ).after(250, 'stop')

def perc():
    print('perc')
    p7.reset() >> play(
        'X(g[gg][ggg][gggg])ttl[hhj][jj][vRR]',
        amp = linvar([.2, .3], 12),
    ).after(215, 'stop')

def acme():
    print('acme')
    p6.reset() >> pluck(
        P[(1, 2), (2, 3, 1), (3, 4, 1), ([5, 6, 7, 8, 9], 9)],
        dur = [1, 1, 1, 6],
        amp = 1.6,
        oct = var([3, 4, 5], 9),
        lpf = var([2400, 1200, 800], 9),
        sus = [2, 2, 2, 8],
        vib = [0, 0, 0, .8],
    ).after(64, 'stop')

def final():
    print('final')
    p1.reset() >> viola(
        P[(1, 2, 3), 4, (5, 3, 4), (4, 2, 3), (7, 8), 1],
        dur = [2, 4, 2, 2, 4, 2],
        vib = [0, 1.2, 0, 0, 0.2, 0],
        sus = [4, 5, 4, 4, 5, 4],
        oct = 4,
        lpf = 800,
        room = 10,
        mix = 5,
        verb = 2,
    ).after(42, 'stop')

Clock.set_time(0)

Clock.future(0, opening)
Clock.future(15, perc)
Clock.future(30, acme)
Clock.future(120, acme)
Clock.future(188, final)
