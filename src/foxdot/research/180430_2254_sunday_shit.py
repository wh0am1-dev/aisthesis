"""
  Mauro Di Giovanni - Sunday shit:
  https://www.youtube.com/watch?v=bf_fO34QOAw

  How to:
  - Run the statements line by line (alt+enter),
    go to the next one whenever you feel like
  - The "#### > run block <" blocks should be
    executed together (ctrl+enter)
  - If you want to fast-forward through the song,
    just execute the blocks together (ctrl+enter)
    from the beginning, so you don't have to go
    through every variation of each instrument
  - Enjoy ! :+1:
"""

Scale.default = Scale.major
Root.default = 0
Clock.bpm = 140

t1 >> pads([0,0,0],verb=0,room=0,hpf=linvar([80,1000],16),)

t2 >> bass([0,0,0],scale=Scale.minor,amp=linvar([0,0.8],16),lpf=linvar([80,1000],12),)
t2 >> bass([0,0,0],scale=Scale.minor,amp=0.8,)

t1 >> pads([0,1,2],scale=Scale.minor)

#### > run block <
t1 >> pads(verb=0.5,room=1,)
t2 >> bass(verb=0.5,room=1,)
#### > run block <

t2.stop()

#### > run block <
t1 >> pads(verb=0,room=0,)
t2 >> bass([0,0,0],scale=Scale.minor,amp=0.8,lpf=linvar([80,1000],12),)
p1 >> play("(x )(-[-x]-)")
p2 >> play("  ( H) ")
p3 >> play("m  m  m ")
#### > run block <

p2.solo(), p3.solo(), t2 >> bass(verb=0.5,room=1,)

#### > run block <
t1 >> pads(verb=0,room=0,)
t2 >> bass([0,0,0],scale=Scale.minor,amp=0.8,lpf=linvar([80,1000],12),)
p1 >> play("(x )(-[-x]-)")
p2 >> play("  ( H) ")
p3 >> play("m  m  m ")
#### > run block <

p2.solo(), p3.solo(), t2 >> bass(verb=0.5,room=1,)

#### > run block <
t1 >> pads([0,0,0],verb=0,room=0,hpf=linvar([80,1000],12),)
t2 >> bass([0,0,0],scale=Scale.minor,amp=linvar([0,0.8],16),lpf=linvar([80,1000],12),)
#### > run block <

#### > run block <
t1 >> pads(verb=0,room=0,)
t2 >> bass([0,0,0],scale=Scale.minor,amp=0.8,lpf=linvar([80,1000],12),)
p1 >> play("(x )(-[-x]-)")
p2 >> play("  ( H) ")
p3 >> play("m  m  m ")
#### > run block <

p2.solo(), p3.solo(), t2 >> bass(verb=0.5,room=1,)

#### > run block <
t1 >> pads([0,0,0],verb=0,room=0,hpf=linvar([80,1000],12),)
t2 >> bass([0,0,0],scale=Scale.minor,amp=linvar([0,0.8],16),lpf=linvar([80,1000],12),)
#### > run block <

#### > run block <
t2 >> dub([0],dur=[0.5],scale=Scale.major,amp=[0,0.5],)
p1 >> play("x ",sample=2,)
p2 >> play("  ( H) ")
p3 >> play("--",sample=2,amp=0.5,hpf=linvar([1000,8000],1),)
p4 >> play("  o ",sample=7,)
#### > run block <

t2.stop()
p1.stop()
p2.stop()
p3.stop()
p4.stop()
Clock.clear()

