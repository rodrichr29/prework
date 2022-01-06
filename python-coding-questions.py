# Question 1
def hello_name(user_name):
    user_name=input("Type in your username!: ")
    print("Hello "+user_name+"!")
hello_name("user_name")
print(hello_name)

# Question 2
def first_odds():
    start,end=1,100
    for num in range(start,end+1):
        if num%2!=0:
            print(num,end=" ")
first_odds()
print(first_odds)

# Question 3
def max_num_in_list(a_list):
    max_num=a_list[0]
    for i in a_list:
        if i > max_num:
            max_num=i
    return max_num
max_num_in_list("a_list")
print(max_num_in_list([0.124,0.1,0.041,0.010043,0.240214,0.0000001]))

# Question 4
def is_leap_year(a_year):
    
is_leap_year("a_year")