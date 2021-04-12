import json

global connection
connection = False


class database:
    global usernames
    usernames = []

    def __init__(self, daabase, path, username, password):
        self.database = daabase  # this is not a mistake, i changed it to reduce conflict between the class and var
        self.username = username
        self.password = password
        self.path = path
        with open(path, 'a') as f:
            f.close()

    def connect(self, username, password):
        self.jname = username
        if username == self.username:
            if password == self.password:
                global connection
                connection = True
                print("connected to", self.database)
            else:
                raise ConnectionError("Password was incorrect")
        else:
            if username in usernames:
                connection = True
            else:
                raise ConnectionError("Username was sus")

    def close(self):
        global connection
        if connection == False:
            raise ConnectionResetError("Database was not connected")
        else:
            connection = False
            print("Disconnected to", self.database)

    def addminor(self, username, password):
        if self.jname == self.username:
            global usernames
            usernames.append(username)
        else:
            return PermissionError("MINORS CANNOT GENERATE MINORS")

    def insertwrapper(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)

    def insert(self, d, table):
        if self.jname == self.username:
            if connection != False:
                try:
                    with open(self.path) as json_file:
                        data = json.load(json_file)

                        temp = data[table]
                        temp.append(d)

                    self.insertwrapper(data)
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
        if connection != False:
            with open(self.path, 'r') as openfile:
                json_object = json.load(openfile)

            return json_object
        else:
            raise ConnectionError("not connected")

    def fetch_json(self):
        if connection != False:
            with open(self.path, 'r') as openfile:
                json_object = json.load(openfile)

            y = json.dumps(json_object)
            return y
        else:
            raise ConnectionError("not connected")

    def fetchsp(self, table):
        if connection != False:
            with open(self.path, 'r') as openfile:
                json_object = json.load(openfile)
            try:
                return json_object[table]
            except KeyError:
                return "table not found"
        else:
            raise ConnectionError("not connected")
