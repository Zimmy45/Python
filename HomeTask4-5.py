pol1 = "12*x**4+5*x**3+1*x**2+15"
pol2 = "12*x**4+5*x**3+1*x**2+1*x**1+15"
pol1 = pol1.split("+")
pol2 = pol2.split("+")

print(pol1)
print(pol2)

for indx, value in enumerate(pol1):
    pol1[indx] = list(map(int,value.split('*x**')))

print(pol1)

for indx, value in enumerate(pol2):
    pol2[indx] = list(map(int,value.split('*x**')))

print(pol2)

pol3 = pol1 + pol2
print(pol3)

pol3 = sorted(pol3, key=lambda x: x[1] if len(x) > 1 else 0, reverse = True)
print(pol3)
pol4 = []
cur_indx = 0
while cur_indx < len(pol3)-1:
    cur_num = pol3[cur_indx]
    next_num = pol3[cur_indx+1]
    if len(cur_num)>1 and len(next_num)>1:
        if cur_num[1] == next_num[1]:
            sum_koeff = cur_num[0]+next_num[0]
            pol4.append([sum_koeff, cur_num[1]])
            cur_indx+=1
        else:
            pol4.append([pol3, cur_indx])
    if len(cur_num)>1 and len(next_num)==1:
        pol4.append([pol3, cur_indx])
    if len(cur_num)==1 and len(next_num)==1:
        pol4.append([cur_num[0]+next_num[0]])
    
    cur_indx+=1
    
print(pol4)