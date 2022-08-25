
def maximum_pairwise():
    nothing = input()
    lst = input().split()
    lst = sorted(list(map(int, lst)),reverse=True)
   
    return int(lst[0])*int(lst[1])



if __name__ =='__main__':
    print(maximum_pairwise())

