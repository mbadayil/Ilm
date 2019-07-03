import csv

with open('csv1.csv','r') as f1:
    csv_read=csv.reader(f1)
    #next(csv_read)
    with open('csv2.csv','w')as f2:
        csv_write=csv.writer(f2,delimiter='\t')

        for line in csv_read:
            csv_write.writerow(line)
