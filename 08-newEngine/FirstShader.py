import numpy as np
from glapp.PyOGLApp import *
from glapp.Utils import *

vertex_shader = r'''
#version 330 core

void main()
{
    gl_Position = vec4(0, 0, 0, 1)
}
'''

fragment_shader = r'''
version 330 core
out vec4 frag_color
void main()
{
    frag_color = vec4(0, 1, 0, 1)
}
'''
