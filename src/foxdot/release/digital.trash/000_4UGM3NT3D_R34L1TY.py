# wh0am1 - 000_4UGM3NT3D_R34L1TY

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120
t = [0, 5, 10, 15, 19, 24]
d = [0, 7, 12, 17, 21, 26]

Samples.addPath('C:/Users/wh0am1/software/livecoding/samples/databenders/')

Clock.set_time(0)

def pre():
    print('in')
    l1.reset() >> loop(
        'drums/kicksub/sub-hit',
        dur = PDur(3, 8) * 4,
        rate = .8,
        chop = 300,
        amp = .2,
    ).after(500, 'stop')
Clock.future(0, pre)
def intro():
    print('intro')
    x1.reset() >> ripple(
        (0, 1),
        dur = 8,
        sus = 6,
        lpf = 800,
        formant = [0, 1],
        room = 1,
        mix = 1,
        tremolo = 4,
    ).after(368, 'stop')
    s1.reset() >> pulse(
        [0],
        room = 1,
        mix = .5,
        verb = 1,
        sus = 2,
        oct = (2, 4),
        fmod = linvar([.2, 5]),
        amp = .2,
    ).after(32, 'stop')
Clock.future(32, intro)
def perc0():
    print('perc0')
    p1.reset() >> play(
        'Wl(g[gg][ggg][gggg])',
        amp = .5,
        dur = PDur(3, 8) * 2,
        rate = PRand([0.5, 1, 2]),
        formant = 1,
        lpf = 1000,
    ).after(64, 'stop')
    x2.reset() >> swell(
        [0, 8],
        dur = 8,
        sus = 10,
        formant = [0, 1],
        mix = 1,
        delay = 10,
        amp = .6,
    ).after(64, 'stop')
Clock.future(64, perc0)
def perc1():
    print('perc1')
    p3.reset() >> play(
        'V',
        dur = 2,
        lpf = 1200,
    ).every(
        8, 'stutter', 4, dur=3, rate=.25
    )
Clock.future(128, perc1)
def p3_dur1():
    print('p3_dur1')
    p3.dur = 1
    p3.delay = .5
    l2.reset() >> loop(
        'drums/kicksub/kick-hard',
        dur = 1,
        room = .5,
        mix = .5,
    ).every(5, 'stutter', hpf=6500)
Clock.future(160, p3_dur1)
def p3_dur38():
    print('p3_dur38')
    p3.dur = PDur(3, 8)
Clock.future(192, p3_dur38)
def bridge():
    print('bridge')
    l2.stop()
    p3.dur = 1
    p3.delay = 0
    perc0()
Clock.future(224, bridge)
def sanity():
    print('sanity')
    p3.stop()
    x2.reset() >> swell(
        [0, 8],
        dur = 8,
        sus = 10,
        formant = [0, 1],
        mix = 1,
        delay = 10,
        amp = .6,
    ).after(64, 'stop')
Clock.future(256, sanity)
def insanity():
    print('insanity')
    n1.reset() >> snick(
        oct = PRand([4, 5, 6]),
        dur = PDur(3, 8),
        amp = 2,
        pan = PWhite(-1, 1),
        shape = .5
    )
Clock.future(288, insanity)
def dooonk():
    print('dooonk')
    m1.reset() >> donk(
        P[0, 5] + PWalk(2),
        dur = P[.5, .25, .25] * var([1, 2], [12, 4]),
        oct = PRand([5, 6, 7]),
    )
Clock.future(320, dooonk)
def safety():
    print('safety')
    n1.stop()
    Clock.future(16, lambda: m1.stop())
Clock.future(352, safety)
def end():
    print('end')
    p3.reset() >> play(
        'V',
        dur = 1,
        lpf = 1200,
    ).after(64, 'stop')
    x2.reset() >> swell(
        [0, 8],
        dur = 8,
        sus = 10,
        formant = [0, 1],
        mix = 1,
        delay = 10,
        amp = .6,
    ).after(72, 'stop')
Clock.future(372, end)

p2.reset() >> play(
    'funky',
    dur = var([.5, .25], [12, 4]),
    amp = .2,
    rate = PRand([.5, 1, 2])
)
