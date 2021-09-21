class Covid19Record:
    """
    A class to represent a row in the covid19-download.csv.
    By Corey Morris
    ...

    Attributes
    ----------
    _id : int
        The id of the row
    _pruid : str
        First property of csv row
    _prname : str
        Second property of csv row
    _prnameFR : str
        Third property of csv row
    _date : str
        Fourth property of csv row
    _numconf : int
        Sixth property of csv row
    _numprob : int
        Seventh property of csv row
    _numdeaths : int
        Eighth property of csv row
    _numtotal : int
        Ninth property of csv row
    _numtoday : int
        Fourteenth property of csv row
    _ratetotal : float
        Sixteenth property of csv row

   Methods
   -------
   id()
        Returns id property.

   id.setter(v)
        Sets id to the passed property v

   pruid()
        Returns pruid property.

   pruid.setter(v)
        Sets pruid to the passed property v

   prname()
        Returns prname property.

   prname.setter(v)
        Sets prname to the passed property v

   prnameFR()
        Returns prnameFR property.

   prnameFR.setter(v)
        Sets prnameFR to the passed property v

   date()
        Returns date property.

   date.setter(v)
        Sets date to the passed property v

   numconf()
        Returns numconf property.

   numconf.setter(v)
        Sets numconf to the passed property v

   numprob()
        Returns numprob property.

   numprob.setter(v)
        Sets numprob to the passed property v

   numdeaths()
        Returns numdeaths property

   numdeaths.setter(v)
        Sets numdeaths to the passed property v

   numtotal()
        Returns numtotal property.

   numtotal.setter(v)
        Sets numtotal to the passed property v

   numtoday()
        Returns numtoday property.

   numtoday.setter(v)
        Sets numtoday to the passed property v

   ratetotal()
        Returns ratetotal property.

   ratetotal.setter(v)
        Sets ratetotal to the passed property v

   get_table_row(table)
       Appends row information to table
   """

    def __init__(self, id, pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
        """
        CSVRow constructor for variables representing properties of covid19-download.csv

        Parameters
        ----------
        id : int
            The id of the row
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
        self._id = id
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
    def id(self):
        """
        Returns id property.

                Returns:
                        id (int): The ID of the record
        """
        return self._id

    @id.setter
    def id(self, v):
        """
        Sets id to given param
                    @Param (int) id: The id of the record
        """
        int(v)  # Throws ValueError exception if wrong type
        self._id = v

    @property
    def pruid(self):
        """
        Returns pruid property.

                Returns:
                        pruid (str): A property of the CSV row
        """
        return self._pruid

    @pruid.setter
    def pruid(self, v):
        """
        Sets pruid to given param
                    @Param (int) pruid: The pruid of the record
        """

        if int(v) < 0:  # Throws ValueError exception if wrong type
            raise TypeError("Only positive integers are allowed")  # Throws exception if negative number
        self._pruid = v

    @property
    def prname(self):
        """
        Returns prname property.

                Returns:
                        prname (str): A property of the CSV row
        """
        return self._prname

    @prname.setter
    def prname(self, v):
        """
        Sets prname to given param
                    @Param (str) prname: The prname of the record
        """
        str(v)  # Throws ValueError exception if wrong type
        self._prname = v

    @property
    def prnameFR(self):
        """
        Returns prnameFR property.

                Returns:
                        prnameFR (str): A property of the CSV row
        """
        return self._prnameFR

    @prnameFR.setter
    def prnameFR(self, v):
        """
        Sets prnameFR to given paramFR
                    @Param (str) prnameFR: The prnameFR of the record
        """
        str(v)  # Throws ValueError exception if wrong type
        self._prnameFR = v

    @property
    def date(self):
        """
        Returns date property.

                Returns:
                        date (string): A property date of the CSV row
        """
        return self._date

    @date.setter
    def date(self, v):
        """
        Sets date to given param
                    @Param (string) date: The date of the record
        """
        str(v)  # Throws ValueError exception if wrong type
        self._date = v

    @property
    def numconf(self):
        """
        Returns numconf property.

                Returns:
                        numconf (int): A property date of the CSV row
        """
        return self._numconf

    @numconf.setter
    def numconf(self, v):
        """
        Sets numconf to given param
                    @Param (int) numconf: The numconf of the record
        """
        if int(v) < 0:  # Throws ValueError exception if wrong type
            raise TypeError("Only positive integers are allowed")  # Throws exception if negative number
        self._numconf = v

    @property
    def numprob(self):
        """
        Returns numprob property.

                Returns:
                        numprob (int): A property date of the CSV row
        """
        return self._numprob

    @numprob.setter
    def numprob(self, v):
        """
        Sets numprob to given param
                    @Param (int) numprob: The numprob of the record
        """
        if int(v) < 0:  # Throws ValueError exception if wrong type
            raise TypeError("Only positive integers are allowed")  # Throws exception if negative number
        self._numprob = v

    @property
    def numdeaths(self):
        """
        Returns numdeaths property.

                Returns:
                        numdeaths (int): A property date of the CSV row
        """
        return self._numdeaths

    @numdeaths.setter
    def numdeaths(self, v):
        """
        Sets numdeaths to given param
                    @Param (int) numdeaths: The numdeaths of the record
        """
        if int(v) < 0:  # Throws ValueError exception if wrong type
            raise TypeError("Only positive integers are allowed")  # Throws exception if negative number
        self._numdeaths = v

    @property
    def numtotal(self):
        """
        Returns numtotal property.

                Returns:
                        numtotal (int): A property date of the CSV row
        """
        return self._numtotal

    @numtotal.setter
    def numtotal(self, v):
        """
        Sets numtotal to given param
                    @Param (int) numtotal: The numtotal of the record
        """
        if int(v) < 0:  # Throws ValueError exception if wrong type
            raise TypeError("Only positive integers are allowed")  # Throws exception if negative number
        self._numtotal = v

    @property
    def numtoday(self):
        """
        Returns numtoday property.

                Returns:
                        numtoday (int): A property date of the CSV row
        """
        return self._numtoday

    @numtoday.setter
    def numtoday(self, v):
        """
        Sets numtoday to given param
                    @Param (int) numctoday: The numtoday of the record
        """
        if int(v) < 0:  # Throws ValueError exception if wrong type
            raise TypeError("Only positive integers are allowed")  # Throws exception if negative number
        self._numtoday = v

    @property
    def ratetotal(self):
        """
        Returns ratetotal property.

                Returns:
                        ratetotal (int): A property date of the CSV row
        """
        return self._ratetotal

    @ratetotal.setter
    def ratetotal(self, v):
        """
        Sets ratetotal to given param
                    @Param (float) ratetotal: The ratetotal of the record
        """
        if float(v) < 0:  # Throws ValueError exception if wrong type
            raise TypeError("Only positive numbers are allowed")  # Throws exception if negative number
        self._ratetotal = v

    def get_table_row(self, table):
        """
        Appends a new table row with object's properties
        """
        table.add_row(str(self.id), str(self.pruid), str(self.prname), str(self.prnameFR), str(self.date),
                      str(self.numconf), str(self.numprob), str(self.numdeaths), str(self.numtotal), str(self.numtoday),
                      str(self.ratetotal), "Corey Morris")
