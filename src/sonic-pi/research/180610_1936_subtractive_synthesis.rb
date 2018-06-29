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

define :subt_synth do |note, sus|
  at do
    with_fx :lpf, cutoff: 40, amp: 2 do |fx|
      control fx, cutoff_slide: 6, cutoff: 100
      synth :prophet, note: note, sustain: sus
    end
    
    with_fx :hpf, cutoff_slide: 0.01 do |fx|
      synth :dsaw, note: note + 12, sustain: sus
      
      (sus * 8).times do
        control fx, cutoff: rrand(70, 110)
        sleep 0.125
      end
    end
  end
end

subt_synth :e1, 8
sleep 8
subt_synth :e1 - 4, 8
