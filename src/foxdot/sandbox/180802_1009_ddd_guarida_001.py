Scale.default = Scale.chromatic
Root.default = 2
Clock.bpm = 110
t = [0, 7, 12, 17, 19, 24] # 0-7-5-5-2-5

Group(p1, p2, b1, d3, d4).solo()
Group(p1, p2, d4).solo()
a2.solo()

~a1 >> ambi(P[3,7,2]+(0,7), oct=3, dur=4, sus=4, room=.5, mix=.5)
~a2 >> ripple([3,2,7,2], dur=P[11,1,13,11]/3, sus=a1.dur, room=.5, mix=.5, amp=1.2, chop=a1.dur*3)

~p1 >> prophet([-1,(14,26),-1], dur=P[rest(24),1,rest(11)]/3, sus=2/3, room=.5, mix=.5, coarse=4)
~p2 >> pads(P[3,7,2]+(0,7), oct=4, dur=4, sus=4, coarse=[12,8,6], room=.5, mix=linvar([0,1],12), amp=.8, chop=128)
~p3 >> dirt([7], dur=12, amp=.5, oct=[4,5], lpf=2400).spread()

~b1 >> bass(var([3,7,2],4), dur=PDur(3,8)*2, oct=4, amp=.5, lpf=1200).every(5, 'offadd', [5,7], cycle=8)

~d1 >> play('X....(..X)', dur=2/3, lpf=800, amp=.8)
~d2 >> play('......T..........gT.....', dur=1/3, amp=.8, lpf=2000) # defghtET:+^%$@
~d3 >> play('($ ) ( $)%', amp=.5, sample=3, lpf=2400, room=.5, mix=.1)
~d4 >> play('d', dur=PDur(3,16), sample=2, amp=.5)

