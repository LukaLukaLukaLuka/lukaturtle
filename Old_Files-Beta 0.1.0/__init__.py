from turtle import *
def shape(number_of_sides, length):
    if number_of_sides < 3:
        print("Number of sides must be at least 3!")
    else:
        st()
        for _ in range(number_of_sides):
            fd(length)
            lt(360 // number_of_sides)