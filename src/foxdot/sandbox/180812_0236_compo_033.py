Scale.default = 'dorian'
Root.default = 0
Clock.bpm = 100

print(Scale.names())
print(SynthDefs)
print(FxList)
print(Samples)
print(PatternMethods)
print(Clock.playing)

var.ch = var([3,0,2,-1,1,0],[4,4,4,4,8,8])

~p1 >> play('V  V    ', amp=.8, dur=1, sample=3, formant=PWhite(.4,1.6), shape=PWhite(.2,.8), lpf=sinvar([50, 300],32), room=1)

~s1 >> ambi(var.ch, amp=.5, dur=4, oct=(3,4), coarse=var([4,8,16],[8,4,4]), shape=.5, lpf=200)

~p2 >> play(' (^$)', amp=.5, sample=1, lpf=2500, drive=.01, rate=var([1,.5],[12,4]), room=1)

~p3 >> play('@@ @ @@ @@  @ @ ', amp=.5, sample=0, rate=.1, cut=.1, room=1)

~s2 >> blip(var.ch+PWalk()[:32], amp=PRand([0,.5])[:64], dur=.25, formant=1, drive=.05, oct=PRand([4,5,6])[:32], room=1).often('stutter', 4, dur=3, oct=7)

~s1 >> ambi(var.ch, amp=.5, dur=4, oct=(3,4), vib=12, shape=.5, lpf=200, room=1)

~p4 >> play('V', amp=.5, dur=1, lpf=1200, room=1)

~s3 >> squish(var.ch, amp=.001, dur=PDur(3,8)*2, coarse=8, chop=4, oct=3, formant=-1, room=1, shape=.125).spread()
