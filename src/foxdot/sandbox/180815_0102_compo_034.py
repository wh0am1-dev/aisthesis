Scale.default = 'dorian'
Root.default = 0
Clock.bpm = 120

var.ch = var([7,3,4,0])

~p1 >> play('([++ ]+++)(xo)', amp=.8, sample=3, lpf=1200, room=1).every(6.5, 'stutter', 4, dur=3, cycle=8)

~s1 >> soprano(var.ch, amp=.3, dur=8, sus=12, formant=.5, oct=3, chop=48, drive=.05, room=1).spread()

~s2 >> sawbass(var.ch+PWalk(), amp=PRand([0,.6])[:32], dur=.25, formant=.5, room=1, oct=PRand([5,6,7]))

~p2 >> play('s', dur=.5, room=1, hpf=PRand([7000,8000])[:16], hpr=.1).often('stutter', 2, dur=.5, cycle=8)

~s1 >> soprano(var.ch+(0,var([2,3,4,4],[8,8,8,8])), amp=.3, dur=8, sus=12, formant=.5, oct=3, chop=48, drive=.05, room=1).spread()

Group(p1, s1).only()

~s2 >> prophet(var.ch+PWalk(), amp=PRand([0,.8])[:128], dur=PRand([.125,.25]), formant=.5, room=1, oct=PRand([6]), drive=.05)

