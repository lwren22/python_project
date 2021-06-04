import csv


def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data


def run():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    print('Total sales: {}'.format(total))


def sales_changes():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    current_month = month-1
    last_month = month-2
    next_month = month

    current_sales = sales[current_month]
    last_sales = sales[last_month]
    next_sales = sales[next_month]

    last_change = current_sales - last_sales
    last_fraction = last_change / last_sales
    from_last_month = int(last_fraction * 100)
    positive_from_last_month = from_last_month * -1

    next_change = current_sales - next_sales
    next_fraction = next_change / next_sales
    from_next_month = int(next_fraction * 100)
    positive_from_next_month = from_next_month * -1

    last_increase = "Sales were {}% more than the previous month".format(from_last_month)
    last_decrease = "Sales were {}% less than the previous month".format(positive_from_last_month)
    next_increase = "Sales were {}% more than the next month".format(from_next_month)
    next_decrease = "Sales were {}% less than the next month".format(positive_from_next_month)

    if month == 1 and from_next_month >= 0:
        print(next_increase)
    elif month == 1 and from_next_month < 0:
        print(next_decrease)
    elif month == 12 and from_last_month >= 0:
        print(last_increase)
    elif month == 12 and from_last_month < 0:
        print(last_decrease)
    elif from_next_month >= 0 and from_last_month >= 0:
        print(last_increase)
        print(next_increase)
    elif from_next_month >= 0 and from_last_month < 0:
        print(last_decrease)
        print(next_increase)
    elif from_next_month < 0 and from_last_month >= 0:
        print(last_increase)
        print(next_decrease)
    elif from_next_month < 0 and from_last_month < 0:
        print(last_decrease)
        print(next_decrease)


def exp_changes():
    data = read_data()

    expenditures = []
    for row in data:
        expenditure = int(row['expenditure'])
        expenditures.append(expenditure)

    current_month = month-1
    last_month = month-2
    next_month = month

    current_expenditures = expenditures[current_month]
    last_expenditures = expenditures[last_month]
    next_expenditures = expenditures[next_month]

    last_change = current_expenditures - last_expenditures
    last_fraction = last_change / last_expenditures
    from_last_month = int(last_fraction * 100)
    positive_from_last_month = from_last_month * -1

    next_change = current_expenditures - next_expenditures
    next_fraction = next_change / next_expenditures
    from_next_month = int(next_fraction * 100)
    positive_from_next_month = from_next_month * -1

    last_increase = "Expenditures were {}% more than the previous month".format(from_last_month)
    last_decrease = "Expenditures were {}% less than the previous month".format(positive_from_last_month)
    next_increase = "Expenditures were {}% more than the next month".format(from_next_month)
    next_decrease = "Expenditures were {}% less than the next month".format(positive_from_next_month)

    if month == 1 and from_next_month >= 0:
        print(next_increase)
    elif month == 1 and from_next_month < 0:
        print(next_decrease)
    elif month == 12 and from_last_month >= 0:
        print(last_increase)
    elif month == 12 and from_last_month < 0:
        print(last_decrease)
    elif from_next_month >= 0 and from_last_month >= 0:
        print(last_increase)
        print(next_increase)
    elif from_next_month >= 0 and from_last_month < 0:
        print(last_decrease)
        print(next_increase)
    elif from_next_month < 0 and from_last_month >= 0:
        print(last_increase)
        print(next_decrease)
    elif from_next_month < 0 and from_last_month < 0:
        print(last_decrease)
        print(next_decrease)


def min_max():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    months = []
    for row in data:
        all_months = row['month']
        months.append(all_months)

    min_sales = min(sales)
    max_sales = max(sales)

    min_position = sales.index(min(sales))
    min_month = months[min_position].title()

    max_position = sales.index(max(sales))
    max_month = months[max_position].title()

    min_words = "{} had the minimum sales with {}".format(min_month, min_sales)
    max_words = "{} had the maximum sales with {}".format(max_month, max_sales)
    print("{} and {}".format(min_words, max_words))


run()

min_max()

month = int(input("Which month would you like to know about? (1-12) "))

sales_changes()

exp_changes()