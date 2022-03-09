import digitalclock

def number0(char):
    print(
        digitalclock.horizontal_line(5, char) + \
        digitalclock.two_vertical_lines(5, 3, char) + \
        digitalclock.horizontal_line(5, char)
    )

def number1(char):
    print(digitalclock.vertical_line(4, 5, char))

def number2(char):
    print(
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(4, 1, char) + \
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(0, 1, char) + \
        digitalclock.horizontal_line(5, char)
    )

def number3(char):
    print(
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(4, 1, char) + \
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(4, 1, char) + \
        digitalclock.horizontal_line(5, char)
    )

def number4(char):
    print(
        digitalclock.two_vertical_lines(5, 2, char) + \
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(4, 2, char)
    )

def number5(char):
    print(
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(0, 1, char) + \
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(4, 1, char) + \
        digitalclock.horizontal_line(5, char)
    )

def number6(char):
    print(
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(0, 1, char) + \
        digitalclock.horizontal_line(5, char) + \
        digitalclock.two_vertical_lines(5, 1, char) + \
        digitalclock.horizontal_line(5, char)    
    )

def number7(char):
    print(
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(4, 4, char)
    )

def number8(char):
    print(
        digitalclock.horizontal_line(5, char) + \
        digitalclock.two_vertical_lines(5, 1, char) + \
        digitalclock.horizontal_line(5, char) + \
        digitalclock.two_vertical_lines(5, 1, char) + \
        digitalclock.horizontal_line(5, char)  
    )

def number9(char):
    print(
        digitalclock.horizontal_line(5, char) + \
        digitalclock.two_vertical_lines(5, 1, char) + \
        digitalclock.horizontal_line(5, char) + \
        digitalclock.vertical_line(4, 2, char)
    )

number0("%")
number1("%")
number2("&")
number3("!")
number4("@")
number5("*")
number6("h")
number7("%")
number8("#")
number9("!")