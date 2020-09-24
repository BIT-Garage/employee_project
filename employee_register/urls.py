from employee_register.views import employee_delete
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.employee_form,name='employee_insert'),
    path('<int:id>/',views.employee_form,name='employee_update'),
    path('list/',views.employee_list,name='employee_list'),
    path('form/',views.employee_form),
    path('delete/<int:id>',views.employee_delete, name='employee_delete'),
]