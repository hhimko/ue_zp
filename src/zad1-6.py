def zad_1(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"

def zad_2(a: int, b: int) -> int:
    return a * b

def zad_3(num: int) -> bool:
    return num & 2 == 0

def zad_4(a: int, b: int, c: int) -> bool:
    return a + b > c

def zad_5(l: list[int], num: int) -> bool:
    return num in l

def zad_6(l1: list[int], l2: list[int]) -> list[int]:
    l3 = list(set(l1 + l2))
    return [num ** 3 for num in l3]


if __name__ == "__main__":
    print(zad_1("Dawid", "Cyganek"))
    print(zad_2(7, 8))
    even = zad_3(9)
    if even:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
    print(zad_4(1, 2, 3))
    print(zad_5([1, 2, 3], 4))
    print(zad_6([1, 2, 3], [3, 4, 1]))


