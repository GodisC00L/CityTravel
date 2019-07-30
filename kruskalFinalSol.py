class graph:
    #initialize graph with N vertices, and no edges
    def __init__(self, N):
        self.vertices = N #no. of vertices
        self.edges = [] #dictionary to keep edges etc.
        
    #edge is represented by (src,dst,weight)
    def addEdge(self,src,dst,weight):
        self.edges.append([src,dst,weight])
        
    #find the "representative" of the group node i belongs to
    def find(self, representatives, i): 
        #print(representatives, i)
        if representatives[i-1] == i: 
            return i
        return self.find(representatives, representatives[i-1]) 
    
    #unite two groups and decide their new representative by rank
    def unite(self, representatives, rank, x, y): 
        xRep = self.find(representatives, x) 
        yRep = self.find(representatives, y) 
        if rank[xRep-1] < rank[yRep-1]: 
            representatives[xRep-1] = yRep 
        elif rank[xRep-1] > rank[yRep-1]: 
            representatives[yRep-1] = xRep 
        else : 
            representatives[yRep-1] = xRep 
            rank[xRep-1] += 1  
            
class Solution:
    #run kruskal algorithm to find weight of MST
    def minimumCost(N, connections):
        g = graph(N)
        for item in connections:
            g.addEdge(item[0],item[1],item[2])
            
        sum = 0; i = 0; e = 0;
        edges = sorted(g.edges, key = lambda item:item[2])
        representatives =[]; rank = [];
        #build a list where every element represents the group of the node in the matching index
        for nodeInd in range(N):
            representatives.append(nodeInd+1)
            rank.append(0)
            
        #haven't built a tree yet, and there are more edges to go through
        while e < N-1 and i < len(edges):
            u,v,w = edges[i]
            i += 1
            rep1 = g.find(representatives, u) 
            rep2 = g.find(representatives ,v)
            #different groups -> unite them into one
            if rep1 != rep2: 
                e = e + 1     
                sum += w 
                g.unite(representatives, rank, rep1, rep2)
        
        if(e < N-1): #no tree can be built
            return -1
        else:
            return sum
        
print("Minimal cost for MST:" ,Solution.minimumCost(N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]))