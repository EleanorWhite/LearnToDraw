import edgeDetection

def cornerFind(arr):
    leftMost = arr[0]
    corners = []
    closed = []
    fringe = []
    fringe.append((leftMost,None))
    while not len(fringe) == 0:
        current = fringe.pop()
        print("current:", current)
        print("fringe", fringe)
        currentNode = current[0]
        # if we haven't seen this pixel yet
        if currentNode not in closed:
            # corner search
            if current[1] == None:
                closed.append(currentNode)
                corners.append(currentNode)
                nodeNeighbors = neighbors(currentNode)
                #print("Node neighbors", nodeNeighbors)

                leftNeighbor = None
                rightNeighbor = None
                for neighbor in nodeNeighbors:
                    #print("neighbor", neighbor)

                    if neighbor[0] not in closed and neighbor[0] in arr:
                        if leftNeighbor == None:
                            leftNeighbor = neighbor[0]
                            rightNeighbor = neighbor[0]
                        else:
                            rightNeighbor = neighbor[0]
                    elif leftNeighbor != None and neighbor[0] not in closed:
                        centerNeighbor = ((leftNeighbor[0]+rightNeighbor[0])/2, (leftNeighbor[1]+rightNeighbor[1])/2)
                        direction = (centerNeighbor[0]-currentNode[0], centerNeighbor[1]-currentNode[1])
                        fringe.append((centerNeighbor, direction))
                        leftNeighbor = None
                        rightNeighbor = None
            # line sarc    h 
            else:
                direct = current[1]
                nextNode = (currentNode[0]+direct[0], currentNode[1]+direct[1])
                # if the line stops, redo with corner search
                if nextNode not in arr:
                    fringe.append((currentNode,None))
                else:
                    closed.append(currentNode)
                    fringe.append((nextNode, direct))
        #print("corners", corners)
        #print("fringe", fringe)
    return corners

def neighbors(node):
    """ This takes in a node, and returns a sampling of the nodes
    15 pixels away from it"""
    
    radius = 5
    neighbors = []

    #neighbors.append((radius,radius))
    #neighbors.append((radius,0))
    #neighbors.append((radius,-radius))
    #neighbors.append((0, radius,))
    #neighbors.append((0, -radius))
    #neighbors.append((-radius, radius))
    #neighbors.append((-radius,0))
    #neighbors.append((-radius,-radius))
    for i in range(-radius, radius+1):
        neighbors.append((-radius, i))
    for i in range(-radius, radius+1):
        neighbors.append((i, radius))
    for i in range(radius-1, -radius, -1):
        neighbors.append((radius, i))
    for i in range(radius-1, -radius,-1):
        neighbors.append((i, -radius))

    for i in range(len(neighbors)):
        neighbors[i] = ((neighbors[i][0]+node[0], neighbors[i][1]+node[1]),neighbors[i])

    return neighbors


'''
def neighbors(node):
    """ TODO: write"""
    radius = 5
    neighbors = []
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            neighbors.append((i,j))
    neighbors.sort(key=lambda x:x[0]**2+x[1]**2)
    
    neighbors = neighbors[1:]
    for i in range(len(neighbors)):
        neighbors[i] = ((neighbors[i][0]+node[0], neighbors[i][1]+node[1]),neighbors[i])
    return neighbors
'''


def conSort(img):
    tooFar = 1000
    tolerance = 10
    path = []
    path.append(img[0])
    img = img[1:]
    backtrack = -2
    while img != []:
        closestDist = float("inf")
        bestPix = None
        currPixel = path[-1]
        for pix in img:
            dist = (currPixel[0]-pix[0])**2 + (currPixel[1]-pix[1])**2
            if dist < closestDist + tolerance:
                bestPix = pix
                closestDist = dist
            elif (dist - closestDist) < tolerance and len(path) > 1:
                prevPix = path[-2]
                direct = (currPixel[0]-prevPix[0],currPixel[1]-prevPix[1])
                bestPixDirect = (bestPix[0]-currPixel[0], bestPix[1]-currPixel[1])
                otherDirect = (pix[0]-currPixel[0], pix[1]-currPixel[1])
                
                bestPixDist = (direct[0]-bestPixDirect[0])**2 + (direct[1]-bestPixDirect[1])**2
                otherDist = (direct[0]-otherDirect[0])**2 + (direct[1]-otherDirect[1])**2

                if bestPixDist > otherDist:
                    bestPix = pix

        if closestDist > tooFar:
            #return path
            # backtrack
            if len(path) < -backtrack: #check for off by one error
                return path
            path.append(path[backtrack])
            backtrack -= 2
        else:
            backtrack = -2
            path.append(bestPix)
            img.remove(bestPix)
        
    return path


def useImage(filename):
    img = edgeDetection.getImageArray(filename)
    #print(img)
    
    newImg = conSort(img)
    maxDist = 0
    biggestJump = 0
    prev = newImg[0]
    for i in newImg[1:]:
        dist = (prev[0]-i[0])**2 + (prev[1]-i[1])**2
        prev = i
        if dist > maxDist:
            maxDist = dist
            biggestJump = i
    #print(maxDist, biggestJump)

    return newImg

def ind0(arr):
    return arr[0]

def ind1(arr):
    return arr[1]

def main():
    path = useImage('ePicture.png')
    cutDown = 5
    p = [path[i] for i in range(len(path)) if i%cutDown == 0]
    x = [ind0(i) for i in p]
    y = [ind1(i) for i in p]
    print(x,y)
    #print(p)


if __name__ == "__main__": main()
