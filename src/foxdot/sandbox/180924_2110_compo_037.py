Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 80

print(Scale.names())
print(SynthDefs)
print(Samples)
print(FxList)
print(Attributes)
print(PatternMethods)
print(Clock.playing)

var.ch = var([7,0,5,0,3],[4,4,4,4,8])

~p1 >> play('x..t', room=1)
~p2 >> play('f', dur=PDur(3,16)*2, room=1)
~p3 >> play('<V>< o>', dur=1, amp=.5, lpf=800)
~p4 >> play('-', dur=.5, amp=.25, delay=var([0,.25],[12,4]), sample=PRand(4), rate=PRand([.5,1,2]), room=1, mix=.25)

~s1 >> sinepad(var.ch, amp=.5, dur=4, sus=5, room=1).spread()
~s2 >> dbass(var.ch, dur=4, sus=6, oct=4, room=1, amp=.25, shape=.5, lpf=500).spread()
~s3 >> piano(var.ch+PWalk(), dur=PRand([.25,.5,.5,1]), amp=.5, oct=PRand([4,5,5,6]), scale=Scale.phrygian, formant=linvar([.1,.5],16), room=1)
~s4 >> sitar(var.ch+(0,5,12), amp=PRand([0,.4]), dur=PDur(var([3,5],[8,16]),8), oct=PRand([5,6,7]), room=1, formant=1)

