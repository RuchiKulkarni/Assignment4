from django.urls import path 
from . import views
from .views import add_department,add_lecture,add_student
urlpatterns = [
    
    path('',views.home,name='home'),
    path('add_department/',add_department.as_view(),name='add_department'),
    path('lecturehome/',views.lecturehome,name='lecturehome'),
    path('add_lecture/',add_lecture.as_view(),name='add_lecture'),
    path('studenthome/',views.studenthome,name='studenthome'),
    path('add_student/',add_student.as_view(),name='add_student'),
    path('search/',views.student_search,name='search'),
    path('lecture/',views.lecture_search,name='lecture')
]