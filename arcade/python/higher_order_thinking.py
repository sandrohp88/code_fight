import math


def tryFunctions(x, functions):
    '''
    You've been working on a numerical analysis when something went horribly wrong: your solution returned completely unexpected results. It looks like you apply a wrong function at some point of calculation. This part of the program was implemented by your colleague who didn't follow the PEP standards, so it's extremely difficult to comprehend.
    To understand what function is applied to x instead of the one that should have been applied, you decided to go ahead and compare the result with results of all the functions you could come up with. Given the variable x and a list of functions, return a list of values f(x) for each x in functions.
    Example
    For x = 1 and
    functions = ["math.sin", "math.cos",
        "lambda x: x * 2", "lambda x: x ** 2"],
    the output should be
    tryFunctions(x, functions) = [0.84147, 0.5403, 2, 1].

    '''

    return [eval(f)(x) for f in functions]


from functools import partial
'''
    Consider two straight lines given as y = mx + b. You forgot what they mean but you're sure that the destiny of the universe depends on them. To save the world, you have to choose one of these lines. Here is how to make the proper choice:
    Consider all integer coordinates a for all possible values of a from l to r, inclusive.
    For each vertical x = a, find the points where this vertical intersects with line1 and line2. Denote these points as p1 and p2, respectively. If p1 and p2 don't coincide, give one point to the line which is higher in that vertical.
    Choose the line which has a larger score. Return "first" for line1, "second" for line2 and "any" if both lines have the same score.
    Example
    For line1 = [1, 2], line2 = [2, 1], l = 0, and r = 2, the output should be
    twoLines(line1, line2, l, r) = "any";
    For line1 = [1, 2], line2 = [2, 1], l = -1, and r = 2, the output should be
    twoLines(line1, line2, l, r) = "first";
    For line1 = [1, 2], line2 = [2, 1], l = 0, and r = 3, the output should be
    twoLines(line1, line2, l, r) = "second".
'''


def line_y(m, b, x):
    return m * x + b


def twoLines(line1, line2, l, r):
    line1_y = partial(line_y, *line1)
    line2_y = partial(line_y, *line2)
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"


def compose(f, g):
    return lambda x: f(g(x))


def simpleComposition(f, g, x):
    '''
    In computer science, function composition is a mechanism of combining simple functions to build more complicated ones. Here's the deal: your colleague working on the databases implemented a low-level API that you have to deal with, and there's no way for you to update it and make it more sophisticated (or simply useful). Now you need to make a function that will be able to combine low-level functions into a single one using the function composition.
    Given two functions f and g that you need to combine and a variable x, return the result of the applying the function to x, i.e. f(g(x)).
    Example
    For f = "math.log10", g = "abs", and x = -100,
    the output should be
    simpleComposition(f, g, x) = 2.
    math.log10(abs(x)) = log10(abs(-100)) = log10(100) = 2.
    '''
    return compose(eval(f), eval(g))(x)


def compose(functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def functionsComposition(functions, x):
    '''
    As a professional and respected database programmer, you implemented a low-level API for your front-end colleagues to use. One of them, however, appeared to be quite an ungrateful exemplar, and had the nerve to criticize your work: it seems to him that the functionality your API provides is too basic, and he has to implement several additional functions on his end to make things work.
    You don't like to leave the users of your ingenious work disgruntled, so you have to update your API. It can be done quite simple: most of the high-level functionality can be added by combining several basic functions. Now you need to implement a function that will compose an arbitrary number of functions, and test it on some variable x.
    Example
    For functions = ["abs", "math.sin", "lambda x: 3 * x / 2"]
    and x = 3.1415, the output should be
    functionsComposition(functions, x) = 1.
    abs(math.sin(3 * 3.1415 / 2)) = abs(sin(4.71225)) ≈ abs(-1) = 1.
    '''
    return compose(map(eval, functions))(x)


def mergingVines(vines, n):
    '''
    One summer Felicia was visiting her granny's summer house. There were several old and withered vines growing in the garden, that no longer produced grapes. Felicia found it sad, and decided to decorate the vines with wooden grapes she carved out herself. She also watered them with cola, since cola makes everything better.
    When winter came, Felicia left, but the vines were still there, better than ever before. Each year they grew higher and wider, and the pairs of neighboring vines entangled together, forming a single vine. The wooden grapes were also doing just fine: they remained firmly attached to the vines.
    Now that n years has passed, Felicia is going to visit her granny again, and she is curious about how the vines are doing. Given the number of grapes she hang on the vines, return the number of grapes on each vine after n years, assuming that each year the (2 * i - 1)th and the (2 * i)th vines (1-based) merged into a single vine (for each integer i in range [1, <number_of_vines> / 2]).
    Example
    For vines = [1, 2, 3, 4, 5] and n = 2, the output should be
    mergingVines(vines, n) = [10, 5].
    After the first year vines two pairs of vines entangled: vines 1 and 2 and vines 3 and 4 (1-based). The last vine didn't have anything to entangle with. The vines could thus be represented as [3, 7, 5].
    After the second year, another pair of vines entangled. The first and the second vines entangled, forming a single vine. It's possible to represent the vines as [10, 5], which is the answer.
    '''
    def nTimes(n):
        def decorator(func):
            def wrapper(vines):
                for i in range(n):
                    vines = func(vines)
                return vines
            return wrapper
        return decorator

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)


def main():
    functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"]
    x = 1
    # Expected result  [0.84147, 0.5403, 2, 1].
    print(tryFunctions(x, functions))


if __name__ == '__main__':
    main()
