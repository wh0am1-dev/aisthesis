Samples.addPath("C:\Users\wh0am1\software\livecoding\samples")

Clock.bpm = 120

l1 >> loop(
    "acid/acidloops/dist1echo",
    dur = 8,
    chop = 0,
    coarse = 16,
)

l2 >> loop(
    "acid/acidloops/dry1",
    dur = 8,
    lpf = 400,
    coarse = 4,
)

l3 >> loop(
    "acid/acidloops/italobass3",
    dur = 4,
    shape = PWhite(0, 0.5),
    pan = PWhite(-0.5, 0.5),
    chop = 128,
    rate = 1,
    coarse = 2,
)

l4 >> loop(
    "acid/acidloops/spaceecho",
    dur = 32,
)

l5 >> loop(
    "acid/acidloops/space2",
    dur = 8,
)

l6 >> loop(
    "acid/acidloops/sync5",
    dur = 8,
)

l7 >> loop(
    "acid/acidloops/vocallo",
    dur = 8,
    dist = 0.1,
    pan = PWhite(-1,1),
    delay = (0, 0.75),
).every(5, "stutter", 2)

l8 >> loop(
    "acid/acidloops/vocalhi",
    dur = PDur(5,8) * 4,
    rate = -1,
)

l9 >> loop(
    "acid/acidloops/vocalmid2",
    dur = PRand([4,6]),
    rate = PRand([2,4]),
)

s5 >> loop(
    "acid/acidsynths/Future Strings - TB303/TB-303_Big_Res_Loop-C1-3TU4",
    dur = PDur(5,8),
    rate = 1 + PRand(P[0,2,5,7,10] * 1/12),
    delay = (0, 0.5),
)

d1 >> loop(
    "acid/aciddrums/kick_acid",
    dur = 1,
).every(
    3,
    "stutter",
    n = 2,
    dur = 1,
)

d2 >> loop(
    "acid/aciddrums/clap_2_acid",
    dur = [rest(1),0.5,rest(0.5)],
)

d3 >> loop(
    "acid/aciddrums/shaker_acid",
    dur = 1/4,
    amp = PWhite(0.2,0.4),
    pan = PWhite(-1,1),
    rate = PWhite(),
)

d4 >> loop(
    choose(["acid/aciddrums/tom_lo_acid", "acid/aciddrums/tom_mid_acid"]),
    amp = PRand([0,0,0,0.25,0.5]),
    dur = 1/2,
    delay = (0,0.25),
)

