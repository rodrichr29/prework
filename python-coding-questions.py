# Question 1
def hello_name(user_name):
    user_name = input("Type in your username!: ")
    print("Hello " + user_name + "!")
hello_name("user_name")
print(hello_name)



# Question 2
def first_odds():
    list=[*range(1,100)]
    for numbers in list:
        if numbers % 2:
            print(numbers, end = " ")
first_odds()
print(first_odds)



# Question 3
def max_num_in_list(a_list):
    a_list=[0.002, 0.010042, 0.2, 0.2001, 0.004012]
    print(max(a_list))
max_num_in_list("a_list")
print(max_num_in_list)



# Question 4
def is_leap_year(a_year):
    a_year = int(input("Input an year: "))
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(a_year, "is a leap year.")
    elif a_year % 400 == 0 and a_year % 100 == 0:
        print(a_year, "is a leap year.")
    else:
        print(a_year, "is not a leap year")
is_leap_year("a_year")
print(is_leap_year)



# Question 5
def is_consecutive(a_list):
    for i in range(1, len(a_list)):
        if(a_list[i - 1] + 1 != a_list[i]):
            return False
    return True
print(is_consecutive([1, 2, 8, 4, 5]))
