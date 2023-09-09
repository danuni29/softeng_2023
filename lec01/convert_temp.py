def f2c(temp):
    return (temp - 32) * 5/9


def c2f(temp):
    return (temp * 1.8) +32

def main():
    print("화씨를 섭씨로 변환해드려요")
    temp_f = int(input("변환할 온도를 입력하세요"))
    print(f"{temp_f}F => {f2c(temp_f):.1f}℃")

    print("섭씨를 화씨로 변환해드려요")
    temp_c = int(input("변환할 온도를 입력하세요"))
    print(f"{temp_c}℃ => {c2f(temp_c):.1f}F")



if __name__ == '__main__':
    main()