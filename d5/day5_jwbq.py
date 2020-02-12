for num_cock in range(1,100):    
    for num_hen in range(1,100):       
        if 14*num_cock+8*num_hen-200 == 0 and 100-num_hen-num_cock >=0:            
            print('公鸡',num_cock,'只，母鸡',num_hen,'只','小鸡',100-num_hen-num_cock,'只')