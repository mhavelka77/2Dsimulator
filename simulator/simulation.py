import numpy as np
import time

import constants
import physics
from display import Display

class Simulation:
    def __init__(self, time_constant, terminal):
        self.bodies = []
        self.time_constant = time_constant
        self.display = Display(terminal, time_constant) 

    def add_body(self, mass, position, velocity=(0,0)):
        self.bodies.append(physics.Body(mass, position, velocity))

    # TODO: optimize this
    def update(self):
        # update positions and velocities
        for i in range(len(self.bodies)):
            self.bodies[i].position += self.time_constant * self.bodies[i].velocity
            self.bodies[i].velocity += self.time_constant * self.bodies[i].acceleration 

        # update accelerations
        for i in range(len(self.bodies)):
            acceleration = physics.Vector((0,0))
            for n in range(len(self.bodies)):
                acceleration += physics.force_between_bodies(self.bodies[i], self.bodies[n])  
            acceleration /= self.bodies[i].mass
            self.bodies[i].acceleration = acceleration

    def draw(self):
        canvas = np.zeros((constants.CANVAS_SIZE, constants.CANVAS_SIZE), dtype=bool)
        xmax = canvas.shape[0]//2 
        ymax = canvas.shape[1]//2 

        if (constants.AXIS):
            canvas[xmax] = 1 
            canvas[:,ymax] = 1 

        for body in self.bodies:        
            if abs(round(body.position.x)) < xmax and abs(round(body.position.y)) < ymax:
               canvas[-round(body.position.y) + ymax][round(body.position.x) + xmax] = 1
        
        self.display.render(canvas)

    def run(self):
        iteration = 0
        oldtime = time.time()
        while True:
            if (time.time() - oldtime) > self.time_constant:
                print(f"iteration number: {iteration}")
                iteration += 1
                oldtime = time.time()
                self.update()
                self.draw()
     
