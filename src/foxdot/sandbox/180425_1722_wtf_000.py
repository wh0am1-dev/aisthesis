Scale.default = Scale.egyptian
Root.default = 0

p1 >> play(
    P["x--(-[--])o--o(-=)-"].layer("mirror"),
    # P["x--(-[--])o--x(-=)-"].layer("mirror"),
    # P["x--(-[--])x--o(-=)-"].layer("mirror"),
    sample = 2,
    dur = PDur(5, 8),
    rate = var([1,2,1,2,1,4],[3,1,3,2,3,4])
)
