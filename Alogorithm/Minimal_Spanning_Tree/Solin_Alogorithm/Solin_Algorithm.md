##  Solin's  Algorithm

-------

Forest state

- The state in which not all trees connected as one

Algorithm Description

1. Starting, we define all node is tree (forest state)
2. We select the smallest weight edge in each forest
3. Until the tree state, we repeat 1,2



----

솔린 알고리즘의 가장 큰 특징은 Greedy Algorithm 방식으로 MST를 구현했다는 것이다.

아래의 코드는 완벽한 방식으로 구현 했다기에는 애매하지만 솔린 알고리즘의 방식은 따른다.(미숙해서 코드가 효율적이지 않음)



```python
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
```

