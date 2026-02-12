from django.urls import path
from .views import *

urlpatterns=[
    path('',exam_list,name='exam_list'),# API
    path('<int:exam_id>/questions/',question_list,name='question_list'),# API
    path('<int:exam_id>/take/',take_exam,name='take_exam'),# REAL EXAM
]