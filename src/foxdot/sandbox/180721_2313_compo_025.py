Scale.default = Scale.minorPentatonic
Root.default = 0
Clock.bpm = 80

print(Scale.names())
print(Pattern.get_methods())
print(SynthDefs)
print(Player.get_attributes())
print(BufferManager())
print(Clock.playing)

var.base = P[0,2,5,4]
~s1 >> ripple(dur=4, oct=(3,4), pan=linvar([-.5,.5],4), drive=0.05, amp=.8)
~s2 >> lazer(var(var.base,2), dur=PDur(5,8)*2, oct=(5,6), coarse=PRand([2,4]), chop=PRand([0,2,4]))
~s3 >> piano(var(var.base,2)+PWalk(), oct=PRand([4,5,6]), dur=.25, drive=0.05, dist=0.02, fmod=(0,1)).spread()

~p1 >> play('Z Z Z [ZZ Z            ] ', dur=4, lpf=800)
~p2 >> play('w', dur=.25, amp=.3, rate=PRand([.25,.5,1,2]), shape=PRand([0,.125,.25,.5]))
~p3 >> play('b', dur=PRand([.25,.5,1]), rate=PRand([1,2,4]), amp=PWhite(0,.5), echo=.125, room=1, mix=.25, pan=PWhite(-.5,.5))
~p4 >> play('nnnnnn[  nn]n', dur=.5, delay=.25, hpf=2000, pan=(-1,1))
~p5 >> play('yyyyyyyyyyyyyy[yy  ]y', hpf=2000, pan=(-1,1))
~p6 >> play('VV[VV  ]VVV[VV  ]VVV[  VV]VVVVV', dur=1)

