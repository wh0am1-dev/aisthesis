Scale.default = Scale.minorPentatonic
Root.default = 0
Clock.bpm = 120

print(Scale.names())
print(Pattern.get_methods())
print(SynthDefs)
print(Player.get_attributes())
print(BufferManager())
print(Clock.playing)

~p1 >> play('w', dur=PSum(3,8), lpf=1200, room=.5, mix=.5, amp=.6)
~p2 >> play('n', dur=.5, room=.5, mix=.5, lpf=5000, amp=.6).often('stutter')
~p3 >> play('<Vs><  f >', lpf=0, amp=.5).every(5, 'stutter', 4, dur=3, cycle=8)
~p4 >> play('I', dur=2, delay=1)

~s1 >> feel(P[5,2,3,1]+(0,var([1,2],8)), dur=1, oct=(4,5), amp=.8, drive=.05)
~s2 >> spark(P[5,2,3,1]+(0,2,4), dur=4, delay=(0,.5,1), amp=.5, oct=4, vib=.2)
~s3 >> pasha(P[9], dur=16, amp=.5, oct=[3,4], bits=4, pan=(-1,1))
~s4 >> pluck(P[5,2,3,1]+PWalk(), dur=PRand([.25,.5,1,1]), oct=PRand([4,5,6]))
~s5 >> dirt(P[9]+PWalk(), dur=PDur(var([3,5],8),var([8,16],4)), oct=3, amp=.8, cut=.8).spread()

Scale.default = Scale.majorPentatonic
Root.default = 2

Scale.default = Scale.minorPentatonic
Root.default = 0

p3.stop()
p4.stop()
s1.stop()
s5.stop()
s2.stop()
s3.stop()
p2.solo()

