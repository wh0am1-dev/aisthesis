Scale.default = [0,2,3,5,6,7,10]
Root.default = 0
Clock.bpm = 80

~s1 >> ambi(P[5,1,3,0]+(0,[3,2,3,3],5), amp=.8, dur=8, oct=4, room=1)

~p1 >> play('x  [  x]', amp=.8, dur=1, lpf=800, room=1)

~p2 >> play('*  (   [       **])', amp=.2, dur=1, hpf=7000, hpr=.05, room=1, mix=.5)

~s2 >> keys(s1.pitch[0]+PWalk()[:32], amp=PRand([0,1])[:32], dur=.25, oct=5, drive=.05, room=1)
~s2 >> keys(s1.pitch[0]+PWalk()[:32], amp=PRand([0,1])[:32], dur=.25, oct=5, drive=.05, room=1, vib=12, chop=64).spread()
~s2 >> keys(s1.pitch[0]+PWalk()[:32], amp=PRand([0,1])[:128], dur=.125, oct=5, drive=.05, room=1, vib=12, chop=32).often('offadd', 5, dur=.25).spread()
~s2 >> keys(s1.pitch[0]+PWalk()[:32], amp=PRand([0,1])[:128], dur=.125, oct=5, drive=.05, room=1, vib=12, chop=32).often('oct.offadd', 1, dur=.25).spread()

