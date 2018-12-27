Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 120
_ = [0,5,10,15,19,24]

print('>>> scales <<<')
print(Scale.names())
print('n>>> synths <<<')
print(SynthDefs)
print('n>>> fx <<<')
print(FxList)
print('n>>> pattern <<<')
print(PatternMethods)
print('n>>> samples <<<')
print(Samples)

~z1 >> play('x(n-n[--])on', amp=.5, lpf=1500, lpr=.25, sample=1)
~a1 >> ambi(P(0,[5,7],12), dur=8, oct=(3,4), amp=.8, room=1, mix=.5, dist=.025, chop=32)
~p1 >> feel(var([5,7],8)+PWalk(), amp=.4, dur=[1,1,.5,.5,1,1,1,1,.5,.5], scale=Scale.romanianMinor, oct=4, shape=.25)
~p2 >> gong(oct=PRand([3,4]), dur=.25, amp=PRand([0,.3,.3])[:64], drive=.025, chop=128)
~b1 >> sawbass(P[0,[5,7,12]], dur=PDur(3,8), oct=4, amp=.5, formant=.25).often('offadd', 21)
