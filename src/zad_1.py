def zad_a(names: list[str]) -> None:
    for name in names:
        print(name)


def zad_b1(nums: list[float]) -> list[float]:
    res = []
    for num in nums:
        res.append(num * 2.0)
    return res


def zad_b2(nums: list[float]) -> list[float]:
    return [num * 2.0 for num in nums]


def zad_c(nums: list[int]) -> None:
    for num in nums:
        if num % 2 == 0:
            print(num)


def zad_d(nums: list[int]) -> None:
    for i in range(0, len(nums) - 1, 2):
        print(nums[i])


if __name__ == "__main__":
    zad_a(["Adam", "Maciej", "Dawid", "Jan", "Kamil"])
    print(zad_b1([1.1, 2.2, 3.3, 4.4, 5.5]))
    print(zad_b2([1.1, 2.2, 3.3, 4.4, 5.5]))
    zad_c([1, 8, 6, 7, 3, 1, 2, 0, 6, 9])
    zad_d([1, 8, 6, 7, 3, 1, 2, 0, 6, 9])
