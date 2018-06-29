/*{
  "audio": true,
  "pixelRatio": 6
}*/

#ifdef GL_ES
precision mediump float;
#endif

// glslsandbox uniforms
uniform float time;
uniform vec2 resolution;
uniform sampler2D spectrum;
uniform sampler2D samples;
uniform float volume;
uniform vec2 mouse;

// shadertoy globals
float iTime;
vec3  iResolution;

#define snd audio()

float audio() {
  return texture2D(spectrum, vec2(.1)).x;
}

// --------[ Original ShaderToy begins here ]---------- //
#define RAYMARCH_STEPS 30
#define EPS 0.001

float rand(vec2 n) {
  return fract(sin(dot(n, vec2(12.9898, 4.1414))) * 43758.5453);
}

float noise(vec2 p){
  vec2 ip = floor(p);
  vec2 u = fract(p);
  u = u*u*(3.0-2.0*u);

  float res = mix(
    mix(rand(ip),rand(ip+vec2(1.0,0.0)),u.x),
    mix(rand(ip+vec2(0.0,1.0)),rand(ip+vec2(1.0,1.0)),u.x),u.y);
  return res*res;
}


vec2 pMod2(inout vec2 p, float size){
  float halfsize = size*0.5;
  vec2 c = floor((p+halfsize)/size);
  p = mod(p+halfsize,size)-halfsize;
  return c*snd;
}

float sdSphere( vec3 p, float s ) {
  return length(p)-s *.1-snd*2.5;
}

float map(vec3 p){
    vec2 index = pMod2(p.xz, 5.);
    float valNoise = noise(index);
    p.y -= valNoise * 14.0;
    float pulse = (sin(iTime * length(index)) + 1.0) / 4.0;
  return sdSphere(p, valNoise + 0.2 + pulse);
}

float raymarch(vec3 ro, vec3 rd){
  float t = 0.0;
    for(int i = 0; i < RAYMARCH_STEPS; ++i){
        vec3 p = ro + rd * t;
      float d = map(p);

        if (d < EPS){
          break;
        }

        t += min(d, 2.5);
    }
    return t;
}

mat3 setCamera( in vec3 ro, in vec3 ta, in float cr ) {
  vec3 cw = normalize(ta-ro);
  vec3 cp = vec3(cos(cr), cos(cr),0.0);
  vec3 cu = normalize( cross(cw,cp) );
  vec3 cv = normalize( cross(cu,cw) );
    return mat3( cu, cv, cw );
}

void mainImage( out vec4 fragColor, in vec2 fragCoord ) {
    vec2 uv = fragCoord/iResolution.xy;
    uv = uv * 2.0 - 1.0;
    uv.x *= iResolution.x / iResolution.y;

    vec3 ro = vec3(12.0*cos(iTime / 3.0), 10.0,12.0*sin(iTime / 3.0) );
    vec3 ta = vec3(0.0,5.0, 0.0);

    mat3 cam = setCamera(ro, ta, 0.0);
    vec3 rd = cam * normalize(vec3(uv,2.0));

    float dist = raymarch(ro, rd);

    float fog = 2.0 / (1.0 + dist * dist * 0.001);

    vec2 asdf = fragCoord / iResolution.xy;
    float x = asdf.x;
    float y = asdf.y;
    float a = atan(y, x);

    fragColor = vec4(fog * vec3(
      snd / 1.,
      x,
      y-.25
    ),1.0);
}
// --------[ Original ShaderToy ends here ]---------- //

void main(void) {
    iTime = time;
    iResolution = vec3(resolution, 0.0);

    mainImage(gl_FragColor, gl_FragCoord.xy);
}
