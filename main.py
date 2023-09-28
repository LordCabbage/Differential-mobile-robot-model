
import pygame
import math
import Enviroment
import Robot



pygame.init()
start = (200,200)
dims = (800,1200)
running = True



if __name__ == '__main__':

    enviroment = Enviroment.Envir(dims)
    robot = Robot.Robot(start,"robot.png",0.02*3779.52)
    robot.dt = 0
    lasttime = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            robot.move(event)
        robot.dt = (pygame.time.get_ticks() - lasttime)/1000
        lasttime = pygame.time.get_ticks()
        pygame.display.update()
        enviroment.map.fill(enviroment.black)
        robot.move()
        enviroment.write_info(robot.vl,robot.vr,robot.theta)
        robot.draw(enviroment.map)
        enviroment.robot_frame((robot.x,robot.y),robot.theta)
        enviroment.trail((robot.x,robot.y))


