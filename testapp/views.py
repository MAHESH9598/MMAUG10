from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def emp_data_view(request):
    emp_data={
    'eno':100,
    'ename':'mahi',
    'esal':40000,
    'eadd':'Mumbai',
    }
    resp='<h1>Employee Number:{}<br> Employee Name:{}<br> Employee Salary:{} <br>Employee Address:{}<h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eadd'])

    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data={
    'eno':100,
    'ename':'mahi',
    'esal':40000,
    'eadd':'Mumbai',
    }

    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={
    'eno':100,
    'ename':'mahi',
    'esal':40000,
    'eadd':'Mumbai',
    }
    return JsonResponse(emp_data)






