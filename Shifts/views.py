from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse
from shiftAdmin.models import Employee,Shift,Schedule
import random

# Create your views here.
def createMock():
    employees = []
    for i in range(1, 6):
        employee = Employee.objects.create(name=f'Employee {i}')
        employees.append(employee)
        print('created mock employees')

    # Create Shifts
    shifts = []
    for i in range(1, 6):
        start_time = timezone.now() + timezone.timedelta(days=i)
        end_time = start_time + timezone.timedelta(hours=8)
        shift = Shift.objects.create(name=f'Shift {i}', start_time=start_time, end_time=end_time)
        shifts.append(shift)
        print('created mock employees')

    # Assign random shifts to employees for the next 30 days
    for _ in range(30):
        date = timezone.now() + timezone.timedelta(days=1)
        for employee in employees:
            schedule = Schedule.objects.create(
                employee=employee,
                shift=random.choice(shifts),
                date=date
            )
            print('created mock employees')
            date += timezone.timedelta(days=1)
    
def shiftsview(request):    
    return render(request,"Shifts\shifts.html")

def getShift(request):
    employee_id = 1  # Assuming you want schedules for Employee 1
    schedules = Schedule.objects.filter(employee__name='Employee 1')
    
    data = []
    for schedule in schedules:
        data.append({
            "title": schedule.shift.name,
            "start": schedule.shift.start_time,  # Convert to ISO format
            "end": schedule.shift.end_time,      # Convert to ISO format
        })
    
    return JsonResponse(data, safe=False)


