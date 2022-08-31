# Uses python3
import sys
def fibonacci_last_digit(number):

    lst=[0,1]
    number=number%60

    for n in range(2,60):
        lst.append((lst[n-1]+lst[n-2])%10)

    return lst[number]

def fibonacci_partial_sum_naive(from_, to):

    lst = [0, 1]
    last = [0, 1]
    for n in range(2, 60):
        lst.append(lst[n - 1] + lst[n - 2])
        last.append(int(str(lst[n])[-1]))

    m, n = from_,to
    q = int( (n - m + 1) / 60 )

    total = 0
    for n in range((m + q * 60), (n + 1)):
        total = total + last[n % 60]

    return total % 10


if __name__ == '__main__':

    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
