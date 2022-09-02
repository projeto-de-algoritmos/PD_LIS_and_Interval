def Find_Subsequence(arr, n):
    print(arr)
    print(n)
    
    L = [[]]*n
    
    L[0].append(arr[0])

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and (len(L[i]) < len(L[j]) + 1):
                L[i] = L[j].copy()   # atualiza predecessor

        L[i].append(arr[i])
 
    MAX = L[0]
 
    for item in L:
        if len(item) > len(MAX):  # encontra maior L
            MAX = item
    
    print(MAX)
    return MAX
    
 
if __name__ == "__main__":
 
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    n = len(arr)
    print(n)
 
    
    Find_Subsequence(arr, n)#10 22 33 41 60 80 

