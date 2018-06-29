Samples.addPath("C:/Users/wh0am1/software/livecoding/samples/databenders/WAV/")

p1 >> loop("FX/FX_AMBIENCE/FX-Ambience-1",dur=8,shape=0)

p2 >> loop("FX/FX_AMBIENCE/FX-Ambience-4",dur=16,rate=0.5,dist=0.02,)

p3 >> loop("FX/FX_MATRIX/",dur=16,sample=PRand([0,1,2,3,4,5,6,7,8,9,10,11,12,13]),lpf=800,dist=0.2)

d1 >> loop("DRUMS/KICKSUB/Kick-Hard",dur=1,lpf=1000)

d2 >> loop("DRUMS/SNARE/Snare-Hi",dur=2,).every(8,"stutter",3,dur=2/3)

d2 >> loop("DRUMS/PERC/Perc-Verb",dur=16,sus=16,rate=0.5,chop=32,formant=1)

x1 >> play(PZip("Vs","  n "),dur=0.5).every(5,"stutter",2,dur=1)

p4 >> loop("STABS/STAB_ELEGANCE/",sample=0,dur=Pvar([PDur(3,8)*2,PDur(5,8)*2],8),hpf=linvar([500,1000],12),hpr=linvar([0.1,1],16),slide=-1)
