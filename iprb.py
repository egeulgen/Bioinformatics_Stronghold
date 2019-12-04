import sys


if __name__ == "__main__":
    k, m, n = [float(x) for x in sys.stdin.read().splitlines()[0].split(' ')]
    total = k + m + n
    print((2 * k * m + 2 * k * n + k * (k - 1) + m * n + m * (m - 1) * 3/4) / (total * (total-1)))