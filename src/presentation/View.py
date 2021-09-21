from model.Covid19Record import Covid19Record  # Represents record(s) of the CSV file
from business.Service import Service  # The Service that View will use to input and retrieve all information
from datetime import date  # Used for insertion of record with date as the current date
from rich.console import Console  # API Library - Rich terminal text
from rich.table import Table  # API Library - Rich terminal text


class View:
    """
    Responsible for displaying and gathering information to the user and acts as a gateway to Service
    By Corey Morris
    ...

    Attributes
    ----------
    _service : Service
        The Service instance View will use
    _RELOAD : (CONSTANT) Value: r
        Represents a menu option that will trigger reload all records
    _SHOW_ALL : (CONSTANT) Value: a
        Represents a menu option that will trigger show all records
    _SHOW_ONE : (CONSTANT) Value: v
        Represents a menu option that will trigger show one record
    _INSERT : (CONSTANT) Value: i
        Represents a menu option that will trigger inserting record(s)
    _UPDATE : (CONSTANT) Value: u
        Represents a menu option that will trigger update record(s)
    _DELETE : (CONSTANT) Value: d
        Represents a menu option that will trigger delete record(s)
    _SAVE : (CONSTANT) Value: s
        Represents a menu option that will trigger save all records
    _EXIT : (CONSTANT) Value: x
        Represents a menu option that will exit the program

    Methods
    -------
    showMenu()
        The main menu of the program. Awaits user input for processing or exiting

    printMenu()
        Prints main menu

    reload()
        Reloads all records from datastore

    printRecords()
        Prints all records

    viewOne()
        Prints the requested record

    insert()
        Inserts given parameters into a record which is then inserted into record array in memory

    update()
        Updates record matching the id of the given record

    delete()
        Deletes record matching the id of the given record

    saveToDisk()
        Saves current record array to disk

    createNewRecord(id)
        @param id: Sets the id of the new record and skips requesting the id from the user if not blank
        Returns a Covid19Record from user input

    processResponse()
        Based on input, triggers the approperiate function

    createTable()
        Returns a table from Rich API for displaying Covid19-download.csv data

    """

    def __init__(self):
        """
        Instantiates Service and all menu constants

        Parameters
        ----------
        _service : Service
            The Service instance View will use
        _RELOAD : (CONSTANT) Value: r
            Represents a menu option that will trigger reloading of all records drom datastore
        _SHOW_ALL : (CONSTANT) Value: a
            Represents a menu option that will trigger show all records
        _SHOW_ONE : (CONSTANT) Value: v
            Represents a menu option that will trigger show one record
        _INSERT : (CONSTANT) Value: i
            Represents a menu option that will trigger inserting record(s)
        _UPDATE : (CONSTANT) Value: u
            Represents a menu option that will trigger update record(s)
        _DELETE : (CONSTANT) Value: d
            Represents a menu option that will trigger delete record(s)
        _SAVE : (CONSTANT) Value: s
            Represents a menu option that will trigger saving all records
        _EXIT : (CONSTANT) Value: x
            Represents a menu option that will exit the program
        """
        self._service = Service()
        self._RELOAD = "r"
        self._SHOW_ALL = "a"
        self._SHOW_ONE = "v"
        self._INSERT = "i"
        self._UPDATE = "u"
        self._DELETE = "d"
        self._SAVE = "s"
        self._EXIT = "x"

    def showMenu(self):
        """
        The main menu of the program. Awaits user input for processing or exiting
        """
        exitProgram = False
        while not exitProgram:
            self.printMenu()
            response = input()
            if response.lower() == self._EXIT.lower():
                exitProgram = True
            else:
                self.processResponse(response)

    def printMenu(self):
        """
        Prints main menu
        """
        print("Author: Corey Morris")
        print("Please enter an option:")
        print("(r) Reload records")
        print("(a) All records")
        print("(v) View a record")
        print("(i) Insert record")
        print("(u) Update record")
        print("(d) Delete record")
        print("(s) Save all records")
        print("(x) Exit program")

    def reload(self):
        """
        Reloads all records from datastore
        """
        self._service = Service()  # Re-instatiates Service which reloads all records

    def printRecords(self):
        """
        Prints all records
        """
        records = self._service.getAll()
        console = Console()
        table = self.createTable()
        for record in records:  # Iterates through each row then calls CSVRow print function for that object's instance
            record.get_table_row(table)  # Calls function get_table_row in each CSVRow object to append a new table row
        console.print(table)

    def viewOne(self):
        """
        Prints the requested record
        """
        console = Console()
        table = self.createTable()

        print("Please enter the id of the record")
        recordid = input()
        newRecord = Covid19Record(recordid, "", "", "", "", "", "", "", "", "", "")
        returnrecord = self._service.getRecord(newRecord)
        if returnrecord != '':
            returnrecord.get_table_row(table)
            console.print(table)
        else:
            print("No record with that id")
            print("")

    def insert(self):
        """
        Inserts given parameters into a record which is then inserted into record array in memory
        """
        verified = False  # verified is updated from Service insertion. If success verified is true
        while not verified:
            verified = self._service.insertRecord(self.createNewRecord(''))
            if not verified:
                print("Error entering record. Try again.")
        self.printRecords()
        print("Inserted record successfully")

    def update(self):
        """
        Updates record matching the id of the given record
        """
        console = Console()
        table = self.createTable()

        updaterecord = ''  # Empty string to signal that record still hasnt been retrieved
        while updaterecord == '':
            print("Please enter the id of the record to update")
            updateid = input()
            temprecord = Covid19Record(updateid, '', '', '', '', '', '', '', '', '', '')
            updaterecord = self._service.getRecord(
                temprecord)  # Service.getRecord either retrieves record or sends empty string
            if updaterecord == '':
                print("No record with that ID")
            else:
                updaterecord.get_table_row(table)
                console.print(table)
        r = self.createNewRecord(updateid)
        success = self._service.updateRecord(r)
        if success:
            print("Updated record sucessfully")
        else:
            print("Failed to updated record")
            print(
                "One of the properties are the wrong type. Make sure properties are the right type (EX. numconf must be a int")

    def delete(self):
        """
        Deletes record matching the id of the given record
        """
        print("Please enter id of record to delete")
        recordid = input()
        deleterecord = Covid19Record(recordid, '', '', '', '', '', '', '', '', '', '')
        success = self._service.deleteRecord(deleterecord)
        if success:
            print("Sucessfully deleted record")
        else:
            print("Failed to delete record")

    def saveToDisk(self):
        """
        Saves current record array to disk
        """
        self._service.saveAllRecords("Covid19SavedRecords.txt")
        print("Saved all records\n")

    def createNewRecord(self, id):
        """
        Creates a Covid19Record from user input
            @param id: Sets the id of the new record and skips requesting the id from the user if not blank
            Returns:
                The new Covid19Record
        """
        newid = ''
        if id == '':
            print("Please enter new record id. Must be whole number")
            newid = input()
        else:
            newid = id
        print("Please enter new pruid. Must be whole number")
        newpruid = input()
        print("Please enter new prname. Can be words or number")
        newprname = input()
        print("Please enter new prnameFR. Can be words or number")
        newprnameFR = input()
        print("Please enter new numconf. Must be whole number")
        numconf = input()
        print("Please enter new numprob. Must be whole number")
        numprob = input()
        print("Please enter new numdeaths. Must be whole number")
        numdeaths = input()
        print("Please enter new numtotal. Must be whole number")
        numtotal = input()
        print("Please enter new numtoday. Must be whole number")
        numtoday = input()
        print("Please enter new ratetotal. Must be a number")
        ratetotal = input()
        return Covid19Record(newid, newpruid, newprname, newprnameFR, date.today().strftime('%Y-%m-%d'), numconf,
                             numprob, numdeaths, numtotal, numtoday, ratetotal)

    def processResponse(self, inputMenu):
        """
        Based on input, triggers the appropriate function
        """
        if inputMenu == self._SHOW_ALL:
            self.printRecords()
        elif inputMenu == self._RELOAD:
            self.reload()
        elif inputMenu == self._SHOW_ONE:
            self.viewOne()
        elif inputMenu == self._INSERT:
            self.insert()
        elif inputMenu == self._UPDATE:
            self.update()
        elif inputMenu == self._DELETE:
            self.delete()
        elif inputMenu == self._SAVE:
            self.saveToDisk()
        elif inputMenu == self._EXIT:
            print("Exiting program")
        else:
            print("Please enter a valid option")

    def createTable(self):
        """
        Creates table from Rich API for displaying Covid19-download.csv data

            Returns:
                The table that is formatted with Covid19-download.csv properties
        """
        table = Table(show_header=True, header_style="bold yellow")
        table.add_column("id")
        table.add_column("pruid")
        table.add_column("prname")
        table.add_column("prnameFR")
        table.add_column("date")
        table.add_column("numconf")
        table.add_column("numprob")
        table.add_column("numdeaths")
        table.add_column("numtotal")
        table.add_column("numtoday")
        table.add_column("ratetotal")
        table.add_column("Author")
        return table
