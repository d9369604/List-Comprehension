def sequence_square_sum():
    return sum([i ** 2 if i % 2 else -(i ** 2) for i in range(1, 11)])


if __name__ == '__main__':
    print sequence_square_sum()
