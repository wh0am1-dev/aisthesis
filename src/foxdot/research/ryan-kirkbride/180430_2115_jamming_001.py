"""
  Ryan Kirkbride - Jamming 001:
  https://www.youtube.com/watch?v=HTGTv0gyw9Q

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

d1 >> play("x u ",)
d1 >> play("(x )( x)u ",)
d1 >> play("(x )( |x2|)u ",)
d1 >> play("(|x3| )( |x2|)u ",)
d1 >> play("(|x3| )( |x2|)|u1| ",)
d1 >> play("(|x3| )( |x2|)|u[12]| ",)
d1 >> play("(|x3| )( |x2|)|u([12]3)| ",)
d1 >> play("(|x3| )( |x[24]|)|u([12]3)| ",)
d1 >> play("(|x3| )( |(xv)[24]|)|u([12]3)| ",)
d1 >> play("(|{x[xx][mx]}3| )( |(xv)[24]|)|u([12]3)| ",)
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",)
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":0},default=1),)
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":1},default=1),)

Scale.default = Scale.dorian

b1 >> sawbass(var([0,9,5]),)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8),)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=4,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=1,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=1,pan=(-1,1),)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=(1,2),pan=(-1,1),)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=(1,2),pan=(-1,1),room=0.5,)

p1 >> space([0,4],dur=[6,2],)
p1 >> space([[0,2],4],dur=[6,2],)

b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=(1,2),pan=(-1,1),room=0.5,crush=4,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=(1,2),pan=(-1,1),room=0.5,crush=32,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=(1,2),pan=(-1,1),room=0.5,crush=PRand([0,4,8,32]),)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=(1,2),pan=(-1,1),room=0.5,crush=PRand([0,4,8,32]),spin=4,)
b1 >> sawbass(var([0,9,5]),dur=PDur(3,8)|2,oct=5,shape=0.5,sus=1/2,fmod=(1,2),pan=(-1,1),room=0.5,crush=PRand([0,4,8,32]),spin=4,formant=P[:7],)

b2 >> bass(var([0,5],[4,8]),)
b2 >> bass(var([0,5],[4,8]),dur=[4,8],)
b2 >> bass(var([0,-2],[4,8]),dur=[4,8],)
b2 >> bass(var([0,-3],[4,8]),dur=[4,8],)
b2 >> bass(var([0,-4],[4,8]),dur=[4,8],)
b2 >> bass(var([0,-4],[4,8]),dur=[4,8],lpf=400,)
b2 >> bass(var([0,-4],[4,8]),dur=[4,8],lpf=400,room=1,)

d2 >> play("Vs",lpf=400,)

#### > run block <
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":1},default=1),).every([6,2],"reverse")
d2 >> play("Vs",lpf=800,)
#### > run block <

d2 >> play("Vs",lpf=800,lpr=0.2,)

d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":1},default=1),dur=var([0.5,0.25],[14,2]),).every([6,2],"reverse")

d2 >> play("Vs",lpf=1000,lpr=0.2,)
d2 >> play("Vs",lpf=1500,lpr=0.3,)

d3 >> play("  * ")
d3 >> play("  |*2| ")
d3 >> play("  |*2| ",room=0.5,amp=1.5,)

b2.stop()

b1 >> sawbass(var([0,9,5]),dur=4,oct=5,shape=0.5,sus=1/2,fmod=(1,2),pan=(-1,1),room=0.5,crush=PRand([0,4,8,32]),spin=4,formant=P[:7],)
b1 >> sawbass(var([0,9,5]),dur=4,oct=5,shape=0.5,sus=3,fmod=(1,2),pan=(-1,1),room=0.5,crush=PRand([0,4,8,32]),spin=4,formant=P[:7],)
b1 >> sawbass(var([0,9,5]),dur=4,oct=5,shape=0.5,sus=3,chop=4,fmod=(1,2),pan=(-1,1),room=0.5,crush=PRand([0,4,8,32]),spin=4,formant=P[:7],)
b1 >> sawbass(var([0,9,5]),dur=4,oct=5,shape=0.5,sus=3,chop=4,fmod=(1,2),pan=(-1,1),room=1,crush=PRand([0,4,8,32]),spin=4,formant=P[:7],)
b1 >> sawbass(var([0,9,5]),dur=4,oct=5,shape=0.5,sus=3,chop=4,fmod=(1,2),pan=(-1,1),room=1,crush=PRand([0,4,8,32]),spin=4,formant=P[:7],slide=PStep(7,-1),)

d2 >> play(" s",lpf=1500,lpr=0.3,)

d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":0},default=1),dur=var([0.5,0.25],[14,2]),).every([6,2],"reverse")

#### > run block <
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":var([1,0],[28,4])},default=1),dur=var([0.5,0.25],[14,2]),).every([6,2],"reverse")
d2 >> play("Vs",lpf=1500,lpr=0.3,)
#### > run block <

d2 >> play("Vs",lpf=2500,lpr=0.3,)

p1 >> space([b1.pitch[0] + 2,4],dur=[6,2],)
p1 >> space([b1.pitch[0] + 2,4],dur=[6,2],).every(6,"offadd",2)
p1 >> space([b1.pitch[0] + 2,4],dur=[6,2],room=0.5,pan=(-1,1),).every(6,"offadd",2)

#### > run block <
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":var([1,0],[28,4])},default=1),dur=var([0.5,0.25],[14,2]),room=1,mix=1,).every([6,2],"reverse")
d2 >> play(" s",lpf=2500,lpr=0.3,)
#### > run block <

d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":var([1,0],[28,4])},default=1),dur=var([0.5,0.25],[14,2]),room=0,mix=0,).every([6,2],"reverse")

d3 >> play("  |*2| ",room=0.5,amp=1.5,).every(6,"rate.offadd",1,0.75)

d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":var([1,0],[28,4])},default=1),dur=var([0.5,0.25],[14,2]),room=0.1,mix=0,echo=PStep(7,0.75),).every([6,2],"reverse")
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":var([1,0],[28,4])},default=1),dur=var([0.5,0.25],[14,2]),room=0.1,mix=0,echo=PStep(7,0.75),crush=PStep(5,32),).every([6,2],"reverse")
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":var([1,0],[28,4])},default=1),dur=var([0.5,0.25],[14,2]),room=0.1,mix=0,echo=PStep(7,0.75),crush=PStep(5,32),slide=PStep(7,-11),).every([6,2],"reverse")
d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":var([1,0],[28,4])},default=1),dur=var([0.5,0.25],[14,2]),room=0.1,mix=0,echo=PStep(7,0.75),crush=PStep(5,32),slide=PStep(7,-1),).every([6,2],"reverse")

d2 >> play(" s",lpf=2500,lpr=0.3,amp=d2.char.map({"V":var([1,0],[28,4])}),)

d3 >> play("  |*2|( |~(01)|)",room=0.5,amp=1.5,).every(6,"rate.offadd",1,0.75)

d1 >> play("<(|{x[xx][mx]}3| )( |(xv)[24]|)|u([21]3)| ><[--]>",amp=d1.char.map({"x":var([1,0],[28,4])},default=1),dur=1/2,room=0.1,mix=0,echo=PStep(7,0.75),crush=PStep(5,32),slide=PStep(7,-1),).every([6,2],"reverse")

b1 >> sawbass(var([0,9,5]),dur=4,oct=5,shape=0.5,sus=3,chop=4,fmod=(1,2),pan=(-1,1),room=1,crush=PRand([0,4,8,32]),spin=4,formant=P[:7],slide=PStep(7,-1),) + (0,4)
b1 >> sawbass(var([0,9,5]),dur=4,oct=5,shape=0.5,sus=3,chop=4,fmod=(1,2),pan=(-1,1),room=1,crush=PRand([0,4,8,32]),spin=4,formant=P[:7],slide=PStep(7,-1),)

d_all.stop()

b1.stop()

Clock.clear()
