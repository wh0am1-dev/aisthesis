# alt+r: run
# alt+return: run
# alt+s: stop

# alt+shift+o: load
# alt+shift+s: save

# alt+x|c|v: cut-copy-paste
# alt+a: select all
# alt+f: forward (?)
# alt+b: backwards (?)
# alt+backspace: delete word
# alt+d: delete until end of line

# ALT+U: UPPERCASE RIGHT
# alt+l: lowercase right
# alt+m: beautify
# alt++: font up
# alt+-: font down

# f9: show buttons
# f11: show log
# alt+i: docs panel
# alt+shift+f: fullscreen
# alt+p: settings

live_loop :random_riff do
  use_random_seed 10300
  use_synth :prophet
  s = [0.125, 0.25, 0.5].choose
  
  8.times do
    r = [0.125, 0.25, 1, 2].choose
    n = (scale :e3, :minor).choose
    co = rrand(30, 100)
    play n, release: r, cutoff: co
    sleep s
  end
end

live_loop :drums do
  use_random_seed 2001
  
  16.times do
    r = rrand(0.5, 10)
    sample :drum_bass_hard, rate: 4, amp: rand
    sleep 0.125
  end
end




















