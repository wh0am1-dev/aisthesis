Scale.default = "chromatic"
Root.default = 2
Clock.bpm = 110

d1 >> play(
  degree = "V (- )( [--])O (-#) ",
)

d2 >> play(
  degree = "<Vs><  n >"
).every(
  3,
  "stutter",
  2,
  dur = 1,
)

d3 >> play(
  degree = "funky",
     dur = 0.5,
    rate = PRand([0.25, 0.5, 1]),
)

a1 >> ambi(
  degree = P[0, 5, 3] + (0, 12),
     dur =  [8, 4, 4],
     oct = 4,
)

a2 >> prophet(
  degree = a1.degree,
).every(
    16,
    "offadd",
    7,
)

n1 >> nylon(
  degree = a1.degree[0],
     dur = 0.25,
     oct = PRand([5,6]),
     hpf = linvar([1000, 2000], 20),
     hpr = linvar([0.1, 1], 12),
)

b1 >> bass(
  degree = a1.degree[0],
     dur = 4,
  coarse = 4,
     lpf = 200,
).spread().every(
  5,
  "offadd",
  7,
)

p1 >> piano(
  degree = a1.degree[0],
     dur = PDur(3, 8) * 2,
   shape = 0.5,
).every(
  4,
  "offadd",
  3,
)

