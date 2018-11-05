from functools import reduce


def scariestMask(mask):
    asymetric = 0
    for m in mask:
        asymetric += count_asymetric(m)
    return asymetric


def count_asymetric(s):
    start = 0
    end = len(s) - 1
    asymetric = 0
    while start < end:
        if s[start] != s[end]:
            asymetric += 1
        start += 1
        end -= 1
    return asymetric


def main():
    mask = ["A    A",
            " O  O ",
            "= WW ="]
    print(scariestMask(mask))


if __name__ == '__main__':
    main()
