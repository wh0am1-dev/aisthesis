# mistertribs - experiment 5
# https://youtu.be/dCLGgLZ7pPI

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

~p1 >> blip()
~p1 >> blip(P*(0,1))
~p1 >> blip(P*(0,[2,7,9]))
~p1 >> blip(P*(0,[2,7,9]), vib=12)
~p1 >> blip(P*(0,[2,7,9]), vib=12, shape=.5)

~b1 >> dbass([0,2,-3,1], dur=8)

~p1 >> blip(P*(0,[2,7,9]+b1.pitch), vib=12, shape=.5)

~b1 >> dbass([0,2,-3,1], dur=8, chop=8)
~b1 >> dbass([0,2,-3,1], dur=8, chop=(16,12), pan=(-1,1))

~p1 >> blip(P*(0,[2,7,9]+b1.pitch), vib=12, shape=.5).every(12, 'stutter', 3)

~d1 >> play('(XV) h ')
~d1 >> play('(XV)  ( V)')

~d2 >> play('[--] [--] [--]i')

~b2 >> klank(b1.pitch+4)
~b2 >> klank(b1.pitch+var([4,3],8))

~p2 >> space(b2.pitch+[0,-1], dur=[6,2])
~p2 >> space(b2.pitch+[0,-1], dur=[6,2], oct=5)

~d1 >> play('<(XV)  ( V)><  h >', echo=.5)

Scale.default = Scale.phrygian

~p3 >> soprano(b4.pitch-2, oct=6, dur=8)

~p1 >> blip(P*(0,[2,7,9]+b1.pitch), vib=12, shape=.5, room=1, mix=linvar([0,1],32)).every(12, 'stutter', 3)
~p1 >> blip(P*(0,[2,7,9]+b1.pitch), vib=12, shape=.5, room=1, mix=linvar([0,1],32)).every(12, 'stutter', 3).every(20, 'reverse')
~p1 >> blip(P*(0,[2,4,-3,9]+b1.pitch), vib=12, shape=.5, room=1, mix=linvar([0,1],32)).every(12, 'stutter', 3).every(20, 'reverse')

~b1 >> dbass([0,2,-3,1], dur=8, chop=(16,12), pan=(-1,1), oct=(4,5))
~b1 >> dbass([0,2,-3,1], dur=[8,6], chop=(16,12), pan=(-1,1), oct=(4,5))

~b2 >> klank(b1.pitch+var([4,3],8), slide=.1, oct=4)

p3.stop()

~b2 >> klank(b1.pitch+var([4,3],8), slide=.1, oct=4) + [0,4,6,10]

nextBar(Group(p2, b2).solo)

~b2 >> klank(var([4,3],8), slide=.1, oct=4) + [0,4,6,10]
~b2 >> klank(var([4,3,0,9],8), slide=.1, oct=4) + [0,4,6,10]

~d3 >> play('V', dur=4, room=1, mix=.5, amp=.6)
~d3 >> play('V', sample=PRand(4), dur=4, room=1, mix=.5, amp=.6)
~d3 >> play('V', sample=PRand(4), dur=4, room=1, mix=linvar([0,1],16), amp=.6)

p2.stop()

~d3 >> play('V[----]', sample=PRand(4), dur=4, room=1, mix=linvar([0,1],16), amp=.6)
~d3 >> play('V', sample=PRand(4), dur=4, room=1, mix=linvar([0,1],16), amp=.6)

~b3 >> bass(b2.pitch, dur=8, chop=120, amp=.5)
~b3 >> bass(b2.pitch, dur=8, chop=120, amp=.5, shape=.5)

~x1 >> karp(PTri([3,4,5]), dur=.5, scale=Scale.default.pentatonic)
~x1 >> karp(PTri([3,4,5]), dur=.5, scale=Scale.default.pentatonic, oct=6)
~x1 >> karp(PTri([3,4,5])+b3.pitch, dur=.5, scale=Scale.default.pentatonic, oct=6)
~x1 >> karp(PTri([3,4,5])+b3.pitch, dur=PDur(5,8), scale=Scale.default.pentatonic, oct=6)

b1.stop()
b3.stop()

~b2 >> sawbass([4,3,0,9], dur=8, chop=12)

### > block <
~d1 >> play('<(XV)  ( V)><  h >', echo=.5)
~d2 >> play('[--] [--] [--]i')
~d3 >> play('V', sample=PRand(4), dur=4, room=1, mix=linvar([0,1],16), amp=.6)
###

~b3 >> ambi(dur=12).follow(b2)

~d1 >> play(P['<(XV)  ( V)><  h >'].layer('mirror'), echo=.5)

~b2 >> sawbass(P*(4,3,0,9), dur=8, chop=12) + (0,[9,7])

~x1 >> karp((PTri([3,4,5])+b3.pitch)%7, dur=PDur(5,8), scale=Scale.default.pentatonic, oct=6)
~x1 >> karp((PTri([3,4,5])+b3.pitch)%7, dur=PDur(5,8), scale=Scale.default.pentatonic, oct=6).every(6, 'offadd', 4)

~b1 >> dbass(b2.pitch, oct=4)
~b1 >> dbass(b2.pitch, oct=4, dur=PDur(3,8))
~b1 >> dbass(b2.pitch, oct=4, dur=PDur(3,8).loop(3)|[2,1,1])

~d4 >> play('#', dur=32)

~d5 >> play('p', rate=PWhite(1,10))
~d5 >> play('p', rate=PWhite(1,10), room=.2, mix=1)
~d5 >> play('p', dur=.5, rate=PWhite(1,10), room=.2, mix=1)
~d5 >> play('p', dur=.5, rate=PWhite(1,10), room=.2, mix=1, amp=PRand([0,1])[:16])
~d5 >> play('p', dur=.5, rate=PWhite(1,10)[:16], room=.2, mix=1, amp=PRand([0,1])[:16])
~d5 >> play('p', dur=.5, rate=PWhite(1,10)[:16], room=.2, mix=1, amp=PRand([0,1])[:16], delay=.5)

~x1 >> karp(Pvar([(PTri([3,4,5])+b3.pitch)%7,PWalk()],[12,4]), dur=PDur(5,8), scale=Scale.default.pentatonic, oct=6).every(6, 'offadd', 4)
~x1 >> karp(Pvar([(PTri([3,4,5])+b3.pitch)%7,PWalk()],[12,4]), dur=Pvar([PDur(5,8),.25],[12,4]), scale=Scale.default.pentatonic, oct=6).every(6, 'offadd', 4)
~x1 >> karp(Pvar([(PTri([3,4,5])+b3.pitch)%7,PWalk()],[12,4]), dur=Pvar([PDur(5,8),.25],[12,4]), scale=Scale.default.pentatonic, oct=var([6,7],6)).every(6, 'offadd', 4)

### > block <
Clock.bpm += 10
Root.default += 1
###

nextBar(lambda: Scale.default.set('dorian'))

d6 >> play('o', dur=.5, amp=linvar([0,0,1,0],[28,4,0,0]))

~x1 >> space(Pvar([(PTri([3,4,5])+b3.pitch)%7,PWalk()],[12,4]), dur=Pvar([PDur(5,8),.25],[12,4]), scale=Scale.default.pentatonic, oct=var([6,7],6)).every(6, 'offadd', 4)

~x2 >> soprano([0,-1,-2,-3], dur=8, oct=6)

~b2 >> sawbass(P*(4,3,0,9), dur=8, chop=12)
~b2 >> sawbass(P*(4,3,0,9), dur=8, chop=(12,16), pan=(-1,1)) + (0,[9,7])

~x1 >> space(Pvar([(PTri([3,4,5])+b3.pitch)%7,PWalk()],[12,4]), dur=Pvar([PDur(5,8),.25],[12,4]), scale=Scale.default.pentatonic, oct=var([4,5],6)).every(6, 'offadd', 4)

x2.stop()

~x3 >> pulse(cut=.5)
~x3 >> pulse([0,4,7,8], cut=.5)
~x3 >> pulse([0,4,7,8], cut=.5, shape=.5)
~x3 >> pulse([0,4,7,8], cut=.5, shape=.5) + (0,3)
~x3 >> pulse([[0,1,3],4,7,8], cut=.5, shape=.5) + (0,3)
~x3 >> pulse([[0,1,3],4,7,8], cut=.5, shape=linvar([0,1],8), dur=.5) + (0,3)

~x1 >> space(Pvar([(PTri([3,4,5])+b3.pitch)%7,PWalk()],[12,4]), dur=Pvar([PDur(5,8),.25],[12,4]), scale=Scale.default.pentatonic, oct=var([4,5],6), lpf=linvar([200,5000],16), lpr=linvar([.1,1],12)).every(6, 'offadd', 4)

~x3 >> pulse(P[[0,1,3],4,7,8].loop(3)|PTri(4), vib=16, cut=.5, shape=linvar([0,1],8), dur=.5) + (0,3)
~x3 >> pulse(P[[0,1,3],4,7,8].loop(3)|PTri(4), vib=16, cut=.5, shape=linvar([0,1],8), dur=.5, fmod=(0,1)) + (0,3)

### > block <
Clock.bpm += 10
Root.default += 1
###

nextBar(lambda: Scale.default.set('major'))

~k1 >> dirt()

~x3 >> pulse(P[[0,1,3],4,7,8].loop(3)|PTri(4)*2, vib=16, cut=.5, shape=linvar([0,1],8), dur=.5, fmod=(0,1)) + (0,3)

Root.default += 1

d_all.stop()
nextBar(b_all.stop)
x3.stop()
nextBar(Clock.clear)

