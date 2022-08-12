import mysql.connector
class open_command_db:
    def __init__(self):
        self.connect=mysql.connector.connect(
            host='localhost',
            username='root',
            password='********',
            database='command_db'
        )
        self.cursor=self.connect.cursor(buffered=True)
        query="create table if not exists open_command_table(id int auto_increment primary key ,  command varchar(255))"
        self.cursor.execute(query)
        # print("A table open_command_table is created successfully if not exists")

    def insert_command(self,command):
        '''This fucntion will help user to insert any command through which he can use to operate to open any application '''
        tempquery="insert into open_command_table(command) values(%s)"
        self.cursor.execute(tempquery,[command])
        self.connect.commit()
        # print("row Inserted")

    def remove_command(self,command):
        '''This fucntion will help user to delete any command through which he can use to operate to open any application '''
        self.cursor.execute("delete from open_command_table where command=%s",[command])
        self.connect.commit()
        # print("row deleted")

    def update_command(self,oldcommand,newcommand):
        self.cursor.execute("update open_command_table set command=%s where command=%s",(newcommand,oldcommand))
        self.connect.commit()

    def printit(self):
        self.cursor.execute("select * from open_command_table")
        for row in self.cursor:
            print(row)

    def get_opencmd_list(self):
        self.cursor.execute("select * from open_command_table")
        newlist=[]
        # newlist=list(self.cursor)
        for row in self.cursor:
            temp=str(row[0])
            print("temp is "+str(temp))
            newlist.append(temp)
            print(row)
        print(newlist)
        return newlist

class close_command_db:
    def __init__(self):
        self.connect=mysql.connector.connect(
            host='localhost',
            username='root',
            password='********',
            database='command_db'
        )
        self.cursor=self.connect.cursor(buffered=True)
        query="create table if not exists close_command_table(id int auto_increment primary key ,  command varchar(255))"
        self.cursor.execute(query)
        # print("A table close_command_table is created successfully if not exists")

    def insert_command(self,command):
        tempquery="insert into close_command_table(command) values(%s)"
        self.cursor.execute(tempquery,[command])
        self.connect.commit()
        # print("row Inserted")

    def remove_command(self,command):
        self.cursor.execute("delete from close_command_table where command=%s",[command])
        self.connect.commit()
        # print("row deleted")

    def update_command(self,oldcommand,newcommand):
        self.cursor.execute("update close_command_table set command=%s where command=%s",(newcommand,oldcommand))
        self.connect.commit()

    def printit(self):
        self.cursor.execute("select * from close_command_table")
        for row in self.cursor:
            print(row)

    def get_closecmd_list(self):
        self.cursor.execute("select * from close_command_table")

        newlist=[]
        # newlist=list(self.cursor)
        for row in self.cursor:
            temp=str(row[0])
            print("temp is "+str(temp))
            newlist.append(temp)
            print(row)
        print(newlist)
        return newlist

class normal_command_db:
    def __init__(self):
        self.connect=mysql.connector.connect(
            host='localhost',
            username='root',
            password='********',
            database='command_db'
        )
        self.cursor=self.connect.cursor(buffered=True)
        query="create table if not exists normal_command_table(id int auto_increment primary key ,  command varchar(255))"
        self.cursor.execute(query)
        # print("A table normal_command_table is created successfully if not exists")

    def insert_command(self,command):
        tempquery="insert into normal_command_table(command) values(%s)"
        self.cursor.execute(tempquery,[command])
        self.connect.commit()
        # print("row Inserted")

    def remove_command(self,command):
        self.cursor.execute("delete from normal_command_table where command=%s",[command])
        self.connect.commit()
        # print("row deleted")

    def update_command(self,oldcommand,newcommand):
        self.cursor.execute("update normal_command_table set command=%s where command=%s",(newcommand,oldcommand))
        self.connect.commit()

    def printit(self):
        self.cursor.execute("select * from normal_command_table")
        for row in self.cursor:
            print(row)

    def get_normalcmd_list(self):
        self.cursor.execute("select * from normal_command_table")
        newlist=[]
        # newlist=list(self.cursor)
        for row in self.cursor:
            temp=str(row[0])
            print("temp is "+str(temp))
            newlist.append(temp)
            print(row)
        print(newlist)
        return newlist

# myopendb=open_command_db()
# myclosedb=close_command_db()
# mynormaldb=normal_command_db()
# myopendb.insert_command('open')
# myopendb.remove_command('open')
# myopendb.update_command('start','open')
