import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, OPENGL | DOUBLEBUF | pygame.RESIZABLE)

# Set up the camera perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)  # Move camera back

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)       # Red
    glVertex3f(0, 1, 0)      # Top
    glColor3f(0, 1, 0)       # Green
    glVertex3f(-1, -1, 0)    # Bottom-left
    glColor3f(0, 0, 1)       # Blue
    glVertex3f(1, -1, 0)     # Bottom-right
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 1, 1, 1)   # Rotate 1 degree per frame around Y axis

    draw_triangle()

    pygame.display.flip()
    pygame.time.wait(10)

    glEnable(GL_DEPTH_TEST)
