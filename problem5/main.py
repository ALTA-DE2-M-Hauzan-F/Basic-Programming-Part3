def pangkat(base, pangkat):
    # your code here
    p=base
    for i in range(1,pangkat):
        p *=base
    return p


if __name__ == '__main__':
    print(pangkat(2, 3)) # 8
    print(pangkat(5, 3)) # 125
    print(pangkat(10, 2)) # 100
    print(pangkat(2, 5)) # 32
    print(pangkat(7, 3)) # 343