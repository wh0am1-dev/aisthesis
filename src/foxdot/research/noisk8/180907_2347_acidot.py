# acidot - noisk8
# https://youtu.be/_dGkRJUqnS0

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 128

~k2 >> play('[//]', dur=1)
~k2 >> play('[//] ', dur=1)

~h3 >> play('Z', dur=PDur(1,8), sample=PRand(2), amp=linvar([0,1.3]), hpf=linvar([10,1200]))
~h3 >> play('Z', dur=PDur(1,8), sample=PRand(2), amp=linvar([0,1.5]), hpf=linvar([10,1200]))

~k3 >> play(' *', dur=1)
~k3 >> play(' *', dur=1, amp=2)

~k4 >> play('u ', dur=1)
~k4 >> play('u ', dur=1, sample=PRand(1))

~h1 >> play('|K2|', dur=PDur(1,8), hpf=linvar([10,700]), amp=1.2)

~k2 >> play('[/-/] ', dur=1)
~k2 >> play('[/-] ', dur=1)
~k2 >> play('[--] ', dur=1)
~k2 >> play('[--]', dur=1)

~h1 >> play('|K2|', dur=PDur(2,8), hpf=linvar([10,700]), amp=1.2)
~h1 >> play('|K2|', dur=PDur(3,8), hpf=linvar([10,700]), amp=1.2)

~k1 >> play('|V0| ')

~k2 >> play('[--]', amp=2, dur=.5)

~k4 >> play('u ', dur=1, sample=PRand(3))

~h3 >> play('Z', dur=PDur(2,8), sample=PRand(2), amp=linvar([0,1.5]), hpf=linvar([10,1200]))

~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=.2, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=.3, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=.6, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=.8, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=.9, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=1, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=1.2, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=1.4, vib=2)

~k4 >> play('+ ', dur=1, sample=PRand(3))

~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=1.7, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=2, vib=2)

~h3 >> play('Z', dur=PDur(3,8), sample=PRand(2), amp=linvar([0,1.5]), hpf=linvar([10,1200]))
~h3 >> play('Z ', dur=PDur(3,8), sample=PRand(2), amp=linvar([0,1.5]), hpf=linvar([10,1200]))
~h3 >> play('Z ', dur=PDur(3,8), sample=PRand(1), amp=linvar([0,1.5]), hpf=linvar([10,1200]))

~k3 >> play(' =', sample=3, dur=1, amp=2)
~k3 >> play(' =', sample=3, dur=.5, amp=2)

~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=2.4, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=2.7, vib=2)
~h2 >> play('|k0||k2| |k3|', dur=PDur(4,8), amp=2.7, vib=4)

~h1 >> play('|K1|', dur=PDur(3,8), hpf=linvar([10,700]), amp=1.2)

~k3 >> play(' |o3|', dur=1, amp=2)
~k3 >> play(' |o3|', dur=1, amp=1.3)

~h1 >> play('|K1|', dur=PDur(5,8), hpf=linvar([10,700]), amp=1.2)
~h1 >> play('|K1|', dur=PDur(5,8), hpf=linvar([10,700]), amp=1.5)

~h2 >> play('|k0||k2| |k3|', dur=PDur(5,8), amp=2.7, vib=4)

h3.stop()

~h3 >> space(oct=4, dur=16)

### > block <
~k3 >> play(' |o3|', dur=.5, amp=1.3)
~k4 >> play('+', dur=PDur(3,8), sample=PRand(3))
###

~k3 >> play(' |o3|', dur=1, amp=1.3)

~k4 >> play('+', dur=PDur(3,8), amp=2, sample=PRand(3))

~k3 >> play(' =', sample=3, dur=1, amp=2)

~k2 >> play(' n', amp=2, dur=.5)

~h2 >> play('|k0||k2| |k3|', dur=PDur(5,8)|2, amp=2.7, vib=4)

~h1 >> play('|K1|', dur=PDur(5,8), hpf=linvar([10,600]), amp=1.5)

~h2 >> play('|k0||k1| |k3|', dur=PDur(5,8)|2, amp=2.7, vib=4)
~h2 >> play('|k0||k1| |k3|', dur=PDur(5,8), amp=2.7, vib=4)
~h2 >> play('|k0||k1| |k3|', dur=PDur(5,8), amp=2.7, vib=8)
~h2 >> play('|k0||k1| |k3|', dur=PDur(5,8), amp=2.7, vib=1)
~h2 >> play('|k0||k1| |k3|', dur=PDur(3,8), amp=2.7, vib=1, vibdepth=.1)
~h2 >> play('|k0||k2| |k3|', dur=PDur(3,8), amp=2.7, vib=1, vibdepth=.1)

~h3 >> space(oct=4, dur=16, slide=.8)
~h3 >> space(oct=4, dur=16, slide=.9)

~k3 >> play(' |o3|', sample=3, dur=1, amp=1.3)
~k3 >> play(' |o3|', sample=3, dur=1, amp=1.3).every(2, 'stutter', 3)
~k3 >> play(' |o3|', sample=3, dur=2, amp=1.3).every(4, 'stutter', 3)

~k4 >> play('+', dur=PDur(5,8), amp=2, sample=PRand(3))
~k4 >> play('e', dur=PDur(5,8), amp=2, sample=PRand(1))

~h2 >> play('|k0||k2| |k3|', dur=PDur(3,8), amp=2.8, vib=1, vibdepth=.1)

~k1 >> play('|V4| ', dur=1)

k3.stop()

~k2 >> play(' ~', amp=2, dur=.5)
~k2 >> play(' ~', amp=4, dur=.5)

~k1 >> play('|V4| ', dur=.5)
~k1 >> play('|V4| ', dur=.5, hpf=linvar([12,400]))

~k2 >> play(' =', amp=4, dur=.5)

~k3 >> play(' |o3|', dur=1, amp=1.3).every(4, 'stutter', 3)

~h2 >> play('|k0||k2| |k3|', dur=PDur(5,8), amp=2.8, vib=1, vibdepth=.1)

~k4 >> play('e', dur=PDur(5,8).rotate(2), amp=2, sample=PRand(1))
~k4 >> play('e', dur=PDur(5,8).rotate(4), amp=2, sample=PRand(1))

k1.stop()

~k1 >> play('|V2| ', dur=.5)

~h3 >> space(oct=4, dur=16, slide=.1)

~k4 >> play('e', dur=PDur(1,8).rotate(4), amp=2, sample=PRand(1))

~k3 >> play(' |o3|', dur=1, amp=1.3).every(4, 'stutter', 2)

~h1 >> play('|K1|', dur=PDur(7,8), hpf=linvar([10,600]), amp=1.5)

~h2 >> play('|k0||k2| |k3|', dur=PDur(7,8), amp=2.8, vib=1, vibdepth=.1)
~h2 >> play('|k0||k2| |k3|', dur=PDur(7,8), amp=2.8, vib=1, vibdepth=.4)
~h2 >> play('|k0||k2| |k3|', dur=PDur(7,8), amp=2.8, vib=1, vibdepth=.9)

k2.stop()
k3.stop()

~h2 >> play('|k0||k2| |k3|', dur=PDur(7,8), amp=2.8, vib=5, vibdepth=.9)
~h2 >> play('|k0||k2| |k3|', dur=PDur(7,8), amp=2.8, vib=9, vibdepth=.9)

~k1 >> play('|V2| ', dur=2)
~k1 >> play('|V2| ', dur=4)

~h3 >> space(oct=4, dur=16, slide=.9)
~h3 >> space(oct=4, dur=16, slide=.999999)

~h2 >> play('|k0||k2| |k3|', dur=PDur(7,8), amp=3, vib=9, vibdepth=.9)
~h2 >> play('|k0||k2| |k3|', dur=PDur(7,8), amp=4, vib=9, vibdepth=.9)

~h1 >> play('|K1|', dur=PDur(7,8), hpf=linvar([10,600]), amp=2)
~h1 >> play('|K1|', dur=PDur(7,8), hpf=linvar([10,600]), amp=3)
~h1 >> play('|K1|', dur=PDur(7,8), hpf=linvar([10,600]), amp=2)

### > block <
~k1 >> play('|V2| ', dur=.5)
~k2 >> play(' =', amp=4, dur=.5)
###

~h2 >> play('|k0||k2| |k3|', dur=PDur(7,8), amp=4, vib=4, vibdepth=.9)
~h2 >> play('|k0||k2||k3|', dur=PDur(7,8), amp=4, vib=4, vibdepth=.9)
~h2 >> play('|k0||k2||k3|', dur=PDur(5,8), amp=4, vib=4, vibdepth=.9)
~h2 >> play('|k0||k2||k3|', dur=PDur(5,8), amp=4, vib=4, vibdepth=.5)
~h2 >> play('|k0||k2||k3|', dur=PDur(5,8), amp=4, vib=4, vibdepth=.3)
~h2 >> play('|k0||k2||k3|', dur=PDur(5,8), amp=4, vib=4, vibdepth=linvar([0,.5]))
~h2 >> play('|k0||k2||k3|', dur=PDur(5,8), amp=4, vib=4, vibdepth=linvar([0,.8,.9]))

~h1 >> play('|K1|', dur=PDur(7,8), hpf=linvar([10,900]), amp=2)
~h1 >> play('|K1|', dur=PDur(7,8), hpf=linvar([10,100]), amp=2)

### > block <
~k3 >> play(' |o3|', dur=1, amp=1.3).every(2, 'stutter', 2)
~k4 >> play('e', dur=PDur(3,8).rotate(4), amp=2, sample=PRand(1))
###

~h3 >> space(oct=4, dur=16, slide=.999999, amp=1.2)
~h3 >> space(oct=4, dur=16, slide=.999999, amp=1.4)
~h3 >> space(oct=4, dur=16, slide=.999999, amp=1.6)
~h3 >> space(oct=4, dur=16, slide=.999999, amp=1.8)
~h3 >> space(PSine(3), oct=4, dur=16, slide=.999999, amp=1.8)

~h2 >> play('|k0||k2||k3|', dur=PDur(3,8), amp=4, vib=4, vibdepth=linvar([0,.8,.9]))

~k3 >> play(' |o3|', dur=2, amp=1.3).every(2, 'stutter', 2)

~k4 >> play('e', dur=PDur(1,8).rotate(4), amp=2, sample=PRand(1))

~h3 >> space(PSine(8), oct=4, dur=16, slide=.999999, amp=1.8)

~h1 >> play('|K1|', dur=PDur(1,8), hpf=linvar([10,100]), amp=2)

~h2 >> play('|k0||k2||k3|', dur=PDur(1,8), amp=4, vib=4, vibdepth=linvar([0,.8,.9]))
~h2 >> play('|k0||k2||k3|', dur=PDur(1,32), amp=4, vib=4, vibdepth=linvar([0,.8,.9]))

### > block <
~k1 >> play('|V0| ', dur=.5)
~k2 >> play(' =', amp=4, dur=2)
###

~h1 >> play('|K1|', dur=PDur(1,56), hpf=linvar([10,100]), amp=2)

~k1 >> play('|V0| ', dur=.4)
~k1 >> play('|V0| ', dur=4)

~k2 >> play(' =', amp=4, dur=45)

~k1 >> play('|V0| ', dur=100)

~k3 >> play(' |o3|', dur=100, amp=1.3).every(2, 'stutter', 2)

Clock.clear()

