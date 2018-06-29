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

use_debug false
bizet_bass = (ring, :d, :r, :r, :a, :f5, :r, :a, :r)
#bizet_bass = (ring :d, :r, :r, :Bb, :g5, :r, :Bb, :r)

live_loop :clock do
  sleep 1
end

with_fx :reverb, room: 1, mix: 0.3 do
  live_loop :bizet do
    with_fx :slicer, phase: 0.125 do
      synth :blade, note: :d4, release: 8, cutoff: 100, amp: 1.5
    end
    
    16.times do
      tick
      play bizet_bass.look, release: 0.1
      play bizet_bass.look - 12, release: 0.3
      sleep 0.125
    end
  end
end

live_loop :ind do
  # sync "/live_loop/clock"
  sample :loop_industrial, beat_stretch: 1, cutoff: 100, rate: 1
  sleep 1
end

live_loop :drums do
  sample :bd_haus, cutoff: 110
  synth :beep, note: 49, attack: 0, release: 0.1
  sleep 0.5
end





















