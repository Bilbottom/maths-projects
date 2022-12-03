

def main():
    i = 0
    while i**2 < 10_000:
        print(i, i**2, str(i**2) == str(i**2)[::-1])
        i += 1


if __name__ == '__main__':
    main()
