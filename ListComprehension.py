if __name__ == '__main__':
    print(sum([i ** 2 if i % 2 else -(i ** 2) for i in range(1, 11)]))
