
import snap
Epinions_Graph = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt", 0, 1)
email_Graph = snap.LoadEdgeList(snap.PNGraph, "email-EuAll.txt", 0, 1)
def Judge(Graph,num):
    G1=snap.GetBfsTree(Graph,num,True,False)
    G2=snap.GetBfsTree(Graph,num,False,True)
    forward=G1.GetNodes()
    backward=G2.GetNodes()
    if (forward<backward and forward*5>backward) or (forward>backward and forward<backward*5):
        print "Node %d belongs to SCC " % (num)
    elif forward>backward:
        print "Node %d belongs to IN " % (num) 
    elif forward<backward:
        print "Node %d belongs to OUT " % (num) 
Judge(Epinions_Graph,9809)
Judge(Epinions_Graph,1952)
Judge(email_Graph,189587)
Judge(email_Graph,675)




        