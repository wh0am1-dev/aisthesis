# boudoir - relief de sang
# https://www.youtube.com/watch?v=TJkl4E1mF4g
# https://gist.github.com/jf-parent/004e97c7ea361722fe6829206ee4bdcf

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

def opening():
    print('opening')
    p4.reset() >> noise(
        [0, 1],
        dur = [.5, .25],
        amp = .4,
        hpf = linvar([800, 100], 16),
        mix = 1,
        room = 1,
        formant = var(P[:4], 8),
        oct = [3, 4, 5],
    ).after(45, 'stop')
    p5.reset() >> blip(
        [0, [1, 2]],
        dur = 4,
        vib = 2,
        oct = [4, 5],
        formant = 1,
        lpf = 1000,
        mix = 1,
        room = 10,
    ).after(45, 'stop')

def bg():
    print('bg')
    b1.reset() >> loop(
        'beat-1',
        dur = 4,
    )
    p1.reset() >> pluck(
        [0],
        dur = 12,
        amp = .4,
        vib = 2,
        room = 1,
        mix = 1,
    )
    p2.reset() >> sawbass(
        [1, (2, 3), (3, 4)],
        dur = [4, 8, 8],
        amp = .8,
        room = 1,
        mix = 1,
    )
    p3.reset() >> pasha(
        [0, 1],
        dur = [8, 6],
        oct = [4, [5, 6]],
        formant = [3, 2],
        amp = linvar([.6, 1.2], 12),
    )
    b2.reset() >> play(
        'U',
        sample = 2,
        dur = 4,
        amp = .4,
        delay = 2,
    )
    b4.reset() >> play(
        'Xx XXx',
        amp = .6,
        dur = var([1, 2], 64),
    )

def crime():
    print('crime')
    b3.reset() >> loop(
        'murder',
        dur = 32,
        amp = 1.2,
    ).after(32, 'stop')

def missing():
    print('missing')
    b6.reset() >> loop(
        'murder-2',
        dur = 32,
        amp = 1.2,
    ).after(32, 'stop')

def ending():
    print('ending')
    b7.reset() >> loop(
        'murder-3',
        amp = 1.2,
        dur = 60,
    ).after(60, 'stop')
    p4.reset() >> play(
        'x x(xX)',
        amp = .8,
    )

def text():
    print('text')
    p6.reset() >> pluck(
        [1, 3, 5],
        dur = 8,
        sus = 6,
        vib = 0,
        oct = 4,
        formant = 2,
    ).after(30, 'stop')
    p7.reset() >> bass(
        [2, 4, 6],
        dur = 8,
        delay = 1,
        oct = 4,
        formant = 2,
        sus = 6,
        lpf = 1000,
    ).after(30, 'stop')

def middle():
    print('middle')
    p8.reset() >> karp(
        [(1, 2), (3, 4), (4, 5), (3, 4)],
        dur = 8,
        room = 1,
        mix = 1,
        formant = 2,
        oct = 4,
    ).after(60, 'stop')

def closing():
    print('closing')
    p9.reset() >> squish(
        [0, 1],
        sus = 12,
        dur = 8,
        vib = 4,
        room = 1,
        mix = 1,
        oct = 4,
        lpf = 100,
        hpf = 1000,
    ).after(80, 'stop')
    b8.reset() >> loop(
        'murder-4',
        dur = 6,
        amp = .8,
    ).after(30, 'stop')
    b9.reset() >> loop(
        'murder-4',
        dur = 6,
        delay = 1,
        amp = 1.2,
    ).after(30, 'stop')
    b1.reset() >> loop(
        'murder-4',
        dur = 6,
        delay = 2,
        amp = 1.2,
    ).after(30, 'stop')
    Group(p9, b8, b9, b1).solo()

Clock.set_time(0)
Clock.future(0, opening)
Clock.future(30, bg)
Clock.future(45, crime)
Clock.future(80, missing)
Clock.future(100, text)
Clock.future(120, crime)
Clock.future(160, missing)
Clock.future(160, text)
Clock.future(220, middle)
Clock.future(300, ending)
Clock.future(360, closing)

