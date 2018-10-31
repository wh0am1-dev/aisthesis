Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 60

var.base = var([2,0,-1,-2],2)

b1 >> sawbass(var.base, amp=.8, dur=[1.5,.5], oct=4, lpf=1200, room=1, mix=.25, dist=.05).spread()  # coarse=[24,8], formant=.125, pan=PWhite(-1,1)

p1 >> play('P', amp=.8, dur=1, sample=1, room=1, mix=.5)

p2 >> play('p', amp=PRand([0,.8]), dur=1/6, sample=PRand(5), room=1, mix=.25, rate=.5, lpf=1200, lpr=var([.1,1,.1,1,.3],[1,3,1,2,1]), dist=.1)

p2.amp=PRand([0,.4,.8])
p2.amp=PRand([0,.8])

ch = P(2,5,9)

c1 >> piano(ch, amp=.6, dur=PDur(5,16)*(1,2), oct=3, chop=16, formant=1)

c1.dur=PDur(5,16)*(2,1)
c1.dur=PDur(5,16)*(1,2)

k1 >> klank(ch, amp=.1, oct=(3,4), rate=P[:16], lpf=1200, room=1)

pg = [2,5,9,5,2,5]
s1 >> sitar(pg, amp=PRand([0,.6]), dur=[1/3,1/6,1/6], room=1, mix=.25, oct=4, shape=.25, chop=1, lpf=1500, dist=.05)  #.often('offadd', 5)

m1 >> pluck(var.base, amp=.8, dur=2, oct=3, room=1, mix=.5).spread()
