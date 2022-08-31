def fibonacci_huge_naive(number, m):


    
    v1, v2, v3 = 1, 1, 0  
    
    for rec in bin(number)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2

if __name__ == '__main__':
    number,m = map(int,input().split())
    print(fibonacci_huge_naive(number,m))   
    
    

