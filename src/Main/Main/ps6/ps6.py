import math
import random

from matplotlib import pylab

from ps6 import ps6_visualize


class Position(object):
    def __init__(self, x, y):
        self.x, self.y = x,y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getnewposition(self, angle, speed, pos):
        """
        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getx(), self.gety()
        # Compute the change in position
        delta_y = speed * math.sin(angle)
        delta_x = speed * math.cos(angle)
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def get_randomposition(self, Room):
        if type(Room) == RectangularRoom:
            return Position(random.randint(0, Room.getWidth),random.randint(0, Room.getHeight))
        else:
            raise TypeError

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        self.cleaned_tiles = []
        self.w = width
        self.h = height
        self.origin = Position(random.randint*self.h,random.randint*self.w)

    def getWidth(self):
        return self.w
    def setWidth(self, x):
        self.w = x

    def getHeight(self):
        return self.h
    def setHeight(self, x):
        self.h = x

    def cleanTileAtPosition(self, pos):
        if type(pos.getx,pos.gety) == int:
            self.cleanedtiles = self.cleanedtiles.append(pos)
        else:
            self.cleanedtiles = self.cleaned_tiles.append((Position(int(pos.getx), (int(pos.gety)))))


    def isTileCleaned(self, pos):
        pos1 = Position(int(pos.getx),int(pos.gety))
        if self.cleanedtiles.__contains__(pos1):
            return True
        else:
            return False

    def getNumTiles(self):
       return self.w*self.h

    def getNumCleanedTiles(self):
        return self.cleanedtiles.__sizeof__()

    def getRandomPosition(self):
        a = self.getHeight()
        b = self.getWidth()
        rx = random.randint(0, a)
        ry = random.randint(0, b)
        return Position(rx,ry)

    def isPositionInRoom(self, pos):
        for i in range(self.getWidth()):
            for j in range(self.getHeight()):
                if pos == Position(i,j):
                    return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        self.room = room
        self.position = Position.getRandomPosition(self, self.room)
        self.angle = random.randint(0, 360)
        self.speed = 1

        """"
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """

    def getRobotPosition(self):
        return self.position

    def setRobotPosition(self, position):
        self.position = position

    def getRobotDirection(self):
        return self.angle

    def setRobotDirection(self, direction):
        self.angle = direction

    def updatePositionAndClean(self):
        self.position = self.position.getNewPosition(self, self.getRobotDirection(), self.speed)
        self.room.cleanTileAtPosition(self.position)

# === Problem 2

# === Problem 2
class StandardRobot(Robot):

    def updatePositionAndClean(self):
        candidatePosition = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(candidatePosition):
            self.setRobotPosition(candidatePosition)
            self.room.cleanTileAtPosition(self.position)
        else:
            self.direction = random.randrange(360)


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    visualize = False
    total_time_steps = 0.0
    for trial in range(num_trials):
        if visualize:
            anim = ps6_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        robotCollection = []
        for i in range(num_robots):
            robotCollection.append(robot_type(room, speed))
        if visualize:
            anim.update(room, robotCollection)
        while (room.getNumCleanedTiles()/float(room.getNumTiles())) < min_coverage:
            for robot in robotCollection:
                robot.updatePositionAndClean()
            total_time_steps += 1
            if visualize:
                anim.update(room, robotCollection)
        if visualize:
            anim.done()
    return total_time_steps / num_trials


class RandomWalkRobot(Robot):

    def updatePositionAndClean(self):

        cur_pos = self.getRobotPosition()
        cur_dir = self.getRobotDirection()
        self.setRobotDirection(random.randrange(360))
        new_pos = cur_pos.getNewPosition(cur_dir, self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(new_pos)


def showPlot1(title, x_label, y_label):
    """
    Produces a plot comparing the two robot strategies in a 20x20 room with 80%
    minimum coverage.
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot2(title, x_label, y_label):
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


showPlot1('Time to clean 80% of a 20x20 room',' for various numbers of robots', 'Number of robots',)
showPlot2('Time to clean 80% of a 400-tile room for various room shapes','Aspect Ratio')
