class CSVRow:
    """
   A class to represent a row in the covid19-download.csv.
    By Corey Morris
   ...

   Attributes
   ----------
    pruid : str
        First property of csv row
    prname : str
        Second property of csv row
    prnameFR : str
        Third property of csv row
    date : int
        Fourth property of csv row
    numconf : int
        Sixth property of csv row
    numprob : int
        Seventh property of csv row
    numdeaths : int
        Eighth property of csv row
    numtotal : int
        Ninth property of csv row
    numtoday : int
        Fourteenth property of csv row
    ratetotal : int
        Sixteenth property of csv row

   Methods
   -------
   pruid()
        Returns pruid property.

   prname()
        Returns prname property.

   prnameFR()
        Returns prnameFR property.

   date()
        Returns date property.

   numconf()
        Returns numconf property.

   numprob()
        Returns numprob property.

   numdeaths()
        Returns numdeaths property
        .
   numtotal()
        Returns numtotal property.

   numtoday()
        Returns numtoday property.

   ratetotal()
        Returns ratetotal property.

   get_table_row(table)
       Appends row information to table
   """

    def __init__(self, pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
        """
        CSVRow constructor for variables representing properties of covid19-download.csv

        Parameters
        ----------
        pruid : str
            First property of csv row
        prname : str
            Second property of csv row
        prnameFR : str
            Third property of csv row
        date : int
            Fourth property of csv row
        numconf : int
            Sixth property of csv row
        numprob : int
            Seventh property of csv row
        numdeaths : int
            Eighth property of csv row
        numtotal : int
            Ninth property of csv row
        numtoday : int
            Fourteenth property of csv row
        ratetotal : int
            Sixteenth property of csv row
        """
        #
        self._pruid = pruid
        self._prname = prname
        self._prnameFR = prnameFR
        self._date = date
        self._numconf = numconf
        self._numprob = numprob
        self._numdeaths = numdeaths
        self._numtotal = numtotal
        self._numtoday = numtoday
        self._ratetotal = ratetotal

    @property
    def pruid(self):
        '''
        Returns pruid property.

                Returns:
                        pruid (str): A property of the CSV row
        '''
        return self._pruid

    @property
    def prname(self):
        '''
        Returns prname property.

                Returns:
                        prname (str): A property of the CSV row
        '''
        return self._prname

    @property
    def prnameFR(self):
        '''
        Returns prnameFR property.

                Returns:
                        prnameFR (str): A property of the CSV row
        '''
        return self._prnameFR

    @property
    def date(self):
        '''
        Returns date property.

                Returns:
                        date (int): A property date of the CSV row
        '''
        return self._date

    @property
    def numconf(self):
        '''
        Returns numconf property.

                Returns:
                        numconf (int): A property date of the CSV row
        '''
        return self._numconf

    @property
    def numprob(self):
        '''
        Returns numprob property.

                Returns:
                        numprob (int): A property date of the CSV row
        '''
        return self._numprob

    @property
    def numdeaths(self):
        '''
        Returns numdeaths property.

                Returns:
                        numdeaths (int): A property date of the CSV row
        '''
        return self._numdeaths

    @property
    def numtotal(self):
        '''
        Returns numtotal property.

                Returns:
                        numtotal (int): A property date of the CSV row
        '''
        return self._numtotal

    @property
    def numtoday(self):
        '''
        Returns numtoday property.

                Returns:
                        numtoday (int): A property date of the CSV row
        '''
        return self._numtoday

    @property
    def ratetotal(self):
        '''
        Returns ratetotal property.

                Returns:
                        ratetotal (int): A property date of the CSV row
        '''
        return self._ratetotal

    def get_table_row(self, table):
        '''
        Appends a new table row with object's properties
        '''
        table.add_row(self.pruid, self.prname, self.prnameFR, self.date, self.numconf, self.numprob, self.numdeaths, self.numtotal, self.numtoday, self.ratetotal)
