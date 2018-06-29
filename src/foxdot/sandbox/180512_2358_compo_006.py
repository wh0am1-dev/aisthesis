s1 >> play("x[--]h[--]xh[--o]x", swell = 10).every(3,'reverse')

s1.stop_calling_all()

s2 >> blip().follow(p1) + (0, P*(2,4))


s2.stop()


Root.default = -10

Scale.default = Scale.indian

p1 >> gong(
    [0,[2,4],P+(3,5),[P*(5,6,4),P*(5,6,7)]],
    dur = 2,
) + (0, 7)

p2 >> soprano(
    p1.degree,
    dur = 4,
    chop = 0,
    oct = var([3, 2],16),
    pan = linvar([-1,0,1,0], 2),
    amp = 0.5,
    coarse = 16
)

p3 >> donk(
    0,
    dur = PRand(10) + .125,
    delay = (0, PRand([0, PRand(p3.dur)/3])),
    amp = linvar([.25, .5], PRand(8, 32)),
    lpf = linvar([2200, 4000], PRand(36)),
    oct = PRand([5, 6]),
) + (0, 2)

p4 >> soprano(
    [0, 4, (3, 1), 2],
    dur = 8,
    sus = p4.dur / 2,
    amp = 0.5,
    lpf = 1200,
    slide = var([-1, 1], 16),
    coarse = 24,
    oct = 4,
    pan = PWalk(-1,1),
)

p5 >> play(
    "{  N@[N@][@N]}",
    dur = 2,
    sample = PRand(2),
    rate = PRand([-0.5, 0.5, 1.0]),
    amp = 0.25,
    hpf = 1500,
    delay = (0, 0.25, 0.75),
    pan = PRand(-1, 1),
)

pattern = P[]

# https://www.youtube.com/watch?v=TklM2-lSby4





















