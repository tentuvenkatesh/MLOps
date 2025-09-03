class Empiloyee:
    def __init__(self):
        self.id = "MA23M025"
        self.salary = 100000
        self.designation = "Software Engineer"
    def travel(self,destination):
        print(f"Traveling to {destination}")
# Creating an object or instance
emp = Empiloyee()
print(emp.id)
print(emp.salary)
emp.travel("Bangalore")
print(type(emp))