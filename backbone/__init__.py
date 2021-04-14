import json
from json.decoder import JSONDecodeError



class database:

    def __init__(self, db, path, username, password):
        self.connection = False
        self.usernames = []
        self.database = db  # this is not a mistake, i changed it to reduce conflict between the class and var
        self.majoruser = username
        self.password = password
        self.path = path
        with open(path, 'a') as f:
            f.close()

    def connect(self, username, password):
        self.jname = username
        if username == self.majoruser:
            if password == self.password:
                self.connection = True
                print("connected to", self.database)
            else:
                raise ConnectionError("Password was incorrect")
        else:
            if username in self.usernames:
                connection = True
            else:
                raise ConnectionError("Username was sus")

    def close(self):
        if self.connection == False:
            raise ConnectionResetError("Database was not connected")
        else:
            self.connection = False
            print("Disconnected to", self.database)

    def addminor(self, username, password):
        if self.jname == self.majoruser:
            global usernames
            self.usernames.append(username)
        else:
            return PermissionError("MINORS CANNOT GENERATE MINORS")

    def xdfgssbdgdgbe(self, data):    # THIS IS A PRIVATE FUNCTION TO BE USED BY def INSERT ONLY
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)

    def insert(self, d, table):
        if self.jname == self.majoruser:
            if self.connection != False:
                try:
                    with open(self.path) as json_file:
                        data = json.load(json_file)

                        temp = data[table]
                        temp.append(d)

                    self.xdfgssbdgdgbe(data)
                # assuming there is no content rn inside the file
                except json.decoder.JSONDecodeError:
                    with open(self.path, "w") as outfile:
                        json.dump(d, outfile)
                except KeyError:
                    with open(self.path, 'a') as l:
                        json.dump(data, l)
                    return "table not found"
            else:
                raise ConnectionError("not connected")
        else:
            raise PermissionError('MINORS DONT HAVE PERMISSION TO INSERT!')

    def fetch(self):
        if self.connection != False:
            try:
                with open(self.path, 'r') as openfile:
                    json_object = json.load(openfile)

                return json_object
            except JSONDecodeError:
                raise IOError("database is either cleared or not formatted properly")

        else:
            raise ConnectionError("not connected")

    def fetch_json(self):
        if self.connection != False:
            try:
                with open(self.path, 'r') as openfile:
                    json_object = json.load(openfile)

                y = json.dumps(json_object)
                return y
            except JSONDecodeError:
                raise IOError("database is either cleared or not formatted properly")
        else:
            raise ConnectionError("not connected")
    def cleardb(self):
        if self.connection != False:
            if self.jname == self.majoruser:
                with open(self.path, 'w+') as o:
                    o.truncate()
                    o.close()
            else:
                raise PermissionError('MINORS CANNOT CLEAR A DATABASE')
        else:
            raise ConnectionError("not connected")

    def fetchsp(self, table):
        if self.connection != False:
            with open(self.path, 'r') as openfile:
                json_object = json.load(openfile)
            try:
                return json_object[table]
            except KeyError:
                return "table not found"
        else:
            raise ConnectionError("not connected")
