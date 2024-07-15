from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from pygal.style import DarkStyle # 'DarkStyle' -> changeable
from django.http import HttpResponse
from .models import Employee
from .charts import EmployeePieChart, EmployeeGaugeChart, EmployeeBarChart

def clear(request):
    Employee.objects.all().delete()
    return redirect('/home')

def home(request):
    if request.method == 'POST':
        department = request.POST['department']
        strength = request.POST['strength']
        print(department)
        print(strength)
        Employee.objects.create(department=department, strength=strength)
    return render(request, 'home.html')

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        cht_employee = EmployeePieChart(height=600, width=800, explicit_size=True, style=DarkStyle)
        context['cht_employee'] = cht_employee.render(is_unicode=True)
        return context
    
class IndexView1(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView1, self).get_context_data(**kwargs)
        cht_employee = EmployeeGaugeChart(height=600, width=800, explicit_size=True, style=DarkStyle)
        context['cht_employee'] = cht_employee.render(is_unicode=True)
        return context

class IndexView2(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)
        cht_employee = EmployeeBarChart(height=600, width=800, explicit_size=True, style=DarkStyle)
        context['cht_employee'] = cht_employee.render(is_unicode=True)
        return context
    
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['department', 'strength']
    template_name = 'employee_edit.html'
    success_url = '/employees/'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = '/employees'