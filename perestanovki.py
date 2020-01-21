# Генерация всех перестановок чисел от 0 до N в массивах размера M


def generate_numbers(N, M, prefix=None):
    if M == 0:
        print(prefix)
        return 0
    prefix = prefix or []
    for n in range(N):
        prefix.append(n)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


generate_numbers(2, 4)
