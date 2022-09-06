from copy import deepcopy

from pascal_triangle import pascal_triangle

def sierpinski_triangle(pascal_triangle):
    """
    return a nested list representing a sierpinski triangle by
    taking the given pascal triangle and then changing every number
    to 1s if number is odd else changing to 0s
    """

    # https://youtube.com/watch?v=0iMtlus-afo -> min 6:22
    # https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#Pascal's_triangle
    
    # Remove the border of 0s
    pascal_triangle = [[n for n in row if n] for row in pascal_triangle]
    
    for Y, row in enumerate(deepcopy(pascal_triangle)):
        for X, num in enumerate(row):
            pascal_triangle[Y][X] = 0 if num % 2 == 0 else 1
    
    return pascal_triangle
