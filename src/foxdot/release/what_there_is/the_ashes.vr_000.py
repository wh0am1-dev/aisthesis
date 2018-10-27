Scale.default = Scale.minor
Root.default = 0
Clock.bpm = 80

chords = P[5,0,3,0]
var.ch1 = var(chords,1)
var.ch2 = var(chords,2)
var.ch4 = var(chords,4)
var.ch8 = var(chords,8)

s1 >> charm(var.ch1, amp=.8, dur=PDur(3,8)*(1,2), chop=2, lpf=800, oct=4, formant=.25, room=1, mix=.25).spread()

s2 >> ambi(chords, amp=.8, dur=4, oct=(3,4), room=1, mix=.5)

s3 >> glass(chords, amp=.8, dur=4, oct=(2,3), room=1, mix=.5, lpf=1200)

p1 >> play('(n-)---', amp=.2, dur=.25, room=1, sample=0, formant=linvar([-.25,-1],16))

p2 >> play('v', amp=.25, dur=PDur(3,16)*4, dist=.1, room=1, rate=.25)

p1 >> play('(n-)---', amp=.2, dur=.25, room=1, sample=0, formant=linvar([-.25,-1],16)).often('stutter', 4, dur=3/2)

s4 >> noise([0], amp=PWhite(0,.4), dur=1, room=1, mix=.5, chop=PRand([1,2,4])*2, oct=4)
s4 >> noise(var.ch4, amp=PWhite(0,.4), dur=1, room=1, mix=.5, chop=PRand([1,2,3,4])*2, oct=4)

p3 >> play('V', amp=.4, dur=1, rate=.5, room=linvar([0,1],16), mix=linvar([0,.5],12), lpf=800)

s3.stop()  # glass
s2.stop()  # ambi

s1.every(4, 'degrade')
Clock.future(16, s1.stop)  # charm

p3.stop()  # kick
s4.stop()  # noise

s5 >> bass(var.ch2, amp=.4, dur=PDur(3,8)*(1,2), dist=.05, oct=(4,5))

p1 >> play('(n-)---', amp=.5, dur=.25, room=1, sample=0, formant=linvar([-.25,-1],16), pan=PWhite(-1,1)).often('stutter', 4, dur=3/2)

p3 >> play('V', amp=.4, dur=1, rate=.5, room=linvar([0,1],16), mix=linvar([0,.5],12), lpf=800)

p4 >> play('i', amp=.4, dur=2, delay=1, sample=2, room=1, mix=[.1,.1,.1,.5], lpf=1500)

s2 >> klank(chords, amp=.8, dur=4, oct=(3,4), room=1, mix=.5)
s2 >> klank(chords, amp=.5, dur=4, oct=(3,4), room=1, mix=.5, formant=1)

s3 >> glass(chords, amp=.8, dur=4, oct=(2,3), room=1, mix=.5, lpf=1200)

s1 >> charm(var.ch1, amp=.8, dur=PDur(3,8)*(1,2), chop=2, lpf=800, oct=4, formant=.25, room=1, mix=.25).spread()

s5 >> bass(var.ch2, amp=.4, dur=PDur(3,8)*(1,2), oct=(4,5))

s1 >> charm(var.ch1, amp=.8, dur=PDur(3,8)*(1,2), chop=2, lpf=800, oct=4, formant=.25, room=1, mix=.25).spread().penta(0)

s5.stop()  # bass
p4.stop()  # snare
p3.stop()  # kick
s2.stop()  # klank

s1.every(4, 'degrade')
Clock.future(16, s1.stop)  # charm

p1.stop()  # hihat
s3.stop()  # glass
p2.stop()  # glitch

Clock.clear()
