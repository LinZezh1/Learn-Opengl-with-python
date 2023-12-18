import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL )
pygame.display.set_caption('OpenGL in Python')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

done = False
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")

# init_ortho函数 定义正交投影矩阵
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)


done = False
init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 清除颜色和深度缓冲区
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)  # 设置模型矩阵为单位矩阵
    glLoadIdentity()
    glPointSize(20)

    # 设置点出现的位置
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glVertex2i(400,300)
    glVertex2i(400, 50)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
