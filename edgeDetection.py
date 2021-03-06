import cv2


def getRedImage(filename):
    img = cv2.imread(filename)

    # get only the red for every pixel
    redImg = [[ind0(x) for x in y] for y in img]

    return redImg


def getImageArray(filename):
    """This takes in a png filename, and gives out an
    array that contains tuples with the coordinates of
    all 0 (black) pixels in the array (starting at the 
    upper left corner, prioritizing left)"""
    img = cv2.imread(filename)
     
    # get only the red for every pixel
    redImg = [[ind0(x) for x in y] for y in img]
    

    # get coordinates for zero pixels
    coords = []
    for i in range(0,len(redImg)):
        for j in range(0,len(redImg[i])):
            if redImg[i][j] == 0:
                coords.append((i,j))


    return coords


def ind0(arr):
    return arr[0]



def main():
    print(getRedImage("ePicture.png"))
    #print(getImageArray("rectangle.png"))


if __name__ == "__main__": main()
