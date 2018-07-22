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
~s1 >> ripple(amp=.8, dur=4, oct=(3,4), pan=linvar([-.5,.5],4), drive=0.05)
~s2 >> lazer(var(var.base,2), amp=1, dur=PDur(5,8)*2, oct=(5,6), coarse=PRand([2,4]), chop=PRand([0,2,4]))
~s3 >> piano(var(var.base,2)+PWalk(), amp=.5, oct=PRand([4,5,6]), dur=PRand([.25,.25,.25,.25,.5,.5,1]), drive=0.05, dist=0.02, fmod=(0,1)).spread()
~s4 >> prophet(var(var.base,2)+(0,2,5), amp=1, oct=(3,4), dur=PDur(var([3,5],8),8), vib=12)

~p1 >> play('Z Z Z [ZZ Z            ] ', amp=.8, dur=4, lpf=800)
~p2 >> play('w', amp=.3, dur=.25, rate=PRand([.25,.5,1,2]), shape=PRand([0,.125,.25,.5]), room=.5, mix=.5)
~p3 >> play('b', amp=PWhite(0,.5), dur=PRand([.25,.5,1]), rate=PRand([1,2,4]), echo=.125, room=1, mix=.25, pan=PWhite(-.5,.5))
~p4 >> play('nnnnnn[  nn]n', amp=.6, dur=.5, delay=.25, hpf=2000, pan=(-1,1))
~p5 >> play('yyyyyyyyyyyyyy[yy  ]y', amp=.6, hpf=2000, pan=(-1,1))
~p6 >> play('VV[VV  ]VVV[VV  ]VVV[ VV ]VVVVV', amp=.8, dur=1)
~p7 >> play('<P   ><{  ppP[pP][Pp][  pP][  Pp][pP  ][Pp  ][ pP ][ Pp ]}>', amp=.8, dur=1, sample=PRand(5), rate=PRand([.5,1,2]), slide=PRand([0,0,0,0,0,0,-1,1]), shape=PRand([0,.125,.25]))
