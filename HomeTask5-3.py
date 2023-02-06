line_original = "11122223"
line1 = list(line_original)
print(line1)
line_result = []
i = 0
count = 1
for i in range(len(line1)):
    if line1[i+1] == line1[i]:
        print("count -", count)
        count = count+1
    line_result.append(count)
    line_result.append(line1[i])
    #i = i + 1
print(line_result)