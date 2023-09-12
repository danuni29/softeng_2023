from week01.prime import is_prime

def main():


    list_prime = [x for x in range(1, 101) if is_prime(x)]
    print(list_prime)


if __name__ == '__main__':
    main()