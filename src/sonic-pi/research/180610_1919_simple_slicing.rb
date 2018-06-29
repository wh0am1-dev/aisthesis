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

live_loop :sliced_amen do
  n = 8
  s = line(0, 1, steps: n).choose
  f = s + (1.0 / n)
  sample :loop_amen, beat_stretch: 2, start: s, finish: f
  sleep 2.0 / n
end

live_loop :acid_bass do
  with_fx :reverb, room: 1, reps: 32, amp: 0.6 do
    tick
    n = (octs :e0, 3).look - (knit 0, 3 * 8, -4, 3 * 8).look
    co = rrand(70, 110)
    synth :beep, note: n + 36, release: 0.1, wave: 0, cutoff: co
    synth :tb303, note: n, release: 0.2, wave: 0, cutoff: co
    sleep (ring 0.125, 0.25).look
  end
end
