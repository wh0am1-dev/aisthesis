Scale.default = Scale.chromatic
Root.default = 0
Clock.bpm = 138

print(Scale.names())
print(Pattern.get_methods())
print(SynthDefs)
print(Player.get_attributes())
print(BufferManager())
print(Clock.playing)

Samples.addPath('/Users/neko250/software/livecoding/samples/psy0/')

~l1 >> loop('nia_138_drums 1_full_swung', dur=2, amp=.25)
~l2 >> loop('nia_138_big_downsynth_fx', dur=8, rate=.5, amp=.5)
~l3 >> loop('nia_138_cshp_arp_delay_synth', dur=16, amp=.5)
~l4 >> loop('nia_138_dshp_synth_bass_7', dur=16, lpf=0, shape=0, formant=0, amp=.5)

~p1 >> play('{ ppP[pP][Pp][pP  ][Pp  ][ pP ][ Pp ][  pP][  Pp]}', sample=2, rate=PRand([.25,.5,1,2]), dur=1, shape=PWhite(0,.25), amp=1.5)

~s1 >> pulse(P[3]+(0,5,7), oct=(4,5), coarse=PRand([2,4,8,16,32]), dur=8, amp=.75, chop=PRand([0,2,4,8]), delay=(0,.25,.5))
~s2 >> ambi(P[3], oct=(3,4), dur=4, vib=12)
