# 특정원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 두원소 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모테이블 초기화
test_case = []
# 부모테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i 

# 각 연산을 하나씩 확인
for i in range(e):
    test, a, b = map(int, input().split())
    # 합집합 연산인 경우
    if test == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif test == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
