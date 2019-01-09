# https://www.youtube.com/watch?v=u7K72X4eo_s
# https://tabs.ultimate-guitar.com/tab/massive_attack/teardrop_official_2252437
# https://tabs.ultimate-guitar.com/tab/massive_attack/teardrop_chords_42259

Scale.default = Scale.chromatic
Root.default = 4
Clock.bpm = 77

_ = [0,5,10,15,19,24]
Aadd9 = P(5,12,19,21,24)
G = P(3,7,10,15,19,27)
D = P(10,17,22,26)
F = P(1,8,13,17,20,25)

print('>>> scales <<<')
print(Scale.names())
print('\n>>> synths <<<')
print(SynthDefs)
print('\n>>> fx <<<')
print(FxList)
print('\n>>> pattern <<<')
print(PatternMethods)
print('\n>>> samples <<<')
print(Samples)

~a1 >> play(
  '<|s0|s><vv v    ><    $   >',
  amp=.8, dur=.25, sample=2,
  lpf=1500, lpr=.5, room=1,
)

~e1 >> karp(
  P[5,17,24,17,22,17,22,[24,17]],
  amp=.5, dur=.5, room=1, oct=4,
  drive=PStep(8,.05,.0125).rotate(-1), formant=1,
  dist=.02, shape=.25, pan=linvar([-1,1],8),
)

~e2 >> keys(
  P[5,17,24,17,22,17,22,[24,17]],
  amp=.75, dur=.5, room=1, oct=4,
  drive=PStep(8,.05,.0125).rotate(-1), formant=1,
  dist=.02, shape=.25, pan=linvar([1,-1],8),
)

~i1 >> piano(
  [Aadd9,G,D,Aadd9]*2+[F,G,Aadd9],
  dur=[4]*8+[8,4,4], amp=.8, room=1, mix=.5,
  oct=4, formant=.5,
)
