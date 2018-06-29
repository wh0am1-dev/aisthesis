Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 120

p2.reset() >> play("V ", lpf=linvar([500, 1000], 12), lpr=linvar([0.1, 1], 8)).every(3, "stutter", 2, dur=1, lpf=400)
k2.reset() >> karp(PRand([0,3,5,7]), oct=PRand([5,6,7]), dur=0.25, shape=0.25, room=0.5, mix=0.5, formant=1, amp=1.5, hpf=linvar([1000, 2000], 16), hpr=linvar([0.1, 1], 20))

p1.reset() >> play("{  ppP[pP][Pp]}", dur=0.5, sample=PRand(7), rate=PWhite(0.5,1))
p2.reset() >> play("V ").every(3, "stutter", 2, dur=1, lpf=400)
p3.reset() >> play(" (---([--][---][--][----]))")
p4.reset() >> play("|=1|", dur=32, rate=0.125, formant=1)
k1.reset() >> klank([(0,5,12,var([17, 19],8))], oct=4)
k2.reset() >> karp(PRand([0,5,7]), oct=PRand([5,6,7]), dur=0.25, shape=0.25, room=0.5, mix=0.5, formant=1, amp=1)
k3.reset() >> donk(k2.degree + PWalk(), dur=0.5, room=0.5, mix=0.5)
