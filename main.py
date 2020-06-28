from Bplustree import Bplustree
import csv
fn = "C:/Users/user/PycharmProjects/bptree/output_big5.csv"
# output_big5.csv
# test.csv


def build(a, b):
    with open(fn) as csvFile:
        csv_reader = csv.reader(csvFile)
        lists = list(csv_reader)
    csvFile.close()
    lists.remove(lists[0])
    #print(lists)
    new_tree = Bplustree()
    dicts = new_tree.merge_data(lists, a, b)
    for i in dicts:
        print(i)
        print(dicts[i])
        ll=[]
        ll.append(str(i))
        new_tree.sett(ll, dicts[i])
    return new_tree

# print(dicts)
# print("B+tree create complete")

# ins = str(input())
# ser = []
# ser.append(ins)
# print(dicts[tree.get(ser)])


aa = 0
while True:
    # c = "BPlusTree no exist"
    if aa == 0:
        tree = build(0, 1)
        c = "BPlusTree Build Complete (Default)(Sort By StudentID)"
        aa = 3
    if aa == 1:
        c = "BPlusTree Build Complete (Sort By StudentID)"
    elif aa == 2:
        c = "BPlusTree Build Complete (Sort By CourseID)"
    print(c)
    print("What are you want to do?")
    print("1. Insert data")
    print("2. Delete data")
    print("3. build BPlusTree by StudentID")
    print("4. build BPlusTree by CourseID")
    print("5. search")
    print("6. Exit")
    # print(type(tree))
    choose = input()
    if choose == "1":
        print("Insert")
        key = input()
        value = input()
        ll = []
        ll.append(key)
        tree.sett(ll, value)  # set data to B+tree
        tree.insert(key, value)  # add data to dicts
    elif choose == "2":
        key = input()
        ll =[]
        ll.append(key)
        print("Delete ", key, "all data?(y/n)")
        scan = input().upper()
        if scan == "Y":
            tree.remove_item(ll)  # remove item in B+tree
        elif scan == "N":
            print("input:")
            value = input()
            # print(type(tree.dicts[key]))
            tree.dicts[key].remove(value)  # remove data in dicts
        else:
            print("incorrect command!!!")
    elif choose == "3":
        print("build")
        tree = build(0, 1)
        a = "BPlusTree Build Complete (Sort By StudentID)"
        aa = 1
        print()
    elif choose == "4":
        print("build")
        tree = build(1, 0)
        a = "BPlusTree Build Complete (Sort By CourseID)"
        aa = 2
        print()
    elif choose == "6":
        break
    elif choose == "5":
        print("search")
        ins = str(input())
        ser = []
        ser.append(ins)
        try:
            lisss = tree.get(ser)
            print(lisss)
        except ValueError:
            print(ins, "is not in list")

    else:
        print("incorrect command!!!")

