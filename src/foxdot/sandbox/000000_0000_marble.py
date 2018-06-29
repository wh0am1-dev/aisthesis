Scale.default = "minor"
Root.default = 0
Clock.bpm = 120

p1.reset() >> piano([0,2,P*(4,5),[6,8]], chop=0, lpf=800, formant=(-1,1)) + (0,2)

d1.reset() >> play("<V   >< h >", dur=1/2, shape=0, lpf=1200).every(5, "stutter", 4, dur=3)

p2.reset() >> ambi((0, 7, 12), oct=4, dur=1) + var([0, 2], 8)

p3.reset() >> soprano(dur=8, oct=(3,4)) + var([0, 2], 8)

d2.reset() >> play("{  ppP[pP][Pp]}", sample=PRand(5), dur=1/2, shape=PWhite(0,0.5), rate=PRand([.5,1,2]))
