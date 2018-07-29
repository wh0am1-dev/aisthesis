Scale.default = Scale.lydian
Root.default = 0
Clock.bpm = 120

print(Scale.names())
print(Pattern.get_methods())
print(SynthDefs)
print(Player.get_attributes())
print(BufferManager())
print(Clock.playing)

Group(p1, p2, p5, p6, s1, s2, s3, s4, l1).only()
Group(p1, p5, p6, s3, s4).only()
Group(p1, p5, s3).only()
Group(p1, s3).only()

~p1 >> play('V', amp=.8, dur=4, room=1, mix=.1, lpf=1500)
~p2 >> play('Y', amp=.8, dur=PDur(3,8)*2, rate=(.25,.5), room=1, mix=.8)
~p3 >> play('c', amp=.5, dur=PRand([8,12]), rate=.25, coarse=2)
~p4 >> play('<Xs><  n >', amp=.8, sample=2, lpf=1200)
~p5 >> play('t', amp=.5, dur=PDur(var([3,5],8),8), sample=PRand(5), rate=PRand([.5,1,1,1,2]))
~p6 >> play('e', amp=.8, dur=PDur(3,16))

~l1 >> loop('foxdot', P[:16], amp=1.2, rate=(.125,.25), room=.5, mix=.5)

~s1 >> twang(amp=1, dur=8, oct=(2,3), coarse=PRand([2,4,8]), echo=.25)
~s2 >> bug(amp=.25, dur=16, oct=3, pan=sinvar([-.5,.5],8))
~s3 >> glass([(0,2,var([4,5],16))], amp=1, dur=8, oct=4).spread()
~s4 >> swell(var([0,2,4,2],16), amp=.5, dur=8, oct=(3,4), vib=12, pan=(-1,1))

