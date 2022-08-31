def fibonacci_number(number):

    lst=[0,1]
    

    for n in range(2,number+1):
        lst.append(lst[n-1]+lst[n-2])
    
    return lst[number]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
