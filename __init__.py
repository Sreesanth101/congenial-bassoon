import json

class Database:
    def __init__(self,path,username,password):
        self.path = path
        self.username = username
        self.password= password
        self.connected = False
    def connect(self,username,password):
        if username == self.username and password == self.password:
            with open(self.path,'r') as f:
                f.close()
            self.connected = True
        else:
            raise PermissionError('Username and password are not correct')
    def close(self):
        if self.connected == True:
            self.connected = False
        else:
            raise IOError('connection already closed')

    def add(self,dictionary):
        if self.connected == True:
            if type(dictionary) == dict:
                with open(self.path,'ab+') as f:
                    f.seek(0, 2)
                    if f.tell() == 0:  #
                        f.write(json.dumps([dictionary]).encode())
                    else:
                        f.seek(-1, 2)
                        f.truncate()
                        f.write(' , '.encode())
                        f.write('\n'.encode())
                        f.write(json.dumps(dictionary).encode())
                        f.write(']'.encode())
            else:
                raise TypeError(dictionary,'Is not a dictionary to dump in json')
        else:
            raise ConnectionError('Not connected')

    def get_unfiltered(self):
        if self.connected == True:
            with open(self.path,'r') as f:
                x = f.read()
                x = json.loads(x)
                return x
        else:
            raise ConnectionError('Not connected')

    def get_json(self):
        if self.connected == True:
            with open(self.path,'r') as f:
                x = f.read()
                x = json.loads(x) # just to make sure
                x = json.dumps(x)
                return x
        else:
            raise ConnectionError('Not connected')

    def version(self):
        return 'congenial-bassoon v0.0-beta'