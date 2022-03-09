# FUNCTION:   horizontal_line
# INPUT:      a width value (integer) and a single character (string)
# PROCESSING: generates a single horizontal line of the desired size
# OUTPUT:     returns the generated pattern (string)
def horizontal_line(width,char):
    return width * char + "\n"

# FUNCTION:   vertical_line
# INPUT:      a shift value and a height value (both integers)  and a single character (string)
# PROCESSING: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# OUTPUT:     returns the generated pattern (string)

def vertical_line(shift,height,char):
    pattern = ""
    for i in range(height):
        pattern += shift * " " + char + "\n"
    return pattern

# FUNCTION:   two_vertical_lines
# INPUT:      a width value and a height value (both integers)  and a single character (string)
# PROCESSING: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# OUTPUT:     returns the generated pattern (string)
def two_vertical_lines(width,height,char):
    pattern = ""
    for i in range(height):
        pattern += char + " " * (width-2) + char + "\n"
    return pattern
