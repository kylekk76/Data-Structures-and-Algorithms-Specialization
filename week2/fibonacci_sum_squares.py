def fibonacci_sum_squares(number):

    lst = [0, 1]
    last = [0, 1]
    for n in range(2, 60):
        lst.append(lst[n - 1] + lst[n - 2])
        last.append(int(str(lst[n])[-1]))

    
    answer = last[number % 60] * last[number % 60] + last[number % 60] * last[(number - 1) % 60]

    return(answer % 10)
if __name__ == '__main__':
    number = int(input())
    print(fibonacci_sum_squares(number))


