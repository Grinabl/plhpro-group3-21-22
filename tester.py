number_range = 64
for i in range(7):
        
    for j in range(number_range):
        if (number_range == 64) :
            external = j // 4 + 1
            internal_num = j % 4 + 1
            p_internal_num = 1 if (internal_num == 1 or internal_num == 2) else 2
            print(str(i + 1) + '.' + str(external) + '.'  + str(internal_num) + '\t--> ' + str(i + 2) + '.' + str(external) + '.' + str(p_internal_num))
        elif (number_range == 32) :
            external = j // 2 + 1
            internal_num = j % 2 + 1
            print(str(i + 1) + '.' + str(external) + '.'  + str(internal_num) + '\t--> ' + str(i + 2) + '.' + str(external) + '.1')
        elif (number_range == 16) :
            external = j + 1
            internal_num = 1
            p_external = (external + 1) // 2 if external % 2 == 1 else external // 2   
            print(str(i + 1) + '.' + str(external) + '.'  + str(internal_num) + '\t--> ' + str(i + 2) + '.' + str(p_external))
        elif (number_range == 8) :
            external = j + 1
            p_external = (external + 1) // 2 if external % 2 == 1 else external // 2   
            print(str(i + 1) + '.' + str(external)+ '\t--> ' + str(i + 2) + '.' + str(p_external))
        elif (number_range == 4) :
            external = j + 1
            p_external = (external + 1) // 2 if external % 2 == 1 else external // 2   
            print(str(i + 1) + '.' + str(external)+ '\t--> ' + str(i + 2) + '.' + str(p_external))
        elif (number_range == 2) :
            external = j + 1
            print(str(i + 1) + '.' + str(external) + '\t--> ' + "7.1")
        else:
            print("7.1")


    number_range = number_range // 2

# 1.1.1
# 1.1.2   2.1.1
# 1.1.3
# 1.1.4   2.1.2   3.1.1

# 1.2.1
# 1.2.2   2.2.1
# 1.2.3
# 1.2.4   2.2.1   3.2.1   4.1