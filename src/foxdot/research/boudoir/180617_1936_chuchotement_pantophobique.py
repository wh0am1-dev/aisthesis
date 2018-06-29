# boudoir - chuchotement pantophobique
# https://www.youtube.com/watch?v=KL2zW6Q5hWs
# https://gist.github.com/jf-parent/c8ea7e54e30593af01512f4e21b54670

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

b1.reset() >> glass(
    [0],
    dur = 16,
).after(16, 'stop')

def play1():
    print('play1')
    p1.reset() >> bass(
        [0, [0, 1, 2]],
        dur = 8,
        oct = 5,
        lpf = 600,
        room = 1,
        mix = 1,
    ).after(320, 'stop')

def play2():
    print('play2')
    p2.reset() >> soft(
        [0],
        formant = linvar([0, 1], 8),
        sus = 2,
        vib = linvar([0, 2], 4),
        oct = var([3, 4, 5], 4),
    ).every(
        16,
        'stutter'
    ).after(290, 'stop')

def play3():
    print('play3')
    p3.reset() >> sawbass(
        P[0, 2, 4, [5, 6, 7]],
        dur = [1, [1, 2], 2, [2, 4]],
        oct = [4, 5, 6, 6],
        vib = [0, 0, 0, [0, 1]],
        formant = var([0, 1], 8),
    ).after(48, 'stop')

Clock.set_time(0)

Clock.future(0, play1)
Clock.future(30, play2)
Clock.future(60, play3)
Clock.future(120, play3)
Clock.future(240, play3)
