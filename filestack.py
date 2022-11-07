import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS FILES
         (ID INTEGER PRIMARY KEY        AUTOINCREMENT NOT NULL ,
         FILE_ID         CHAR(10)    NOT NULL UNIQUE,
         PLACE_INDEX     INTEGER     NOT NULL UNIQUE,
         DESCRIPTION     TEXT
         );''')

print("Table created successfully")

conn.execute("INSERT INTO FILES (FILE_ID, PLACE_INDEX) VALUES ('A2', 5)")
conn.commit()
cur  = conn.execute('SELECT * from FILES;')
for i in cur:
    print(i)


conn.close()
class FileObject:
    id = []
    description = ""
    index = None
    def __init__(self, id, index):
        self.id = id
        self.index = index

class FileStack:
    files = []
    def __init__(self):
        pass
    
    def place(self, item):
        self.files.append(item)

    

    def __str__(self):
        res = ""
        for id, it in enumerate(self.files):
            res += f"{id} : {str(it.id)}\n"
        return res

if __name__ == '__main__':
    f = FileStack()
    f.place(FileObject(0, "as"))
    f.place(FileObject(1, "as"))

    print(f)