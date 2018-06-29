Scale.default = "minor"

p1.reset() >> play('X(---[--]---[---])', amp=.5).stop()
p2.reset() >> play('V O ', lpf=800, amp=.25).stop()
p3.reset() >> play('{  ppP[pP][Pp]}', amp=.5, sample=PRand(7), rate=PRand([.5,1,2]), shape=PWhite(0,.5))
s1.reset() >> space(P[0,2,[3,5],4]+(0,var([7,12],8),const(5)), dur=4, oct=4, delay=(0,.5,.25), vib=.2, amp=.5)
a1.reset() >> ambi(P[0,2]+(0,7), dur=8, oct=3, chop=24)

Group(p1,p3,a1).stop()

