class Employee:
    def __init__(self, name, salary, age, email, address):
        self.Name = name
        self.Salary = salary
        self.Age = age
        self.Email = email
        self.Address = address

    def __str__(self):
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)