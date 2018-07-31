# mistertribs - experiment 4
# https://youtu.be/bHvZQIrdThE

Scale.default.set([i*12/19 for i in [0,1,4,7,8,11,12,15,16]])
Root.default = 0
Clock.bpm = 120

~b1 >> klank(P[0,4,7])
~b1 >> klank(P[0,4,7], formant=linvar([0,2],8))

~p1 >> blip([0,3,5,4,7,2], dur=.5)
~p1 >> blip([0,3,5,4,7,2], dur=.5, room=.5, mix=.5)

~d1 >> play('{p[pp][ppp]}', rate=PWhite(4,10))
~d1 >> play('{p[pp][ppp]}', rate=PWhite(4,10), room=1, mix=.5)
~d1 >> play('{p[pp][ppp]}', rate=PWhite(4,10), room=1, mix=.5, amp=.5)

var.ch = var([0,-2,4,6],8)

### > block <
~b1 >> klank(P[0,4,7]+var.ch, formant=linvar([0,2],8))
~p1 >> blip([0,3,5,4,7,2]+var.ch, dur=.5, room=.5, mix=.5)
###

~b2 >> bass(var.ch, dur=4)

~d2 >> play('X  f')
~d2 >> play('X  (  [fff])')

~p2 >> viola(p1.degree, dur=[6,2,4,4])

~p1 >> blip([0,3,5,4,7,2]+var.ch, dur=.5, room=.5, mix=.5).every(12, 'reverse')
~p1 >> blip([0,3,5,4,7,2]+var.ch, dur=.5, room=.5, mix=.5).every(12, 'reverse').every(10, 'stutter', 4, dur=2, oct=6)

~p2 >> viola(p1.degree, dur=[6,2,4,4]).every(6, 'offadd', 5)

var.ch = var([0,3,7,6,5], [8,4,4,8,8])

~b2 >> bass(var.ch, dur=8, shape=.2)

~d2 >> play('X  (  [fff])', bits=4)
~d2 >> play('X  (  [fff])', bits=6)

~p3 >> soprano(p1.degree, dur=8)
~p3 >> soprano(p1.degree, dur=8, oct=6)
~p3 >> soprano(p1.degree, dur=8, oct=6, slide=P[0,0,0,-1])

~d1 >> play('{p[pp][ppp]}', rate=PWhite(4,10), room=1, mix=.5, amp=.5*(p3.slide==0))

Group(p1, p2).amplify = p3.slide == 0

~d3 >> play('  o ')

### > block <
p3.stop()
Group(p1, p2).amplify = 1
~d1 >> play('{p[pp][ppp]}', rate=PWhite(4,10), room=1, mix=.5, amp=.5)
###

~p1 >> blip([0,1,3,5,6,2]+var.ch, dur=.5, room=.5, mix=.5).every(12, 'reverse').every(10, 'stutter', 4, dur=2, oct=6)

nextBar(lambda: p2.stop())
nextBar(lambda: b1.stop())

~b2 >> bass(var.ch, dur=PDur(5,8), shape=.2)

~p1 >> blip([0,1,3,5,6,2]+var.ch, dur=PDur(3,2), room=.5, mix=.5).every(12, 'reverse').every(10, 'stutter', 4, dur=2, oct=6)

~b2 >> bass(var.ch, dur=PDur(5,8), shape=.1)

~d2 >> play('V X(  [fff])', bits=6)

~p1 >> blip([0,1,3,5,6,2]+var.ch, dur=PDur(3,4), room=.5, mix=.5).every(12, 'reverse').every(10, 'stutter', 4, dur=2, oct=6)

~b1 >> klank(P[0,4,7]+var.ch, formant=linvar([0,2],8))

nextBar(lambda: Group(d2, d3).stop())
nextBar(lambda: b_all.stop())

Clock.bpm = 100
Clock.bpm = 80

nextBar(Clock.clear)

