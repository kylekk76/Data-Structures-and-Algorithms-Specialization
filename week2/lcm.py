


def gcd(a, b):
    
    while b:
        a,b=b,a % b
    return abs(a)

def lcm(a, b):
    return int(a * b / gcd(a, b))



if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

