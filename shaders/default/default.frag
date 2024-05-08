#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light {
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;
uniform vec4 shift_color;


vec3 getLight(vec3 color) {
    vec3 Normal = normalize(normal);

    // ambient light
    vec3 ambient = light.ambient;

    // diffuse light
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(Normal, lightDir));
    vec3 diffuse = diff * light.diffuse;

    // specular light
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(0, dot(viewDir, reflectDir)), 32);
    vec3 specular = spec * light.specular;


    return color * (ambient + diffuse + specular);
}

void main() {
    float gamma = 2.2;
    vec4 color_rgba = texture(u_texture_0, uv_0);
    vec3 color = color_rgba.rgb;

    // gamma correction pt. 1
    color = pow(color, vec3(gamma));

    color = getLight(color);

    // gamma correction pt. 2
    color = pow(color, vec3(1.0 / gamma));

    fragColor = vec4(color, color_rgba.a) * shift_color;
}
