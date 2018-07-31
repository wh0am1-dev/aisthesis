Scale.default = Scale.romanianMinor
Root.default = 0
Clock.bpm = 120

print(Scale.names())
print(SynthDefs)
print(Samples)
print(FxList)
print(Attributes)
print(PatternMethods)
print(Clock.playing)

var.ch = var([0,2,1,3],8)

~s1 >> ripple(amp=.8, dur=16, oct=(3,4), swell=2, hpr=.5, formant=.5, vib=12, vibdepth=2)
~s2 >> noise((PSine(7),PSine(13)), amp=.25, dur=32, oct=(3,4), lpf=800, lpr=.2).spread()
~s3 >> blip([(0,var.ch+PWalk())], amp=.8, dur=PRand([.25,.25,.5,.5,1]), oct=PRand([4,4,4,4,5]), room=.2, mix=.2)
~s4 >> star(var.ch+(0,2,4), amp=.05, dur=8, oct=4, shape=.5, vib=.1).spread()
~s5 >> glass(var.ch+(0,2,4), amp=.75, dur=8)

~p1 >> play('tyty[ttyy]ty', amp=.5, sample=2, rate=1, dur=1, lpf=1200)
~p2 >> play('funky', amp=.3, dur=.5, sample=PRand(5), rate=2)
~p3 >> play('m', amp=1, dur=2, rate=.5, room=.5, mix=.5)
~p4 >> play('e', amp=.5, dur=PDur(5,8)*2|[2,1,1,1,2,.5,.5], rate=2)

