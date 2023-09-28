import pygame
import math





class Envir:
    def __init__(self,dimentions):
        self.black = (0,0,0)

        self.height = dimentions[0]
        self.width = dimentions[1]

        pygame.display.set_caption("Differential drive robot")
        self.map = pygame.display.set_mode((self.width,self.height))

        self.font = pygame.font.Font('freesansbold.ttf',20)
        self.text = self.font.render('default',True,(255,255,255),self.black)
        self.textRect = self.text.get_rect()
        self.textRect.center = (dimentions[1]-600,dimentions[0]-100)
        self.trail_set = []

    def write_info(self,vl,vr,theta):
        txt = f"Vl = {vl} Vr = {vr} Thehta = {int(math.degrees(theta))}"
        self.text=self.font.render(txt,True,(255,255,255),self.black)
        self.map.blit(self.text,self.textRect)

    def trail(self,pos):
        for i in range(0,len(self.trail_set)-1):

            pygame.draw.line(self.map,(255,255,255),(int(self.trail_set[i][0]),int(self.trail_set[i][1])),
                             (int(self.trail_set[i+1][0]),int(self.trail_set[i+1][1])))
        if self.trail_set.__sizeof__() > 30000:
            self.trail_set.pop(0)
        self.trail_set.append(pos)


    def robot_frame(self,pos, rotation):
        n = 80

        centerx,centery = pos
        x_axis = (centerx + n * math.cos(-rotation),centery + n*math.sin(-rotation))
        y_axis = (centerx + n * math.cos(-rotation+math.pi/2),
                  centery + n*math.sin(-rotation+math.pi/2))
        pygame.draw.line(self.map,(255,0,0),(centerx,centery),x_axis,3)
        pygame.draw.line(self.map,(0,255,0),(centerx,centery),y_axis,3)

