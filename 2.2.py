from __future__ import division
import snap
import matplotlib.pyplot as plt
Epinions_Graph = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt", 0, 1)
email_Graph = snap.LoadEdgeList(snap.PNGraph, "email-EuAll.txt", 0, 1)

def Plot(Graph,bool1,bool2):
    nodes=set()
    listy=[]
    listx=[]
    while len(nodes)<100:
        length=len(nodes)
        node=Graph.GetRndNId()
        nodes.add(node)
        if len(nodes)-length==0:
            continue
        Traverse=snap.GetBfsTree(Graph,node,bool1,bool2)
        listy.append(Traverse.GetNodes())
        listx.append(len(nodes)/100)
    listy.sort()
    plt.figure()
    plt.plot(listx, listy, marker='o', markersize=3, color="red")
    plt.ylim((0.1,Graph.GetNodes()))
    plt.xlim((0,1.1))
    plt.yscale('log')
    plt.show()
print("Epinions: outlinks")   
Plot(Epinions_Graph,True,False)
print("Epinions: inlinks")   
Plot(Epinions_Graph,False,True)
print("Email: outlinks")   
Plot(email_Graph,True,False)
print("Email: inlinks")   
Plot(email_Graph,False,True)
        