if __name__ == '__main__':

    # 1st task

    a, b, c = 9, 0.5, 5
    print(f"1st answer: {round((a * c) ** b, 3)}")

    # 2st task

    a, b, c, d = 9.99, 9.98, 1000, 1000.1
    print(f"2st answer: {(float(a) > b) and (float(c) != d)}")

    # 3st task

    a, b = 1234, 5678
    a = (a // 10) % 100
    b = (b // 10) % 100
    print(f"3st answer: {a + b}")

    # 4st task

    a, b = 13.42, 42.13
    print(f"4st answer: {(a // 1) == round(b % 1, 2) * 100 or (b // 1) == round(a % 1, 2) * 100}")
