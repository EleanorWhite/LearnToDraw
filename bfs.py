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
        currentNode = current[0]
        # if we haven't seen this pixel yet
        if currentNode not in closed:
            # corner search
            if current[1] == None:
                closed.append(currentNode)
                corners.append(currentNode)
                nodeNeighbors = neighbors(currentNode)
                print("Node neighbors", nodeNeighbors)
                for neighbor in nodeNeighbors:
                    #print("neighbor", neighbor)

                    if neighbor[0] not in closed and neighbor[0] in arr:
                        fringe.append(neighbor)
            # line search 
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
    radius = 15
    neighbors = []

    neighbors.append((radius,radius))
    neighbors.append((radius,0))
    neighbors.append((radius,-radius))
    neighbors.append((0, radius,))
    neighbors.append((0, -radius))
    neighbors.append((-radius, radius))
    neighbors.append((-radius,0))
    neighbors.append((-radius,-radius))
    #for i in range(-radius, radius+1):
    #   neighbors.append((radius-1,i))
    #   neighbors.append((-1*radius+1, i))
    #   neighbors.append((i, radius-1))
    #   neighbors.append((i, -1*radius+1))
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

def useImage(filename):
    img = edgeDetection.getImageArray(filename)
    return cornerFind(img)

def main():
    print(useImage('rectangle.png'))

if __name__ == "__main__": main()
