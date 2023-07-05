#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# MY PREDICTION: no values assigned to variables, but 5 gets returned when the function is called and therefore the value of number_of_food_groups is 5. what's returned gets printed so 5 gets logged.
# OUTCOME:
# 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# # MY PREDICTION: because number_of_days_in_a_week_silicon_or_triangle_sides is never assigned a value, it is undefined and although the value of number_of_military_branches becomes 5, nothing will get logged due to an error from trying to add something undefined and an integer.
# OUTCOME:
# NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# # MY PREDICTION: number_of_books_on_hold becomes 5 once it is called. It never returns the second expression. 5 gets printed.
# OUTCOME:
# 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# MY PREDICTION: number_of_fingers becomes 5 when it is called and 5 is logged.
# OUTCOME:
# 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# MY PREDICTION: number_of_great_lakes is called and becomes 5 and the variable x is set to 5 and then logged/ printed.
# OUTCOME:
# 5
# None

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# MY PREDICTION: 8 gets printed
# OUTCOME:
# 3
# 5
# but final print log never happens due to unsupported operand


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# MY PREDICTION: prints 25
# OUTCOME:
# 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# MY PREDICTION:
# 100
# 100
# 10
# 7
# OUTCOME:
# 100
# 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# MY PREDICTION:
# 7
# 14
# 21
# OUTCOME:
# 7
# 14
# 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# # MY PREDICTION:
# 8
# OUTCOME:
# 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# MY PREDICTION:
# 500
# 500
# 300
# 500
# OUTCOME:
# 500
# 500
# 300
# 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# MY PREDICTION:
# 500
# 500
# 300
# 500
# OUTCOME:
# 500
# 500
# 300
# 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# MY PREDICTION:
# 500
# 500
# 300
# 300
# OUTCOME:
# 500
# 500
# 300
# 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# MY PREDICTION:
# 1
# 2
# 3
# OUTCOME:
# 1
# 3
# 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# MY PREDICTION:
# 1
# 3
# 5
# 10
# OUTCOME:
# 1
# 3
# 5
# 10