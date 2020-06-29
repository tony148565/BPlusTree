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
    # print(lists)
    new_tree = Bplustree()
    dicts = new_tree.merge_data(lists, a, b)
    for k in lists:
        if k[1] in new_tree.course_name:
            continue
        else:
            new_tree.course_name[k[1]] = k[2]
    for i in dicts:
        # print(i)
        # print(dicts[i])
        ll=[]
        ll.append(str(i))
        new_tree.sett(ll, dicts[i])
    print(new_tree.course_name)
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
        # li = []
        # li.append(value)
        # set data to B+tree
        if value not in tree.course_name:
            print("this course is new course")
            print("please type the course name")
            new_course = input()
            tree.course_name[value] = new_course
        tree.insert(key, value)  # add data to dicts
        tree.sett(ll, tree.dicts[key])
    elif choose == "2":
        key = input()
        ll = []
        ll.append(key)
        print("Delete ", key, "all data?(y/n)")
        scan = input().upper()
        if scan == "Y":
            try:
                tree.remove_item(ll)  # remove item in B+tree
                if aa == 2:
                    print("Do you want to remove this course", key, "(y/n)?")
                    sc = input()
                    if sc == "y":
                        del tree.course_name[key]
            except ValueError:
                print(key, "is not in list")
        elif scan == "N":
            print("type studentID or CourseID:")
            value = input()
            print(type(tree.dicts[key]))
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
        print("type studentID or CourseID")
        ins = str(input())
        ser = []
        ser.append(ins)
        try:
            lisss = tree.get(ser)
            print(lisss)
            for i in lisss:
                print(i, " ", tree.course_name[i])
        except ValueError:
            print(ins, "is not in list")
    else:
        print("incorrect command!!!")

