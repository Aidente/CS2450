def guess_age(start, end):
    print("Hi, I'm trying to guess your age")
    name = input("Name : ")
    for i in range(start, end + 1):
        answer = input(f"Your age is {i}: ")
        if answer == "y":
            print(f"{name} is {i} years old")
            break
        else:
            print("Rats")

guess_age(15, 30)
