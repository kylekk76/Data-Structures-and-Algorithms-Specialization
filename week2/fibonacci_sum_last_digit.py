def fibonacci_sum(number):

    lst=[0,1]
    number = number%60

    for n in range(2,number+1):
        lst.append((lst[n-1]+lst[n-2])%60)
    if number==0:
        sum_=0
    else: sum_= sum(lst)%10
    return sum_

if __name__ == '__main__':
    number = int(input())
    print(fibonacci_sum(number))
   