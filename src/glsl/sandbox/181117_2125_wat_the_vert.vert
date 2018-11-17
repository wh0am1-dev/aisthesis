/*{
  "vertexCount": 300,
  "pixelRatio": 1,
}*/

#define sndx soundx()
#define sndy soundy()
#define sndz soundz()

precision mediump float;
attribute float vertexId;
uniform float vertexCount;
uniform float time;
uniform vec2 resolution;
uniform sampler2D samples;
uniform sampler2D spectrum;
uniform float volume;
varying vec4 v_color;

float soundx() {
	return texture2D(spectrum, vec2(.1)).x;
}

float soundy() {
	return texture2D(spectrum, vec2(.1)).y;
}

float soundz() {
	return texture2D(spectrum, vec2(.1)).z;
}

void main() {
  float i = vertexId + time * .25;

  vec3 pos = vec3( // * 2^x
    cos(i * 4.0 * sndy),
    sin(i * 4.0 * sndy),
    cos(i * 1.0)
  );

  gl_Position = vec4(pos.x, pos.y, pos.z, 1);
  v_color = vec4(
    cos(time)*.5+.5,
    cos(time)*.5+.5,
    fract(vertexId / 3.),
    1.0
  );
}
