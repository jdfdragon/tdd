import csv


def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):

    if (query_column is None) != (query_value is None):
        raise ValueError(
            "query_column and query_value must both be provided or None"
        )

    with open(file_name, mode='r', encoding='utf-8', newline='') as file:

        reader = csv.reader(file)

        header = next(reader)

        results = []

        if return_header:
            results.append(header)

        for row in reader:
            if query_column is not None and row[query_column] != query_value:
                continue

            results.append(row)

    return results


def get_column_index(header, column_name):

    if not isinstance(column_name, str):
        raise TypeError("Column Name must be string")

    if not isinstance(header, list):
        raise TypeError("Header Name must be list")

    return header.index(column_name)


def get_fire_gdp_year_data(co2_file, gdp_file, country):

    co2Data = get_data(co2_file, 0, country, True)

    gdpData = get_data(gdp_file, 0, country, True)

    firesIndex = get_column_index(co2Data[0], "Forest fires")

    yearIndex = get_column_index(co2Data[0], "Year")

    data = []

    for row in co2Data[1:]:
        year = row[yearIndex]
        fires = row[firesIndex]
        gdpIndex = get_column_index(gdpData[0], year)
        gdp = gdpData[1][gdpIndex]
        if gdp:
            data.append([int(year), float(fires), float(gdp)])

    return data
