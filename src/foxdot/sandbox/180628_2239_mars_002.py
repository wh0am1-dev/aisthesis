Scale.default = Scale.major
Root.default = 0
Clock.bpm = 120

Samples.addPath('C:/Users/wh0am1/software/livecoding/samples/')
dyel = 'danielyoureelewis/'

~l1 >> loop(
    dyel + 'vocal/lordchristhavemercy',
    dur = 16,
    rate = .5,
).spread()

~l2 >> loop(
    dyel + 'vocal/onehundredpercent',
    dur = 64,
)

~l3 >> loop(
    dyel + 'vocal/sinnedagainst',
    dur = 32,
    amp = [0, 1]
)

~l4 >> loop(
    dyel + 'vocal/c1',
    dur = 16,
    room = .25,
    mix = .5,
)

~l5 >> loop(
    dyel + 'vocal/c2',
    dur = 8,
    amp = .25,
)

~p1 >> play(
    '|V2|  ( ([tt][mmm]))',
    dur = 1,
)

~p2 >> play(
    'y',
    dur = var([1, .5, .25, .125], [32, 24, 4, 4]),
    hpf = 10000,
    amp = .4,
)

