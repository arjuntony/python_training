import csv
data = []


def inventory_cost(filename):
    with open(filename) as obj1:
        read1 = csv.reader(obj1)
        row0 = read1.next()
        row0.append('Total_Cost')
        for item in read1:
            item.append (str(int(item[1]) * float(item[2])))
            data.append(item)

        with open('inventory_with_cost.csv', 'w') as obj2:
            write1 = csv.writer(obj2)
            write1.writerow(row0)
            for i in data:
                write1.writerow(i)
        total_cost = 0
        for i in data:
            total_cost = total_cost+float(i[3])

    print("Total Cost is {}". format(total_cost))


def main():
    filename = raw_input(str("Please Enter the File Name with extension: "))
    inventory_cost(filename)


if __name__ == '__main__':
    main()
