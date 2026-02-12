from django.urls import path
from .views import *

urlpatterns=[
    path('<int:student_id>/',student_result,name='student_result'),
]