#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 21:57:02 2018

@author: tshen
"""
import snap
Epinions_Graph = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt", 0, 1)
email_Graph = snap.LoadEdgeList(snap.PNGraph, "email-EuAll.txt", 0, 1)
total1=0
def Judge(Graph,num):
    G1=snap.GetBfsTree(Graph,num,True,False)
    G2=snap.GetBfsTree(Graph,num,False,True)
    forward=G1.GetNodes()
    backward=G2.GetNodes()
    if (forward<backward and forward*10>backward) or (forward>backward and forward<backward*10):
        return True
def GetSccNode(graph):
    for N1 in graph.Nodes():
        if Judge(graph,N1.GetId())==True:
            return N1.GetId()
def Cal(Graph,num):
    Scc=0
    G1=snap.GetBfsTree(Graph,num,True,False)
    G2=snap.GetBfsTree(Graph,num,False,True)
    G3=snap.GetBfsTree(Graph,num,True,True)
    IN=G2.GetNodes()
    OUT=G1.GetNodes()
    print "Nodes DISCONNECTED: %d" % (Graph.GetNodes()-G3.GetNodes())
    for N1 in Graph.Nodes():
        if G1.IsNode(N1.GetId())==True and G2.IsNode(N1.GetId())==True:
            Scc+=1
    IN=IN-Scc
    OUT=OUT-Scc
    print "Nodes SCC: %d" % (Scc)
    print "Nodes IN: %d" % (IN)
    print "Nodes OUT: %d" % (OUT)
    print "Nodes TENDRILS: %d" % (G3.GetNodes()-IN-OUT-Scc)
        
print("Email graph:")
Cal(email_Graph,GetSccNode(email_Graph))
print("Epinions graph:")
Cal(Epinions_Graph,GetSccNode(Epinions_Graph))




