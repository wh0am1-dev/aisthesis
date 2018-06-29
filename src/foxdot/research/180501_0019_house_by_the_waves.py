"""
  Chovin Carlson - House by the Waves:
  https://www.youtube.com/watch?v=nkU8r5QKN3Y

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

n1 >> noise(PSine(32),)
n1 >> noise(P(PSine(32),PSine(24)),)
n1 >> noise(P(PSine(32),PSine(24),PSine(27)),)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7),)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,dur=.5,)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,dur=.5,formant=(linvar([1,3],48),linvar([3,1],53)),)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,dur=.5,formant=(linvar([1,3],48),linvar([3,1],53)),chop=16,)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,dur=.5,formant=(linvar([1,3],48),linvar([3,1],53)),chop=16,lpf=1200,lpr=(linvar([0,6],64),linvar([3,0],53))+PSine(5)*.7)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,dur=.5,formant=(linvar([1,3],48),linvar([3,1],53)),chop=0,lpf=1200,lpr=(linvar([0,6],64),linvar([3,0],53))+PSine(5)*.7)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,dur=.5,formant=(linvar([1,3],48),linvar([3,1],53)),chop=2,lpf=1200,lpr=(linvar([0,6],64),linvar([3,0],53))+PSine(5)*.7)
n1 >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,dur=.5,formant=(linvar([1,3],48),linvar([3,1],53)),chop=linvar([0,16],65),lpf=1200,lpr=(linvar([0,6],64),linvar([3,0],53)))
n1.reset() >> noise(P(PSine(32),PSine(24),PSine(27),PSine(18)*.7,PSine(45)),amp=P(.8,.7,.8,.7,.9)*.4,dur=.5,formant=(linvar([1,3],48),linvar([3,1],53)),chop=16,lpf=1200,lpr=(linvar([0,6],64),linvar([3,0],53)))

b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12),)
b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.5,)
b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.5,delay=(0,PRand(b1.dur)/8),)
b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.5,delay=(0,PRand(b1.dur)/8),amp=.8,)
b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.5,delay=(0,PRand(b1.dur)/8),amp=.8,formant=1,)
b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.5,delay=(0,PRand(b1.dur)/8),amp=.8,formant=2,)
b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.5,delay=(0,PRand(b1.dur)/8),amp=.6,formant=2,)
b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.5,delay=(0,PRand([0,PRand(b1.dur)/8])),amp=.6,formant=2,)

b2 >> bell(0,dur=PRand(20)+.125,delay=(0,PRand([0,PRand(b2.dur)/3])),)
b2 >> bell(0,dur=PRand(20)+.125,delay=(0,PRand([0,PRand(b2.dur)/3])),amp=linvar([.25,.5],PRand(8,32)),)
b2 >> bell(0,dur=PRand(20)+.125,delay=(0,PRand([0,PRand(b2.dur)/3])),amp=linvar([.25,.5],PRand(8,32)),lpf=linvar([2200,4000],PRand(36)),)
b2 >> bell(0,dur=PRand(20)+.125,delay=(0,PRand([0,PRand(b2.dur)/3])),amp=linvar([.25,.5],PRand(8,32)),lpf=linvar([2200,4000],PRand(36)),oct=PRand([5,6]),)
b2 >> bell(0,dur=PRand(20)*1.25+.125,delay=(0,PRand([0,PRand(b2.dur)/3])),amp=linvar([.25,.5],PRand(8,32)),lpf=linvar([2200,4000],PRand(36)),oct=PRand([5,6]),)

b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.25,delay=(0,PRand([0,PRand(b1.dur)/8])),amp=.6,formant=2,)

s1 >> soprano([0,4,(3,1),2],dur=8,)
s1 >> soprano([0,4,(3,1),2],dur=8,sus=s1.dur/2,)
s1 >> soprano([0,4,(3,1),2],dur=8,sus=s1.dur/2,amp=.6,)
s1 >> soprano([0,4,(3,1),2],dur=8,sus=s1.dur/2,amp=.6,lpf=1200,)
s1 >> soprano([0,4,(3,1),2],dur=8,sus=s1.dur/2,amp=.2,lpf=1200,)
s1 >> soprano([0,4,(3,1),2],dur=8,sus=s1.dur/2,amp=.4,lpf=1200,)
s1 >> soprano([0,4,(3,1),2],dur=8,sus=s1.dur/2,amp=.6,lpf=1200,)

s2 >> spark((7,5,[4,9]),dur=PRand(6,24),)
s2 >> spark((7,5,[4,9]),dur=PRand(6,24),delay=P(0,.125,.25),)
s2 >> spark((7,5,[4,9]),dur=PRand(6,24),delay=P(0,.125,.25),sus=.15,)
s2 >> spark((7,5,[4,9]),dur=PRand(6,24),delay=P(0,.125,.25),sus=.15,chop=1,)
s2 >> spark((7,5,[4,9]),dur=PRand(6,24),delay=P(0,.125,.25),sus=.15,chop=1,amp=.8,)
s2 >> spark((7,5,[4,9]),dur=PRand(6,24),delay=P(0,.125,.25)*.8,sus=.15,chop=1,amp=.8,)
s2 >> spark((7,5,[4,[9,10]]),dur=PRand(6,24),delay=P(0,.125,.25)*.8,sus=.15,chop=1,amp=.8,)

p1 >> pluck(var([9,7,3,4,2,1],8) + (0,0,0,0),dur=4,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,0,0,0),dur=4,amp=P(PRange(4,0,-1)/8+.25),)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,0,0,0),dur=4,amp=P(PRange(4,0,-1)/8+.25),delay=P(PRange(4,0,-1)/4),)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,0,0,0),dur=4,amp=P(PRange(4,0,-1)/8+.25),delay=P(PRange(4,0,-1)/4),formant=1,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,0,0,0),dur=4,amp=P(PRange(4,0,-1)/8+.25),delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,0,0,0),dur=4,amp=P(PRange(4,0,-1)/8+.25),delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,2),dur=4,amp=P(PRange(4,0,-1)/8+.25),delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=4,amp=P(PRange(4,0,-1)/8+.25),delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=4,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)

b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=.4,)
b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=.4,echo=1,)
b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=.4,echo=1,decay=1,)
b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=.4,echo=1,decay=1,sus=b3.dur-1.5,)
b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=.4,echo=1,decay=1,sus=b3.dur-1.5,formant=1,)
b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=.4,echo=1,decay=1,sus=b3.dur-1.5,formant=(0,1),)

b1 >> blip(PRand(8)+(0,PRand(4)),dur=PRand(2,12)*1.25,delay=(0,PRand([0,PRand(b1.dur)/8])),amp=.5,formant=2,)

s1 >> soprano([0,4,(3,1),2],dur=8,sus=s1.dur/2,amp=.5,lpf=1200,)

p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=3,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=2.5,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=2,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=1.5,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=1,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=.75,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=.5,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=.25,amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)

#### > run block <
piv = [1,1.5,2,2.5,3,3,4,4]
piv.extend(piv[::-1])
pivd = 16
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=var(piv,pivd),amp=P(PRange(4,0,-1)/8+.25)*.6,delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
#### > run block <

b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=.3,echo=1,decay=1,sus=b3.dur-1.5,formant=(0,1),)
b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=(.4,.3),echo=1,decay=1,sus=b3.dur-1.5,formant=(0,1),)

#### > run block < danger
piv = [0.25,0.25,1/3,1/3,0.5,0.625,0.75,0.875,1,1.5,2,2.5,3,3,4,4]
piv.extend(piv[::-1])
pivd = 8
p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=var(piv,pivd),amp=P(PRange(4,0,-1)/8+.25)*linvar([.4,.6,.4],[[pivd*2]+[pivd*(len(piv)-4)]+[pivd*2]]),delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)
#### > run block <

p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),dur=Pvar([linvar(piv,pivd),var(piv,pivd)],len(piv)*pivd),amp=P(PRange(4,0,-1)/8+.25)*linvar([.4,.6,.4],[[pivd*2]+[pivd*(len(piv)-4)]+[pivd*2]]),delay=P(PRange(4,0,-1)/4),formant=1,lpf=1500,hpf=200,)

s1 >> soprano([0,4,(3,1),2],dur=8,sus=s1.dur/2,amp=.6,lpf=1200,)

b3 >> bass((p1.degree-1)+(0,2),dur=8,amp=(.4,.3),echo=1,decay=1,sus=b3.dur-1.5,formant=(0,1),)

Group(p1).amplify = 0.9
Group(p1).amplify = 0.8
Group(p1).amplify = 0.7
Group(p1,s2).amplify = 0.7
Group(p1,s2,b1).amplify = 0.7
Group(p1,s2,b1).amplify = 0.6
Group(p1,s2,b1,s1).amplify = 0.6
Group(p1,s2,b1,s1,b2).amplify = 0.6
Group(p1,s2,b1,s1,b2).amplify = 0.5
Group(p1,s2,b1,s1,b2,n1).amplify = 0.5
Group(p1,s2,b1,s1,b2,n1).amplify = 0.4
Group(p1,s2,b1,s1,b2,n1).amplify = 0.3
Group(p1,s2,b1,s1,b2,n1).amplify = 0.2
Group(p1,s2,b1,s1,b2,n1,b3).amplify = 0.2
Group(p1,s2,b1,s1,b2,n1,b3).amplify = 0.4
Group(p1,s2,b1,s1,b2,n1,b3).amplify = 0

