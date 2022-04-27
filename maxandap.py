n = int(input())
list = []
for i in range(0, n):
    list.append(int(input()))

print(max(list))
nr_aparitii = 0
for i in range(0,n):
     if list[i] == max(list):
         nr_aparitii += 1
print(nr_aparitii)
