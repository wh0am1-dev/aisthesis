Scale.default = Scale.minor
Root.default = 0
Clock.bpm = 100

p1 >> play("<Vn>",sample=1)
p1 >> play("<Vn><{ pP[pp][PP][pP][Pp]}>",sample=1)
p1 >> play("<Vn><{ +s[++][ss][+s][s+]}>",sample=2).every(8,"amen")

p2 >> play("c",amp=0.5)
p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=0.5,rate=1,chop=0,coarse=0,pan=0)
p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=1,chop=0,coarse=0,pan=0)
p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=0.5,chop=0,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=1,chop=0,coarse=0,pan=linvar([-1,1],[8,8]))

p2 >> play("w",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=1,chop=1,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("w",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=0.5,chop=1,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("w",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=[1]*6+[0.5],chop=1,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("w",dur=1/4,amp=PRand([1,0.5,0.25]),rate=0.5,chop=1,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("w",dur=1/4,amp=PRand([1,0.5,0.25]),rate=0.5,chop=2,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("w",dur=1/4,amp=PRand([1,0.5,0.25]),rate=0.5,chop=var([1,2],[3.5,0.5]),coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("w",dur=1/4,amp=PRand([1,0.5,0.25]),rate=1,chop=var([1,2],[3.5,0.5]),coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("c",amp=0.5)

p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=1,chop=1,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=1,chop=2,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=0.5,chop=2,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=0.5,chop=1,coarse=0,pan=linvar([-1,1],[8,8]))
p2 >> play("c",dur=PDur(5,8)|[0.5,1.5],amp=PRand([1,0.5,0.25]),rate=0.5,chop=0,coarse=2,pan=linvar([-1,1],[8,8]))

a1 >> klank(PWalk(16,4),shape=PWalk(1,0.1))
