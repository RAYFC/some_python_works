from cImage import *
import math

def squaredEuclidDistance(point1, point2):
  # This function computes the squared Euclidean distance between
  # two points and returns the distance.  
  sum1 = 0
  for index in range(len(point1)):
      diff = (point1[index]-point2[index]) ** 2
      sum1 = sum1 + diff
  return sum1  
def createCentroids(k, image, myImageWindow,width,height):
  # This function asks the user to select k pixels with distinct RGB
  # values from the image and store them as centroids. Note that the
  # way you store these centroids is completely up to you. You can store
  # the pixel objects, store their (R,G,B) tuple values, etc.
  # Let the user click on k points of the image, store them as centroids,
  # and print x and y coordinates of them in k lines. If a selected point 
  # has the same RGB values as one of the previous ones, don't accept it 
  # and wait for another one. You can display a message and ask the user 
  # to input another pixel.
  centroids=[]
  print('please select '+k+' points')
  i=0 
  lst=[(10,165),(92,78),(133,78),(175,35)]
  #while i<=int(k)-1:
  #  position=myImageWindow.getMouse()
  for position in lst: 
    pixel=image.getPixel(position[0],position[1])
    red=pixel.getRed()
    green=pixel.getGreen()
    blue=pixel.getBlue()
    centroid=(red,green,blue)    
    if centroid not in centroids:
      print('position '+str(i+1)+' : '+str(position))
      centroids.append(centroid)
      i+=1
    else:
      print('please select another point')
  return centroids
def createDataFile(image):
  # This function creates a dictionary with index of image pixels as keys
  # and the actual image pixels as the values and returns the dataFile
  # dictionary. Be sure to refer to your textbook to get an idea of how to
  # implement this part efficiently. Note that the data structure you use 
  # to store points is up to you (I used dictionary :))  
  width=image.getWidth()
  height=image.getHeight()
  datadict={}
  for i in range(width):
    for m in range(height):
      pixel=image.getPixel(i,m)
      red=pixel.getRed()
      green=pixel.getGreen()
      blue=pixel.getBlue()
      datadict[(i,m)]=(red,green,blue)
  return datadict
def createNewImage(image,clusters, centroids, width, height):
  # This function creates a new image (You can check Chapter 6, page 192
  # of your textbook to get some hint :)) where each pixel
  # has the colour value of its centroid (use the round() function for each 
  # RGB value) and returns the new image.
  # Hint: The size of the new image should be the same as the old one. So
  # you can use width and height arguments to create such an image with
  # the same size.
  for cluster in clusters:
    index=clusters.index(cluster)
    for tuples in cluster:
      red=round(centroids[index][0],0)
      green=round(centroids[index][1],0)
      blue=round(centroids[index][2],0)
      col=tuples[0]
      row=tuples[1]
      pixel=Pixel(red,green,blue)
      image.setPixel(col,row,pixel)
  return image
def computeDistance(clusters, centroids, image,datadict):
  # This function computes the total distance and returns its value which
  # has been rounded to 2 digits beyond the decimal point in form of
  # a string.
  # The total distance is defined as the sum of all distances between
  # points and their centroids.
  # NOTE: you should round the total result to two digits of precision 
  # beyond the decimal point.
  # Hint: you may use the squaredEuclidDistance function in this
  # part to compute the distance between every point and its centroid
  # and add them up to calculate the total distance.  
  sum1=0
  for cluster in clusters:
    index=clusters.index(cluster)
    for tuples in cluster:
      dis=0
      squareddis=squaredEuclidDistance(datadict[tuples],centroids[index])
      dis+=squareddis
      sum1+=(dis)
  return round(sum1,2)
def updateCentroids(clusters,centroids,image,datadict):
  # This function updates the centroids by averaging RGB values of all
  # the pixels in each cluster. It then returns the new centroids.
  # Hint: To compute new centroids based on the clusters, remember that
  # you need to compute the average of all the points (of the original
  # image, not the ones from the previous pass) that belong to a given
  # cluster. You should iterate over all pixels in a single cluster and
  # compute the new centroid by averaging RGB values of those pixels.  
  newcentroids=[]
  k=len(centroids)
  for cluster in clusters:
    length=len(cluster)
    index=clusters.index(cluster)
    sumred=0
    sumgreen=0
    sumblue=0
    for tuples in cluster:
      red=datadict[(tuples[0],tuples[1])][0]
      green=datadict[(tuples[0],tuples[1])][1]
      blue=datadict[(tuples[0],tuples[1])][2]
      sumred+=red
      sumgreen+=green
      sumblue+=blue
      Red=sumred/length
      Green=sumgreen/length
      Blue=sumblue/length
    newcentroids.append((Red,Green,Blue))
  return newcentroids
def createClusters(centroids, dataFile,width,height):
  # This function creates clusters from dataFile and returns a list of
  # clusters. It assigns every pixel of the image to its nearest centroid.
  # When you group the pixels together and create clusters, you should
  # then return a list of the clusters.
  # Note: if ties happen, i.e. a pixel can be assigned to two or more
  # centroids you should break ties by assigning the centroid to the
  # first centroid in the centroid list.
  k = len(centroids)
  clusters=[]
  w=width
  h=height
  for i in range(k):
      clusters.append([])
  for key1 in range(w): 
    for key2 in range(h):
      dis=[]
      for index in range(k):
        sqareddistance=squaredEuclidDistance(dataFile[(key1,key2)],centroids[index])
        dis.append(sqareddistance)
      mindist = min(dis)
      index = dis.index(mindist)
      clusters[index].append((key1,key2))
  return clusters
