# Kolmogorov Toolbox - FoxDot J0M
# https://youtu.be/wzD3M49LUGo

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 130

r1.reset() >> pulse(
    1,
    room = 1,
    verb = 1,
    mix = .5,
    sus = 2,
    oct = (4, 2),
    fmod = linvar([.2, 5]),
    lpf = 1200,
)

r2.reset() >> play(
    "..-..+",
    rate = (10, .2),
    cut = .1,
    dur = PDur(3, 5) * 4,
    hpf = 5000,
    chop = 300,
    amp = .2,
    room = .6,
    mix = .5,
)

r2.amp = .4
r2.amp = 1
r2.cut = .2
r2.cut = .4
r2.degree = "(.m).-..+"
r2.degree = "(.ms).-..+"
r2.degree = "(.m.s).-..+"
r2.degree = "(.m.sPr).-..+"
r2.degree = "(.m.sPr).-([--][hhhhh]).+"
r2.pan = [1, -1]
r2.chop = linvar([300, 3000], 100)
r2.dist = 0.01
r2.dist = 0.05
r2.dist = 0.08
r2.degree = "(.m.sPr).-([--][hhhhh])(.Wlg)+"
r2.degree = "(.m.sPr).-([--][hhhhh])(.Wlg3)+"
r2.degree = "(.m.sPr).-([--][hhhhh]...)..(.Wlg3)+"
r2.degree = "(.m.sPr).-([--][hhhhh]...)..(.Wl.g3)+"

g1.reset() >> play(
    "t.l.",
    dur = 2,
    room = .8,
    mix = .8,
    echo = linvar([.2, .8]),
    amp = .1,
)

r2.dur = PDur(3, 5) * 2

g1.amp = .2
g1.amp = .4
g1.amp = .5
g1.degree = "x.l."
g1.echo = [.5, 1]
g1.lpf = 1200
g1.amp = .8
g1.amp = 1
g1.amp = 2

r3.reset() >> saw(
    [[5], [1]],
    lpf = 1200,
    oct = (4, 6),
    fmod = 10,
    chop = 400,
    amp = .2,
)

r3.degree = [5]
r3.degree = (5,1)
r3.chop = 4000
r3.chop = linvar([400, 4400], 20)
r3.sus = 1.5
###
r3.room = 1
r3.mix = 1
r3.verb = .6
###
r3.amp = .4

g2.reset() >> play(
    "(pm)-.[hh]",
    chop = 4,
    amp = .1,
    verb = 1,
    dur = 2,
)

###
r3.lpf = linvar([2400, 400], 20)
r3.lpr = .5
###
r3.chop = linvar([400, 4400], 2)

g1.echo = [.5, .8]

g2.degree = "(pm)-.[hhhh]"

r3.bits = 8
r3.bits = 5
r3.bits = 6
###
r3.bits = 4
r3.amp = .2
###
r3.pan = linvar([-1, 1])

###
g2.degree = "(pm)-.([hhhh][hh])"
g2.lpf = 2000
###

r1 >> saw(1)

r4.reset() >> glass(
    1,
    room = 1,
    verb = 1,
    mix = .5,
    sus = 2,
    oct = (4, 2),
    fmod = linvar([.2, 5]),
    lpf = 1200,
    pan = [-.5, .5]
)

r4.oct = (4, 5)
r4.sus = 1
r4.oct = 5
r4.chop = 100
r4.amp = 1.1
r4.amp = 1.2
r4.oct = 1

g1.dist = 0.02
g1.dist = 0.04
g1.dist = 0.05
g1.dist = 0.06
g1.dist = 0.09
g1.dist = 0.1

g3.reset() >> pulse(
    -2,
    lpf = linvar([0, 2000]),
    lpr = .2,
    amp = .2,
    fmod = 2,
)

