Scale.default = 'indian'
Root.default = 0
Clock.bpm = 80

print(Scale.names())
print(SynthDefs)
print(FxList)
print(PatternMethods)
print(Samples)
print(Clock.playing)

var.ch = var([0,1],[15,3])

~p1 >> play('W', amp=.5, dur=6, shape=.5, rate=.5, room=1, formant=[1,1,2])
~p2 >> play('m', amp=.8, dur=2/3, sample=[0,1,0], room=1).often('stutter', 2, dur=1.5, pan=PRand([-1,1]), rate=1.5)

~s1 >> klank(var.ch+(0,var([2,3,4],6)), amp=.5, oct=4)
~s1 >> klank(var.ch+(0,var([2,3,4],6)), amp=.3, oct=4, spin=1)
~s1 >> klank(var.ch+(0,var([2,3,4],6)), amp=.2, oct=4, spin=2)
~s1 >> klank(var.ch+(0,var([2,3,4],6)), amp=.5, oct=4, spin=4)

~s2 >> blip(var.ch, amp=PWhite(0,.6), dur=PDur(4,6)*2, oct=PRand([4,4,4,5,5,6]), lpf=800, room=1).sometimes('offadd', 4)

~s3 >> sitar(var.ch+PWalk(), dur=.25, amp=PRand([0,.8])[:36], formant=1, oct=PRand([6,7,8]), vib=12, room=1)

~s1 >> klank(var.ch+(0,var([2,3,4],6)), amp=.5, oct=4, spin=4, formant=1)

s3.every(6, 'degrade')
Clock.future(36, s3.stop)

~p3 >> play('( k[kk ] k[ kk]) |r3|', dur=1, rate=.5, amp=.5, lpf=00, formant=1)

p_all.stop()

