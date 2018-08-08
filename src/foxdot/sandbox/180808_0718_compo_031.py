Scale.default = 'minor'
Root.default = 0
Clock.bpm = 120

var.ch = var([0,5,1,3],8)

# ================================================

~p1 >> play('x(...v)v', amp=.8, dur=2/3, room=1).often('rate.offmul', 1.5, 1/3)
~p2 >> play('V.', amp=.6, lpf=800, room=1)
~p3 >> play('.n', amp=.8, room=1).sometimes('stutter', 4, dur=3, rate=[.5,2])

~p4 >> play('V(sss[ss]ss[ss]s)', amp=.6, lpf=0, room=1)
~p5 >> play('funky', amp=.4, dur=.5, sample=PRand(5), pan=PWhite(-1,1), rate=PRand([.5,1,2]))

# ================================================

~s1 >> sawbass(var.ch, amp=.6, dur=8, chop=8, coarse=16, cutoff=linvar([1000,7000],32), room=1).every(6, 'offadd', 7, 1/3)
~s2 >> space(var.ch+[0,7,3,4], amp=.6, dur=2, room=1, oct=4, shape=.125).spread()
~s3 >> donk([0,[3,4,7]], amp=.1, dur=PDur(3,8), oct=[5,6,4], drive=.5).every(5, 'stutter', 2, dur=.5, oct=6)#.penta()
~s4 >> klank((0,2,4), amp=.8, dur=8)

~s5 >> soprano(s4.pitch, amp=.6, vib=12, oct=4, coarse=var([3,4],8), shape=.125).penta()
~s6 >> pulse(P[:16].shuffle().layer('mirror'), dur=.25, amp=PRand([0,.075])[:32], oct=4, drive=.5, striate=(0,1), bits=[1,8]).penta().every(6, 'splice', [6,7])  # saw, pulse

p_all.stop()
