#version 330 core

layout (location = 0) in vec3 in_position;

uniform mat4 m_model;
uniform mat4 m_view;
uniform mat4 m_proj;
uniform vec3 color;

out vec3 frag_color;

void main() {
    frag_color = color;
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}
