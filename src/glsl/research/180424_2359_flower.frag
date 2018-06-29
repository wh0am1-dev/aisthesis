// Based on
//https://www.shadertoy.com/view/lsScDd

precision mediump float;

uniform float time;
uniform vec2 resolution;

const float PI = 3.141592653589793;
const float PI2 = PI * 2.;

void main( ) {
  vec2 uv = (gl_FragCoord.xy * 2.0 - resolution) / min(resolution.x, resolution.y);
  uv *= 2.0;
  float pic = cos(-1.);
  float interval = 0.5;
  float base = .4;
  float xhz = base;
  float yhz = base * pow(pow(2., 1./17.), interval); // 3./2.
  float zhz = base * 4./2.;

  // cartesian to polar coordinates
  float r = length(uv);
  float a = atan(uv.y, uv.x);
  // Repeat side acoriding to angle
  float sides = 6.;
  float ma = mod(a, PI2/sides);
  ma = abs(ma - PI/sides);
  // polar to cartesian coordinates
  uv = r * vec2(cos(ma), sin(ma));
  uv -= cos(r/-ma*PI + time*pic);

  vec3 uv3 = vec3(uv, 0);
  vec3 color = vec3(0, 0, 0);
  for (int i = 0; i<15; i++) {
    float t = time - float(i)/base;
    vec3 signal = vec3(
          sin(t*pic * 2. * xhz),
          sin(t*pic * 2. * yhz),
          sin(t*pic * 2. * zhz));
    if (distance(signal.xy * 50., uv * 50.) < 6.) {
      float depth = signal.z;
      color = color + vec3(depth,
        (1. - abs(depth)),
        -depth) + 0.5;
    }
  }

  gl_FragColor = vec4(color, 1.0);
}
