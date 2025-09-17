from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.
# def studentsView(request):

    # 1. static data
    # student = [
    #     {"id": 1, "name": "Jaimin", "age": 21},
    #     {"id": 2, "name": "Prince", "age": 20},
    #     {"id": 3, "name": "Pratham", "age": 22}, 
    #     ]
    
    # return JsonResponse(student) 
    # return JsonResponse(student, safe=False)


    # 2. dynamic data, retrieving data from database
    # student = Student.objects.all()

    # manually serializing
    # students_list = list(student.values())
    # return JsonResponse(students_list, safe=False)

    

# using serializer
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        # get all the data from student database 
        students_data = Student.objects.all()
        serializer = StudentSerializer(students_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # adding a student to the database
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
# get an single object, primary key based operation
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk = pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # update the data, accept updated incoming data
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # delete data
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    


# ---------------------------------------------------------------------------------------------------------------
# class based views :-

# from rest_framework.views import APIView
# from employees.models import Employee
# from .serializers import EmployeeSerializer 

# class EmployeeListAPIView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# from django.http import Http404
# # Primary key based operations :- 
# class EmployeeCreateAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#             return employee
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK) 
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 




# ----------------------------------------------------
# Mixins 

# from .serializers import EmployeeSerializer
# from employees.models import Employee
# from rest_framework import mixins, generics

# class EmployeeListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    


# class EmployeeCreateAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)




# ----------------------------------------------------
# Generics
 
# from .serializers import EmployeeSerializer
# from employees.models import Employee
# from rest_framework import generics

# class EmployeeListAPIView(generics.ListAPIView, generics.CreateAPIView): 
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# OR

# class EmployeeListAPIView(generics.ListCreateAPIView): 
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class EmployeeCreateAPIView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     # based on what we want to take out data
#     lookup_field = 'pk'  # based on primary key

# OR

# class EmployeeCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     # based on what we want to take out data
#     lookup_field = 'pk'
    



# ----------------------------------------
# ViewSet :-
# (i) - using viewsets.ViewSet

# from .serializers import EmployeeSerializer
# from employees.models import Employee
# from rest_framework import viewsets
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# class EmployeeViewSet(viewsets.ViewSet): 
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def create(self, request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 




# ----------------
# ViewSet :-
# (ii) - using viewsets.ModelViewSet

from .serializers import EmployeeSerializer
from employees.models import Employee
from rest_framework import viewsets
from rest_framework.response import Response
from .paginations import CustomPagination

class EmployeeViewSet(viewsets.ModelViewSet): 
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
    pagination_class = CustomPagination




# --------------------------------------------------------------------------------------------------------
# Blog & Comments:-

from rest_framework import generics
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer

class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# primary key based operation
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class commentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    lookup_field = 'pk'