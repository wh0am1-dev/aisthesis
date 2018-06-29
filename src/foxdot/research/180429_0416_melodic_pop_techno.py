"""
  Ryan Kirkbride - Melodic pop techno:
  https://www.youtube.com/watch?v=No-bBhbJAac

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

Clock.bpm = 120
Root.default = 0
Scale.default = Scale.minor

p1 >> gong(dur=4,)

var.chords = var([0,2],8)

p1 >> gong(var.chords,dur=4,)
p1 >> gong(var.chords,dur=PDur(3,8)*2,)
p1 >> gong(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,)
p1 >> gong(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=2,)

p2 >> bell(var.chords + var([(0,2),(2,4)]),dur=[1,1/2],amp=0.5,)

d1 >> play("x ",sample=2,dur=2,)
d1 >> play("x[ n]",sample=2,dur=2,)
d1 >> play("x[ [sn]]",sample=2,dur=2,)

b1 >> sawbass(var.chords,)
b1 >> sawbass(var.chords,dur=PDur(5,8),)
b1 >> sawbass(var.chords,dur=PDur(5,8),cutoff=linvar([100,8000],30),)
b1 >> sawbass(var.chords,dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),)
b1 >> sawbass(var.chords,dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-2,2),)
b1 >> sawbass(var.chords,dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1),)
b1 >> sawbass(var.chords + var([0,5,1],[16,8,8]),dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1),)

d2 >> play("- -- - -- ",)
d2 >> play("- -- - -- ",dur=1/4,)

d1 >> play("<x[ [sn]]>< h>",sample=2,dur=2,)

p3 >> prophet([3,2,var.chords],dur=1/2,hpf=linvar([0,5000],[16,0]),)
p3 >> prophet(P[3,2,var.chords],dur=1/4,hpf=linvar([0,5000],[16,0]),)
p3 >> prophet(P[3,2,var.chords].loop(3)|P[4,4,4,4],dur=1/4,hpf=linvar([0,5000],[16,0]),)
p3 >> prophet(P[3,2,var.chords].loop(4)|P[4,4,4,4],dur=1/4,hpf=linvar([0,5000],[16,0]),)
p3 >> prophet(P[3,2,var.chords].loop(4)|P[4,4,4,4],dur=1/4,hpf=linvar([0,2000],[16,0]),)
p3 >> prophet(P[3,2,var.chords].loop(4)|P[4,4,4,4],dur=1/4,hpf=linvar([0,2000],[16,0]),hpr=linvar([0.1,1],25),)
p3 >> prophet(P[3,2,var.chords].loop(4)|P[var([4,6])].stutter(4),dur=1/4,hpf=linvar([0,2000],[16,0]),hpr=linvar([0.1,1],25),)
p3.solo()
p3 >> prophet(P[3,2,var.chords].loop(4)|P[var([4,6])].stutter(4),dur=1/4,hpf=linvar([0,2000],[16,0]),hpr=linvar([0.1,1],25),formant=var([0,4],[6,2]),)
p3 >> prophet(P[3,2,var.chords].loop(4)|P[var([4,6])].stutter(4),dur=1/4,hpf=linvar([0,2000],[16,0]),hpr=linvar([0.1,1],25),formant=PRand(4),)
p3 >> prophet(P[3,2,var.chords].loop(4)|P[var([4,6])].stutter(4),dur=1/4,hpf=linvar([0,2000],[16,0]),hpr=linvar([0.1,1],25),formant=PRand(4)[:16],)

#### > run block <
p1 >> gong(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=2,)
p2 >> bell(var.chords + var([(0,2),(2,4)]),dur=[1,1/2],amp=0.5,)
#### > run block <

p1 >> blip(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=1,)
p1 >> blip(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=1,sus=2,)
p1 >> blip(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=1,sus=2,).every(8,"offadd",4)
p1 >> blip(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=1,sus=2,).every(8,"offadd",4).every(6,"stutter",4,dur=3,pan=[-1,1])
p1 >> blip(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=1,sus=2,).every(8,"offadd",4).every(6,"stutter",4,dur=3,pan=[-1,1],oct=6)

#### > run block <
b1 >> sawbass(var.chords + var([0,5,1],[16,8,8]),dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1),)
d1 >> play("<x[ [sn]]>< h>",sample=2,dur=2,)
d2 >> play("- -- - -- ",dur=1/4,)
#### > run block <

d3 >> play("  o ",sample=3,dur=1,)

d4 >> play("K",sample=[1,2,3],dur=PDur(3,8,[0,2]),)

b2 >> bass(p1.pitch,dur=8,)
b2 >> bass(p1.pitch,dur=8,rate=5,)
b2 >> bass(p1.pitch,dur=8,rate=5,room=1,)
b2 >> bass(p1.pitch,dur=8,rate=5,room=1,).spread()

d1 >> play("<x[ [sn]]>< h><  y>",sample=2,dur=1,)
d1 >> play("<x[ [sn]]>< h><  (yt+)>",sample=2,dur=1,)

d3 >> play("  o ",sample=3,dur=1,).every([6,2],"mirror")
d3 >> play("  o ",sample=3,dur=1/2,).every([6,2],"mirror")
d3 >> play("  o ",sample=3,dur=1/2,echo=var([0,0.5],[6,2]),).every([6,2],"mirror")

b1 >> sawbass(var.chords + var([0,5,1],[16,8,8]),dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1) + PStep(4,0,(0,9)),)
b1 >> sawbass(var.chords + var([0,5,1],[16,8,8]),dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1) + PStep(4,(0,9),0),)

d2 >> play("[--]",dur=1/4,)
d2 >> play("[--]",dur=1/2,)

d3 >> play("  o( K)",sample=3,dur=1/2,echo=var([0,0.5],[6,2]),).every([6,2],"mirror")
d3 >> play("  o( S)",sample=3,dur=1/2,echo=var([0,0.5],[6,2]),).every([6,2],"mirror")

d_all.solo()

d5 >> play("funky",rate=5,).every(4,"amen")
d5 >> play("funky",rate=5,).every(4,"amen").every(6,"stutter",4,dur=1)
d5 >> play("funky",rate=PRand(5,10),).every(4,"amen").every(6,"stutter",4,dur=1)

d_all.lpf = var([0,500],[28,4])

#### > run block <
p1 >> blip(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=1,sus=2,).every(8,"offadd",4).every(6,"stutter",4,dur=3,pan=[-1,1],oct=6)
p2 >> bell(var.chords + var([(0,2),(2,4)]),dur=[1,1/2],amp=0.5,)
p3 >> prophet(P[3,2,var.chords].loop(4)|P[var([4,6])].stutter(4),dur=1/4,hpf=linvar([0,2000],[16,0]),hpr=linvar([0.1,1],25),formant=PRand(4)[:16],)
b1 >> sawbass(var.chords + var([0,5,1],[16,8,8]),dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1) + PStep(4,(0,9),0),)
b2 >> bass(p1.pitch,dur=8,rate=5,room=1,).spread()
#### > run block <

s1 >> soprano([7,6,4,2,0],dur=[8,2,2,2,2],)
s1 >> soprano([7,6,4,2,0],dur=[2,2,2,2,8],)
s1 >> viola([7,6,4,2,0],dur=[2,2,2,2,8],)
s1 >> viola([7,6,4,2,0],dur=[2,2,2,2,8],blur=1.5,)
s1 >> viola([7,6,4,2,var.chords + var([0,2],8)],dur=[2,2,2,2,8],blur=1.5,)

b2 >> bass(p1.pitch[0],dur=8,rate=5,room=1,).spread()

s1 >> viola([7,6,4,2,b2.pitch + var([0,2],8)],dur=[2,2,2,2,8],blur=1.5,)

d3.stop()

#### > run block <
d2 >> play("[ss]",dur=1/2,sample=2,)
d3 >> play("<  H ><  * >")
#### > run block <

d3 >> play("<  H ><  * >",sample=1,)
d3 >> play("<  H ><  * >",sample=(0,1),)
d3 >> play("<  H ><  * *>",sample=(0,1),)

var.chords = var([0,-1,-2,-3],8)

b1 >> sawbass(var.chords + var([0,5],[16]),dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1) + PStep(4,(0,9),0),)

d1 >> play("<x[ [sn]]>< h><  (yt+)>",sample=2,dur=1/2,)
d1 >> play("<x[sn]>< h><  (yt+)>",sample=2,dur=1/2,)

d_all.stop()

#### > run block <
d6 >> play("o",amp=linvar([0,0,2,0],[28,4,0,0]),)
d7 >> play("#",dur=32,amp=2,room=1,)
#### > run block <

#### > run block <
d1 >> play("<x[sn]>< h><  (yt+)>",sample=2,dur=1/2,)
d2 >> play("[ss]",dur=1/2,sample=2,)
d3 >> play("<  H ><  * *>",sample=(0,1),)
d4 >> play("K",sample=[1,2,3],dur=PDur(3,8,[0,2]),)
d5 >> play("funky",rate=PRand(5,10),).every(4,"amen").every(6,"stutter",4,dur=1)
#### > run block <

d3 >> play("<  % ><  * *>",sample=(0,1),cut=(0.5,0),)
d3 >> play("<  % ><  * *>",sample=(0,1),cut=(0.5,0),shape=(1,0),)
d3 >> play("<  % ><  * *>",sample=(0,1),cut=(0.5,0),shape=(1,0),room=0.1,echo=var([0,0.75],[12,4]),)

#### > run block <
var.chords = var([0,2],8)
Root.default += 4
#### > run block <

b1 >> sawbass(var.chords + var([0,5,1],[16,8,8]),dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1) + PStep(4,(0,9),0),)
b1 >> sawbass((var.chords + var([0,5],[16])) % 7,dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1) + PStep(4,(0,9),0),)

s1.stop()
Group(p1,p2).stop()
Group(b2).stop()
Group(d2,d3).stop()
Group(d4,d5).stop()
Group(d6,d7).stop()

d1 >> play("<x[sn]><  h ><  y>",sample=2,dur=1/2,)

b1.stop()

Scale.default = Scale.major

#### > run block <
p1 >> blip(P[var.chords,4,6,7][:6],dur=PDur(3,8)*2,amp=1,sus=2,).every(8,"offadd",4).every(6,"stutter",4,dur=3,pan=[-1,1],oct=6)
p2 >> bell(var.chords + var([(0,2),(2,4)]),dur=[1,1/2],amp=0.5,)
#### > run block <

d1 >> play("<x[sn]><  h ><  y>",sample=2,dur=1/2,).every([6,2],"mirror")
d1 >> play("<x[sn]><  h ><  y>",sample=2,dur=1/2,echo=var([0,0.5],[6,2]),).every([6,2],"mirror")

d2 >> play("[ss]",dur=1/2,sample=2,)

var.chords = var([0,2,-2,3],8)

#### > run block <
b1 >> sawbass(var.chords % 7,dur=PDur(5,8),cutoff=linvar([100,8000],30),amp=linvar([0.5,0.8],20),fmod=PWhite(-1,1) + PStep(4,(0,9),0),)
b2 >> bass(p1.pitch[0],dur=8,rate=5,room=1,).spread()
#### > run block <

d6 >> play("o",amp=linvar([0,0,2,0],[28,4,0,0]),dur=1/2,)

#### > run block <
d3 >> play("<  % ><  * *>",sample=(0,1),cut=(0.5,0),shape=(1,0),room=0.1,echo=var([0,0.75],[12,4]),)
d4 >> play("K",sample=[1,2,3],dur=PDur(3,8,[0,2]),)
d5 >> play("funky",rate=PRand(5,10),).every(4,"amen").every(6,"stutter",4,dur=1)
d7 >> play("#",dur=32,amp=2,room=1,)
#### > run block <

d6 >> play("o",amp=linvar([0,0,2,0],[28,4,0,0]),dur=1/4,)

b2 >> bass(p1.pitch[0],dur=8,rate=8,room=1,).spread()
b2 >> bass(p1.pitch[0],dur=8,rate=8,room=1,sus=2,shape=1,).spread()
b2 >> bass(p1.pitch[0],dur=8,rate=8,room=1,sus=4,shape=1,).spread()

var.chords = var(PChain({
    0 : [2,3],
    2 : [0,5],
    3 : [0,5],
    5 : [3]
}), 8)

d_all.stop()

p3 >> prophet(P[3,2,var.chords].loop(4)|P[var([4,6])].stutter(4),dur=1/4,hpf=linvar([0,2000],[16,0]),hpr=linvar([0.1,1],25),formant=PRand(4)[:16],)

p4 >> saw(PWalk(),scale=Scale.default.pentatonic,dur=1/2,oct=3,)
p4 >> saw(PWalk(),scale=Scale.default.pentatonic,dur=1/2,oct=4,)
p4 >> saw(PWalk(),scale=Scale.default.pentatonic,dur=1/2,oct=4,shape=0.5,fmod=1,)
p4 >> saw(PWalk(),scale=Scale.default.pentatonic,dur=1/4,oct=5,shape=0.5,fmod=1,)
p4 >> pulse(PWalk(),scale=Scale.default.pentatonic,dur=1/4,oct=5,shape=0.5,fmod=1,)
p4 >> pulse(PWalk(),scale=Scale.default.pentatonic,dur=1/4,oct=5,shape=0.5,fmod=1,) + var([0,(0,1)],[12,4])
p4 >> pulse(PWalk(),scale=Scale.default.pentatonic,dur=1/4,oct=5,shape=0.5,fmod=1,) + (var([0,(0,1)],[12,4]) + var([0,4,5,3]))

d6 >> play("o",amp=linvar([0,0,2,0],[28,4,0,0]),dur=1/4,)

#### > run block <
d1 >> play("<x[sn]><  h ><  y>",sample=2,dur=1/2,echo=var([0,0.5],[6,2]),).every([6,2],"mirror")
d2 >> play("[ss]",dur=1/2,sample=2,)
d3 >> play("<  % ><  * *>",sample=(0,1),cut=(0.5,0),shape=(1,0),room=0.1,echo=var([0,0.75],[12,4]),)
d4 >> play("K",sample=[1,2,3],dur=PDur(3,8,[0,2]),)
d5 >> play("funky",rate=PRand(5,10),).every(4,"amen").every(6,"stutter",4,dur=1)
d7 >> play("#",dur=32,amp=2,room=1,)
#### > run block <

d7 >> play("#",dur=16,amp=2,room=1,)

p4 >> pulse(PWalk(),scale=Scale.default.pentatonic,dur=1/4,oct=5,shape=0.5,fmod=1,vib=12,) + (var([0,(0,1)],[12,4]) + var([0,4,5,3]))
p4 >> pulse(PWalk(),scale=Scale.default.pentatonic,dur=1/4,oct=5,shape=0.5,fmod=1,vib=0,) + (var([0,(0,1)],[12,4]) + var([0,4,5,3]))
p4 >> pulse(PWalk(),scale=Scale.default.pentatonic,dur=1/4,oct=5,shape=0.5,fmod=1,vib=12,) + (var([0,(0,1)],[12,4]) + var([0,4,5,3]))

d1 >> play("<x[sn]><  I ><  y>",sample=2,dur=1/2,echo=var([0,0.5],[6,2]),).every([6,2],"mirror")

nextBar(Clock.clear)

