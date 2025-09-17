import django_filters
from .models import Employee

# Filter By Designation :-
# class EmployeeFilter(django_filters.FilterSet):
#     designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')

#     class Meta:
#         model = Employee
#         fields = ['designation']



# Filter By Employee Name & Designation :-
# class EmployeeFilter(django_filters.FilterSet):
#     designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
#     emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')

#     class Meta:
#         model = Employee
#         fields = ['designation', 'emp_name']



# Filter By Employee ID(Primary-Key) Range :-
# class EmployeeFilter(django_filters.FilterSet):
#     designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
#     emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')

#     # RangeFilter - only work with Integer Field
#     id = django_filters.RangeFilter(field_name='id')

#     class Meta:
#         model = Employee
#         fields = ['designation', 'emp_name', 'id']



# Filter By Created ID of Employee (emp_id) :-
class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')

    id_min = django_filters.CharFilter(method='filter_by_id_range', label='from emp_id')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='to emp_id')

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, name, value): 
        if name == 'id_min':
            return queryset.filter(emp_id__gte = value) 
        elif name == 'id_max':
            return queryset.filter(emp_id__lte = value) 
        return queryset