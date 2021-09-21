import csv  # Import python csv library to read csv
from model.Covid19Record import Covid19Record  # Represents record(s) of the CSV file


class Datastore:
    """
    This class is responsible for all retrieving and storing of records for the Covid19-download CSV
    By Corey Morris
    ...

    Attributes
    ----------
    _FILE_NAME : str
        (private) The CSV file name that is stored on disk

    Methods
    -------
    getAll()
        Gets all records from Covid19-download.csv

    getRecord(id)
        Returns record representing a row in the CSV that also matches the given ID.

    loadRecordsFromFIle()
        Returns an array of records from CSV file

    insertAll(records)
        Insert the provided records into data store

    insertRecord(record)
        Inserts the single record into data store

    updateRecord(record)
        Updates the single record in the data store

    deleteRecord(record)
        Deletes the single record from the data store

    saveDataToFile(name, records):
        Saves the given records to file and names the file with the given name
    """

    def __init__(self):
        """
        Instantiates _FILE_NAME - The name and relative location of Covid19 CSV file

        Parameters
        ----------
        _FILE_NAME : string
            The name and relative location of CSV file
        """
        self._FILE_NAME = "../covid19-download.csv"

    def getAll(self):
        """
        Gets all records from Covid19-download.csv

            Returns:
                The array that contains all records
        """
        return self.loadRecordsFromFile()

    def insertAll(self, records):
        """
        Insert records into data store
        Not yet Implemented
        """

    def getRecord(self, id):
        """
        Returns record matching given id.

            Returns:
                The record matching id from covid19-download
        """
        returnRecord = ''  # Set variable to a blank string. This is to signal if no records match id
        for r in self.getAll():
            if str(r.id) == str(id):
                returnRecord = r
        return returnRecord

    def insertRecord(self, record):
        """
        Inserts the single record into data store
        """

    def updateRecord(self, record):
        """
        Updates the single record in the data store
        """

    def deleteRecord(self, record):
        """
        Deletes the single record from the data store
        """

    def loadRecordsFromFile(self):
        """
        Reads properties from CSV and returns an array of each record(row)

            Returns:
                records: An array of records from Covid19-download CSV
        """
        try:
            with open(self._FILE_NAME, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skips headers
                records = []

                rowId = 0  # Used to create unique ids for each row
                for row in range(100):  # Loops through each row 100 times
                    row = next(reader)
                    record = Covid19Record(rowId, row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8],
                                           row[13], row[15])  # Add properties to CSVRow object representing the row in the CSV file
                    records.append(record)
                    rowId += 1
        except FileNotFoundError as error:  # Exception handler for csv file missing
            print(str(error) + " in the root directory of the program")
        finally:
            file.close()
            return records

    def saveDataToFile(self, name, records):
        """
        Saves the given records to file and names the file with the given name
        """
        file = open(name, "w")
        for record in records:
            file.write(str(record.id) + "," + str(record.pruid) + str(record.prname) + "," + str(record.prnameFR) + ","
                       + str(record.date) + "," + str(record.numconf) + "," + str(record.numprob) + ","
                       + str(record.numdeaths) + "," + str(record.numtotal) + "," + str(record.numtoday) + "," + str(
                record.ratetotal))
        file.close()
