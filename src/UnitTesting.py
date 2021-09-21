import unittest
from persistence.DataStore import Datastore


# Corey Morris morr0621

class Tests(unittest.TestCase):

    def test_record_properties(self):
        """
        Verifies that each type of each properties is correct.
        Useful for using a different datasource and ensuring the records are compatible
        """
        _datastore = Datastore()
        records = _datastore.loadRecordsFromFile()
        self._id = id
        for record in records:
            #   Checks if int or 0
            self.assertTrue(int(record.id) == 0 or int(record.id), 'Not a number')
            #   Checks if int or 0
            self.assertTrue(int(record.pruid) == 0 or int(record.pruid), 'Not a number')
            #   Checks if string
            self.assertTrue(str(record.prname), 'Not a string')
            #   Checks if string
            self.assertTrue(str(record.prnameFR), 'Not a string')
            #   Checks if string
            self.assertTrue(str(record.date), 'Not a string')
            #   Checks if int or 0
            self.assertTrue(int(record.numconf) == 0 or int(record.numconf), 'Not a number')
            #   Checks if int or 0
            self.assertTrue(int(record.numprob) == 0 or int(record.numprob), 'Not a number')
            #   Checks if int or 0
            self.assertTrue(int(record.numdeaths) == 0 or int(record.numdeaths), 'Not a number')
            #   Checks if int or 0
            self.assertTrue(int(record.numtotal) == 0 or int(record.numtotal), 'Not a number')
            #   Checks if int or 0
            self.assertTrue(int(record.numtoday) == 0 or int(record.numtoday), 'Not a number')
            #   Checks if float, also accepts empty strings as covid19-download.csv has blank entrys for this
            self.assertTrue(str(record.ratetotal) == "" or float(record.ratetotal) == 0.0 or float(record.ratetotal),
                            'Not a float number')


if __name__ == '__main__':
    unittest.main()
