def full_prima(N):
    # cek apakah N adalah bilangan prima
    if N<2:return False
    for i in range(2,N):
            if N%i == 0: return False  

    #cek apakah masing-masing digit dari N adalah bilangan prima
    while N:
        dig=N%10
        if (dig !=2 and dig !=3 and dig !=5 and dig !=7):
            return False
        N = int(N/10)
    return True

if __name__ == '__main__':
    print(full_prima(0)) # True
    print(full_prima(-3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True