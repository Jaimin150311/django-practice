from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def students(request):
    student = [
        {"id": 1, "name": "Jaimin", "age": 21},
        {"id": 2, "name": "Prince", "age": 20},
        {"id": 3, "name": "Pratham", "age": 22},
        ]
    
    # return HttpResponse('<h1>This is H1</h1>')

    return HttpResponse(student)