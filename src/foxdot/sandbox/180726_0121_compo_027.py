Scale.default = Scale.minorPentatonic
Root.default = 0
Clock.bpm = 120

print(Scale.names())
print(Pattern.get_methods())
print(SynthDefs)
print(Player.get_attributes())
print(BufferManager())
print(Clock.playing)

~p1 >> play('v', amp=.3, dur=2, lpf=1200)
~p2 >> play('i', amp=.2, dur=1, lpf=sinvar([200,1200],8), lpr=sinvar([.1,1],12), shape=[0,.25,.5,.25]).often('stutter', dur=1/3)
~p3 >> play('universe', amp=.5, dur=.5, lpf=1500, sample=PRand(5), rate=PRand([.25,.5,1,2,4]), echo=PRand([0,0,0,0,0,0,0,.125]), room=.5, mix=.5)

~s1 >> glass(P[2,3,1,4]+(0,1,var([3,4],32)), amp=2, dur=8, oct=(3,4,5), vib=.1, room=.5, mix=.5)
~s2 >> pads(s1.degree[0]+(0,3,var([5,6],16)), dur=var([8,4],16), amp=.6, delay=(0,.25,.5), oct=(3,4), coarse=PRand([4,6,8]), lpf=600).every(5, 'offadd', 3, cycle=8)
~s3 >> dirt(s1.degree[0], amp=1, oct=4, dur=PDur(3,16), lpf=800)
