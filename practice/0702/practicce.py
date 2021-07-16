import sys
import math

def area_triangle(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def per_triangle(a,b,c):
    return a+b+c

def area_circle(r):
    return r**2 * math.pi

def per_circle(r):
    return r*2*math.pi

def area_rectangle(a,b):
    return a*b

def per_rectangle(a,b):
    return 2*(a+b)

def main():
    function_1 = sys.argv[1]
    function_2 = sys.argv[2]
    str_nums = sys.argv[3:]

    nums = list(map(int, str_nums))
    
    if (function_1 == 'area' and function_2 == 'triangle'):
        return area_triangle(nums)

    if (function_1 == 'area' and function_2 == 'circle'):
        return area_circle(nums)

    if (function_1 == 'area' and function_2 == 'rectangle'):
        return area_rec(nums)

    if (function_1 == 'perimeter' and function_2 == 'triangle'):
        return per_triangle(nums)

    if (function_1 == 'perimeter' and function_2 == 'circle'):
        return per_circle(nums)

    if (function_1 == 'perimeter' and function_2 == 'rectangle'):
        return per_rectangle(nums)
    
if __name__ == "__main__":
    print(main())