numbers = [[1,2,3], [4,5,6], [7,8,9]]
result = []
for row in numbers:
    for element in row:
        if element % 2 == 0:
            result.append(element)
print(result)
