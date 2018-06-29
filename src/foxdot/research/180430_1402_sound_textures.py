"""
  Ryan Kirkbride - Playing with sound textures:
  https://www.youtube.com/watch?v=qpb1XeEu6qc

  How to:
  - Run the statements line by line (alt+enter),
    go to the next one whenever you feel like
  - The "#### > run block <" blocks should be
    executed together (ctrl+enter)
  - If you want to fast-forward through the song,
    just execute the blocks together (ctrl+enter)
    from the beginning, so you don't have to go
    through every variation of each instrument
  - Enjoy ! :+1:
"""

b1 >> bass(dur=8,)
b1 >> bass(dur=8,fmod=(0,1),pan=(-1,1),)
b1 >> bass(dur=8,fmod=(0,1),pan=(-1,1),room=1,verb=1,)
b1 >> bass(dur=8,fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,)
b1 >> bass(dur=8,fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),)
b1 >> bass(dur=8,fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=320,)
b1 >> bass(dur=8,fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=320,lpf=40,)
b1 >> bass(dur=PRand(8,16)[:8],fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=320,lpf=40,)
b1 >> bass(PRand(8),dur=PRand(8,16)[:8],fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=320,lpf=40,)
b1 >> bass(PRand(8),dur=PRand(8,16)[:8],fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=320,lpf=40,lpr=0.2,)
b1 >> bass(PRand(8),dur=PRand(8,16)[:8],fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=40,lpr=0.2,)
b1 >> bass(PRand(8),dur=PRand(8,16)[:8],fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=0.2,)
b1 >> bass(PRand(8),dur=PRand(8,16)[:8],fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PWhite(-1,1),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1)),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=1,verb=1,blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),echo=PStep(8,0.75),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=1,verb=PWhite(0.5,1),blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),echo=PStep(8,0.75),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=PStep(9,0,1),verb=PWhite(0.5,1),blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),echo=PStep(8,0.75),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=PStep(9,0,1),verb=PWhite(0.5,1),blur=1.5,oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),echo=PStep(8,0.75),slide=(0,-0.1),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=PStep(9,0,1),verb=PWhite(0.5,1),blur=P[1.5].loop(16)|P[0.5].loop(16),oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),echo=PStep(8,0.75),slide=(0,-0.1),)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=PStep(9,0,1),verb=PWhite(0.5,1),blur=P[1.5].loop(16)|P[0.5].loop(16),oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),echo=PStep(8,0.75),slide=-1,)
b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=PStep(9,0,1),verb=PWhite(0.5,1),blur=P[1.5].loop(16)|P[0.5].loop(16),oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),echo=PStep(8,0.75),slide=PRand([0,0,-1,(0,-0.5)]),)

p1 >> bell(dur=12,amp=1/4,)
p1 >> bell(dur=12,amp=1/4,oct=6,)
p1 >> bell(dur=12,amp=1/4,oct=6,room=1,)
p1 >> bell(dur=12,amp=1/4,oct=6,room=1,echo=0.25,)
p1 >> bell(dur=12,amp=1/2,oct=7,room=1,echo=0.25,)
p1 >> bell(dur=PWhite(0.1,2),amp=PWhite(0,1/2),oct=7,room=1,echo=0.25,)
p1 >> bell(dur=PWhite(0.1,2),amp=PWhite(0,1/2),oct=7,room=1,echo=0.25,pan=linvar([-1,1]),)
p1 >> bell([0,6],dur=PWhite(0.1,2),amp=PWhite(0,1/2),oct=7,room=1,echo=0.25,pan=linvar([-1,1]),)
p1 >> bell([0,6,2],dur=PWhite(0.1,2),amp=PWhite(0,1/2),oct=7,room=1,echo=0.25,pan=linvar([-1,1]),)

b1.stop()

c1 >> play("c",dur=4,rate=1/2,echo=0.02,)
c1 >> play("c",dur=4,rate=1/2,echo=0.02,room=1,)
c1 >> play("c",dur=4,rate=1/2,echo=(0.02,0.04),room=1,)
c1 >> play("c",dur=4,rate=1/2,echo=(0.02,0.04),room=1,amp=1/2,)
c1 >> play("c",dur=4,rate=PWhite(0.1,0.5),echo=(0.02,0.04),room=1,amp=1/2,)
c1 >> play("c",dur=PWhite(2,6),rate=PWhite(0.1,0.5),echo=(0.02,0.04),room=1,amp=1/2,)
c1 >> play("c",dur=PWhite(2,6),rate=PWhite(0.1,0.5),echo=(0.02,0.04),room=1,amp=1/2,pan=PWhite(-1,1),)
c1 >> play("c",dur=PWhite(2,6),rate=PWhite(0.1,0.5),echo=(0.02,0.04),room=1,amp=1/2,pan=PWhite(-1,1),chop=320,)
c1 >> play("c",dur=PWhite(2,6),rate=PWhite(0.1,0.5),echo=(0.02,0.04),room=1,amp=1/2,pan=PWhite(-1,1),chop=0,)
c1 >> play("c",dur=PWhite(2,6),rate=PWhite(0.1,0.5),echo=(0.02,0.04),room=1,amp=1/2,pan=PWhite(-1,1),coarse=PRand([0,4,8,12,32]),)
c1 >> play("c",dur=PWhite(2,6),rate=PWhite(0.1,0.5),echo=(0.02,0.01),room=1,amp=1/2,pan=PWhite(-1,1),coarse=PRand([0,4,8,12,32]),)
c1 >> play("c",dur=PWhite(2,6),rate=PWhite(0.1,0.5),echo=(0.02,0.01),room=1,amp=1/2,pan=PWhite(-1,1),coarse=0,)
c1 >> play("c",dur=PWhite(2,6),rate=50,echo=(0.02,0.01),room=1,amp=1/2,pan=PWhite(-1,1),coarse=0,)
c1 >> play("c",dur=PWhite(2,6),rate=50,echo=(0.02,0.01),room=1,amp=1/2,pan=PWhite(-1,1),coarse=0,slide=PStep(6,-1),)

p1 >> bell([0,6,2],dur=PWhite(0.1,2),amp=PWhite(0,1/2),oct=PRand(6,9),room=1,echo=0.25,pan=linvar([-1,1]),)
p1 >> bell([0,6,2],dur=PWhite(0.1,2),amp=PWhite(0,1/2),oct=PRand(7,10),room=1,echo=0.25,pan=linvar([-1,1]),)

c2 >> play("p",sample=PRand(5),)
c2 >> play("{ppP[pp]}",sample=PRand(5),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=0.5,)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=0.5,verb=0.2,)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=0.5,verb=linvar([0,1],8),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=linvar([0,1],16),verb=linvar([0,1],8),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=linvar([0,1],12),verb=linvar([0,1],8),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=linvar([0,4000],12),hpr=linvar([0.1,1],17),)
c2.solo()
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2])*PRand([1,1,2,1/2]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2])*PRand([1,1,2,1/2,-1]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2])*PRand([1,1,2,1/2,-1]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),lpf=4000,)
c2 >> play("{ppP[pp]}",sample=PRand(5),dur=1/4,pan=PWhite(-1,1),rate=PRand([1,.8,1.2])*PRand([1,1,2,1/2,-1]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),lpf=PRand([0,400,4000]),)

b1 >> bass(PRand(8),dur=PRand(8,16)[:16]|P[1/4].loop(16),fmod=(0,1),pan=PStep(6,P*(-1,1),PWhite(-1,1)),room=PStep(9,0,1),verb=PWhite(0.5,1),blur=P[1.5].loop(16)|P[0.5].loop(16),oct=PRand([3,4,5]),chop=PRand(32)*PRand([10,50,1]),lpf=linvar([20,4000],64),lpr=PWhite(0.1,0.5),echo=PStep(8,0.75),slide=PRand([0,0,-1,(0,-0.5)]),)

p1 >> bell([0,6,2],dur=PWhite(0.1,2),amp=PWhite(0,1/2),oct=PRand(7,10),room=1,echo=0.25,pan=linvar([-1,1]),)

c1 >> play("c",dur=PWhite(2,6),rate=50,echo=(0.02,0.01),room=1,amp=1/2,pan=PWhite(-1,1),coarse=0,slide=PStep(6,-1),)

Clock.bpm = 160
Clock.bpm = 190
Clock.bpm = 220
Clock.bpm = 260
Clock.bpm = 300
Clock.bpm = 400

Clock.clear()

