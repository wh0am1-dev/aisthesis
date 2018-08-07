"""
  Ryan Kirkbride - Delta (fragment):
  https://www.youtube.com/watch?v=6i4PJ128d7Y
"""

Scale.default = Scale.mixolydian
Root.default = 0
Clock.bpm = 140

ch = var([0,-1,3],8)

s1 >> soprano(
    [(ch,7)],
    dur = 8,
    sus = 12,
) + 0 #+ PRand([0,0,2])

c1 >> crunch(
    dur = 0.25,
    amp = 1, # PWhite(0,0.5)
    pan = PSine(),
)

d1 >> play(
    "x   x  x",
)

d2 >> play(
    "--[----]---[  --]",
    amp = PWhite(0,1),
    pan = [0.5],
)

b1 >> bass(
    [ch,7,6,7],
    sus = 2,
    dur = [1.5, 1.25, 0.75, 0.5],
    amp = 0.5,
)

p1 >> pads(
    [3,2,0],
    sus = 4,
    oct = 6,
    dur = [0.5] * 4 + [0.25] * 6,
    amp = PWhite(0.2, 0.5),
    pan = var([-1,1],4),
)

e1 >> bell(
    ch,
    oct = 5,
).offbeat() + [0,(7,9),0,(7,10)]

u1 >> pluck(
    dur = 0.25,
    sus = 4,
).follow(p1) + [0,2]

u1 >> pluck(
    dur = 0.25,
    sus = 4,
    scale = Scale.majorPentatonic,
).solo()

u1 >> pluck(
    PWalk(16,4),
    dur = 0.25,
    sus = 4,
    scale = Scale.majorPentatonic,
)

u1 >> pluck(
    PWalk(16,4),
    dur = 0.25,
    sus = 4,
    scale = Scale.majorPentatonic,
    pan = PWhite(-1,1),
)

d3 >> play(
    "  o " * 3 + "  o[oo]",
)

r1 >> ambi(
    [0,2],
    dur = 16,
)

d4 >> play(
    "  * ",
    amp = 0.5,
)

ch.update([0,3,3.5,4])
