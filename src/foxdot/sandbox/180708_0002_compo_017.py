Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 80

~p1 >> play('m', dur=PDur(3,8)*2)
~p2 >> play('v', dur=PDur(3,8))
~p3 >> play('t', dur=PDur(3,16))
~p4 >> play('?', dur=16, amp=[1,0], rate=.25)
~p5 >> play('!', dur=16, amp=[0,1], rate=.25)

~s1 >> piano(P[0,1,5,3]+(0,2), dur=8, oct=4, pan=(-1,1)).spread()
~s2 >> space(P[0], dur=PDur(3,8)*2).every(6, 'offadd', [5,7], cycle=8)
~s3 >> glass(P[0,1]+(0,12), dur=8, oct=(4,5))
~s4 >> ambi(P[1,2]+(0,2), dur=8, scale=Scale.minor)

def h_play():
    print(BufferManager())
def h_synth():
    print(SynthDefs)
def h_att():
    print(Player.get_attributes())

