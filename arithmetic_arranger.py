class TestFailed(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


def convert_problem_to_elements(problem):
    a, b, c = problem.split(" ")

    if b not in ["+", "-"]:
        raise TestFailed("Error: Operator must be '+' or '-'.")

    if len(a) > 4 or len(c) > 4:
        raise TestFailed("Error: Numbers cannot be more than four digits.")

    if not (a.isdigit() and c.isdigit()):
        raise TestFailed("Error: Numbers must only contain digits.")

    return a, b, c


def include_spaces_between_functions(lines):

    if not lines[0] == "":
        for i in range(len(lines)):
            lines[i] += "    "

    return lines


def arithmetic_arranger(problems, result=False):
    lines = [""] * 4 if result else [""] * 3

    if len(problems) > 5:
        return "Error: Too many problems."

    for p in problems:
        try:
            a, b, c = convert_problem_to_elements(p)
            desired_size = max(len(a), len(c)) + 2

            lines = include_spaces_between_functions(lines)

            lines[0] += a.rjust(desired_size)
            lines[1] += b + c.rjust(desired_size-1)
            lines[2] += "-" * desired_size
            if result:
                math_result = str(int(a) + int(c) if b == "+" else int(a) - int(c))
                lines[3] += math_result.rjust(desired_size)

        except TestFailed as x:
            return x.message

    return "\n".join(lines)
