import csv


def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):
    """Get data from a file. The file is assumed to be a csv.

    Parameters
    ----------
    file_name : str
        The name of a csv.

    query_column : int
        The index of a column to search for a value of. Optional.

    query_value : Various
        The value to search for. Required with query_column.

    return_header : Bool
        Option to return the header of the file.


    Returns
    -------
    results
        List of lists of various types from the file, matching
        query_value if specified.

    """

    # Need bothcolumn and value to proceed
    if (query_column is None) != (query_value is None):
        raise ValueError(
            "query_column and query_value must both be provided or None"
        )

    with open(file_name, mode='r', encoding='utf-8', newline='') as file:

        reader = csv.reader(file)

        # Strips the header. Discards if return_header is false.
        header = next(reader)

        results = []

        if return_header:
            results.append(header)

        # Simple loop. If query is specified, breaks loop when condition fails.
        for row in reader:
            if query_column is not None and row[query_column] != query_value:
                continue

            results.append(row)

    return results


def get_column_index(header, column_name):
    """Get the index of a value of a list. Specifically for lists
    of strings.

    Parameters
    ----------
    header : list
        List to search for column_name in.

    column_name : str
        Value to find the index of in header.


    Returns
    -------
    index
        Int position of column_name in header.

    """

    if not isinstance(column_name, str):
        raise TypeError("Column Name must be string")

    if not isinstance(header, list):
        raise TypeError("Header Name must be list")

    index = header.index(column_name)

    return index


def get_fire_gdp_year_data(co2_file, gdp_file, country):
    """Matches years with co2 emissions data with appropriate GDP
    for countries in files.

    Assumes certain aspects of the csv files, like their headers containing
    certain values and columns. Not generalizable.

    Parameters
    ----------
    co2_file : str
        Path to a csv file containing a column called Year and a column called
        Forest fires. Rows represent a year.

    gdp_file : str
        Path to a csv file containing gdps of countries. Columns
        represent years.

    country : str
        Country to search for inside both csv tables.


    Returns
    -------
    data
        List of lists of int (year), float (CO2 from fires), and float (gdp).

    """

    co2Data = get_data(co2_file, 0, country, True)

    gdpData = get_data(gdp_file, 0, country, True)

    firesIndex = get_column_index(co2Data[0], "Forest fires")

    yearIndex = get_column_index(co2Data[0], "Year")

    data = []

    # co2Data has a header, so discard it before running loop
    for row in co2Data[1:]:
        year = row[yearIndex]
        fires = row[firesIndex]
        gdpIndex = get_column_index(gdpData[0], year)
        # gdpData has a header too
        gdp = gdpData[1][gdpIndex]
        if gdp:
            data.append([int(year), float(fires), float(gdp)])

    return data
