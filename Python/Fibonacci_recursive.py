# Create fibonacci sequence based on input (list containing starting int) and stops before a provided max number


def fib(seq, max_num):
    if len(seq) == 1:
        seq.append(seq[0])
    while seq[-1] + seq[-2] < max_num:
        seq.append(seq[-1] + seq[-2])
        fib(seq, max_num)
    return seq


print(fib([1], 10000))