# Solin Algorithm 

# 첫째 줄에 node의 개수 n 과 간선의 개수 m이 주어진다. (node는 1~n)
# 두 번쨰 줄 부터 간선의 가중치 v , 간선이 연결된 node n1, n2가 순서대로 주어진다 
# 입력 예시 

# 5 5
# 1 2 3
# 2 4 3
# 8 2 0
# 9 4 2
# 6 2 4

# ----------------

# 5 5
# 1 2 3
# 2 4 3
# 8 2 0
# 9 4 2
# 6 1 4

# 7 10
# 4 0 1
# 3 0 2
# 5 1 2
# 4 1 4
# 2 1 3
# 7 2 5
# 5 2 6
# 11 2 4
# 8 3 4
# 3 4 6

# 다음과 같이 주어졌을 때 최소 신장트리를 만들어서 출력하시오 

import sys 

n, m = map(int,sys.stdin.readline().split())

matrix = []

# matrix[i][0] : 가중치 / [1]: node1 / [2]: node2
for i in range(m):
    matrix_line = list(map(int,sys.stdin.readline().split()))
    matrix.append(matrix_line)



matrix_map = [[] for _ in range(n)]

for k in matrix:
    x1 = k[1]
    x2 = k[2]
    w = k[0]

    matrix_map[x1].append([x2, w])
    matrix_map[x2].append([x1, w])

for index,i in enumerate(matrix_map):
    if(not i):
        print('can\'t make the MST')
        sys.exit(0)
    else:
        matrix_map[index] = sorted(i, key=lambda x:x[1])

tree_map = []
forest_list = []

for i in range(n):
    forest_list.append(set([i]))

empty = 0
while(empty==0):

    if (len(set(forest_list[0]))==n):
        break

    remove_list = []

    empty = 1
    for k in forest_list:
        temp_remove_list = []
        for i in k:
            index2 = -1
            index1 = -1      

            if(matrix_map[i]):
                empty=0

                for j in matrix_map[i]:
                    node1 = j[0]
                    weight = j[1]
                    break_point = 0
                    for index ,k in enumerate(forest_list):
                        if(node1 in k and i in k):
                            break_point = 1
                            break
                        if(node1 not in k and i in k):
                            index1 = index
                        if(i not in k and node1 in k):
                            index2 = index

                    if(break_point==1):
                        break
                    if(index!=-1):
                        temp_remove_list.append([node1,i,weight])
                        #print(i,node1,weight)
                        break

        if(temp_remove_list):
            temp_remove_list = sorted(temp_remove_list, key=lambda x : x[2])
            remove_list.append(temp_remove_list[0])
            tree_map.append(temp_remove_list[0])

        if(index1 != -1):
            a1 = set(forest_list[index1])
            a2 = set(forest_list[index2])
            a = a1.union(a2)
            forest_list.remove(a1)
            forest_list.remove(a2)
            forest_list.append(a)
            if (len(set(forest_list[0]))==n):
                break
        print("=== step ====")
        print("Forest list")
        print(forest_list)
        print("Tree Map")
        print(tree_map)
        print("\n\n")
            
    for k in remove_list:
        rm_node1 = k[0]
        rm_node2 = k[1]
        weight = k[2]
        matrix_map[rm_node1].remove([rm_node2,weight])
        matrix_map[rm_node2].remove([rm_node1,weight])

if (len(set(forest_list[0]))!=n):
        print("There is no MST")

print("============================= The Answer =============================")
print("[Node1 , Node2 , Weight]")
print(tree_map)