def cornerFind(arr):
	leftMost = arr[0]
	corners = []
	closed = []
	fringe = Stack()
	fringe.push((leftMost,None))
	while fringe not Empty:
		current = fringe.pop()
		currentNode = current[0]
		if currentNode not in closed:
			if current[1] == None:
				closed.append(currentNode)
				corners.append(currentNode)
				nodeNeighbors = neighbors(currentNode)
				for neighbor in nodeNeighbors:
					if neighbor not in closed and neighbor in arr:
						fringe.push(neighbor)
			else:
				dir = current[1]
				nextNode = (currentNode[0]+dir[0], currentNode[1]+dir[1])
				if nextNode not in arr:
					fringe.push((currentNode,None))
				else:
					closed.append(currentNode)
		return corners

def neighbor(node):
	radius = 5
	neighbors = []
	for i in range(-radius,radius+1):
		for j in range(-radius,radius+1):
			neighbors.append((i,j))
	neighbors.sort(key=lambda x:x[0]**2+x[1]**2)
	
	neighbors = neighbors[1:]
	for i in range(neighbors):
		neighbors[i] = ((neighbors[i][0]+node[0], neighbors[i][1]+node[1]),neighbor[i])
	return neighbors