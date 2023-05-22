#python中生成随机整数、随机小数、0--1之间小数方法
import random

def generate_random_numbers():
    # 生成随机整数
    random_int = random.randint(1, 100)
    
    # 生成随机小数
    random_float = random.uniform(0, 1)
    
    # 生成 0 到 1 之间的随机小数
    random_float_0_to_1 = random.random()
    
    # 打印生成的随机数
    print("随机整数:", random_int)
    print("随机小数:", random_float)
    print("0到1之间的随机小数:", random_float_0_to_1)

# 调用生成随机数的函数
generate_random_numbers()
