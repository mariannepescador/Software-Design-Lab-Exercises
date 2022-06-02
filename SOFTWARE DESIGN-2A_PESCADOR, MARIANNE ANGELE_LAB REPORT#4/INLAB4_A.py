def MinRec(A, n):

    if (n == 1):
        return A[0]
    return min(A[n - 1], MinRec(A, n - 1))
 


if __name__ == '__main__':
    A = [5, 10, 15, 20, -25, 30, 3]
    n = len(A)
    print(MinRec(A, n))

def MaxRec(A, n):
 
    if (n == 1):
        return A[0]
    return max(A[n - 1], MaxRec(A, n - 1))

if __name__ == "__main__":
     
    A = [5, 10, 15, 20, -25, 30, 3]
    n = len(A)
    print(MaxRec(A, n))