# boudoir - seuil enforce
# https://www.youtube.com/watch?v=EdqKe4tDhwg
# https://gist.github.com/jf-parent/0146e0301478e1322dd3bcd9f237a2b8

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

def intro():
    print('intro')
    p1.reset() >> sawbass(
        P[(0, 1), (2, 4), (4, 5), (1, 2)],
        dur = 8,
        formant = 2,
        oct = 4,
        lpf = [400, 600, 600, 400],
        room = 1,
        mix = 1,
        amp = 1.2,
    ).after(420, 'stop')

def second():
    print('second')
    p2.reset() >> pulse(
        [(0, 1, 2), (4, 5, 6), (3, 4, 5), (2, 3, 4)],
        dur = 8,
        oct = 4,
        sus = 2,
        lpf = 500,
        formant = 2,
        amp = .5,
    ).after(400, 'stop')
    b1.reset() >> play(
        'V Vv VvV',
        sample = 0,
        amp = .2,
        delay = 4,
    ).after(400, 'stop')

def acme():
    print('acme')
    b2.reset() >> play(
        '[--][kk][kk][kkk]',
        amp = .2,
    ).after(30, 'stop')
    b3.reset() >> play(
        'I',
        dur = 8,
        sample = [0, 1, 2],
    ).after(30, 'stop')

def middle():
    print('middle')
    p3.reset() >> fuzz(
        [0, P[:8]],
        dur = 4,
        vib = 3,
        oct = 5,
        formant = [0, 3, 6],
        lpf = 900,
        amp = .4,
    ).after(70, 'stop')
    p5.reset() >> swell(
        [0, P[:4]],
        dur = 8,
        sus = 6,
        oct = 4,
        amp = .2,
        mix = 1,
        room = 1,
        vib = 0.5,
        formant = [0, 2, 4],
    ).after(70, 'stop')

def danger():
    print('danger')
    p4.reset() >> growl(
        [0, P[4:8]],
        dur = var([2, 4], 8),
        oct = 4,
        sus = 2,
        tremolo = [2, 3],
        formant = linvar([2, 4], 16),
        lpf = 1600,
    ).after(60, 'stop')
    p6.reset() >> blip(
        [0, [4, 5]],
        dur = 8,
        oct = 3,
        sus = 4,
        formant = 5,
        chop = 0.5,
        amp = .6,
    ).after(60, 'stop')

Clock.future(0, intro)
Clock.future(30, second)
Clock.future(60, acme)
Clock.future(80, middle)
Clock.future(140, acme)
Clock.future(160, danger)
Clock.future(200, acme)
Clock.future(240, middle)
Clock.future(320, danger)

