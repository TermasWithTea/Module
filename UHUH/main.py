from fake_math import devide as fake_math
from true_math import devide as true_math


def main():
    num = 10
    result_fake = fake_math(num, 0)
    result_true = true_math(num, 0)



print(f'Результат (fake_math):{fake_math}')
print(f'Резульат (true_math):{true_math}')
result1 = fake_math(69, 3)
result2 = fake_math(3, 0)
result3 = true_math(49, 7)
result4 = true_math(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

if __name__ == '__main__':
    main()