# github.com/neko250

Scale.default = Scale.minor
Root.default = 0
Clock.bpm = 100

~p1 >> play(
  '<vs><m..m..m.><-[.-]-.[--].-.--.-.--.>',
  sample=p1.degree.map({ '-': 3, 's': 2 }),
  amp=.8, room=1, echo=var([0,.25],4)
).every(15, 'stutter', dur=.5, cycle=16)

~p2 >> play(
  '<.I><...(OOO[oO])>',
  amp=.6, room=1, sample=0
)

~s1 >> sinepad(
  [7,-1,5,0],
  amp=.8, dur=4, sus=4, oct=(3,4),
  lpf=1200, dist=.05, shape=.5
).spread()

~s2 >> prophet(
  s1.degree+PWalk(),
  amp=PRand([0,.8])[:32], dur=.25,
  formant=1, oct=PStep(8,6,5)
).penta()

~s3 >> bass(
  var([7,-1,5,0],4)+(0,5,7),
  dur=PDur(3,8), amp=.6, oct=PStep(6,4,3),
  delay=(0,.25,.5), formant=1, shape=.25,
  room=1, mix=.25
)

p_all.lpf=800

~s4 >> klank(
  var([0,7,5,4],4),
  amp=.8, formant=1, tremolo=4
).spread()

~p3 >> donk(
  Pvar([P[0,3,5], P[0,5,7]], [12,4]),
  amp=.75, dur=PDur(3,8)*(1,2),
  oct=PStep(8,6,5), dist=.05, room=1
)

~s5 >> piano(
  (0,5,7),
  dur=2, delay=.5, amp=.8,
  oct=[4,4,5,4], sus=6
)

p2.stop()
s3.stop()
Group(p1, p3, s5, s4).stop()
s2.stop()

print(Clock.playing)
