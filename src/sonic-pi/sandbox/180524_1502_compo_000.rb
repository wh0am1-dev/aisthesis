# jammin around
# - by wh0am1 -

live_loop :foo do
  sample :loop_garzul
  use_synth :prophet
  play chord(:e3, '+5'), release: 8, cutoff: rrand(70, 130)
  sleep 8
end

live_loop :bar do
  
  sleep 1
end
