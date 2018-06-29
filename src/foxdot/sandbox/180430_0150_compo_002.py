Scale.default = Scale.phrygian
Root.default = 0
Clock.bpm = 80

a1 >> keys(P[0,1,2,[4,6]],dur=4)
a1 >> keys(P[0,1,2,[4,6]],dur=4,chop=1)
a1 >> keys(P[0,1,2,[4,6]],dur=4,chop=2)
a1 >> keys(P[0,1,2,[4,6]],dur=4,chop=4)
a1 >> keys(P[0,1,2,[4,6]],dur=4,chop=8)

a2 >> zap().follow(a1)
a2 >> zap().follow(a1).spread()
a2 >> zap().follow(a1).spread().every(3,"stutter",4,dur=3)
a2 >> zap().follow(a1).spread().every(3,"stutter",4,dur=3) + (0,2)

p1 >> play(P["funky"],dur=1/4)
p1 >> play(P["funky"],dur=1/4,amp=PWhite())
p1 >> play(P["funky"],dur=1/4,rate=PRand(PSine(8)*0.5+0.5),amp=PWhite())

b1 >> bass(a1.degree,dur=4,sus=1)
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1)
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,delay=(0,0.25))
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,delay=(0,0.25)).every(8,"offadd",4)
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,delay=(0,0.25)).every(8,"offadd",4).every(6,"stutter",4,dur=2,pan=[-1,1])
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,delay=(0,0.25),lpf=linvar([500,1000],[16,0]),lpr=linvar([0.1,1],[25])).every(8,"offadd",4).every(6,"stutter",4,dur=2,pan=[-1,1])
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,chop=2,delay=(0,0.25),lpf=linvar([500,1000],[16,0]),lpr=linvar([0.1,1],[25])).every(8,"offadd",4).every(6,"stutter",4,dur=2,pan=[-1,1])
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,chop=4,delay=(0,0.25),lpf=linvar([500,1000],[16,0]),lpr=linvar([0.1,1],[25])).every(8,"offadd",4).every(6,"stutter",4,dur=2,pan=[-1,1])
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,chop=8,delay=(0,0.25),lpf=linvar([500,1000],[16,0]),lpr=linvar([0.1,1],[25])).every(8,"offadd",4).every(6,"stutter",4,dur=2,pan=[-1,1])
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,chop=2,delay=(0,0.25),lpf=linvar([500,1000],[16,0]),lpr=linvar([0.1,1],[25])).every(8,"offadd",4).every(6,"stutter",4,dur=2,pan=[-1,1])
b1 >> bass(a1.degree,dur=PDur(3,8),sus=1,chop=0,delay=(0,0.25),lpf=linvar([500,1000],[16,0]),lpr=linvar([0.1,1],[25])).every(8,"offadd",4).every(6,"stutter",4,dur=2,pan=[-1,1])

