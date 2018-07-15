Scale.default = Scale.aeolian
Root.default = 0
Clock.bpm = 120

print(Scale.names())
print(SynthDefs)
print(Player.get_attributes())
print(BufferManager())
print(Clock.playing)

var.base = P[0,1,3,5]

Group(p1, p3, p4, s4, s6).solo()
nextBar(lambda: Clock.clear())

~p1 >> play('m', dur=4)
~p2 >> play('i', dur=PRand([4,8,12]), lpf=500)
~p3 >> noise([0,1,3,5], dur=PDur(3,16)*2, sus=.125, oct=4)
~p4 >> play('-', dur=.5, amp=.5)
~p5 >> play('<Vn><  n >', sample=2, amp=.5).every(6, 'stutter', 3, n=2, cycle=8)

~s1 >> piano(var.base+(0,2,4), dur=8, oct=(4,5), room=.5, mix=.5, delay=(0,.5,1)).spread()
~s2 >> squish(var(var.base,8), dur=4, oct=6, coarse=2, amp=.125, pan=linvar([-1,1],12))
~s3 >> karp(var(var.base,8), dur=PRand([.5,1,2]), oct=PRand([3,4,5]), shape=PRand([0,.5,1]), pan=PWhite(-1,1))
# ================================
~s4 >> klank(var(var.base,8)+(0,2,4), oct=(3,4), pan=linvar([1,-1],12))
~s5 >> soprano(var(var.base,8)+(0,2), oct=(5,6), vib=12, amp=.5, coarse=var([3,4],8))
~s6 >> prophet(var(var.base,8), oct=PRand([4,5,6]), dur=1, amp=1.5).every(3, 'offadd', 4, cycle=4)

