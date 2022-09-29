import csv



with open("Employees.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line =0
    for row in csv_reader:
        if line==0:
            line+=1
            continue
        else:
            #TODO impliment
            break
