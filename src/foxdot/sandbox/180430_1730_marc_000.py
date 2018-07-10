Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

~n1 >> noise(
    P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),
    amp=P(.8,.7,.8,.7,.9)*.4,
    delay=P(PRange(5)/5),
    dur=.5,
    formant=(linvar([1,3],48), linvar([3,1],53)),
    chop=linvar([0,16],65),
    lpf=1200,
    lpr=(linvar([0,6],64), linvar([3,0],53))
)

~b1 >> blip(
    PRand(8) + P(0, PRand(4)),
    oct = 5,
    dur = PRand(2, 12) * 1.5,
    delay = (0, PRand(b1.dur) / 8),
    amp = 0.8,
    formant = 1
)

def k1solo():
    k1.solo()
    #Clock.schedule(k1stopsolo, Clock.now() + 16)
def k1stopsolo():
    k1.solo(0)
    #Clock.schedule(k1solo, Clock.now() + 16)
k1solo()

s1 >> soprano(
    [0,4,(3,1),2],
    dur=8,
    sus=s1.dur/2,
    amp=.5,
    lpf=1200)

s2 >> spark(
    (7,5,[4,[9,10]]),
    dur = PRand(6,24),
    delay= P(0,.125,.25) * .8,
    sus = .15,
    chop = 1,
    amp = 0.8
)

b1 >> bass(
    (k1.degree-1) + (0,2),
    dur = 8,
    amp = 0.4,
    echo = 1,
    decay = 1,
    sus = b1.dur - 1.5,
    formant = (0,1)
)

k1 >> soft(P[[1, 4, 9, [6, 9, 11]], [3, 5, 7, [6, 9, 11]]], dur=2, sus=20, amp=4, echo=2)

k1.solo()


