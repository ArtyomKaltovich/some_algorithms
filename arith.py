def f(n, x):
    return sum(x ** (2 ** (i-1)) / (1 - x ** (2 ** i)) for i in range(1, n+1))


if __name__ == '__main__':
    #print(f(1000, 0.75))
    #print(f(1000, 0.5))
    #print(f(1000, 0.25))
    #print(f(1000, 0.33))
    #print(len([(x,y) for x in range(1, 10) for y in range(1, 10) if x + y==15]))
    print([(x,y) for x in range(1, 10) for y in range(1, 10) if x + y==15])

