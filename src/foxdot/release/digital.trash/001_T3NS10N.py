# wh0am1 - 001_T3NS10N

Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 120

var.base = P[0, 5]


p1.reset() >> play(
    P["V n([--] )O n( [--])"].amen(),
    sample=2,
    lpf=linvar([500,1500],16), lpr=linvar([0.1,1],20),
    # lpf = 0, lpr = 0,
)


p2.reset() >> play("funky", dur=0.5, rate=PRand([0.5,1,2]), amp=PWhite(0.25,1))


s1.reset() >> snick(oct=PRand([5,6,7]), dur=PDur(3,8), amp=2, pan=PWhite(-1,1))


s2.reset() >> scatter([(0,7,12)], oct=4, amp=2, delay=(0,0.25,0.5))


a1.reset() >> ambi(var.base + (0,7,12), dur=16, coarse=[8,16], chop=0)


m1.reset() >> donk(var.base + PWalk(2), scale=Scale.egyptian, dur=[0.5,0.25,0.25], oct=PRand([5,6,7]), pan=[-1,1])


a2.reset() >> pluck(var(var.base, 4), dur=0.5).every(3, "offadd", [1,3,8], dur=0.25)


x1.reset() >> dbass(var(var.base, 8), dur=PDur(3,8), oct=4, lpf=800, lpr=0.1, hpr=500, shape=0.25)
