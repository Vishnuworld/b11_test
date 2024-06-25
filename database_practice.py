import pymysql

# port -- 3306
# host - localhost / 127.0.0.1
# user - root
# password - root
# database - world, employee

# db_connection =
# # print(dir(db_connection))
# cur = db_connection.cursor()  # handshaking
# cur.execute("show tables;")
# data = cur.fetchall()
# print(data)
# for i in data:
#     print(i[0])


class Employee:
    def __init__(self, name, salary, age, email):
        self.Name = name
        self.Salary = salary
        self.Age = age
        self.Email = email

    def __str__(self):
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)


emp_lst = [
    Employee(name="A", salary=10000, age=25, email="a@gmail.com"),
    Employee(name="B", salary=20000, age=22, email="b@gmail.com"),
    Employee(name="C", salary=30000, age=24, email="c@gmail.com"),
    Employee(name="D", salary=40000, age=23, email="d@gmail.com"),
    Employee(name="E", salary=50000, age=22, email="e@gmail.com"),
    Employee(name="F", salary=60000, age=25, email="f@gmail.com"),
]

# print(emp_lst)


class MySQLDBOperation:
    def __init__(self, host, port, database, user, password):
        self.HOST = host
        self.PORT = port
        self.DATABASE = database
        self.USER = user
        self.PASSWORD = password

    def get_db_connection(self):
        """
        Establishes a connection to the MySQL database.
        Args:
            None

        Returns:
            pymysql.connections.Connection: A connection object representing the connection to the database.

        Raises:
            pymysql.err.OperationalError: If there is an issue connecting to the database.
        """
        self.conn = pymysql.connect(
            host=self.HOST,
            password=self.PASSWORD,
            database=self.DATABASE,
            port=self.PORT,
            user=self.USER,
        )
        return self.conn

    def show_databases(self):
        db_conn = self.get_db_connection()
        cur = db_conn.cursor()
        cur.execute("show databases;")
        data = cur.fetchall()
        db_conn.close()
        return list(map(lambda x: x[0], data))

    def show_tables(self):
        db_conn = self.get_db_connection()
        cur = db_conn.cursor()
        cur.execute("show tables;")
        data = cur.fetchall()
        db_conn.close()
        return list(map(lambda x: x[0], data))

    def create_table(self):
        CREATE_TABLE_QUERY = """CREATE TABLE Employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        salary DECIMAL(10, 2),
        email VARCHAR(255) UNIQUE,
        age INT
    )"""
        db_conn = self.get_db_connection()
        cur = db_conn.cursor()
        cur.execute(CREATE_TABLE_QUERY)
        print("Table created successfully..!")
        db_conn.close()

    def insert_record(self):
        INSERT_RECORD_QUERY = """insert into employee (name, salary, age, email) values ('ABCD', 65450, 24, 'akshit11@gmail.com'), ('XYZ', 75450, 23, 'apeksha11@gmail.com')"""
        db_conn = self.get_db_connection()
        cur = db_conn.cursor()
        cur.execute(INSERT_RECORD_QUERY)
        db_conn.commit()
        print("Record inserted successfully")
        db_conn.close()

    def get_record(self):
        SELECT_QUERY = "select * from employee"
        db_conn = self.get_db_connection()
        cur = db_conn.cursor()
        cur.execute(SELECT_QUERY)
        data = cur.fetchall()
        db_conn.close()
        return data

    def update_record(self, new_sal, eid):
        UPDATE_QUERY = """update employee set salary={} where id={}"""
        db_conn = self.get_db_connection()
        cur = db_conn.cursor()
        cur.execute(UPDATE_QUERY.format(new_sal, eid))
        db_conn.commit()
        print("Record updated successfully..!")
        db_conn.close()

    def insert_records(self):
        """
        Inserts multiple records into the employee table.

        Args:
            employees (list): A list of Employee objects to be inserted into the database.
        """
        INSERT_RECORD_QUERY = """INSERT INTO employee (name, salary, age, email) VALUES (%s, %s, %s, %s)"""
        db_conn = self.get_db_connection()
        cur = db_conn.cursor()
        records = [(emp.Name, emp.Salary, emp.Age, emp.Email) for emp in emp_lst]
        cur.executemany(INSERT_RECORD_QUERY, records)
        db_conn.commit()
        print("Records inserted successfully")





import toml

def read_database_credentials(file_path):
    """
    Reads database credentials from the TOML file and returns them as a dictionary.
    
    Args:
        file_path (str): The path to the TOML file.
    
    Returns:
        dict: A dictionary containing database credentials.
    """
    try:
        with open(file_path, 'r') as f:
            data = toml.load(f)
            return data.get('database', {})
    except FileNotFoundError:
        print("TOML file not found!")
        return {}

credentials = read_database_credentials(r'E:\Python-B11\B11_Practice\database_handling.py\config.local.toml')


obj = MySQLDBOperation(
    host=credentials.get('host'), 
    port=credentials.get('port'), 
    database=credentials.get('database_name'), 
    user=credentials.get('user'), 
    password=credentials.get('password')
)



# data = obj.get_record()
# lst = []
# for emp in data:    # (1, 'A', Decimal('10000.00')
#     emp_obj = Employee(emp[1], emp[2], emp[4], emp[3])
#     lst.append(emp_obj)

# print(lst)


# if __name__ == "__main__":


# insert_records()


# INSERT_RECORD_QUERY = """insert into employee (name, salary, age, email)
# values """
# # ('{}', {}, {}, '{}')

# for emp in emp_lst:
#     t = (f'{emp.Name}', emp.Salary, emp.Age, f'{emp.Email}')
#     INSERT_RECORD_QUERY += str(t) + ","

# INSERT_RECORD_QUERY = INSERT_RECORD_QUERY[:-1]


# def insert_bulk_record():
#     db_conn = get_db_connection()
#     cur = db_conn.cursor()
#     cur.execute(INSERT_RECORD_QUERY)
#     db_conn.commit()
#     print("Records inserted successfully...!")


# insert_bulk_record()


# os module
