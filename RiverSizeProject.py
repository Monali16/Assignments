
#used depth first search algorithm to get the size of the rivers.


def riverSize(matrix):    #iniialize the river size matrix that contains size of all the rivers
    size = []       #initialize size of an array
    visited = [[False for value in row] for row in matrix]   #iterate all elements in matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:  #check the condition if already visited
                continue       #if already visited then skip
            traverseNode(i,j,matrix,visited,size)
    return size
    
def traverseNode(i,j,matrix,visited,size):   
    currentRiversize=0    #current river size is equal to zeor in the beginning
    nodes=[[i,j]]
    while len(nodes):     # check if length of nodes is not zero
        currentNode= nodes.pop()   #pop out the value 
        i= currentNode[0]
        j= currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j]=True
        if matrix[i][j]==0:    
            continue
        currentRiversize +=1
        unvisitedneighbors= getunvisitedneighbors(i,j,matrix,visited)    #get all unvisited neighbors
        for neighbor in unvisitedneighbors:    #check for the neighbor which is not visited
            nodes.append(neighbor)    #append neighbor to nodes which are unvisited
    if currentRiversize>0:      #check the condition
        size.append(currentRiversize)   #if condition is true append the updated current size of river in size
def getunvisitedneighbors(i,j,matrix,visited):
    unvisitedneighbors = []
    if i>0 and not visited[i-1][j]:        #neighbor of above
        unvisitedneighbors.append([i-1,j])
    if i<len(matrix)-1 and not visited[i+1][j]:    #below neighbor
        unvisitedneighbors.append([i+1,j])
    if j>0 and not visited[i][j-1]:         # left neighbor
        unvisitedneighbors.append([i,j-1])
    if j<len(matrix[0])-1 and not visited[i][j+1]:     #right neighbor
        unvisitedneighbors.append([i,j+1])
    return unvisitedneighbors
matrix = [[1,0,0,1,0],
[1,0,1,0,0],
[0,0,1,0,1],
[1,0,1,0,1],
[1,0,1,1,0]]
print(riverSize(matrix))
while True:
    try:
        m = [2,1,5,2,2]
        R = int(input("Enter the number of rows:")) 
        C = int(input("Enter the number of columns:")) 
        mat = [[input('Guess the size of river : ') for x in range (C)] for y in range(R)] 
        if any(ele for ele in [2,1,5,2,2]):
            print('You are the winner')
            break
        if [1,2,5] in mat or [2,2,2] in mat or [2,1,5] in mat or [5,2,1] in mat or [2,1,2] in mat or [2,5,1] in mat or [2,5,2] in mat or [2,2,1] in mat or [2,2,5] in mat:
            print("you got second position")
            break 
        else:  
            print("Invest more money on Almonds, then come back")         
    except:
        try_again= raw_input('Do you want to play again (Y/N)?')
        if try_again == 'Y':
            mat = [[input('Guess the size of river : ') for x in range (C)] for y in range(R)] 
        else:
            exit    

