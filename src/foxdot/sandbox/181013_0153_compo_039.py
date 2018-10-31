Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 120

ch = P[0,5,12,0,5,12,0,14]

~p1 >> play('x.', amp=.8, room=1)
~s1 >> bass(ch, amp=.3, dur=1, oct=3, shape=.5, dist=.05, room=1, mix=.5).spread()

~p2 >> play('-([---][ppp][PP-][tt][rrr][----][i i])', amp=.5, dur=1, room=1, lpf=1200)
~s2 >> glass(P(0), amp=.8, dur=16, oct=(4,5,6), room=1, formant=0).spread()  # P(0/5/7) :: formant=1

Root.default = var([0,5,7,5,12],[32,8,8,8,8])

~p3 >> play(P['V n ([ d]O) n '], dur=.5, amp=.5, lpf=800)
~s3 >> prophet([0,5,7,5], dur=.25, amp=PRand([0,.2,.4]), pan=PWhite(-1,1)).every(16, 'penta', [0,1])  # [0,5,3/7/9/12...,5]

# > block <
p2.stop()
s1.stop()
# > block <

s2.stop()
p3.stop()

p1.stop()
