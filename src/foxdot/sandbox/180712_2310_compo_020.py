Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 120

~p1 >> play('A', dur=4)
~p2 >> play('P', dur=2, sample=3)
~p3 >> play('{  ppP[pP][Pp]}', dur=1, rate=PRand([.5,1,2]), shape=PRand([.5,1]))
~p4 >> play('t', dur=PDur(3,16))
~p5 >> play('m', dur=PDur(3,8)*2, sample=[0,1,1])
~p6 >> play('w', dur=PDur(2,8), lpf=800, hpf=700)

p6.dur = PDur(2,8)
p6.dur = PDur(3,8)
p6.dur = PDur(5,8)
p6.dur = PDur(7,8)
p6.stop()

var.base = P[0,1,0,2,1]
~s1 >> prophet(var.base+(0,3,5), dur=[8,8,8,4,4], delay=(0,.5,1), vib=12, cut=.5)
~s2 >> bass(var(var.base,[8,8,8,4,4]), dur=PDur(3,16), oct=5, hpf=200, amp=.6).spread().every(6, 'offadd', 3, cycle=8)
~s3 >> soprano(var.base+(0,5,7), dur=[8,8,8,4,4], amp=.5, oct=(3,4))

