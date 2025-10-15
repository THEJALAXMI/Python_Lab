def Even_PerfectSq(start, end):
    evenSq = []
    for num in range(start, end + 1):
        # Check if all digits are even
        if all(int(digit) % 2 == 0
               for digit in str(num)):
           # Check if the number is a perfect square
           sqrt = int(num ** 0.5)
           if sqrt * sqrt == num:
               evenSq.append(num)
    return evenSq
start = 1000
end = 9999
result = Even_PerfectSq(start, end)
print(result)
