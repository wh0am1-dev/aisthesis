Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 100

var.chords = P[0,1,0,3,0,1,0,5]
~p1 >> play('x', dur=PDur(3,8))
~p2 >> play('t', dur=PDur(3,16)*2, sample=1)
~p3 >> play('m', dur=4, delay=2)
~p4 >> play('<Vs><  n >', sample=2)
~s1 >> orient(var.chords+(0,2,5,2), dur=4, oct=4, delay=(0,.25,.5,.75), lpf=800, drive=.05)
~s2 >> sitar(var(var.chords,4)+PWalk(), dur=PDur(5,8), oct=PRand([5,6,7]), pan=PWhite(-1,1), shape=PRand([.25,.25,.25,.25,.5,.5,.75]), amp=.5)
~s3 >> gong(var(var.chords,4)+(2,5), dur=PDur(3,8)*2, delay=(0,.5), amp=4)

p_all.lpf=800
s_all.lpf=800

