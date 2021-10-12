def printMenu():
    print ('1. Citire date')
    print ('2. Determinare cea mai lungă subsecvență in care toate numerele sunt pare')
    print ('3. Determinare cea mai lungă subsecvență in care media numerelor nu depășește o valoare citită')
    print ('4. Determinare cea mai lungă subsecvență in care toate numerele sunt divizibile cu un numar')
    print ('5. Iesire')

def citireLista ():
    lst = []
    n = int(input('Dati nr de elemente: '))
    for i in range(n):
        lst.append(int(input('L[' + str(i) + '] =')))
    return lst

def ToateElemSuntPare(lst):
    '''
    determina daca o lista are toate elementele nr pare
    :param lst: lista de nr intregi
    :return: True, daca toate elem din lista sunt nr pare sau False, in caz contrar
    '''
    for i in lst:
        if i % 2 !=0:
            return False
    return True

def test_ToateElemSuntPare(lst):
    assert ToateElemSuntPare([1,2,3]) is False
    assert ToateElemSuntPare([4,6,78,0]) is True
    assert ToateElemSuntPare([17,9,11,5,31,4]) is False

def get_longest_all_even (lst):
    '''
    determina cea mai lunga subsecventa in care toate elementele sunt numere pare
    :param lst: lista de numere intregi
    :return: cea mai lunga subsecventa in care toate elementele sunt numere pare din lst
    '''
    test_ToateElemSuntPare(lst)
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if ToateElemSuntPare(lst[i:j+1]) and len(subsecventaMax) < len(lst[i:j+1]):
                subsecventaMax = lst[i:j+1]
    return subsecventaMax

def test_get_longest_all_even ():
    assert get_longest_all_even([1,3]) == []
    assert get_longest_all_even([2,4,12]) == [2,4,12]
    assert get_longest_all_even([5,90,20,71,10]) == [90,20]


def nr_prim (n: int) :
    for i in range (2,n//2+1):
        if n % i == 0:
            return False
    return True


def get_longest_concat_is_prime (lst: list[int])-> list[int]:
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range (i,len(lst)):
            if nume(lst[i:j+1]) and len(lst[i:j+1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j+1]
    return subsecventaMax


def nume(lst: list[int]) -> int:
    string = " "
    for i in lst:
        string = int(str(string) + str(i))
    return string

def main():
   test_get_longest_all_even()
   lst=[]
   while True:
        printMenu()
        optiune = input('Dati optiunea: ')
        if optiune == "1":
            lst=citireLista()
        elif optiune == "2":
            print(get_longest_all_even(lst))
        elif optiune == "3":
            print(get_longest_concat_is_prime(lst))
        elif optiune == '4':
            break
        else:
            print("Optiune gresita! Reincercati!")


main()