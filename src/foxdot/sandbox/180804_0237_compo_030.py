Scale.default = Scale.romanianMinor
Root.default = 0
Clock.bpm = 100

print(Scale.names())
print(SynthDefs)
print(Samples)
print(FxList)
print(Attributes)
print(PatternMethods)
print(Clock.playing)

~s1 >> sawbass(P[0,3,5,[6,4]]+(0,2), amp=.5, dur=4, oct=4, formant=1, shape=.1, spin=[2,1,4,1], vib=.2)
~s2 >> keys(PTri([3,4,5]), amp=1.2, dur=PDur(3,8), oct=[5,6,5], room=.5, mix=.5, vib=12).often('offadd', [3,5,6])
~s3 >> bass(P[0,3,5,[6,4]], amp=.5, dur=4, oct=4, lpf=1200, lpr=0, room=.1, mix=.1)
~s4 >> donk(PWalk()+(0,5), amp=.5, dur=.5, delay=(0,.25), room=.1, mix=.5, oct=5, formant=-1).often('stutter', 3)

~p1 >> play('m', amp=.8, dur=PDur(3,16), room=.1, mix=.1)
~p2 >> play('P..[.b]', amp=.5, dur=.5, room=.1, mix=.1, sample=1, rate=var([1,2],2))
~p3 >> play('s', amp=.15, dur=.25, room=.1, mix=.1, sample=1).sometimes('stutter', 3)
~p4 >> play('{  r[rr]}', amp=.2, dur=.5, room=.1, mix=.1, sample=PRand([0,3]))
~p5 >> play('G ', amp=.2, dur=var([1,.5],[12,4]), room=.1, mix=.1, sample=0, rate=1)

Group(s2, s3, s4, p1, p2, p4, p5).only()
Group(s3, s4, p1, p2, p4, p5).only()
Group(s3, s4, p1, p2, p4).only()
Group(s3, s4, p1, p2).only()

### > block <
Group(s3, s4, p1, p2).stop()
~q0 >> play('!', amp=.5, dur=8, room=1, mix=.5, echo=2, decay=16, rate=.25)
Clock.future(7, Clock.clear)
###
