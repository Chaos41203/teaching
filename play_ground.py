num_list = []
target_odd_num = list(range(1, 101, 2))
target_even_num = range(0, 101, 2)

print(target_odd_num)

for i in range(len(target_odd_num)):
    
    print("編號 ", i)
    
    if i == 25:
        
        after = target_odd_num[i] + 1
        print("數字 : *", after)
        print("===================================================")
        
        target_odd_num[i] = after
        break
        
    else:
        
        print("數字 : ", target_odd_num[i])
        print("===================================================")
        
print(target_odd_num)