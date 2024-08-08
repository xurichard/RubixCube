class RubixCube:

    class CubeFace:
        def __init__(self, color, name):
            # directions represent connections to different faces of the cube in the 
            # clockwise direction in the order of [N, E, S, W]
            self.directions = [None for x in range(4)] 
            self.face = [[color for x in range(3)] for y in range(3)]
            self.name = name

        def __repr__(self):
            return self.name

    def getClockwiseDirection(direction):
        return globalDirections[(globalDirections.index(direction) + 1) % 4]

    # Cube face examples
    #          U                         U
    #    L     F     R             R     B    L
    #          D                         D
    #
    # colors: Red, Yellow, Blue, Green, White, Orange

    def __init__(self):
        self.front = self.CubeFace("B", "front")
        self.back = self.CubeFace("G", "back")
        self.left = self.CubeFace("O", "left")
        self.right = self.CubeFace("R", "right")
        self.up = self.CubeFace("Y", "up")
        self.down = self.CubeFace("W", "down")

        self.front.directions = [self.up, self.right, self.down, self.left]
        self.back.directions = [self.up, self.left, self.down, self.right]
        self.left.directions = [self.up, self.front, self.down, self.back]
        self.right.directions = [self.up, self.back, self.down, self.front]
        self.up.directions = [self.front, self.left, self.back, self.right]
        self.down.directions = [self.front, self.right, self.back, self.left]


    def printCube(self):
        faces = {"front": self.front,
                 "back": self.back,
                 "left": self.left,
                 "right": self.right,
                 "up": self.up,
                 "down": self.down}
        print("--------------------------------------------")
        # print order:
        #       up  
        # left  front  right
        #       down
        #       back

        #orient the faces correctly
        upCopy = self.up.face.copy()
        for i in range((2 - self.up.directions.index(self.front)) % 4):
            upCopy = self.rotateMatrixClockwise(upCopy)

        print(" "*7 + "up")
        table = [' '.join([str(e) for e in row]) for row in upCopy]
        table = [" "*7 + line for line in table]
        print('\n'.join(table))
        print()


        leftCopy = self.left.face.copy()
        for i in range((1 - self.left.directions.index(self.front)) % 4):
            leftCopy = self.rotateMatrixClockwise(leftCopy)
        leftTable = [' '.join([str(e) for e in row]) for row in leftCopy]

        frontCopy = self.front.face.copy()
        for i in range(self.front.directions.index(self.up) % 4):
            frontCopy = self.rotateMatrixClockwise(frontCopy)
        frontTable = [' '.join([str(e) for e in row]) for row in frontCopy]

        rightCopy = self.right.face.copy()
        for i in range((3 - self.right.directions.index(self.front)) % 4):
            rightCopy = self.rotateMatrixClockwise(rightCopy)
        rightTable = [' '.join([str(e) for e in row]) for row in rightCopy]

        print("left   " + "front  " + "right")
        table = [l + "  " + f + "  " + r for l, f, r in zip(leftTable, frontTable, rightTable)]
        print('\n'.join(table))
        print()


        downCopy = self.down.face.copy()
        for i in range(self.down.directions.index(self.front) % 4):
            downCopy = self.rotateMatrixClockwise(downCopy)
        print(" "*7 + "down")
        table = [' '.join([str(e) for e in row]) for row in downCopy]
        table = [" "*7 + line for line in table]
        print('\n'.join(table))
        print()


        backCopy = self.back.face.copy()
        for i in range(self.back.directions.index(self.down) % 4):
            backCopy = self.rotateMatrixClockwise(backCopy)
        print(" "*7 + "back")
        table = [' '.join([str(e) for e in row]) for row in backCopy]
        table = [" "*7 + line for line in table]
        print('\n'.join(table))
        print()

    # one liner for rotating nxn matrix clockwise
    def rotateMatrixClockwise(self, matrix):
        return [i for i in zip(*matrix[::-1])]


    # given a cubeFace, rotate the face clockwise as well as all surrounding cubeFaces
    def rotateFaceClockwise(self, face):
        rotatedValues = []
        for sideFace in face.directions:
            #find which direction we are
            sideDirection = sideFace.directions.index(face)
            # signifies from the top of the matrix which side we want.
            storedValues = []
            if sideDirection == 0:
                storedValues = [i for i in sideFace.face[0]]
            elif sideDirection == 1:
                storedValues = [i[2] for i in sideFace.face]
            elif sideDirection == 2:
                storedValues = [i for i in sideFace.face[3]]
            elif sideDirection == 3:
                storedValues = [i[0] for i in sideFace.face[::-1]]
            print(storedValues)

            if rotatedValues:
                print(sideDirection)
                print(sideFace)
                if sideDirection == 0:
                    sideFace.face[0] = rotatedValues
                elif sideDirection == 1:
                    for i in range(3):
                        sideFace.face[i][2] = rotatedValues[i]
                elif sideDirection == 2:
                    sideFace.face[3] = rotatedValues
                elif sideDirection == 3:
                    for i in range(3):
                        sideFace.face[i][0] = rotatedValues[i]

            rotatedValues = storedValues

        # add the values back to the face we started at
        sideFace = face.directions[0]
        sideDirection = sideFace.directions.index(face)
        if sideDirection == 0:
            sideFace.face[0] = rotatedValues
        elif sideDirection == 1:
            for i in range(3):
                sideFace.face[i][2] = rotatedValues[i]
        elif sideDirection == 2:
            sideFace.face[3] = rotatedValues
        elif sideDirection == 3:
            for i in range(3):
                sideFace.face[i][0] = rotatedValues[i]

        # rotate the diections one space to align with new faces
        temp = face.directions[-1]
        face.directions = face.directions[:-1]
        face.directions.insert(0, temp)


    # given a cubeFace, rotate the face counter-clockwise as well as all surrounding cubeFaces
    def rotateFaceCounterclockwise(self, face):
        rotatedValues = []
        for sideFace in face.directions[::-1]:
            #find which direction we are
            sideDirection = sideFace.directions.index(face)
            # signifies from the top of the matrix which side we want.
            storedValues = []
            if sideDirection == 0:
                storedValues = [i for i in sideFace.face[0]]
            elif sideDirection == 1:
                storedValues = [i[2] for i in sideFace.face]
            elif sideDirection == 2:
                storedValues = [i for i in sideFace.face[3]]
            elif sideDirection == 3:
                storedValues = [i[0] for i in sideFace.face]

            if rotatedValues:
                if sideDirection == 0:
                    sideFace.face[0] = rotatedValues
                elif sideDirection == 1:
                    for i in range(3):
                        sideFace.face[i][2] = rotatedValues[i]
                elif sideDirection == 2:
                    sideFace.face[3] = rotatedValues
                elif sideDirection == 3:
                    for i in range(3):
                        sideFace.face[i][0] = rotatedValues[i]

            rotatedValues = storedValues

        # add the values back to the face we started at
        sideFace = face.directions[-1]
        sideDirection = sideFace.directions.index(face)
        if sideDirection == 0:
            sideFace.face[0] = rotatedValues
        elif sideDirection == 1:
            for i in range(3):
                sideFace.face[i][2] = rotatedValues[i]
        elif sideDirection == 2:
            sideFace.face[3] = rotatedValues
        elif sideDirection == 3:
            for i in range(3):
                sideFace.face[i][0] = rotatedValues[i]

        # rotate the diections one space to align with new faces
        temp = face.directions[0]
        face.directions = face.directions[1:]
        face.directions.append(temp)



if __name__ == '__main__':
    cube = RubixCube()
    cube.printCube()
    # cube.rotateFaceClockwise(cube.front)
    cube.rotateFaceClockwise(cube.up)
    cube.printCube()
    cube.rotateFaceClockwise(cube.front)
    cube.printCube()



















        # a systematic way to setup the box would be to create the front and left and right
        # faces then add a top face and connect the edges together. Then rotate the cube
        # so that the top becomes the front and continue. This seemed more complicated than
        # efficient so I'll hardcode the faces

        # front = CubeFace()
        # # setup the front and right and left of the cube 
        # right = CubeFace()
        # front.directions[0] = right
        # right.directions[0] = front
        # left = CubeFace()
        # front.directions[2] = left
        # left.directions[0] = front

        # # fold in the box 
        # primaryFace = front
        # leftToFrontDirectionIndex = 0
        # rightToFrontDirectionIndex = 0

        # # check left top for a node, if it doesn't exist, we have to make one
        # while(left.directions[(leftToFrontDirectionIndex - 1)%4] == None):
        #     leftToFrontDirectionIndex = (leftToFrontDirectionIndex - 1)%4
        #     rightToFrontDirectionIndex = (rightToFrontDirectionIndex + 1)%4

        #     newFace = CubeFace()
        #     newFace.directions[0] = left
        #     newFace.directions[3] = primaryFace
        #     newFace.directions[2] = right

        #     left.directions[leftToFrontDirectionIndex] = newFace
        #     right.directions[rightToFrontDirectionIndex] = newFace
        # if it does exist we have to glue the edge 












