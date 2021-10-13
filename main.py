def printMenu():
    print ('1. Citire date')
    print ('2. Determinare cea mai lungă subsecvență in care toate numerele sunt pare')
    print ('3. Determinare cea mai lungă subsecvență in care concatenarea numerelor este un numar prim')
    print ('4. Determinare cea mai lungă subsecvență de numere cu acelasi numar de biti de unu')
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

def nr_biti_unu (n):
    '''
    Transforma numarul din baza 10 in baza 2 si retine numarul aparitiilor lui 1 intr-un contor
    '''
    contor=0
    m=int(n)
    while m > 0:
        if m % 2 == 1:
            contor += 1
        m = m // 2
    return contor

def test_nr_biti ():
    assert nr_biti_unu (2) == 1
    assert nr_biti_unu (17) == 2
    assert nr_biti_unu (23) == 4
    assert nr_biti_unu (1000) == 6

def all_same_bit (lst):
    '''
    Verifica daca toate elementele unei liste au acelasi numar de biti unu
    '''
    test_nr_biti()
    contor2 = nr_biti_unu(lst[0])
    for i in lst:
        if nr_biti_unu(i) != contor2:
            return False
    return True
def get_longest_same_bit_counts (lst):
    '''
    :param lst: o lista de numere
    :return: cea mai lunga subsecventa care indeplineste conditia de la prob 11
    '''
    lista_secv = []
    for start in range (0,len(lst)):
        for end in range (start + 1, len(lst)):
            if all_same_bit(lst[start:end]):
                lista_secv.append(lst[start:end])

    secv_max = []
    for secventa in lista_secv:
        if(len(secventa) > len(secv_max)):
            secv_max = secventa
    return secv_max


def main():
   test_get_longest_all_even()
   test_nr_biti()
   lst=[]
   while True:
        printMenu()
        optiune = input('Alegeti optiunea: ')
        if optiune == "1":
            lst=citireLista()
        elif optiune == "2":
            print(get_longest_all_even(lst))
        elif optiune == "3":
            print(get_longest_concat_is_prime(lst))
        elif optiune == '4':
            print(get_longest_same_bit_counts(lst))
        elif optiune == '5':
            break
        else:
            print("Optiune gresita! Reincercati!")


main()