#!/usr/bin/env python

# panda3d testing

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.load_model()

        # use arrow keys but sticky
        # self.useDrive()

        # self.scene = self.loader.loadModel('models/environment')
        # self.scene.reparentTo(self.render)
        # self.scene.setScale(0.1, 0.1, 0.1)
        # self.scene.setPos(-8, 42, 0)

        ### self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    def load_model(self):
        # self.scene = self.loader.loadModel('models/environment')
        self.scene = self.loader.loadModel('./lamp.obj')
        self.scene.reparentTo(render)
        self.scene.setScale(2, 2, 2)
        self.scene.setPos(-8, 42, 0)

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

if __name__ == '__main__':
    app = MyApp()
    app.run()
