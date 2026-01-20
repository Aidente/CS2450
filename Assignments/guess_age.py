def guess_age():
    print("Hi, I'm trying to guess your age")
    name = input("Name : ")
    for i in range(15,31):
        answer = input(f"Your age is {i}")
        if lower(answer) == "y":
            print(f"{name} is {i} years old")
            break
        else:
            print("Rats")

