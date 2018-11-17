precision mediump float;
uniform float time; // The elapsed time since VEDA has started.
uniform vec2 resolution; // The resolution of the screen.
// uniform vec2 mouse; // Current position of mouse. vec2(0) to vec2(1)
// uniform sampler2D backbuffer; // Rendered result of last frame. RGBA format
// uniform sampler2D samples; // Samples of the audio input.
// uniform sampler2D spectrum; // FFT result of the audio input.
// uniform float volume; // The volume of the audio input.
// uniform sampler2D midi; // Last MIDI event for each channel of MIDI devices. x: 3rd byte of the event
// uniform sampler2D note; // States of note numbers of MIDI devices. x: the volume of the note

// float sound() {
//   return texture2D(spectrum, vec2(.1)).x;
// }

void main() {
  vec2 uv = gl_FragCoord.xy / resolution.xy;
  gl_FragColor = vec4(uv, 0.5 + 0.5 * sin(time), 1.0);
}
