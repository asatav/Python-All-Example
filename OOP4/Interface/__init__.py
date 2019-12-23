from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class Oracle(DBInterface):
    def connect(self):
        print("Connecting to oracle database")
    def disconnect(self):
        print("DisConnecting to oracle database")
        
class Sybase(DBInterface):
    def connect(self):
        print("Connecting to Sybase database")
    def disconnect(self):
        print("DisConnecting to Sybase database")
        
dbname=input("Enter database name:-")
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()
