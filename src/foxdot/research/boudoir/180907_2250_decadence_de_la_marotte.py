# boudoir - decadence de la marotte
# https://www.youtube.com/watch?v=EnVdmTRvllw
# https://gist.github.com/jf-parent/17abfe962599eca3bdb2982fbef047c5

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

chords = [[0, 1], [(1, 2), (2, 3)]]
Clock.stop()
def main():
    print('main')
    ~p1 >> sawbass(chords, oct=[4,[4,5],7], dur=1, formant=[1,2,3], lpf=1200, sus=var([1,.5],[16,8])).after(420, 'stop')
Clock.future(0, main)
def main1():
    print('main1')
    ~p2 >> gong(chords, amp=linvar([.2,1.2],16)).after(360, 'stop')
Clock.future(30, main1)
def main2():
    print('main2')
    ~b1 >> play('-*', amp=linvar([.8,0],16)).after(240, 'stop')
    ~b2 >> play('~', dur=var([.5,1,2],16), amp=.8).after(240, 'stop')
    ~b3 >> play('(gg)', dur=1, amp=linvar([.8,0],16)).after(240, 'stop')
Clock.future(60, main2)
def main3():
    print('main3')
    ~p6 >> blip([(0,1),(2,3),(4,5),(1,2),(2,3),(4,5)], oct=[4,5], amp=linvar([.5,0],16), chop=linvar([0,2,4],8), formant=linvar([0,2,6],32), vib=10, vibdepth=linvar([0,.2,1],[32,8,2]), tremolo=2, echo=2, sus=2).after(120, 'stop')
Clock.future(120, main3)
def main4():
    print('main4')
    ~p7 >> donk([0,1], dur=var([.25,.5],8)).after(320, 'stop')
Clock.future(160, main4)
def main5():
    print('main5')
    ~p8 >> pluck(chords, vib=1, amp=1.2).after(120, 'stop')
Clock.future(240, main5)
def main6():
    print('main6')
    ~p3 >> bug([5]).every(12, 'offadd', 12).after(120, 'stop')
Clock.future(320, main6)
def main7():
    print('main7')
    ~p4 >> squish(P[:4], dur=2, amp=.4).after(60, 'stop')
Clock.future(360, main7)
Clock.future(400, Clock.clear)

