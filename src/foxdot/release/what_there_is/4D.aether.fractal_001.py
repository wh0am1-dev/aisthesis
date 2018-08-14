Scale.default = 'minor'
Root.default = 0
Clock.bpm = 120

def one23(mod, f):
    if Clock.now() % mod == mod - 1:
        f()
    else:
        Clock.future(1, lambda: go(mod))

var.ch = var([5,1,3,0],8)

~p1 >> play('x(...v)v', amp=.8, dur=2/3, room=1).often('rate.offmul', 1.5, 1/3)

~p1 >> play('x(.|p4|.|q1|)v', amp=.8, dur=2/3, room=1).every(23, 'jump', ahead=-1, rate=1.5, cycle=24)

~s1 >> sawbass(var.ch, amp=.6, dur=8, chop=8, coarse=16, cutoff=linvar([1000,7000],32), room=1).every(8, 'offadd', 7, 1/3)

~s3 >> donk([0,[3,4,7]], amp=.1, dur=PDur(3,8), oct=[5,6,4], drive=.5).every(5, 'stutter', 2, dur=.5, oct=6)

~p2 >> play('V.', amp=.6, lpf=800, room=1)

~s2 >> space(var.ch+[0,[7,5],3], amp=.6, dur=[2,2,4], room=1, oct=4, shape=.125).spread()
~s2 >> space(var.ch+[0,[7,5],3], amp=linvar([.6,0],[2,0,2,0,4,0]), dur=[2,2,4], room=1, oct=4, shape=.125, chop=P[4,4,8]).spread()
~s2 >> space(var.ch+[0,[7,5],3]+(0,2), amp=linvar([.6,0],[2,0,2,0,4,0]), dur=[2,2,4], room=1, oct=4, shape=.125, chop=P[4,4,8]).spread()
~s2 >> space(var.ch+[0,[7,5],3]+(0,2), amp=linvar([.6,0],[2,0,2,0,4,0]), dur=[2,2,4], room=1, oct=4, shape=.125, chop=P[4,4,8], delay=(0,[.5,.5,1])).spread().sometimes('offadd', 5)

~s4 >> klank((0,2,4), amp=.8, dur=8)

~p3 >> play('.n', amp=.8, room=1).sometimes('stutter', 4, dur=3, rate=[.5,2])

p_all.stop()

### > block <
s2.every(4, 'degrade')
def go_penta():
    Group(s1,s2).stop()
    ~s3 >> donk([0,[3,4,7]], amp=.1, dur=PDur(3,8), oct=[5,6,4], drive=.5).every(5, 'stutter', 2, dur=.5, oct=6).penta()
Clock.future(16, go_penta)
###

~s4 >> klank((0,2,4), amp=.8, dur=8, formant=1)

~p5 >> play('funky', amp=.4, dur=.5, sample=PRand(5), pan=PWhite(-1,1), rate=PRand([.5,1,2]))

~s5 >> soprano(s4.pitch, amp=.6, vib=12, oct=4, coarse=var([3,4],8), shape=.125).penta()

~p4 >> play('V(sss[ss]ss[ss]s)', amp=.6, lpf=0, room=1)

~s6 >> pulse(P[:16].shuffle().layer('mirror'), dur=var([.5,.25],8), amp=PRand([0,.075])[:32], oct=PStep(4,5,4), drive=.5, striate=(0,1), bits=[1,8]).penta().every(6, 'splice', [6,7])
~s6 >> saw(P[:16].shuffle().layer('mirror'), dur=.25, amp=PRand([0,.075])[:32], oct=PStep(4,5,4), drive=.5, striate=(0,1), bits=[1,8]).penta().every(6, 'splice', [6,7])

p5.stop()
s5.stop()
s4.stop()

### > block <
~s6 >> saw(P[:16].shuffle().layer('mirror'), dur=.25, amp=PRand([0,.075])[:32], oct=PStep(4,5,4), drive=.5, striate=(0,1), bits=[1,8]).every(6, 'splice', [6,7])
~s3 >> donk([0,[3,4,7]], amp=.1, dur=PDur(3,8), oct=[5,6,4], drive=.5).every(5, 'stutter', 2, dur=.5, oct=6)
###

s6.every(4, 'degrade')
Clock.future(16, s6.stop)
Clock.future(32, p4.stop)
Clock.future(38, Clock.clear)
