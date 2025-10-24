#  Employee Details Management System

# -----------------------------------------------
# This Python script demonstrates the use of classes and objects.
# It defines an 'Employees' class that stores employee information,
# calculates bonus based on experience, and displays full details.
# -----------------------------------------------

# Defining the Employees class (Blueprint)
class Employees(): 
    def __init__(self, name, salary, Experience):  
        self.name = name   
        self.salary = salary
        self.Experience = Experience
        self.bonus = self.calculate_bonus()  # Calculate bonus initially based on experience

    #Calculates bonus based on experience:
    def calculate_bonus(self):
        if self.Experience >= 10:
            bonus =  self.salary * 0.20
        elif self.Experience >= 5:
            bonus = self.salary * 0.10
        else:
            bonus = 0
        return bonus
    
    def set_salary(self, new_salary): #Updates the employee's salary and recalculates the bonus
        self.salary = new_salary
        self.bonus = self.calculate_bonus()
        
    def show_details(self): #Displays the employee's complete details.
        final_salary = self.salary + self.bonus
        print(f"Name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"experience: {self.Experience} year")
        print(f"Bonus: {self.bonus}")
        print(f"Final salary: {final_salary}")


# Creating an object (instance) of Employees class      

emp1 = Employees("Sundar", 15000, 8)
emp2 = Employees("Raghav",23500,2)

emp1.show_details()
print()
emp2.show_details()

print("\nAfter promotion:")

# Update salary and show new details
emp1.set_salary(20000)
emp1.show_details()