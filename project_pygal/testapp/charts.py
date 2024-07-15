import pygal 
from .models import Employee

class EmployeePieChart(pygal.Pie):
    def __init__(self, *args, **kwargs):
        super(EmployeePieChart, self).__init__(*args, **kwargs)
        self.title = 'Employee Distribution by Department'
        employees = Employee.objects.all()
        for employee in employees:
            self.add(employee.department, employee.strength)

class EmployeeGaugeChart(pygal.SolidGauge):
    def __init__(self, *args, **kwargs):
        super(EmployeeGaugeChart, self).__init__(*args, **kwargs)
        self.title = 'Employee Strength by Department'
        employees = Employee.objects.all()
        for employee in employees:
            self.add(employee.department, [{'value':employee.strength, 'max_value':500}]) 

class EmployeeBarChart(pygal.Bar):
    def __init__(self, *args, **kwargs):
        super(EmployeeBarChart, self).__init__(*args, **kwargs)
        self.title = 'Employee Strength by Department'
        employees = Employee.objects.all()
        for employee in employees:
            self.add(employee.department, employee.strength)