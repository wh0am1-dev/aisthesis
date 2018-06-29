Scale.default = Scale.egyptian
Root.default = 0
Clock.bpm = 120

print(SynthDefs)
print(BufferManager())
print(Player.get_attributes())

p1 >> play(
    P["@+ET"],
).every(3, "stutter", dur=1/2)

p1 >> play(
    P["V+EA"],
).every(3, "stutter", dur=1/2)

p2 >> play(
    P["<X  ><  n >"],#.layer("mirror"),
    sample = 2,
)

p2.stop()
p3.stop()
p4.stop()

p5 >> play(
    P["{ pPpP[pp][PP][pP][Pp]}"],
    dur = 1/2,
    sample = 1,
    amp = 2
)

v1chop = 128  # 16, 32, 48, 56, 64, 128, 256
v1 >> varsaw(
    [(0,1),(4,5),(1,2),(5,6),(8,9)],
    oct = 4,
    dur = [8,8,8,4,4],
    sus = [8,8,8,4,4],
    pan = (-1, 1),
    slide = 0,
    chop = [v1chop]*3+[v1chop/2]*2,
)

d1 >> dub(
    [0,4,1,5,8],
    oct = 3,
    dur = [8]*3+[4]*2,
    sus = [8]*3+[4]*2,
    pan = (-1,1),
    hpf = 100
)

# ================================
