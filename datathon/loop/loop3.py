#Repititive Problem 2

term = int(input('Specify a term in a Fibonacci Sequence: '))


def fibonacci_sequence(term):
    fib_sequence = [0, 1]
    for i in range(2, term):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)
    return fib_sequence

fib_sequence = fibonacci_sequence(term)

print("Fibonacci sequence:")
for t in fib_sequence:
    print(t, end=" ")
