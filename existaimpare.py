n=int(input(('n=')))
list_nr = []
for i in range(1, n+1):
    list_nr = list(map(int, input().strip().split()))[:n]
    ok=0
    for i in range(len(list_nr)):
        if list_nr[i]%2==1:
            print('DA')
            ok=1
            break

    if ok==0:
        print('NU')