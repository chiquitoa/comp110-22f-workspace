"""Dictionary related utility functions."""

__author__ = "730295419"

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a CSV of data into a list of dicts to create a table."""
    from csv import DictReader

    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return (result)


def column_values(table: list[dict[str, str]], search: str) -> list[str]:
    """Produce a list of all the values in a single column whose name matches a search."""
    search_matches: list[str] = []
    for column in table:
        for item in column:
            if search in item:
                search_matches.append(column[item])
    return (search_matches)


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into a dictionary of columns."""
    new_dict: dict[str, list[str]] = {}
    key: list = []
    key = (table[0].keys())
    for x in key:
        new_dict[x] = column_values(table, x)
    return (new_dict)


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    shortie: dict[str, list[str]] = {}
    for column in table:
        n_items: list = []
        x: int = 0
        while x < rows and x < len(table):
            n_items.append(table[column][x])
            x += 1
        shortie[column] = n_items
    return (shortie)


def select(table: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    shortie: dict[str, list[str]] = {}
    for column in copy:
        shortie[column] = table[column]
    return (shortie)


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    longie: dict[str, list[str]] = {}
    for column in table1:
        longie[column] = table1[column]
    for column in table2:
        if column in longie:
            longie[column] += table2[column]
        else:
            longie[column] = table2[column]
    return (longie)


def count(what: list[str]) -> dict[str, int]:
    """Given a list of columns to count, provides a dictionary denoting how many of each unique value exists in each column."""
    counts: dict[str, int] = {}
    for item in what:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return (counts)