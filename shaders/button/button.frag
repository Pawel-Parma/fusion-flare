#version 330 core

layout (location = 0) out vec4 fragColor;

in vec3 frag_color;

void main() {
    fragColor = vec4(frag_color, 1.0);
}
