a=[3, 4, 6, 10, 11, 15]
b=[1, 5, 8, 12, 14, 19]

def mergeSort(a,b):
    i,j=0,0
    res,m,n=[],len(a),len(b)
    while i < m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i+=1

        else:
            res.append(b[j])
            j+=1

    while i<m:
        res.append(a[i])
        i+=1

    while j<n:
        res.append(b[j])

        j+=1

    return res

mergeSort(a, b)
