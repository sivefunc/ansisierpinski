def pascal_triangle(rows):
    """
    return a nested list representing a pascal triangle with the
    given rows
    """
    
    triangle = [
            [0, 1, 0]
            ]
   
    pascal_row = triangle[0]
    last_digit = 0
    
    for row in range(1, rows):
        new_row = []
        for digit in pascal_row:
            # add two digits of pascal row to gen new row
            new_row.append(digit + last_digit)
            last_digit = digit
        
        triangle.append(pascal_row := new_row + [0])
    return triangle
