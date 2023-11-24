import json
import random
import decimal
import math

def generate_math_problems(num_problems):
    problem_generators = [
        generate_arithmetic_problem,
        generate_equation_problem,
        generate_real_world_problem
    ]

    math_problems = [random.choice(problem_generators)() for _ in range(num_problems)]
    return math_problems

def generate_arithmetic_problem():
    a = decimal.Decimal(random.uniform(-10000, 10000)).quantize(decimal.Decimal('0.00'))
    b = decimal.Decimal(random.uniform(-10000, 10000)).quantize(decimal.Decimal('0.00'))

    operator = random.choice(["+", "-", "*", "/"])

    if operator == "/":
        if b == decimal.Decimal(0):
            return generate_arithmetic_problem()
    
    problem_text = f"计算 {a} {operator} {b} 等于多少？"
    answer_text = f"{a} {operator} {b} ="

    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    result = operators[operator](a, b)

    return {
        "text": f"### Human: {problem_text}\n### Assistant: {answer_text} {result}"
    }

def generate_equation_problem():
    m = random.randint(-100, 100)
    n = random.randint(-100, 100)
    
    while m == 0:
        m = random.randint(-100, 100)

    solution = -n / m

    problem_text = f"解方程 {m}x + {n} = 0"
    answer_text = f"方程的解为：{solution}"

    return {
        "text": f"### Human: {problem_text}\n### Assistant: {answer_text}"
    }

def generate_real_world_problem():
    problem_generators = [
        generate_average_problem,
        generate_function_problem,
        generate_increase_decrease_problem,
        generate_area_problem,
        generate_fraction_simplification_problem,
        generate_mass_problem
    ]

    problem = random.choice(problem_generators)
    return problem()

def generate_average_problem():
    num_values = random.randint(3, 10)
    values = [random.randint(1, 100) for _ in range(num_values)]
    total = sum(values)

    problem_text = f"求以下数据的平均值：{values}"
    result = total / num_values

    return {
        "text": f"### User: {problem_text}\n### Assistant: 平均值为 {result}"
    }

def generate_function_problem():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    x = decimal.Decimal(random.uniform(0.1, 10.0)).quantize(decimal.Decimal('0.00'))
    result = a * (x ** b)

    problem_text = f"当 x = {x} 时，求函数 y = {a}x^{b} 的值"
    answer_text = f"函数的值为：{result}"

    return {
        "text": f"### Human: {problem_text}\n### Assistant: {answer_text}"
    }

def generate_increase_decrease_problem():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    if random.randint(0, 1) == 0:
        problem_text = f"去年销售额为 {a} 万元，今年销售额增加了 {b}%，请计算今年的销售额。"
        result = a + (a * b / 100)
    else:
        problem_text = f"商品原价为 {a} 元，打折后的价格为 {b} 元，请计算打折的折扣比例。"
        result = (a - b) / a * 100

    return {
        "text": f"### Human: {problem_text}\n### Assistant: {result}"
    }

def generate_area_problem():
    length = random.randint(1, 100)
    width = random.randint(1, 100)
    area = length * width

    problem_text = f"一个长方形的长为 {length} 厘米，宽为 {width} 厘米，请计算其面积。"

    return {
        "text": f"### Human: {problem_text}\n### Assistant: 面积为 {area} 平方厘米"
    }

def generate_fraction_simplification_problem():
    numerator = random.randint(1, 9)
    denominator = random.randint(numerator + 1, 10)

    problem_text = f"将分数 {numerator}/{denominator} 进行简化。"

    gcd = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd

    return {
        "text": f"### Human: {problem_text}\n### Assistant: 最简化的形式为：{simplified_numerator}/{simplified_denominator}"
    }

def generate_mass_problem():
    density = random.randint(1, 10)
    volume = random.randint(1, 10)
    
    mass = density * volume

    problem_text = f"某物体的密度为 {density} 克/立方厘米，体积为 {volume} 立方厘米，请计算该物体的质量。"

    return {
        "text": f"### Human: {problem_text}\n### Assistant: {mass} 克"
    }

def format_problem_text(problem):
    problem_text = problem["text"]
    problem_text_no_newline = problem_text.replace("\n", "")
    return problem_text_no_newline

def write_to_json(problems, filename):
    formatted_problems = [format_problem_text(problem) for problem in problems]
    with open(filename, 'w', encoding='utf-8') as f:
        for problem in formatted_problems:
            f.write(f'{{"text": "{problem}"}}\n')
num_problems = 10000
filename = "math_problems.json"

problems = generate_math_problems(num_problems)

write_to_json(problems, filename)

print(f"生成了 {num_problems} 个问题，并将其保存在 {filename} 文件中。")
