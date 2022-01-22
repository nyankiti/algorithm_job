numbers = input()

result = int(numbers[0] + numbers[1] + numbers[2]) + int(numbers[1] +
                                                         numbers[2] + numbers[0]) + int(numbers[2] + numbers[0] + numbers[1])

print(result)
