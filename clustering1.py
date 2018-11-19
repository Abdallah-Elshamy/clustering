#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:54:05 2018

@author: Abdallah-Elshamy
"""
def cluster(edges , k , verticies):
    clusters = []
    for i in range(1 , verticies+1):
        clusters.append({i})
    while(len(clusters) != k):
        edge = edges.pop(0)
        first_flag = False
        second_flag = False
        for i in range(len(clusters)): 
            if edge[0] in clusters[i]:
                first_index = i
                first_flag = True
            if edge[1] in clusters[i]:
                second_index = i
                second_flag = True
            if first_flag and second_flag:
                break
        if first_index != second_index:
            if first_index < second_index:
                clusters.append(clusters.pop(first_index).union(clusters.pop(second_index-1)))
            else:
                clusters.append(clusters.pop(first_index).union(clusters.pop(second_index))) 
    
    same_cluster = True
    while(same_cluster) :
        edge = edges.pop(0)
        for j in range(k):
            if edge[0] in clusters[j] and edge[1] not in clusters[j]:
                ans = edge[2]
                same_cluster = False
            
    return ans
            
        




edges = []
with open('clustering1.txt') as f:
    verticies = int(f.readline())
    data = f.readlines()
    for line in data:
        edge = list(map(int,(line[:-1]).split()))
        edges.append(edge)
f.close()

edges.sort(key = lambda x : x[2])
print(cluster(edges , 4 , verticies))