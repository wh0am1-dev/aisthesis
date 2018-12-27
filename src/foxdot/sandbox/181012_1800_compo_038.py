Scale.default = Scale.minor
Root.default = 0
Clock.bpm = 80

print(Scale.names())
print(SynthDefs)
print(Samples)
print(FxList)
print(Attributes)
print(PatternMethods)
print(Clock.playing)

var.ch = var([0,3,1,5], 8)

~p1 >> play('x  ( [ x])', amp=1, sample=1, room=1)
~p2 >> play('v ', amp=.6, lpf=800, room=1)
~p3 >> play('( o o   o) ', amp=.4, lpf=1200, room=1)

~s1 >> space(var.ch, amp=.8, dur=8, oct=4, room=1).spread()
~s2 >> noise(var.ch+PWhite(), amp=PRand([0,.2])[:32], dur=.5, sus=.25, oct=6, room=1, pan=linvar([-1,1],16))
~s3 >> dbass(var.ch, amp=.05, dur=PDur(3,16)*4, oct=3, room=1, shape=.75, formant=(-1,1))
~s4 >> piano(var.ch+PWalk(), amp=PRand([0,.4,.6])[:64], oct=PRand([4,5,6])[:32], dur=1/3, room=1, pan=PWhite(-1,1), scale=Scale.minor).penta(0)
