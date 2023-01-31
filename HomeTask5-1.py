line = "фцдщвабв абв- abb флоырв: ловрывылваб, ыоврповырп абв?"
combination = "абв"
line_arr = line.split()
print(line_arr)
for i in range(len(line_arr)):
    if combination and "," in line_arr[i]:
         line_arr[i] = ','
    if combination and ";" in line_arr[i]:
         line_arr[i] = ';'
    if combination and "." in line_arr[i]:
         line_arr[i] = '.'
    if combination and ":" in line_arr[i]:
         line_arr[i] = ':'
    if combination and "?" in line_arr[i]:
         line_arr[i] = '?'
    if combination and "!" in line_arr[i]:
         line_arr[i] = '!'
    if combination and "-" in line_arr[i]:
         line_arr[i] = '-'
print(' '.join(line_arr))
