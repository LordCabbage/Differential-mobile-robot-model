import pygame
import math






class Robot:
    def __init__(self,startpos,roboImg, width):
        self.m2p = 3779.52 #meters to pixels
        self.dt = 0
        self.w = width
        self.x = startpos[0]
        self.y = startpos[1]
        self.theta=0
        self.vl = 0.01 * self.m2p
        self.vr = 0.01 * self.m2p
        self.maxspeed = 0.02*self.m2p
        self.minspeed = -0.02*self.m2p

        self.img = pygame.image.load(roboImg)
        self.rotated = self.img
        self.rect = self.rotated.get_rect(center=(self.x,self.y))

    def draw(self, map):
        map.blit(self.rotated,self.rect)


    def move(self,event = None):
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.vl += 0.001*self.m2p
                elif event.key == pygame.K_2:
                    self.vl -= 0.001*self.m2p
                elif event.key == pygame.K_3:
                    self.vr += 0.001*self.m2p
                elif event.key == pygame.K_4:
                    self.vr -= 0.001*self.m2p
        self.x += ((self.vl+self.vr)/2)*math.cos(self.theta)*self.dt
        self.y -= ((self.vl+self.vr)/2)*math.sin(self.theta)*self.dt
        self.theta += (self.vr-self.vl)/self.w*self.dt
        if self.theta>2*math.pi or self.theta<-2*math.pi:
            self.theta = 0

        self.vr = min(self.vr,self.maxspeed)
        self.vl=min(self.vl,self.maxspeed)

        self.vr = max(self.vr,self.minspeed)
        self.vl=max(self.vl,self.minspeed)

        self.rotated = pygame.transform.rotozoom(self.img, math.degrees(self.theta),1)
        self.rect = self.rotated.get_rect(center = (self.x,self.y))
