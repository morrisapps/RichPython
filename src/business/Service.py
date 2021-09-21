from model.Covid19Record import Covid19Record  # Represents record(s) of the CSV file
from persistence.DataStore import Datastore  # The Persistance layer that retrieves data or saves data
import copy  # Used to copy records for verification purposes


class Service:
    """
    This class is responsible for processing data between DataStore and Presentation
    By Corey Morris
    ...

    Attributes
    ----------
    _datastore : str if not assigned, instance of datastore otherwise
        (private) The datastore instance Service will use
    _Covid19Records : Array of Records
        (private) Each Record of array represents a row of Covid19-download CSV

    Methods
    -------
    getAll()
        Returns all records from Covid19-download.csv

    getRecord(record)
        Returns The record that matches the given record's id

    insertRecord(record)
        Inserts record into _Covid19Records array

    updateRecord(record)
        Updates the record in _Covid19Records array

    deleteRecord(record)
        Deletes the record in _Covid19Records array

    saveAllRecords(name)
        Saves all records from current _covid19Records array to a file with the given name in the instance of datastore

    getRecordIndex(record)
        Returns: (int) The index of the record in _Covid19records, or '' if doesnt exist
    """

    def __init__(self):
        """
        Instantiates _datastore and populates _Covid19Record

        Parameters
        ----------
        _datastore : Datastore
            The datastore instance Service will use
        _Covid19Records : Array of Records
            Each Record of array represents a row of Covid19-download CSV
        """
        self._datastore = Datastore()
        self._Covid19Records = self._datastore.getAll()

    def getAll(self):
        """
        Gets all records from Covid19-download.csv

            Returns:
                The array that contains all records
        """
        return self._Covid19Records

    def getRecord(self, record):
        """
        Retrieves record matching the id of the given record

            Returns:
                The record that matches the given record's id
        """
        returnRecord = ''  # Set variable to a blank string. This is to signal if no records match id
        for r in self.getAll():
            if str(r.id) == str(record.id):
                returnRecord = r
        return returnRecord
        #Commented out code is for retrieving records from file instead of memory
        #returnrecord = self._datastore.getRecord(record.id)
        #return returnrecord



    def insertRecord(self, record):
        """
        Inserts record into _Covid19Records array
            Returns:
                boolean: stating pass if true or fail if false
        """
        #   Does not call datastore because it is altering memory and not persistent data
        verified = True
        for arrayRecord in self.getAll():
            if str(arrayRecord.id) == str(record.id):
                verified = False
        if verified:
            self._Covid19Records.append(record)
        return verified

    def updateRecord(self, record):
        """
        Updates the record in _Covid19Records array
            Returns:
                boolean: stating pass if true or fail if false
        """
        #   Does not call datastore because it is altering memory and not persistent data
        index = self.getRecordIndex(record)
        success = True
        if index != '':
            updatingrecord = self.getAll()[index]
            # Sets all properties. The record setters also verify the property type which this method uses to verify
            updatingrecord.id = record.id
            updatingrecord.pruid = record.pruid
            updatingrecord.prname = record.prname
            updatingrecord.prnameFR = record.prnameFR
            updatingrecord.date = record.date
            updatingrecord.numconf = record.numconf
            updatingrecord.numprob = record.numprob
            updatingrecord.numdeaths = record.numdeaths
            updatingrecord.numtotal = record.numtotal
            updatingrecord.numtoday = record.numtoday
            updatingrecord.ratetotal = record.ratetotal
        else:
            success = False
        return success

    def deleteRecord(self, record):
        """
        Deletes the record in _Covid19Records array
            Returns:
                boolean: stating pass if true or fail if false
        """
        success = True
        try:
            deleterecord = self.getRecord(record)
            self._Covid19Records.remove(deleterecord)
        except ValueError:
            success = False
        return success

    def saveAllRecords(self, name):
        """
        Saves all records from current _covid19Records array to a file with the given name in the instance of datastore
        """
        self._datastore.saveDataToFile(name, self._Covid19Records)

    def getRecordIndex(self, record):
        """
        Retrieves record matching the id of the given record
            Returns:
                int: The index of the record in _Covid19records, or '' if doesnt exist
        """
        index = 0
        rIndex = ''
        for r in self.getAll():
            if str(r.id) == str(record.id):
                rIndex = index
            index += 1
        return rIndex
