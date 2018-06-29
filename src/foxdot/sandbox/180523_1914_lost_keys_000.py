Scale.default = "chromatic"
Root.default = 2
Clock.bpm = 100

# ================
print(Scale.names())
print(SynthDefs)
print(Player.get_attributes())
print(BufferManager())
# ================

d1 >> play("x-(-x)(-[  --])", dur=1, room=1, mix=0.5)
s1 >> piano([0,3], dur=4, sus=4, room=1, mix=0.5, oct=4, delay=(0, 0.25, 0.5)) + (0,7,12)
s2 >> keys(s1.degree[0], chop=[2,4], room=0, mix=0).every(4, "offadd", [2, 4, 7])
s3 >> ambi(oct=4, coarse=16, amp=0.5).spread()
s4 >> gong(oct=PRand([6, 7]), dur=0.25)
p1 >> piano(dist=0.01, room=1, mix=0.5, dur=4, sus=4, oct=3, shape=0.25, amp=0.5) + (0, [2,7,4,12])

