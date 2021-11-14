n, m = input().split()
n = int(n)
m = int(m)

n_set = set()
m_set = set()

for n1 in range(n):
    n_set.add(input())
for n2 in range(m):
    m_set.add(input())

print('\n'.join(m_set.intersection(n_set)))

