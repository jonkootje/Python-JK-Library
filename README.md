#JK_LIB

####How to use this library:
-------------
1. Download the 'JK_LIB.py' file
2. Move JK_LIB.py to the directory of the python script you are going to use it in
3. Add 'import JK_LIB as JK' on the top of your python script
4. You're now able to use the library!


####Functions this library contains:
--------------
- JK.readfile(path) = Get a file's content
- JK.writefile(path, data) = Put data in a file
- JK.getjson(url) = Get json data from a url
- JK.writeinline(text) = Writes text without adding a new line
- JK.serialize(object) = Serializes a list or some other kind of object
- JK.unserialize(object) = Unserializes a list or some other kind of object
- JK.database(name, directory) = Initializes the database class



####How to use database:
--------------
First you need to **initialize** the database, you do this by defining the database's name to use.
```
db = JK.database('users')
```

Now the library gives you the ability to **get** the information from the database and **push** the information to the database.

You **get** information by doing this.
```
information = db.get()
print(information) # To display the information
```

You **push** information by doing this.
```
data = {"users":[{"username":"john","age":41,"email":"johnthelegend@legend.com"}, {"username":"mark","age":21,"email":"mark@coldmail.com"}} # Some example data
db.push(data)
```

You can also **switch** from database by **setting** a different one.
```
db.set('emaillist')
```

You can also **create** a new database by doing this.
```
db.create('somedatabase')
```

For some **checking** stuff in your coding you can also check if database **exists**.
```
db.exist('somedatabase') # This will return True or False
```


