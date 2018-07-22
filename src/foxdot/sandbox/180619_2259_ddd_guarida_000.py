Scale.default = Scale.chromatic
Root.default = 2
Clock.bpm = 110
t = [0, 7, 12, 17, 19, 24] # 0-7-5-5-2-5

# ambient  wobwob  vision  kick  cow

ambient = Player()
def _ambient(time=9999):
    ambient.reset() >> ambi(
        P[3, 7, 2] + (0, 7),
        oct = 3,
        dur = 4,
        sus = 4, # + 2/3,
        room = .5,
        mix = .5,
    ).after(time, 'stop')
wobwob = Player()
def _wobwob(time=9999):
    wobwob.reset() >> ripple(
        [3, 2, 7, 2],
        dur = P[11, 1, 13, 11] / 3,
        sus = wobwob.dur, # + 2/3,
        room = .5,
        mix = .5,
        amp = 1.2,
        chop = wobwob.dur * 3,
    ).after(time, 'stop')
vision = Player()
def _vision(time=9999):
    vision.reset() >> prophet(
        [-1, (14, 26), -1],
        dur = P[rest(24), 1, rest(11)] / 3,
        sus = 2/3,
        room = .5,
        mix = .5,
        coarse = 4,
    ).after(time, 'stop')
kick = Player()
def _kick(time=9999):
    kick.reset() >> play(
        'X    ( XX)',
        dur = 2/3,
        lpf = 800,
        amp = .8,
    ).after(time, 'stop')
cow = Player()
def _cow(time=9999):
    cow.reset() >> play(
        # defghtET:+^%$@
        '      T          gT     ',
        dur = 1/3,
        amp = .8,
        lpf = 2000,
    ).after(time, 'stop')
