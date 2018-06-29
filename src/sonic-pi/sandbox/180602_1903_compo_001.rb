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

use_bpm 120

def kick(i)
  tmps = [
    [1, 1, 1, 0.5, 0.5],
    [1, 1, 0.5, 0.5, 1],
    [1, 0.5, 0.5, 1, 1],
    [0.5, 1, 0.5, 1.5, 0.5]
  ]
  
  sample :bd_klub
  sleep tmps[i][0]
  sample :bd_klub
  sleep tmps[i][1]
  sample :bd_klub
  sleep tmps[i][2]
  sample :bd_klub
  sleep tmps[i][3]
  sample :bd_klub
  sleep tmps[i][4]
end

live_loop :kick do
  # with_fx :compressor, mix: 0 do
  with_fx :reverb do
    kick(0)
    kick(1)
    kick(2)
    kick(3)
  end
  # end
end

live_loop :kick_tek do
  sleep 2
  sample :bd_tek
  sleep 2
end

comment do
  live_loop :tri do
    sample :elec_fuzz_tom, amp: 0.125, release: 0.125
    sleep 0.5
    sample :elec_fuzz_tom, amp: 0.125, release: 0.125
    sleep 0.25
    sample :elec_fuzz_tom, amp: 0.125, release: 0.125
    sleep 0.25
  end
end

live_loop :clap do
  sleep 1
  sample :elec_hollow_kick
  sleep 1
end

live_loop :ambi do
  with_fx :echo, phase: 0.25, decay: 4 do
    sample :ambi_piano, rate: choose([0.25, 0.5, 1, 2, 4])
  end
  sleep 4
  sample :ambi_dark_woosh, rate: 0.5
  sleep 4
end

live_loop :tabla do
  with_fx :hpf, cutoff: 50 do
    sample "tabla", rrand_i(0, 24), amp: 2
  end
  sleep 1
end















