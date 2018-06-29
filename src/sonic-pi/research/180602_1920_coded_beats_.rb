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

use_bpm 100

live_loop :amen_break do
  p = [0.125, 0.25, 0.5].choose
  use_bpm 50
  with_fx :slicer, phase: p, wave: 0, mix: rrand(0.7, 1) do
    r = [1, 1, 1, -1].choose
    sample :loop_amen, beat_stretch: 2, rate: r, amp: 2
  end
  sleep 2
end

live_loop :bass_drum do
  sample :bd_haus, cutoff: 70, amp: 1.5
  sleep 0.5
end

live_loop :landing do
  bass_line = (knit :e1, 3, [:c1, :c2].choose, 1)
  with_fx :slicer, phase: [0.25, 0.5].choose, invert_wave: 1, wave: 0 do
    s = synth :square, note: bass_line.tick, sustain: 4, cutoff: 60
    control s, cutoff_slide: 4, cutoff: 120
  end
  sleep 4
end
