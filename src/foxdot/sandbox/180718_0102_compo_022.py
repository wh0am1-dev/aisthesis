Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 120

print(Scale.names())
print(Pattern.get_methods())
print(SynthDefs)
print(Player.get_attributes())
print(BufferManager())
print(Clock.playing)

Group(p2, p3, s1, s2, s4).solo()
Group(p1, p2, p3, s1, s1, s2).solo()

~p1 >> play('d', dur=PDur(3,16), amp=.5)
~p2 >> play('m', dur=2, sample=2, amp=.5)
~p3 >> play('P', dur=1, amp=.5)
~p4 >> play('<As><  n >', sample=0, amp=var([.125,.25,.5,.25,.125],[12,16,16,16,12]), lpf=var([200,400,800,1200,0,1200,800,400,200],[4,8,8,8,16,8,8,8,4]), lpr=var([.125,.25,.5,.8,1,.8,.5,.25,.125],[4,8,8,8,16,8,8,8,4])).every(5, 'stutter', 4, dur=3, cycle=8)

var.base = P[0,3,0,5]
var.base = P[0,3,0,5,0,3,0,9]

~s1 >> glass(var.base+(0,1), dur=4, oct=(4,5), amp=1.5, coarse=4)
~s2 >> pads(var.base, dur=4, coarse=6, oct=3, drive=0.1)
~s3 >> quin(var(var.base,4)+PWalk(5), dur=.5, oct=PRand([4,5,6]), amp=PWhite(0,1), pan=(-1,1), fmod=(0,1), room=.125, mix=.125, echo=0, formant=(-1,1))
~s4 >> sawbass(var(var.base,4), oct=4, dur=PDur(var([3,5],4),8), lpf=800, formant=1, amp=.25, drive=.025, dist=0.02).spread()

