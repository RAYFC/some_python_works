#Collaboration:Ruifeng Chen 1473869   Hao Liu 1475938
from kmeans_skeleton import *
import sys
from cImage import *
def dispalyImage(imagename):
  img=FileImage(imagename)
  width=img.getWidth()
  height=img.getHeight()
  win=ImageWin('photo',width,height)
  return (img,win)
  # This function opens the image whose name is imagename and
  # displays it in a window which is the same size as the image
  # It also returns the image object as well as the window object.
def readCommandLineArgs():
  imagename=sys.argv[1]
  numOfClusters=sys.argv[2]
  return(imagename,numOfClusters)
  # Process the command line arguments. These arguments are the name 
  # of the original image and the number of clusters (k). Consider 6
  # as the default value of k. The user will enter them after the name
  # of your program file in command line

def main():
  # IMPORTANT NOTE: The runtime of this program is proportional
  # to the size of the image we use as the input. So, it is OK
  # if your program takes a couple of minutes to run.

  # read and Process the command line arguments.
  (imageName, numOfClusters) = readCommandLineArgs()

  # Read in the original image and display it. Note that when you displayed 
  # the image in displayImage function, you should return the image object
  # as well as the window object you created in displayImage function.
  image, myImageWindow = dispalyImage(imageName)
  image.draw(myImageWindow)
  # Get width and height of the original image.
  width=image.getWidth()
  height=image.getHeight()

  # Let the user click on k points of the image, store them as centroids,
  # and print x and y coordinates of them in k lines. If a selected point
  # has the same RGB values as one of the
  # previous ones, don't accept it and wait for another one.  
  imageCentroids=createCentroids(numOfClusters, image, myImageWindow,width,height)
  dataFile=createDataFile(image)
  # Create dataFile which is a dictionary with pixel indexes and also the 
  # the pixels as the values of the dictionary.
  #dataFile = createDataFile(image)
  numofIters = 5 #number of k-means iterations 
  counter = 0
  while counter < numofIters:
    # Partition the color values in the image. That is, each pixel is
    # grouped in the cluster whose centroid it is closest to.

    clusters = createClusters(imageCentroids, dataFile,width,height)

    # Create a new image where each pixel has the colour value of its 
    # centroid.
    newImage = createNewImage(image,clusters, imageCentroids, width, height)
    # Display the new image.
    newImage.draw(myImageWindow)

    # Print the total distance rounded to two digits of precision beyond
    # the decimal point. Also NOTE that we are passing the original
    # image to computeDistance as the argument (NOT the newImage we
    # created previously)
    distance = round(computeDistance(clusters, imageCentroids, image,dataFile),2)
    print("Total distance at pass " + str(counter+1) +  " : " + str("%.2f"%distance))
    # Compute new centroids based on the clusters. Note that again we
    # are passing the original image to updateCentroid function as
    # the argument (NOT the newImage)
    imageCentroids = updateCentroids(clusters, imageCentroids,image,dataFile)
    counter += 1
if __name__ == "__main__":
    main()
