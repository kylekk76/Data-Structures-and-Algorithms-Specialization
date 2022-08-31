def fibonacci_last_digit(number):

    lst=[0,1]
    number=number%60

    for n in range(2,60):
        lst.append((lst[n-1]+lst[n-2])%10)

    return lst[number]

if __name__ == '__main__':
    number = int(input())
    print(fibonacci_last_digit(number))
