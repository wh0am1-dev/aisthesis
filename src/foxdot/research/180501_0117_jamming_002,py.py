"""
  Ryan Kirkbride - Jamming 002:
  https://www.youtube.com/watch?v=BnDveBsUfwA

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

p1 >> piano([0,2,4,6],dur=2,)
p1 >> piano([0,2,4,P*(7,6)],dur=2,)
p1 >> piano([0,2,4,P*(7,[6,8])],dur=2,)
p1 >> piano([0,2,4,P*(7,[6,8])],dur=2,sus=3,)
p1 >> piano([0,2,4,P*(7,[6,8],4)],dur=2,sus=3,)
p1 >> piano([0,2,4,P+(7,[6,8],4)],dur=2,sus=3,)
p1 >> piano([0,2,P*(4,5),P+(7,[6,8],4)],dur=2,sus=3,)
p1 >> piano([0,2,P*(4,5),P+(7,[6,8],[4,2,6])],dur=2,sus=3,)
p1 >> piano([0,2,P/(2,4),P+(7,[6,8],[4,2,6])],dur=2,sus=3,)
p1 >> piano([[0,1,2],2,P/(2,4),P+(7,[6,8],[4,2,6])],dur=2,sus=3,)
p1 >> piano([[0,1,2],P+(2,4),P/(2,4),P+(7,[6,8],[4,2,6])],dur=2,sus=3,)
p1 >> piano([[0,1,2],P+(2,4),P/(2,4),P+(7,[6,8],[4,2,6],4)],dur=2,sus=3,)
p1 >> piano([[0,1,2],P+(2,4),P/(2,4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,)
p1 >> piano([[0,1,2],P+(1,2,4),P/(2,4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,)
p1 >> piano([[0,1,2],P+(1,2,4),P/(2,4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,oct=[4,5,5,5],)
p1 >> piano([[0,1,2],P+(1,2,4),P/(2,4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,oct=[(4,5),5,5,5],)
p1 >> piano([[0,1,2],P+(1,2,4),P/(2,4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,oct=[(4,5),5,5],)
p1 >> piano([[0,1,2],P+(1,2,4),P/(2,4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,oct=[(4,5),5],)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/(2,4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,oct=[(4,5),5],)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,oct=[(4,5),5],)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=2,sus=3,oct=[(4,5),5],) + var([0,1],8)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*2,sus=3,oct=[(4,5),5],) + var([0,1],8)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4,sus=3,oct=[(4,5),5],) + var([0,1],8)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4,sus=[3,4,6,[4,1]],oct=[(4,5),5],) + var([0,1],8)

a1 >> ambi(var([0,1],8),)
a1 >> ambi(var([0,1],8),oct=4,)
a1 >> ambi(var([0,1],8),oct=4,) + (0,9)

p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4,sus=[3,4,6,[4,1]],oct=[(4,5),5],amp=linvar([0.8,1],12),) + var([0,1],8)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5)],amp=linvar([0.8,1],12),) + var([0,1],8)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5)],amp=linvar([0.8,1],12),) + var([0,1],8)

a1 >> ambi(var([0,1],8),oct=4,fmod=((0,1),),pan=(-1,1),) + (0,9)

p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5)],amp=linvar([0.9,1],12),) + var([0,1],8)

a1 >> ambi(var([0,1],8),oct=4,fmod=((0,1),),pan=(-1,1),) + (0,var([9,11],16))
a1 >> ambi(var([0,1],8),oct=5,fmod=((0,1),),pan=(-1,1),) + (0,var([9,11],16))
a1 >> ambi(var([0,1],8),oct=5,fmod=((0,1),),pan=(-1,1),) + (0,var([2,4],16))

p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5),[5,P/(5,6)]],amp=linvar([0.9,1],12),) + var([0,1],8)

a1 >> ambi(var([0,1],8),oct=5,fmod=((0,1),),pan=(-1,1),amp=p1.dur<4,) + (0,var([2,4],16))
a1 >> ambi(var([0,1],8),oct=5,fmod=((0,1),),pan=(-1,1),amp=(p1.dur<4 and p1.sus>1),) + (0,var([2,4],16))

p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5),[5,P/(5,6)]],amp=linvar([0.9,1],12),) + var([0,[1,1,1,3]],8)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8],[5,2,6],4)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5),[5,P/(5,6)]],amp=linvar([0.9,1],12),) + var([0,[1,1,1,[-4,3]]],8)

a1 >> ambi(var([0,1],8),oct=4,fmod=((0,1),),pan=(-1,1),amp=(p1.dur<4 and p1.sus>1),) + (0,var([2,4],16))

k1 >> klank()
k1 >> klank(lpf=linvar([4000,200],16),)
k1 >> klank(lpf=linvar([4000,200],16),rate=P[4:24].stutter(2),)

a1 >> ambi(var([0,1],8),oct=4,fmod=((0,1),),pan=(-1,1),amp=(p1.dur<4 and p1.sus>1)*linvar([0.5,1],8),) + (0,var([2,4],16))

k1 >> klank(lpf=linvar([4000,200],16),rate=P[4:24].stutter(2),amp=0.6,)

p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8,9,11],[5,2,6],4)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5),[5,P/(5,6)]],amp=linvar([0.9,1],12),) + var([0,[1,1,1,[-4,3]]],8)
p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8,9,11],[5,2,6],4,2)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5),[5,P/(5,6)]],amp=linvar([0.9,1],12),) + var([0,[1,1,1,[-4,3]]],8)

b1 >> bass(var([0,1],8),dur=8,)
b1 >> bass(var([0,1],8),dur=8,oct=4,)
b1 >> bass(var([0,1],8),dur=8,oct=4,lpf=400,)
b1 >> bass(var([0,1],8),dur=8,oct=4,lpf=400,pan=(-0.5,0.5),)
b1 >> bass(var([0,1],8),dur=8,oct=4,lpf=400,pan=(-0.5,0.5),fmod=(0,1),)
b1 >> bass(var([0,1],8),dur=8,oct=4,lpf=400,pan=(-0.5,0.5),fmod=(0,1),blur=1.25,)
b1 >> bass(var([0,1,5,3],8),dur=8,oct=4,lpf=400,pan=(-0.5,0.5),fmod=(0,1),blur=1.25,)
b1 >> bass(var([0,1,5,3],8),dur=8,oct=4,lpf=400,pan=(-0.5,0.5),fmod=(0,1),blur=1.25,amp=0.8,)

p1 >> piano([[0,1,2],P+(1,2,[4,6]),P/([2,1],4),P+(7,[6,8,9,11],[5,2,6],4)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5),[5,P/(5,6)]],amp=linvar([0.9,1],12),) + var([0,[1,1,1,[-4,3]]],8)
p1 >> piano([[0,1,2],P*(1,2,[4,6]),P/([2,1],4),P+(7,[6,8,9,11],[5,2,6],4)],dur=PDur(5,8)*4|4,sus=[3,4,6,[4,1]],oct=[(4,5),5,P/(4,5),[5,P/(5,6)]],amp=linvar([0.9,1],12),) + var([0,[1,1,1,[-4,3]]],8)

k1 >> klank(lpf=linvar([4000,200],16),rate=P[4:24].stutter(2),amp=0.6,) + var([0,1,2,3],8)

a1 >> ambi(var([0,1],8),oct=4,fmod=((0,1),),pan=(-1,1),amp=(p1.dur<4 and p1.sus>1)*linvar([0.5,1],8),) + (const(7),var([2,4],16))

p2 >> blip([0,7,6,4,2],dur=4,oct=6,)
p2 >> blip([0,7,6,4,2],dur=8,oct=6,)
p2 >> blip([0,7,6,4,2],dur=[7,1],oct=6,sus=8,)
p2 >> blip([0,7,6,4,2],dur=[7,1],oct=7,sus=8,)

p3 >> blip([[4,3],0,1],dur=[5,1.5,1.5],)

#### > run block <
p3 >> blip([[4,3],0,1],dur=[5,1.5,1.5],pan=1,)
p2 >> blip([0,7,6,4,2],dur=[7,1],oct=7,sus=8,pan=-1,)
#### > run block <

p3 >> blip([[4,3],0,1],dur=[5,1.5,1.5],pan=1,sus=5,)
p3 >> blip([[4,3],0,1],dur=[5,1.5,1.5],pan=1,sus=5,oct=6,)

Group(a1,k1,b1).amplify = 0

p2 >> blip([0,7,6,4,2],dur=[7,1],oct=7,sus=8,pan=-1,).every(12,"reverse")

p3 >> blip([[4,3],0,1],dur=[5,1.5,1.5],pan=1,sus=5,oct=6,) + (0,11)

Group(a1,k1,b1,p2,p3).amplify = 0

#### > run block <
@nextBar
def go():
    Group(a1,k1,b1,p2,p3).amplify = 1
#### > run block <

d1 >> play("x - - - ",bits=16,)
d1 >> play("x - - x ",bits=16,)
d1 >> play("x - - (-x)(x[--])",bits=16,)

d2 >> play("this is nice",rate=11,)
d2 >> play("this is nice",rate=11,dur=1/4,)
d2 >> play("this is nice",rate=11,dur=1/4,pan=PWhite(-1,1),)
d2 >> play("this is ok",rate=11,dur=1/4,pan=PWhite(-1,1),)
d2 >> play("this is ok",rate=11,dur=1/4,pan=PWhite(-1,1),).every(5,"stutter",var([2,4]))
d2 >> play("this is ok",rate=11,dur=1/4,pan=PWhite(-1,1),).every(5,"stutter",var([2,4]),pan=[-1,1])
d2 >> play("this is ok",rate=11,dur=1/4,pan=PWhite(-1,1),lpf=6000,).every(5,"stutter",var([2,4]),pan=[-1,1])

d3 >> play("  I ",dur=1,)

a1 >> creep(var([0,1],8),oct=4,fmod=((0,1),),pan=(-1,1),amp=(p1.dur<4 and p1.sus>1)*linvar([0.5,1],8),) + (const(7),var([2,4],16))
a1 >> creep(var([0,1],8),dur=8,oct=4,fmod=((0,1),),pan=(-1,1),amp=(p1.dur<4 and p1.sus>1)*linvar([0.5,1],8),) + (const(7),var([2,4],16))

d3 >> play("  I ",dur=1,rate=(0.9,1),pan=(-1,1),)
d3 >> play("  I ",dur=1,rate=(0.9,1),pan=(-1,1),room=0.2,)
d3 >> play("  I ",dur=1,rate=(0.9,1),pan=(-1,1),room=0.5,)
d3 >> play("  I ",dur=1,rate=(0.9,1),pan=(-1,1),room=1,)
d3 >> play("  I ",dur=1,rate=(0.9,1),pan=(-1,1),room=1,amp=1.4,)

b1.stop()
k1.stop()
a1.stop()
p3.stop()
p2.stop()

Group(d1,d2,d3).amplify = var([1,0],[28,4])

#### > run block <
p2 >> blip([0,7,6,4,2],dur=[7,1],oct=7,sus=8,pan=-1,).every(12,"reverse")
p3 >> blip([[4,3],0,1],dur=[5,1.5,1.5],pan=1,sus=5,oct=6,) + (0,11)
a1 >> creep(var([0,1],8),dur=8,oct=4,fmod=((0,1),),pan=(-1,1),amp=(p1.dur<4 and p1.sus>1)*linvar([0.5,1],8),) + (const(7),var([2,4],16))
k1 >> klank(lpf=linvar([4000,200],16),rate=P[4:24].stutter(2),amp=0.6,) + var([0,1,2,3],8)
b1 >> bass(var([0,1,5,3],8),dur=8,oct=4,lpf=400,pan=(-0.5,0.5),fmod=(0,1),blur=1.25,amp=0.8,)
#### > run block <

d3 >> play("  ( ( I))I( [ I])",dur=1,rate=(0.9,1),pan=(-1,1),room=1,amp=1.4,)
d3 >> play("  ( ( I))I( [ I])",dur=1,rate=(0.9,1),pan=((-1,1),),room=1,amp=1.4,)
d3 >> play("  ( ( I))I( [II])",dur=1,rate=(0.9,1),pan=((-1,1),),room=1,amp=1.4,)
d3 >> play("  ( ( I))I( [II])",dur=1,rate=(0.9,1),pan=0,room=1,amp=1.4,)

b1.stop()
k1.stop()
p3.stop()
p2.stop()
# a1.stop()
d_all.stop()
a1.only()
Clock.clear()
