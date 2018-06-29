# Portishead - Mysterons
# by wh0am1

Scale.default = "chromatic"
Clock.bpm = 160

# d1.reset() >> play("- ", dur=0.5, lpf=8000)
# d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
# d3.reset() >> play("    io   i  [oooo][oooo][oooo][oooo]", dur=0.5, lpf=d3.degree.map({"o":linvar([1000, 2000], [16,0])}))
# p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)
# p2.reset() >> piano([-1,3,5,6,5,6,3,-1], dur=[rest(2),1,1,1,1,1,1,rest(8)], sus=4, amp=[0,0.5,1,1,1,1,1,0], shape=0.5, dist=0.01)
# s1.reset() >> pulse([5,5,10,10,5,5,11,11], dur=[2.5,0.5,4.5,0.5,2.5,0.5,4.5,0.5], slide=[0,5/12,0,-5/12,0,6/12,0,-6/12], oct=4, spin=1, hpf=500)

inst = (d1,d2,d3,p1,p2,s1)
def _(*args):
    for i in inst:
        if i not in args:
            i.stop()

_(p1)
p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)

_(d1,d2,d3,s1)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
d3.reset() >> play("    io   i  [oooo][oooo][oooo][oooo]", dur=0.5, lpf=d3.degree.map({"o":linvar([1000, 2000], [16,0])}))
s1.reset() >> pulse([5,5,10,10,5,5,11,11], dur=[2.5,0.5,4.5,0.5,2.5,0.5,4.5,0.5], slide=[0,5/12,0,-5/12,0,6/12,0,-6/12], oct=4, spin=4, hpf=500)

_(d1,d2,d3,p1)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
d3.reset() >> play("    io   i  [oooo][oooo][oooo][oooo]", dur=0.5, lpf=d3.degree.map({"o":linvar([1000, 2000], [16,0])}))
p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)

_(d1,d2,d3,p1,p2)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
d3.reset() >> play("    io   i  [oooo][oooo][oooo][oooo]", dur=0.5, lpf=d3.degree.map({"o":linvar([1000, 2000], [16,0])}))
p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)
p2.reset() >> piano([-1,3,5,6,5,6,3,-1], dur=[rest(2),1,1,1,1,1,1,rest(8)], sus=4, amp=[0,0.5,1,1,1,1,1,0], shape=0.5, dist=0.01)

_(d1,d2,p1)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)

_(d1,d2,p1,s1)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)
s1.reset() >> pulse([5,5,10,10,5,5,11,11], dur=[2.5,0.5,4.5,0.5,2.5,0.5,4.5,0.5], slide=[0,5/12,0,-5/12,0,6/12,0,-6/12], oct=4, spin=1, hpf=500)

_(d1,d2,d3,p1,p2,s1)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
d3.reset() >> play("    io   i  [oooo][oooo][oooo][oooo]", dur=0.5, lpf=d3.degree.map({"o":linvar([1000, 2000], [16,0])}))
p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)
p2.reset() >> piano([-1,3,5,6,5,6,3,-1], dur=[rest(2),1,1,1,1,1,1,rest(8)], sus=4, amp=[0,0.5,1,1,1,1,1,0], shape=0.5, dist=0.01)
s1.reset() >> pulse([5,5,10,10,5,5,11,11], dur=[2.5,0.5,4.5,0.5,2.5,0.5,4.5,0.5], slide=[0,5/12,0,-5/12,0,6/12,0,-6/12], oct=4, spin=1, hpf=500)

_(d1,d2,d3,p1,p2)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
d3.reset() >> play("    io   i  [oooo][oooo][oooo][oooo]", dur=0.5, lpf=d3.degree.map({"o":linvar([1000, 2000], [16,0])}))
p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)
p2.reset() >> piano([-1,3,5,6,5,6,3,-1], dur=[rest(2),1,1,1,1,1,1,rest(8)], sus=4, amp=[0,0.5,1,1,1,1,1,0], shape=0.5, dist=0.01)

_(d1,d2,p1,p2)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
d2.reset() >> play("X X   XX  XX    ", dur=0.5, sample=1, lpf=2000)
p1.reset() >> pluck([5,6,[10,11],-1], dur=[1,1,1,rest(5)], sus=8, oct=3, lpf=400, shape=[0,0.125,0.25,0]) + (0,12)
p2.reset() >> piano([-1,3,5,6,5,6,3,-1], dur=[rest(2),1,1,1,1,1,1,rest(8)], sus=4, amp=[0,0.5,1,1,1,1,1,0], shape=0.5, dist=0.01)

_(d1,p2)
d1.reset() >> play("- ", dur=0.5, lpf=8000)
p2.reset() >> piano([-1,3,5,6,5,6,3,-1], dur=[rest(2),1,1,1,1,1,1,rest(8)], sus=4, amp=[0,0.5,1,1,1,1,1,0], shape=0.5, dist=0.01)

_()
