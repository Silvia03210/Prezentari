n = int(input())
list = []
for i in range(0, n):
    list.append(int(input()))
list_pare= []
for j in range(0,n):
      if list[j] % 2==0:
           list_pare.append(list[j])

print(max(list_pare))
nr_aparitii = 0
for i in range(0,n):
     if list[i] == max(list_pare):
         nr_aparitii += 1
print(nr_aparitii)


