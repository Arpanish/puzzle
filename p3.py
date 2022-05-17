import csv
f = open(r"C:\Users\ap\Desktop\pop.csv.csv", 'r')
with f:
     reader = csv.DictReader(f)
     for row in reader:
        temp = [  ]
        for col in reader:
            c = col["District"]
            a = float(col["Total number of registered voters"])
            b = float(col["Total population"])
            ratio = (a / b) * 100
            last = (ratio,c)
            thisdict = {}
            thisdict.update({"ratio": ratio})
            thisdict.update({"district":c})
            temp.append(thisdict)
        least = temp[0]["ratio"]
        dis  = temp[0]["district"]
        for item in temp:
            if least>item["ratio"]:
                least = item["ratio"]
                dis = item["district"]
        print(least)
        print(dis)
           