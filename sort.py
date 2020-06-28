# coding=Big5
import csv
fn = "C:/Users/user/Downloads/DB_students_tc_big5.csv"

with open(fn) as csvFile:
    csv_reader = csv.reader(csvFile)
    lists = list(csv_reader)

title = lists[0]
title.append("id")
li = [title]

lists.remove(lists[0])
lists.sort()

count = 1
for i in lists:
    i.append(count)
    li.append(i)
    count = count + 1

out = open('output_big5.csv', 'w', newline='')
oo = csv.writer(out)
oo.writerows(li)
out.close()

