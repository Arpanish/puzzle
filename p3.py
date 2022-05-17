import csv
with open(r"C:\Users\ap\Desktop\pop.csv.csv",'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    # for row in spamreader:
    #     print(', '.join(row))
    for row in spamreader:
        temp = [  ]
        for col in spamreader:
            c = col[0]
            a = float(col[1])
            b = float(col[2])
            # print(f"{a} , {b} , {c}")
            ratio = (a / b) * 100
            # c = col[0]
            temp.append(ratio)
            # temp.append(col[0])
            # print(f"{ratio} , {c}")
            last = (ratio,c)
            print(f"{last[0]} , {last[1]}")
             
        print(temp)   
        data = min(temp)
        
    
print(f"Minimum ratio is {data} of {c} district")

        