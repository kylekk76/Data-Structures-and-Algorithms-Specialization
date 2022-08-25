
def maximum_pairwise():
    nothing = input() # i did this variable because literally they give you a number that if you use it the program is longer
    lst = input().split()
    lst = sorted(list(map(int, lst)),reverse=True)
   
    return int(lst[0])*int(lst[1])

def max_pairwise_product(numbers): # this secondone is what we supouse to do... but i find it way more complicate for nothing
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


# if __name__ == '__main__':
#     _ = int(input())
#     input_numbers = list(map(int, input().split()))
#     print(max_pairwise_product(input_numbers))


if __name__ =='__main__':
    print(maximum_pairwise())

