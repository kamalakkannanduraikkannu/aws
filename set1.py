set_v = set(map(int,input().split()))
set_v1 = set(map(int,input().split()))

c = list(set_v-set_v1) + list(set_v1-set_v)
print(*sorted(c),sep="\n")