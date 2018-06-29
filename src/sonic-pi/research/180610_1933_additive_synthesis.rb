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

define :bell do |n|
  # triangle waves for the 'hit'
  synth :tri, note: n - 12, release: 0.1
  synth :tri, note: n + 0.1, release: 0.1
  synth :tri, note: n - 0.1, release: 0.1
  synth :tri, note: n, release: 0.2
  
  # sine waves for the 'ringing'
  synth :sine, note: n + 24, release: 2
  synth :sine, note: n + 24.1, release: 2
  synth :sine, note: n + 24.2, release: 0.5
  synth :sine, note: n + 11.8, release: 2
  synth :sine, note: n, release: 2
  
  # low sine waves for the bass
  synth :sine, note: n - 11.8, release: 2
  synth :sine, note: n - 12, release: 2
end

bell :e3
sleep 1
bell :c2
sleep 1
bell :d3
sleep 1
bell :g2
