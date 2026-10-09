import csv

def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):

    with open(file_name, mode='r', encoding='utf-8', newline='') as file:

        reader = csv.reader(file)

        header = next(reader)

        results = []

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
    pass

