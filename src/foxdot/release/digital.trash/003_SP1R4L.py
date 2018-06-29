# wh0am1 - 003_SP1R4L

Scale.default = "chromatic"
Root.default = 2
Clock.bpm = 120

drp = [0, 7, 12, 17, 21, 26]
std = [0, 5, 10, 15, 19, 24]

# tri_kick    tabla    harp    ambient
# bassline    clap     pi      drums.amen
Clock.set_time(0)

timer  =  0 # 000 : ambient
Clock.future(timer, lambda: _ambient())
timer += 16 # 016 : ambient, tabla
Clock.future(timer, lambda: _tabla())
timer += 16 # 032 : ambient, tabla, harp
Clock.future(timer, lambda: _harp())
timer += 16 # 048 : ambient, tabla, harp, bassline
Clock.future(timer, lambda: _bassline())
timer += 16 # 064 : ambient, tabla, harp, bassline, tri_kick
Clock.future(timer, lambda: _tri_kick())
timer += 64 # 128 : tabla, harp, bassline
Clock.future(timer, lambda: Group(tabla, harp, bassline).only())
timer += 16 # 144 : harp, clap
Clock.future(timer, lambda: _clap())
Clock.future(timer, lambda: tabla.stop())
Clock.future(timer, lambda: bassline.stop())
timer += 16 # 160 : clap, pi
Clock.future(timer, lambda: _pi())
Clock.future(timer, lambda: harp.stop())
timer += 32 # 192 : clap, pi, drums
Clock.future(timer, lambda: _drums())
timer += 32 # 224 : clap, pi, drums.amen
Clock.future(timer, lambda: _drums_amen())
timer += 32 # 256 : clap, pi, drums, tabla, harp
Clock.future(timer, lambda: _drums())
Clock.future(timer, lambda: _tabla())
Clock.future(timer, lambda: _harp())
timer += 16 # 272 : clap, pi, tabla, harp
Clock.future(timer, lambda: drums.stop())
timer += 16 # 288 : clap, pi, harp
Clock.future(timer, lambda: tabla.stop())
timer += 16 # 304 : clap, pi
Clock.future(timer, lambda: harp.stop())
timer += 16 # 320 : pi
Clock.future(timer, lambda: clap.stop())
timer += 32 # 352 : ?
Clock.future(timer, lambda: pi.stop())

tri_kick = Player()
def _tri_kick(time=9999):
    print('tri_kick: ' + str(time))
    tri_kick >> play(
        '<Vs><  n >',
        sample = 2,
    ).every(
        5,
        'stutter',
        2,
        dur = 3,
    ).after(time, 'stop')
tabla = Player()
def _tabla(time=9999):
    print('tabla: ' + str(time))
    tabla >> play(
        '{  ppP[pP][Pp]}',
        sample = PRand(5),
        rate = PRand([.5, 1, 2]),
    ).after(time, 'stop')
harp = Player()
def _harp(time=9999):
    print('harp: ' + str(time))
    harp >> karp(
        oct = PRand([4, 5, 6]),
        dur = .25,
        hpf = linvar([1000, 2000], 16),
        hpr = linvar([.1, 1], 20)
    ).after(time, 'stop')
ambient = Player()
def _ambient(time=9999):
    print('ambient: ' + str(time))
    ambient >> ambi(
        P[0, 5, 3] + (0, 7, 12),
        dur = [8, 4, 4],
        oct = 4,
    ).after(time, 'stop')
bassline = Player()
def _bassline(time=9999):
    print('bassline: ' + str(time))
    bassline >> bass(
        var([0, 5, 3], [8, 4, 4]),
        dur = PDur(var([3, 5]), 8),
        delay = (0, .25),
    ).spread().every(
        3,
        'offadd',
        7,
    ).after(time, 'stop')
clap = Player()
def _clap(time=9999):
    print('clap: ' + str(time))
    clap >> play(
        P['  h '].layer('mirror'),
        shape = .5,
        chop = 4,
        rate = PRand([1, 2, 4]),
        slide = 1,
    ).after(time, 'stop')
pi = Player()
def _pi(time=9999):
    print('pi: ' + str(time))
    pi >> piano(
        P[0, 5, 3] + (0, 7, 12),
        dur = [8, 4, 4],
        oct = 4,
        delay = (0, .25, .75),
    ).after(time, 'stop')
drums = Player()
def _drums(time=9999):
    print('drums: ' + str(time))
    drums >> play(
        P['VnOn'],
        lpf = 800,
    )
def _drums_amen(time=9999):
    print('drums.amen: ' + str(time))
    drums >> play(
        P['VnOn'].amen(),
        lpf = 800,
    )

