import csv


def read_data():
    data = []

    with open('GlobalLandTemperaturesByCountry.csv', 'r') as GlobalLandTemperaturesByCountry_csv:
        spreadsheet = csv.DictReader(GlobalLandTemperaturesByCountry_csv)
        for row in spreadsheet:
            data.append(row)

    return data


def run():
    data = read_data()

    countries = []
    for row in data:
        available_countries = row["Country"]
        countries.append(available_countries)

    all_countries = list(dict.fromkeys(countries))

    for right_country in all_countries:
        found = []
        for index, suspect in enumerate(countries):
            if right_country == suspect:
                found.append(index)
        first = found[0]
        last = found[-1]

        temps = []
        for row in data:
            all_temps = row["AverageTemperature"]
            temps.append(all_temps)
        right_temps = []
        for temp in temps:
            if first <= last:
                each_temps = temps[first]
                right_temps.append(each_temps)
                first = first + 1
        spaceless_temps = [i for i in right_temps if i]
        if not spaceless_temps:
            all_countries.remove(right_country)
    with open('right_countries.txt', 'w+') as text_file:
        for name in all_countries:
            text_file.write(name)
            text_file.write('\n')
    with open('all_countries.txt', 'w+') as text_file:
        for name in countries:
            text_file.write(name)
            text_file.write('\n')


def right_countries():
    with open('right_countries.txt', 'r') as text_file:
        all_countries = [line.strip() for line in text_file]
        print('The available countries are: {}'.format(all_countries))
    return all_countries


def saved_countries():
    with open('all_countries.txt', 'r') as text_file:
        countries = [line.strip() for line in text_file]
    return countries


def country():
    data = read_data()

    all_countries = right_countries()

    countries = saved_countries()

    chosen_country = input("Which country would you like to see data for? ").title()
    if chosen_country in countries:
        found = []
        for index, suspect in enumerate(countries):
            if chosen_country == suspect:
                found.append(index)
        first = found[0]
        first_two = found[0]
        last = found[-1]
        last_two = found[-1]

        dates = []
        for row in data:
            all_dates = row["dt"]
            dates.append(all_dates)

        right_dates = []

        for date in dates:
            if first <= last:
                each_dates = dates[first]
                right_dates.append(each_dates)
                first = first + 1

        temps = []
        for row in data:
            all_temps = row["AverageTemperature"]
            temps.append(all_temps)
        right_temps = []
        for temp in temps:
            if first_two <= last_two:
                each_temps = temps[first_two]
                right_temps.append(each_temps)
                first_two = first_two + 1

        spaceless_temps = [i for i in right_temps if i]
        float_temps = [float(i) for i in spaceless_temps]
        max_temp = max(float_temps)
        string_max_temp = str(max_temp)
        max_position = right_temps.index(string_max_temp)
        max_date = right_dates[max_position]

        spaceless_temps = [i for i in right_temps if i]
        float_temps = [float(i) for i in spaceless_temps]
        min_temp = min(float_temps)
        string_min_temp = str(min_temp)
        min_position = right_temps.index(string_min_temp)
        min_date = right_dates[min_position]

        print("The min temp is {} and occurred on {}".format(min_temp, min_date))
        print("The max temp is {} and occurred on {}".format(max_temp, max_date))

    else:
        print("That country is not available")


country()
