def main():
    # Modify the variables so that all of the statements evaluate to True.

    var1 = 33
    var2 = "pigeon"
    var3 = [1, 2, 3, 4, 5]
    var4 = ("하이", "나는 다느니", "Hello, Python!", 2)
    var5 = {"happy":7, "egg":"salad", "tuna":"fish"}
    var6 = 40.3

    # Don't edit anything below this comment

    # Numbers
    print(isinstance(var1, int))
    print(isinstance(var6, float))
    print(var1 < 35)
    print(var1 <= var6)

    # Strings
    print(isinstance(var2, str))
    print(var2[5] == "n" and var2[0] == "p")

    # Lists
    print(isinstance(var3, list))
    print(len(var3) == 5)

    # Tuples
    print(isinstance(var4, tuple))
    print(var4[2] == "Hello, Python!")

    # Dictionaries
    print(isinstance(var5, dict))
    print("happy" in var5)
    print(7 in var5.values())
    print(var5.get("egg") == "salad")
    print(len(var5) == 3)
    var5["tuna"] = "fish"
    print(len(var5) == 3)


if __name__ == '__main__':
    main()