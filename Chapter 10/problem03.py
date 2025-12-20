# Create class Employee with salary and increment properties

class Employee:
    salary = int(input("Enter a salary : $"))

    increment = int(input("Enter a Increment in % : "))

    @property
    def salaryAfterIncrement(self):
        # Calculate salary after increment
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # Update increment based on desired salary
        self.increment = ((new_salary / self.salary) - 1) * 100

'''
@salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        if new_salary < self.salary:
            print("New salary cannot be less than base salary")
        else:
            self.increment = ((new_salary / self.salary) - 1) * 100 
'''

e = Employee()
print(e.salaryAfterIncrement)   # Current salary after increment

e.salaryAfterIncrement = 300.0  # Set desired salary
print(e.increment)              # Updated increment percentage
