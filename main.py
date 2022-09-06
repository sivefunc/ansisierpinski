from sys import stdout
from os import get_terminal_size

from parser import parser
from center_text import center_text
from pascal_triangle import pascal_triangle
from sierpinski_triangle import sierpinski_triangle

args = parser()
write = stdout.write

ESC = chr(27)
CSI = ESC + '['

def main():

    rows = get_terminal_size()[1] - 1 if args.fill else args.rows
    triangle = sierpinski_triangle(pascal_triangle(rows))
    
    spaces = len(triangle[-1])
    if args.shownum:
        for row in triangle:
            text = ''.join([str(n) for n in row])
            write(text.center(spaces) + '\n')
    else:
        color1 = f'{CSI}47m' # White
        color2 = f'{CSI}40m' # Black
        for row in triangle:
            text = ''.join([color1 if num else color2 for num in row])
            write(f'{center_text(spaces, text + f"{CSI}0m", len(row))}\n')

if __name__ == '__main__':
    try:
        main()
    
    finally:
        write(f'{CSI}0m')
