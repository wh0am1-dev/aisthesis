Scale.default = Scale.indian

p1 >> donk(P[0,1,2,3],dur=8)

n1 >> nylon(p1.degree + PWalk(),)
n1 >> nylon(p1.degree + PWalk(),dur=PDur(3,8),)
n1 >> nylon(p1.degree + PWalk(),dur=PDur(3,8)|2,)
n1 >> nylon(p1.degree + PWalk(),dur=PDur(3,8)|[0.5,1.5],)
n1 >> nylon(p1.degree + PWalk(),dur=PDur(3,8)|[0.5,1.5],formant=linvar([0,1]),)
n1 >> nylon(p1.degree + PWalk(),dur=PDur(3,8)|[0.5,1.5],formant=linvar([0,1]),delay=(0,0.5),)
n1 >> nylon(p1.degree + PWalk(),dur=PDur(3,8)|[0.5,1.5],formant=linvar([0,1]),delay=(0,0.5),) + (0,9)

p1 >> donk(P[0,1,2,[3,5]],dur=8)
p1 >> donk(P[0,1,2,[3,P*(3,5,7)]],dur=8)
p1 >> donk(P[0,1,2,[3,P*(3,5,7)]],dur=8).every(5,"offadd",4)
p1 >> donk(P[0,1,2,[3,P*(3,5,7)]],dur=PSum(5,8)).every(5,"offadd",4)
p1 >> donk(P[0,1,2,[3,P*(3,5,7)]],dur=PSum(5,8)).every(5,"offadd",4) + (0,2)
p1 >> donk(P[0,1,2,[3,P*(3,5,7)]],dur=PSum(5,8)).every(5,"offadd",4) + (0,2,const(7))

d1 >> play("ppP([pp]p[pP]P)",)
d1 >> play("ppP([pp]p[pP]P)",sample=PWhite(5),)
d1 >> play("ppP([pp]p[pP]P)",sample=PWhite(5),rate=PRand([0.25,0.5,1,2]))

Group(p1,d1).only()

s1 >> snick(p1.degree,)

c1 >> crunch(p1.degree,)
c1 >> crunch(p1.degree,shape=linvar([0,0.8],12),)

Group(p1,s1,c1).only()

#### > run block <
s1.stop()
c1.stop()
d1 >> play("ppP([pp]p[pP]P)",sample=PWhite(5),rate=PRand([0.25,0.5,1,2]))
#### > run block <
