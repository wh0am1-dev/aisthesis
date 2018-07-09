Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 110

~p1 >> play('m', dur=PDur(3,16), sample=[0,2,3])
~p2 >> play('V', dur=1, pan=[-1,1], sample=var([0,2],[24,8]))
~p3 >> play('n', dur=var([.5,.25,.125,2/3],[24,4,2,2]))

p_all.lpf = 0
p_all.rate = .5

~s1 >> space(P[0,3,5,1]+(0,3), dur=4, chop=6, slide=0, echo=.5, room=.5, mix=.5)

~s2 >> glass(P[0,3,5,var([1,8,7],[16,8,8])], oct=4, amp=2)

