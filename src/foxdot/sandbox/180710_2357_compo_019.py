Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 110

~p1 >> play('g', dur=1, rate=(.125,.0625), pan=[-1,1], lpf=200)
~p2 >> play('f', dur=PDur(3,16), sample=2)
~p3 >> play('t', dur=P[1,.5,.5])
~p4 >> play('A', dur=1).every([5,5,6], 'stutter', 3, n=2)

p4.lpf = 800

~s1 >> pads(P[0,2,6,4]+(0,3), oct=(4,5), dur=8, coarse=PRand([8,12,16,24,32,48,64]), slide=0, amp=1)
~s2 >> klank(P[0], oct=(3,4), dur=8, rate=1, amp=1)
~s3 >> piano(P[0,1]+(0,3,5,7), oct=(3,5,4,5), dur=8, amp=1).spread()

s1.coarse = PRand([2,4,6,8,12,16])
s1.chop = 4
s1.slide = -1
