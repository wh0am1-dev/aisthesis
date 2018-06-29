# Dror Ayalon - Live-coding
# https://www.youtube.com/watch?v=EI3OQKqsfNo

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

b1.reset() >> bass(
    0,
    dur = 4,
    pan = (-1, 1),
)

b1.amp = .7
b1.degree = [0, 9]
b1.degree = [(0, 9)]
b1.degree = [(0, 9), (0, 7), (3, 7), (0, 7)]

a1.reset() >> ambi(
    [0, 2, 4],
    dur = 1,
    amp = .75,    
)

a1.dur = [1, .5, .5]
a1.amp = [1, .75, .75]

g1.reset() >> growl(
    [0, 10],
    dur = .5,
    amp = .5,
)

###
g1.degree = [0, 10, 10, 100]
g1.amp = .6
###
g1.degree = [0, 10, 10, 200]

p1.reset() >> pads(
    0,
    dur = 0.5,
    amp = 1,
)

p1.degree = [0, 2]
p1.dur = 4
p1.degree = [0, 2, 4]
p1.degree = [0, 2, (4, 0)]

a1.stop()
p1.stop()
b1.stop()
g1.stop()

