
NBIG = 10000
#NBIG should be the sum of all vertices or larger, otherwise need a special provision for unconnected nodes
def floyd(g):
    #v is shorthand size of graph
    v = len(g)
    dists = []
    preds = []
    #store a matrix of graph distances, and pass through points
    for i in range(v):
        dists.append([])
        preds.append([])
        for j in range(v):
            dists[i].append(NBIG)
            preds[i].append(None)
    #print(dists,preds,g)
    #consider the graph, but building from only passing through the ith vertex
    for i in range(v):
        #iterate all connections of ith vertex first
        for j in range(v):
            f = True
            #all direct connections from i
            if dists[i][j] > g[i][j]:
                dists[i][j] = g[i][j]
                preds[i][j] = i
                f = True
            #all direction connections to i
            if dists[j][i] > g[j][i]:
                dists[j][i] = g[j][i]
                preds[j][i] = j
                f = True

            #consider all paths that could contain i, multidirectional, since this is directional, if they are better note them
            for k in range(v):
                if  dists[i][k] + dists[j][i] < dists[j][k]:
                    dists[j][k] = dists[i][k] + dists[j][i]
                    preds[j][k] = i
            for k in range(v):
                if  dists[k][i] + dists[i][j] < dists[k][j]:
                    dists[k][j] = dists[k][i] + dists[i][j]
                    preds[k][j] = i


    return dists,preds

graph = [
    [0,4,NBIG,NBIG],
    [3,0,15,7],
    [9,3,0,9],
    [NBIG,6,2,0]
]
print("Original Graph:\n",graph,"\n\n")
floyd(graph)
dists, preds = floyd(graph)
print(dists,preds)
