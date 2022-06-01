def required_factors(factors_1num, factors_2num):
    required_factors_hcf = []
    required_factors_lcm = []
    complete_factors = factors_1num+factors_2num
    for item in factors_1num:
        if item in factors_2num:
            required_factors_hcf.append(item)
            factors_2num.remove(item)
    for item in required_factors_hcf:
       complete_factors.remove(item)
    required_factors_lcm.extend(complete_factors)
    return required_factors_lcm, required_factors_hcf


def prime_factors_calculation(n):
    prime_factors = []
    while (n % 2 == 0):
        n = n / 2
        prime_factors.append(2)
    for i in range(3, int(n/2), 2):
        while (n % i == 0):
            n = n / i
            prime_factors.append(i)
    if n > 2:
        prime_factors.append(int(n))
    return prime_factors


def lcm_n_hcf_calculation(num1, num2):
    prime_factors_num1 = prime_factors_calculation(num1)
    prime_factors_num2 = prime_factors_calculation(num2)
    lcm_factors, hcf_factors = required_factors(
        prime_factors_num1, prime_factors_num2)
    lcm = 1
    hcf = 1
    for item in lcm_factors:
        lcm *= item
    for item in hcf_factors:
        hcf *= item
    return lcm, hcf


if __name__ == "__main__":
    num1 = int(input("first number ="))
    num2 = int(input("second number ="))
    lcm, hcf = lcm_n_hcf_calculation(num1, num2)
    print(f"lcm and hcf of {num1}and{num2} are lcm:{lcm},hcf:{hcf}")
