import math

from dijkstar import *
from dijkstar.algorithm import *

class Slide:

    def __init__(self, photo1, photo2=None):
        self.photo1 = photo1;
        self.photo2 = photo2;

    @property
    def getTags(self):
        if (self.photo2 == None):
            #print("single: tags of slide: " + str(self.photo1.getTags))
            return self.photo1.getTags
        else:
            #print("double: tags of slide: " + str(list(set(self.photo1.getTags) & set(self.photo2.getTags))))
            return list(set(self.photo1.getTags).union(set(self.photo2.getTags)))
        
    

class Photo:

    def __init__(self, photoID, tagList):
        self.photoID = photoID
        self.tagList = tagList
        self._slideID = -1;

    @property
    def getTags(self):
        """The tagList property"""
        #print('Taglist getter called')
        #print('Taglist: ' + str(self.tagList))
        return self.tagList

    @property
    def getID(self):
        """The id property"""
        #print('ID getter called')
        #print('photoID: ' +str(self.photoID))
        return self.photoID
    
    @property
    def slideID(self):
        """The slide the photo belongs to"""
        #print('slide ID getter called')
        #print('slideID: ' +str(self._slideID))
        return self._slideID

    @slideID.setter
    def slideID(self, value):
        #print("setter of slideID called")
        self._slideID = value
        



def find_best_path(graph):
    nodes = [x for x in graph.keys()]
    maxcost = 0
    bestpath = []
    for v in nodes:
        pathinfo = find_longest_weighted_path(graph, v)
        path = pathinfo[0]
        cost = int(pathinfo[1])
        if (cost > maxcost):
            maxcost = cost
            bestpath = path
            
    return (bestpath, maxcost)

def find_longest_weighted_path(graph, start):
    
    def CostFunction(u, v, e, prev_e):
        cost =  -e
        return cost
    nodes = [x for x in graph.keys()]
    #nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    maxcost = 0
    bestpath = []
    for v in nodes:
        pathinfo = find_path(graph, start, v, cost_func=CostFunction)
        path = pathinfo[0]
        cost = -int(pathinfo[3])
        if (cost > maxcost):
            maxcost = cost
            bestpath = path

    return (bestpath, maxcost)

slideList = []
vList = []
with open('a_example.txt') as f:
    line = f.readline()
    line = f.readline()
    counter = 1
    while line:
        linelist = line.split();
        #print('linelist: ' + str(linelist))
        tagList = linelist[2:]
        photo = Photo(counter-1, tagList)
        if (linelist[0] == 'V'):
            vList.append(photo)
        else:
            slide = Slide(photo)
            slideList.append(slide)
        #print("pushed the photo to photolist")
        line = f.readline()
        counter += 1
#print("*********************")
#print("displaying all photos in my photolist")
#for photo in photoList:
    #print("PhotoID: {}, Tags: {}, slideID: {}".format(photo.getID, photo.getTags, photo.slideID))


# sort through vertical photos
vList.sort(key= lambda v: len(v.getTags))
for v in range(0,int(len(vList)/2)):
    slideList.append(Slide(vList[v], vList[len(vList)-1-v]))


def get_score(tags1, tags2):
    common  = len(list(set(tags1) & set(tags2)))
    unique1 = len(set(tags1)) - common
    unique2 = len(set(tags2)) - common
    return min(common, unique1, unique2)

graph = {}

for i in range(len(slideList)):
    slide1 = slideList[i]
    edges = {}
    for j in range(len(slideList)):
        if (i!=j):
            slide2 = slideList[j]
            score = get_score(slide1.getTags, slide2.getTags)
            if (score != 0):
                edges[j] = score
    graph[i] = edges


file = open('results2.txt', 'w')
path = find_longest_weighted_path(graph,0)

file.write(str(len(path[0])))
file.write("\n")
for slide in path[0]:
    file.write(str(slideList[slide].photo1.getID) + (" " + str(slideList[slide].photo2.getID) if slideList[slide].photo2 != None else "") + "\n")
    
file.close()

