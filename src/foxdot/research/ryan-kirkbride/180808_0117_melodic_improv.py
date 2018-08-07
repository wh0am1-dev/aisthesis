# ryan kirkbride - melodic improv
# https://youtu.be/7MFQWqMLjRU

Scale.default = 'minor'
Root.default = 0
Clock.bpm = 120

~d1 >> play(P['x  '][:8], drive=.5)
~d1 >> play(P['x v'][:8], drive=.5)
~d1 >> play(P['x v'][:8], drive=.5).sometimes('rate.offmul', 1.5)
~d1 >> play(P['x v'][:8], drive=.5).sometimes('rate.offmul', 1.5, .75)
~d1 >> play(P['x( d)v'][:8], drive=.5).sometimes('rate.offmul', 1.5, .75)
~d1 >> play(P['x( d)v'][:8], drive=.5).sometimes('rate.offmul', 1.5, .75).every(6, 'stutter', 4, dur=3, pan=[-1,1], rate=[2])
~d1 >> play(P['x( d)v'][:8], drive=.5).sometimes('rate.offmul', 1.5, .75).every(6, 'stutter', 4, dur=3, pan=[-1,1], rate=[2,2.5])

~d2 >> play(' -')

~d1 >> play(P['x( d)v'][:8], drive=.5, formant=1).sometimes('rate.offmul', 1.5, .75).every(6, 'stutter', 4, dur=3, pan=[-1,1], rate=[2,2.5])
~d1 >> play(P['x( d)v'][:8], drive=.5, formant=2).sometimes('rate.offmul', 1.5, .75).every(6, 'stutter', 4, dur=3, pan=[-1,1], rate=[2,2.5])
~d1 >> play(P['x( d)v'][:8], drive=.5, formant=4).sometimes('rate.offmul', 1.5, .75).every(6, 'stutter', 4, dur=3, pan=[-1,1], rate=[2,2.5])
~d1 >> play(P['x( d)v'][:8], drive=.5, formant=0).sometimes('rate.offmul', 1.5, .75).every(6, 'stutter', 4, dur=3, pan=[-1,1], rate=[2,2.5])

~d2 >> play('<( m)-><   A>')
~d2 >> play('<( b)-><   A>')
~d2 >> play('<( b)-><   A>', rate=2)
~d2 >> play('<( (bm))-><   A>', rate=2)
~d2 >> play('<( (bm))-><   A>', rate=2).every([6,2], 'mirror')
~d2 >> play('<( (bm))-><   A><  *>', rate=2).every([6,2], 'mirror')
~d2 >> play('<( (bm))-><   A><*( [ *])[ *]>', rate=2).every([6,2], 'mirror')

~d1 >> play(P['x( d)v'][:8], drive=.5, formant=0, hpf=var([0,4000],[28,4])).sometimes('rate.offmul', 1.5, .75).every(6, 'stutter', 4, dur=3, pan=[-1,1], rate=[2,2.5])

~k1 >> soprano(dur=8, chop=4)
~k1 >> soprano(dur=8, chop=8, delay=.5)
~k1 >> soprano(dur=8, chop=8, delay=.5) + (0,9)
~k1 >> soprano(dur=8, chop=8, delay=.5) + (0,6,9)
~k1 >> soprano(dur=8, chop=16, delay=.5) + (0,6,9)
~k1 >> soprano(dur=8, chop=16, delay=.5, room=1) + (0,6,9)
~k1 >> soprano(dur=8, chop=16, delay=.5, room=1) + (var([0,-1,-2],8),6,9)

~b1 >> sawbass(var([0,4,3],8))
~b1 >> sawbass(var([0,4,[3,5]],8), dur=PDur(3,8))
~b1 >> sawbass(var([0,4,[3,5]],8), dur=PDur(3,8), cutoff=linvar([1000,7000],32))

~d2 >> play('<( (em))-><   A><*( [ *])[ *]>', rate=2).every([6,2], 'mirror')
~d2 >> play('<( (|b2|m))-><   A><*( [ *])[ *]>', rate=2).every([6,2], 'mirror')

d_all.stop()

~b1 >> sawbass(var([0,4,[3,5]],8), dur=PDur(3,8,[0,2]), cutoff=linvar([1000,7000],32))
~b1 >> sawbass(var([0,4,[3,5]],8), dur=PDur(3,8,[0,2]), cutoff=linvar([1000,7000],32)).often('offadd', 7)

~k1 >> soprano(dur=8, chop=16, delay=.5, room=1, shape=.5) + (var([0,-1,-2],8),6,9)
~k1 >> soprano(dur=8, chop=16, delay=.5, room=1, shape=.5, oct=4) + (var([0,-1,-2],8),6,9)

~d1 >> play('|x2|:')

~k1 >> soprano(dur=8, chop=32, delay=.5, room=1, shape=.5, oct=4) + (var([0,-1,-2],8),6,9)
~k1 >> varsaw(dur=8, chop=32, delay=.5, room=1, shape=.5, oct=4) + (var([0,-1,-2],8),6,9)
~k1 >> varsaw(dur=8, chop=64, delay=.5, room=1, shape=.5, oct=4) + (var([0,-1,-2],8),6,9)

~b1 >> sawbass(var([0,4,[3,5]],8), dur=PDur(3,8,[0,2]), lpf=5000, cutoff=linvar([1000,7000],32)).often('offadd', 7)
~b1 >> sawbass(var([0,4,[3,5]],8), dur=PDur(3,8,[0,2]), lpf=500, cutoff=linvar([1000,7000],32)).often('offadd', 7)

~d1 >> play('<|x2|:><  * >')

~p1 >> saw(P[:8]).penta()
~p1 >> saw(P[:8], dur=.25).penta()
~p1 >> saw(P[:8], dur=.25, vib=12).penta()
~p1 >> saw(P[:8], dur=.25, vib=12, pan=var([-1,1],4)).penta()
~p1 >> saw(P[:8], dur=.25, vib=12, pan=var([-1,1],4), drive=.5).penta()

~d1 >> play('<|-2|:><  * >')
~d1 >> play('<V:><  * >')
~d1 >> play('<V:><  * >').every(6, 'stutter', 4, dur=3)

~p1 >> saw(P[:8], dur=.25, vib=12, pan=var([-1,1],4), drive=.5).penta().every(6, 'splice', [7,6])
~p1 >> saw(P[:8], dur=.25, vib=12, pan=var([-1,1],4), drive=.5, amp=PRand([0,1])[:16]).penta().every(6, 'splice', [7,6])

~p2 >> pluck((0,2,4,6), dur=PDur(3,8)*2)
~p2 >> pluck((0,2,4,6), dur=PDur(3,8)*2, sus=2)

k1.stop()
d1.stop()
b1.stop()

~p2 >> pluck((0,2,4,6), dur=PDur(3,8)*(1,2), sus=2)
~p2 >> pluck((0,2,4,const(6),const(9)), dur=PDur(3,8)*(1,2), sus=2)
~p2 >> pluck((0,2,4,const(6),const(9)), dur=PDur(3,8)*(1,2), sus=2) + var([0,-4],8)
~p2 >> pluck((0,2,4,const(6),const(9)), dur=PDur(3,8)*(1,2), sus=2) + var([0,1,-2,3],8)
~p2 >> pluck((0,2,4,const(7),const(9)), dur=PDur(3,8)*(1,2), sus=2) + var([0,1,-2,3],8)

~p3 >> space([0,7,3,4], dur=2)
~p3 >> space([0,7,3,4], dur=2).spread()

~d1 >> play('x-*-', hpf=4000)

~p2 >> pluck((0,2,4,const(7),const(9)), dur=PDur(3,8)*(1,2), sus=2, oct=4) + var([0,1,-2,3],8)
~p2 >> pluck((0,2,4,const(7),const(9)), dur=PDur(3,8)*(1,2), sus=2, oct=(4,5)) + var([0,1,-2,3],8)

~d1 >> play('x-*-', hpf=400)
~d1 >> play('x-*-', hpf=400).often('amen')
~d1 >> play('x-*-', sample=2, hpf=400).often('amen').every(5, 'sample.offadd', -2, .75)

~c1 >> creep(dur=32, amp=2, slide=1)

~d1 >> play(' -*-', sample=2, hpf=0).often('amen').every(5, 'sample.offadd', -2, .75)

### > block <
~d1 >> play('x-*-', sample=2, hpf=0).often('amen').every(5, 'sample.offadd', -2, .75)
~c2 >> play('#', dur=32)
c1.stop()
###

~d1 >> play('(x-)(-x)*-', sample=2, hpf=0).often('amen').every(5, 'sample.offadd', -2, .75)
~d1 >> play('(x-)(-x)*-', sample=2, hpf=0).sometimes('amen').every(5, 'sample.offadd', -2, .75)
~d1 >> play('(x-)(-x)*{-x}', sample=2, hpf=0).sometimes('amen').every(5, 'sample.offadd', -2, .75)

~d2 >> play('X ')

~d1 >> play('(x-)(-x)*{-x}', sample=2, hpf=0).sometimes('amen').every(5, 'sample.offadd', -2, .75).every(7, 'stutter', 4, dur=var([3,2,1],7))
~d1 >> play('(x-)(-x)*{-x}', sample=2, hpf=0).sometimes('amen').every(5, 'sample.offadd', -2, .75).every(7, 'stutter', 4, dur=var([3,2,1],7), pan=[-1,1])

p3.only()

~b1 >> sawbass([0,1,5,3], dur=4)
~b1 >> sawbass([0,1,5,3], dur=4).spread()
~b1 >> sawbass([0,1,5,3], dur=4, sus=3.5).spread()
~b1 >> sawbass([0,1,5,3], dur=4, sus=3).spread()
~b1 >> sawbass([0,1,5,3], dur=4, sus=3, room=1).spread()

~p2 >> keys((0,2,4,const(7),const(9)), dur=PDur(3,8)*(1,2), sus=2, oct=(4,5)) + var([0,1,-2,3],8)
~p2 >> keys((0,2,4,const(7),const(9)), dur=PDur(3,8)*(1,2), sus=2, oct=(4,5), rate=linvar([1,32],32)) + var([0,1,-2,3],8)
~p2 >> keys((0,2,4,const(7),const(9)), dur=PDur(3,8)*(1,2), sus=1, oct=(4,5), rate=linvar([1,32],32)) + var([0,1,-2,3],8)

### > block <
~d1 >> play('(x-)(-x)*{-x}', sample=2, hpf=0).sometimes('amen').every(5, 'sample.offadd', -2, .75).every(7, 'stutter', 4, dur=var([3,2,1],7), pan=[-1,1])
~d2 >> play('X ')
###

~b2 >> bell(2, dur=2/3, amp=.5)
~b2 >> bell(2, dur=2/3, amp=.5, pan=linvar([-1,1],32))
~b2 >> bell(2, dur=2/3, amp=.5, pan=linvar([-1,1],32), oct=6)
~b2 >> bell(var([2,4],[12,4]), dur=2/3, amp=.5, pan=linvar([-1,1],32), oct=6)

~p2 >> keys((0,2,4,const(7),const(9)), dur=4, sus=1, oct=(4,5), rate=linvar([1,32],32)) + var([0,1,-2,3],8)
~p2 >> keys((0,2,4,const(7),const(9)), dur=4, rate=linvar([1,32],32)) + var([0,1,-2,3],8)

~p1 >> saw(P[:8], dur=.25, vib=12, pan=var([-1,1],4), drive=.5, amp=PRand([0,1])[:16]).penta().every(6, 'splice', [7,6])

@nextBar
def change():
    Scale.default = 'major'
    Root.default += 2

p1.only()

~p2 >> keys((0,2,4,const(7),const(9)), dur=4, sus=2, rate=linvar([1,32],32)) + var([0,1,-2,3],8)

~p1 >> saw(P[:8], dur=.25, vib=12, pan=var([-1,1],4), room=1, drive=.5, amp=PRand([0,1])[:16]).penta().every(6, 'splice', [7,6])

~b1 >> sawbass([0,1,5,3], dur=PDur(3,8)*2, sus=.5, room=1).spread()
~b1 >> sawbass([0,1,5,3], dur=PDur(3,8)*2, sus=.5, room=0).spread()
~b1 >> sawbass(var([0,1,5,3],4), dur=PDur(3,8)*2, sus=.5, room=0).spread()

~b2 >> bell(var([2,4],[12,4]), dur=2/3, amp=.5, pan=linvar([-1,1],32), oct=6)

~p3 >> space([0,7,3,4], dur=2).spread()

~d2 >> play('|x2|s')
~d2 >> play('<|x2|s><[--]>')

~d3 >> play('  o ', formant=4)
~d3 >> play('  o ', formant=4).every(6.5, 'jump', cycle=8)
~d3 >> play('  o( [ o])', formant=4).every(6.5, 'jump', cycle=8)
~d3 >> play('  o( [( o)o])', formant=4).every(6.5, 'jump', cycle=8)
~d3 >> play('  o(l[( o)o])', formant=4).every(6.5, 'jump', cycle=8)
~d3 >> play('  o(n[( o)o])', formant=4).every(6.5, 'jump', cycle=8)
~d3 >> play('  o(n[( o)o])', formant=4, shape=.2).every(6.5, 'jump', cycle=8)
~d3 >> play('  o(n[( o)o])', formant=4, shape=0).every(6.5, 'jump', cycle=8)

~d2 >> play('<| 2|s><[--]>')

Master().hpf = var([0,3000],[28,4])

~d2 >> play('<|x2|s><[--]>')

Master().hpf = 0

~p2 >> keys((0,2,4,const(7),const(9)), dur=PDur(3,8), sus=1, delay=(0,.5), rate=linvar([1,32],32)) + var([0,1,-2,3],8)

~p3 >> space([0,7,3,4], dur=2).spread().every(7, 'offadd', 7, .75)

~d2 >> play('<|x2|s><[--]><  H >')

~d4 >> play('n', dur=.25, sample=PRand(5))
~d4 >> play('n', dur=.25, sample=PRand(5), pan=PWhite(-1,1))
~d4 >> play('n', dur=.25, sample=PRand(5), pan=PWhite(-1,1)).often('stutter', 4)
~d4 >> play('n', dur=.25, sample=PRand(5), pan=PWhite(-1,1)).often('stutter', 4, dur=.5)
~d4 >> play('n', dur=.25, sample=PRand(5), pan=PWhite(-1,1)).often('stutter', var([4,8]), dur=.5)

d_all.only()

~p3 >> space([0,7,3,4], dur=2).spread().every(7, 'offadd', 7, .75)

~b1 >> sawbass(var([0,1,5,3],4), dur=PDur(3,8)*2, sus=.5, room=0).spread()

~b2 >> bell(var([2,4],[12,4]), dur=2/3, amp=.5, pan=linvar([-1,1],32), oct=6)

Master().amplify = var([1,0],[28,4])

### > block <
~p1 >> saw(P[:8], dur=.25, vib=12, pan=var([-1,1],4), room=1, drive=.5, amp=PRand([0,1])[:16]).penta().every(6, 'splice', [7,6])
~p2 >> keys((0,2,4,const(7),const(9)), dur=PDur(3,8), sus=1, delay=(0,.5), rate=linvar([1,32],32)) + var([0,1,-2,3],8)
###

Master().amplify = 1

d4.stop()
d3.stop()
b2.stop()
b1.stop()
p1.stop()

~p2 >> keys((0,P*(6,4),7), dur=4)

~p3 >> space([2,4,6,7,9], dur=PDur(5,8)).spread().every(7, 'offadd', 7, .75)
~p3 >> space([2,4,6,7,9], dur=PDur(5,8)*2).spread().every(7, 'offadd', 7, .75)

d2.stop()

Scale.default = 'minor'

~p2 >> keys((var([0,-1,-2,-3],8),P*(6,4),7), dur=4)
~p2 >> keys((var([0,-1,-2,-3],8),P*(6,4,2),7), dur=4)
~p2 >> keys((var([0,-1,-2,-3],8),P*(6,4,2),7), dur=4, rate=P[:16])

~k1 >> klank()
~k1 >> klank((0,9))

~p1 >> pulse(dur=PDur(3,9))
~p1 >> pulse(dur=PDur(3,9), delay=(0,.5))
~p1 >> pulse(dur=PDur(3,9), delay=(0,.5), cut=.5)
~p1 >> pulse(dur=PDur(3,9), delay=(0,.5), cut=.25)
~p1 >> pulse(dur=PDur(3,9), delay=(0,.5), cut=.25, vib=12)
~p1 >> pulse((0,4), dur=PDur(3,9), delay=(0,.5), cut=.25, vib=12)
~p1 >> pulse((0,[4,6,7]), dur=PDur(3,9), delay=(0,.5), cut=.25, vib=12)
~p1 >> pulse((0,4), dur=PDur(3,9), delay=(0,.5), cut=.25, vib=12)
~p1 >> pulse((0,4), dur=PDur(3,9), delay=0, cut=.25, vib=12)
~p1 >> pulse((0,[4,6,7]), dur=PDur(3,9), delay=0, cut=.25, vib=12)
~p1 >> pulse((0,[4,6,7]), dur=PDur(3,8)*2, delay=0, cut=.25, vib=12)
~p1 >> pulse((0,[4,6,7]), dur=PDur(3,8)*2, delay=0, cut=.25, vib=12, oct=4)
~p1 >> pulse((0,[4,6,7]), dur=[4,4,2], delay=0, cut=.25, vib=12, oct=4)

~k2 >> play('k', sample=P[:5])
~k2 >> play('k', sample=P[:5], dur=PDur(3,8))
~k2 >> play('k', sample=P[:5], dur=PDur(3,8)*(1,2))
~k2 >> play('k', sample=P[:5], dur=PDur(3,8)*(1,2), pan=(-1,1))

~d1 >> play('x ')

~k1 >> klank((0,9), oct=4)
~k1 >> klank((0,9), oct=4, lpf=linvar([1000,2000],32))

~p1 >> pulse((0,[4,6,7]), dur=[4,4,2], delay=0, cut=.25, vib=12, oct=6)
~p1 >> pulse([0,4,2,6,7,0], dur=.5, amp=PStep(6,0,1)).penta()
~p1 >> pulse([0,4,2,6,7,0], dur=.25, amp=PStep(6,0,1)).penta()

~b1 >> bass(var([0,-1,-2,-3],8), dur=8)
~b1 >> bass(var([0,-1,-2,-3],8), dur=8, room=1)
~b1 >> bass(var([0,-1,[-2,2],[-3,3]],8), dur=8, room=1)
~b1 >> bass(var([0,-1,[-2,2],[-3,3]],8), dur=8, room=1).spread()

~d1 >> play('x:')
~d1 >> play('X:')

~p1 >> pulse([0,4,2,6,7,0], dur=.25, amp=PStep(6,0,1), drive=1).penta()
~p1 >> pulse([0,4,2,6,7,0], dur=.25, amp=PStep(6,0,1), drive=1, shape=.5).penta()
~p1 >> pulse([0,4,2,6,7,0], dur=.25, amp=PStep(6,0,1), drive=1, shape=.5).penta().every(5, 'offadd', 2, .5)
~p1 >> pulse([0,4,2,6,7,0], vib=12, dur=.25, amp=PStep(6,0,1), drive=1, shape=.5).penta().every(5, 'offadd', 2, .5)

~d1 >> play('<X:>< s>')
~d1 >> play('<X:>< s>').often('stutter', dur=var([1,1.5]))

~d2 >> play('  % ', cut=.1)
~d2 >> play('  % ', cut=.1, amp=2)
~d2 >> play('  % ', cut=.25, amp=2)
~d2 >> play('  % ', cut=.25, amp=2)
~d2 >> play('  @ ', cut=.25, amp=2, sample=1)
~d2 >> play('  @ ', cut=.25, amp=2, sample=0)
~d2 >> play('  N ', cut=.25, amp=2, sample=0)

Group(k1,b1,p1,p2,p3).amplify = var([1,0],[28,4])

~d1 >> play('< :>< s>').often('stutter', dur=var([1,1.5]))
~d1 >> play('<V:>< s>').often('stutter', dur=var([1,1.5]))

Group(k1,b1,p1,p2,p3).amplify = 1

~k1 >> klank((0,9), oct=4, lpf=linvar([1000,2000],32), chop=4)
~k1 >> klank((0,9), oct=4, lpf=linvar([1000,2000],32), chop=4, drive=.5)

~b1 >> bass(var([0,-1,[-2,2],[-3,3]],8), dur=PDur(3,8), room=1).spread()

~k1 >> klank((0,9), oct=4, lpf=linvar([1000,2000],32), chop=4, drive=0)
~k1 >> klank((0,9), oct=4, lpf=linvar([1000,2000],32), chop=8, drive=0)

p2.stop()
k1.stop()
k2.stop()
b1.stop()
d1.stop()
d2.stop()
p3.stop()

Clock.clear()
