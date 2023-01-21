dividend = []
for i in range(int(input("Please enter the power of the dividend: ")) + 1):
    dividend.append(int(input(f"Term #{i + 1}: ")))
divisor = []
for i in range(int(input("Please enter the power of the divisor: ")) + 1):
    divisor.append(int(input(f"Term #{i + 1}: ")))

solution = []
for i in range(len(dividend)):
    if dividend[i] == 0 or divisor[0] == 0:
        solution.append(0)
        continue
    solution.append(dividend[i] / divisor[0])
    for j in range(1, len(divisor)):
        if i + j >= len(dividend):
            break
        dividend[i + j] -= divisor[j] * solution[len(solution) - 1]
print(f"Solution: {solution}")
