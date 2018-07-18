Scale.default = Scale.minor
Root.default = 0
Clock.bpm = 110

print(Scale.names())
print(SynthDefs)
print(Player.get_attributes())
print(Pattern.get_methods())
print(BufferManager())
print(Clock.playing)

var.chords = [0,5,0,3,0,5,0,4]
~s1 >> zap(var.chords, dur=8, sus=12, oct=(2,3), amp=1, room=1, mix=.5, coarse=4).spread()
~s2 >> creep(var(var.chords,8), dur=4, oct=PRand([(2,3),(3,4),(4,5)]), amp=.125, drive=.05, formant=1, fmod=(0,1))
~s3 >> noise(var(var.chords,8), dur=PRand([.25,.25,.25,.25,.5,.5,1]), oct=4, cut=.25, amp=.25)
~s4 >> sitar(var(var.chords,8)+PWalk(), dur=.25, oct=PRand([4,5,6]), pan=PWhite(-1,1), hpf=800, lpf=1200, shape=PRand([0,.5,1]), amp=PWhite(.2,.8))

~p1 >> play('V', dur=1, lpf=400).every(13, 'stutter', 4, dur=3, cycle=16)
~p2 >> play('n'*6+'[  nn]n', dur=1, delay=.5)
~p3 >> play('H', dur=2, delay=1)

