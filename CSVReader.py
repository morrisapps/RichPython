import csv  # Import python csv library to read csv
from rich.console import Console  # API Library - Rich terminal text
from rich.table import Table  # API Library - Rich terminal text
from CSVRow import CSVRow  # Class representing each row of the CSV file

"""
This program retrieves information form covid190download.csv and displays the first 5 rows in a table formate
By Corey Morris
"""

def create_table_csv():
    '''
    Reads properties from covid19-download.csv and displays the first 5 rows of properties in a table
    '''
    try:
        with open('covid19-download.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips headers
            rows = []
            console = Console()
            table = Table(show_header=True, header_style="bold yellow")
            table.add_column("pruid", width=20)
            table.add_column("prname", width=22)
            table.add_column("prnameFR", width=22)
            table.add_column("date", width=22)
            table.add_column("numconf", width=10)
            table.add_column("numprob", width=10)
            table.add_column("numdeaths", width=10)
            table.add_column("numtotal", width=10)
            table.add_column("numtoday", width=10)
            table.add_column("ratetotal", width=10)

            for row in range(5):  # Loops through each row 5 times
                row = next(reader)
                csvRow = CSVRow(row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[13],
                                row[15])  # Add properties to CSVRow object representing the row in the CSV file
                rows.append(csvRow)
            for row in rows:  # Iterates through each row then calls CSVRow print function for that object's instance
                row.get_table_row(table)  # Calls function get_table_row in each CSVRow object to append a new table row
            console.print(table)
    except FileNotFoundError as error:  # Exception handler for csv file missing
        print(str(error) + " in the root directory of the program")
    print('By Corey Morris')


create_table_csv()  # Start the application
