Scale.default = Scale.minor
Root.default = -4
Clock.bpm = 100

~d1 >> play(
  P['x--(-[--])o--o(-c)c'],
  amp=.8, sample=6, dur=PDur(5,8), lpf=0, bits=4, chop=0
)

~d2 >> play(
  PZip('Vs', '  n '),
  amp=.5, sample=1, lpf=1500
).every(3, 'stutter', dur=1, sample=3)

~a1 >> bass(
  [7,7,0,0,5,5,4,[4,8]],
  amp=.4, dur=2, oct=(4,5), lpf=500, fmod=(0,1),
  lpr=.25, bits=4, sus=2.25, cut=1, room=1, mix=.5
)

~a2 >> karp(
  var([7,7,5,8]),
  amp=.8, dur=PDur(5,8), oct=PStep(3,6,5),
  bits=4, tremolo=2, chop=2, room=1, mix=.1
)

~f1 >> ambi(
  var([7,5,4],[8,4,4]),
  amp=.4, oct=(3,4)
)

~f2 >> feel(
  [0,-1,2,0,-1,-3],
  dur=[8,8,8,4,2,2], oct=(5,6), delay=(0,1),
  sus=f2.dur+1, dist=.025, room=1
) + P(0,5,7)

print(Clock.playing)
print(FxList)
print(SynthDefs)
print(Scale.names())
