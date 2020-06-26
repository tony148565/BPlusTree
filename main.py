from Bplustree import Bplustree
import csv
fn = "C:/Users/user/PycharmProjects/bptree/test.csv"

with open(fn) as csvFile:
    csv_reader = csv.reader(csvFile)
    lists = list(csv_reader)
csvFile.close()
tree = Bplustree()
for i in lists:
    ll=[]
    ll.append(i[0])
    tree.sett(ll, i[1])

print("B+tree create complete")

ins = str(input())
ser = []
ser.append(ins)
print(tree.get(ser))

