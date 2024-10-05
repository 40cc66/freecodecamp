import sys

from itertools import permutations, product

LOOKUP = 24
TEMPLATES = [
    "{a}{o1}{b}{o2}{c}{o3}{d}",  # a+b+c+d
    "({a}{o1}{b}){o2}{c}{o3}{d}",  # (a+b)+c+d
    "{a}{o1}({b}{o2}{c}){o3}{d}",  # a+(b+c)+d
    "{a}{o1}{b}{o2}({c}{o3}{d})",  # a+b+(c+d)
    "({a}{o1}{b}{o2}{c}){o3}{d}",  # (a+b+c)+d
    "{a}{o1}({b}{o2}{c}{o3}{d})",  # a+(b+c+d)
    "({a}{o1}{b}){o2}({c}{o3}{d})",  # (a+b)+(c+d)
    "(({a}{o1}{b}){o2}{c}){o3}{d}",  # ((a+b)+c)+d
    "({a}{o1}({b}{o2}{c})){o3}{d}",  # (a+(b+c))+d
    "{a}{o1}(({b}{o2}{c}){o3}{d})",  # a+((b+c)+d)
    "{a}{o1}({b}{o2}({c}{o3}{d}))",  # a+(b+(c+d))
]


def solve24(num_string):
    solutions = []
    for a, b, c, d in sorted(set(permutations(num_string))):
        for o1, o2, o3 in list(product("+-*/", repeat=3)):
            for template in TEMPLATES:
                expression = template.format(a=a, b=b, c=c, d=d, o1=o1, o2=o2, o3=o3)
                try:
                    result = eval(expression)
                    # print(f"{expression}={result}")
                    if result == LOOKUP:
                        solutions.append(expression)
                except ZeroDivisionError:
                    pass
    return solutions or "no solution exists"


def main():
    numbers = sys.argv[-1]
    solutions = solve24(numbers)
    if isinstance(solutions, list):
        for solution in solutions:
            print(solution)
    else:
        print(solutions)


if __name__ == "__main__":
    main()
