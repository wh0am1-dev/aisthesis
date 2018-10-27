Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 60

chords = P[5,2,4,2]

s1 >> pads(chords, amp=1, dur=1, sus=s1.dur*1.5, oct=3, lpf=600, room=1, mix=.1, chop=32)
s1.lpf=800; s1.chop=0
s1.lpf=1000; s1.oct=(3,4)
s1.lpf=1200
s1.lpf=1500
s1.lpf=0; s1.dist=.05

p1 >> play('V.-', amp=1, dur=1/3, room=1)

p2 >> play('@', amp=1, dur=8, sample=1, rate=.25, room=1)

p1.degree='V--'

s2 >> bass([2], amp=.8, dur=PDur(3,16), sus=2, oct=4)

####
s2.dist=.05
s2.spread()
p1.degree='<V--><[.t] (nnn[.n])>'
####

####
p3 >> play('.O', amp=.8, dur=1, sample=1, room=1)
s2.often('oct.offadd', 1)
####

s1 >> prophet(var([0,2],4))

####
s1.degree=[5,2,4,2]
s2 >> dbass([2])
####

Root.default = 2

####
Root.default = 0
s1.degree=var([0,2],4)
####

s1.degree=[5,2,4,2]

####
p1.degree='V.-'
p1.mix=.25
s1 >> pads(var([0,2],4))
bridge = Group(s1, p1, p2)
bridge.solo()
####

# begin snare here ??

####
p1.degree='<V--><[.t] (nnn[.n])>'
p1.mix=.1
s1 >> prophet([5,2,4,2])
bridge.solo(0)
####

# half (4)
s3 >> klank([2], amp=.25, rate=P[:16], room=1, lpf=1200, dist=.05)

# full (8)
####
s3.dist=.1
s1 >> pads([5,2,4,2])
s2.stop()
####

p1.degree='<V--><[.t] (n[.n])>'
p1.degree='<V--><[.t]  >'

####
p1.degree='V--'
s1.degree=var([0,2],4)
####

####
s1.degree=[5,2,4,2]
p1.degree='- -'
p3.stop()
####

s1.degree=var([0,2],4)

nextBar(lambda: Group(s1, p1).stop())
p2.stop()  # quick ! D:

Clock.clear()
