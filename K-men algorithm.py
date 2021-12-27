import random, math


data = [10, 90, 78, 69, 34, 21, 72, 65, 44, 37, 81, 95, 100, 30, 29, 18, 11, 62, 55, 75, 52]
print(data)
print()


k = int(input("Enter the number of clusters: "))
while(k < 1 or k > 10):
    k = int(input("Invalid numbers of clusters, try again: "))
print()


centroids = []
while(len(centroids) != k):
    randomItem = random.choice(data)
    if(not(randomItem in centroids)):
        centroids.append(randomItem)
print("Randomly choose centroids from data: ",centroids)
print()


allClusters = []
for i in range(k):
    allClusters.append([])


for item in data:
    minDistance = math.sqrt((item - centroids[0])**2)
    storeIndex = 0
    for i in range(1, k):
        euclideanDistance = math.sqrt((item - centroids[i])**2)
        if(euclideanDistance < minDistance):
            minDistance = euclideanDistance
            storeIndex = i
    allClusters[storeIndex].append(item)


for i in range(k):
    print("Cluster ",i+1," with centroid ",centroids[i]," : ",allClusters[i])
