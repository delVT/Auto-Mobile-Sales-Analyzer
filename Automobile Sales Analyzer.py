


def get_data(filename, model):
    file = open(filename, "r")
    prices = []
    for line in file:
        if line[0].lower()== model:
            prices.append(int(line[2:]))
    return prices


def count_range(price_lst, minimum, maximum):
    count = 0
    for number in price_lst:
        if minimum <= number <= maximum:
            count += 1
    return count


def main():
    print()
    print("Welcome to the Automobile Sales Analyzer!")
    print()
    filename_ = input("Enter the name of the data file:")
    notation = 'n'
    print()
    print('New Automobiles')
    new = get_data(filename_, notation)
    print('\tTotal number sold:', +str(len(new)))
    low = count_range(new, 0, 35000)
    print('\tUnder 35K:' + str(low))

    between_ = count_range(new, 35000, 50000)
    print('\t35K to 50K:' + str(between_))

    high = count_range(new, 50000, 10000000000)
    print('\tOver 50K:' + str(high))

    total_sales = sum(new)
    average = int(total_sales / len(new))

    print('\tTotal sales: ' + str(total_sales))
    print('\tAverage:' +  str(average))
    print('\t')
    notation = 'u'
    print('Used Automobiles')
    used = get_data(filename_, 'u')
    print('\tTotal number sold:', +str(len(used)))
    low = count_range(used, 0, 35000)
    print('\tUnder 12K:' + str(low))

    between_ = count_range(used, 12000, 25000)
    print('\t12K to 25K:' + str(between_))

    high = count_range(used, 25000, 10000000000)
    print('\tOver 25K:' + str(high))

    total_sales = sum(used)
    average = int(total_sales / len(used))

    print('\tTotal sales: ' + str(total_sales))
    print('\tAverage:' + str(average))

    print('Thanks for using the Automobile Sales Analyzer!')


if __name__ == '__main__':
    main()






