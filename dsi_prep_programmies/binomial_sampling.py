from random import choice

def get_bit():
    return choice([0,1])

def generate_n_bits(n=12):
    lst = []
    for _ in range(n):
        lst.append(get_bit())
    return lst

def binary_sampling_dict(n_bits, num_samples=500):
    d = {}

    for _ in range(num_samples):
        binary = generate_n_bits(n=n_bits)
        sum_bits = sum(binary)

        if sum_bits not in d:
            d[sum_bits] = 0
        d[sum_bits] += 1

    return d

d = binary_sampling_dict(12, num_samples=10000)

for k, v in sorted(d.items()):
    print(f' {k}: {v}')