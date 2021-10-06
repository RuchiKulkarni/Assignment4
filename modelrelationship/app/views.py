from django.shortcuts import render,redirect
from django.views.generic import DetailView,CreateView
from django.views import View
from.models import department,lecture,student
from .forms import addepartmentform,addstudentform,addlectuerform


def home(request):
        dep_data=department.objects.all()
        return render(request,'pages/home.html',{'depdata':dep_data})

def add_department(request):
        fm=addepartmentform()
        return render(request,'pages/add_department.html',{'form':fm})
def post(request):
        fm=addepartmentform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'pages/add_department.html',{'form':fm})
class add_department(View):
    def get(self,request):
        fm=addepartmentform()
        return render(request,'pages/add_department.html',{'form':fm})
    def post(self,request):
        fm=addepartmentform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'pages/add_department.html',{'form':fm})





                                  #student

def studenthome(request):
        stu_data=student.objects.all()
        return render(request,'pages/studenthome.html',{'studata':stu_data})

class add_student(View):
    def get(self,request):
        a=addstudentform()
        return render(request,'pages/add_student.html',{'form':a})
    def post(self,request):
        a=addstudentform(request.POST)
        if a.is_valid():
            a.save()
            return redirect('/')
        else:
            return render(request,'pages/add_student.html',{'form':a})

def student_search(request):
    if request.method == "POST":
        search=request.POST['search']
        searched=student.objects.filter(name__contains=search) 
        return render(request,'pages/student_search.html',{'search':search,'searched':searched})
    else:
       return render(request,'pages/student_search.html',{'search':search,'searched':searched})


                              #lecture

def lecturehome(request):
        lec_data=lecture.objects.all()
        return render(request,'pages/lecturehome.html',{'lecdata':lec_data})

class add_lecture(View):
    def get(self,request):
        a=addlectuerform()
        return render(request,'pages/add_lecture.html',{'form':a})
    def post(self,request):
        a=addlectuerform(request.POST)
        if a.is_valid():
            a.save()
            return redirect('/')
        else:
            return render(request,'pages/add_lecture.html',{'form':a})

def lecture_search(request):
    if request.method == "POST":
        lecture=request.POST['lecture']
        searched=student.objects.filter(name__contains=lecture) 
        return render(request,'pages/lecture_search.html',{'search':lecture,'searched':searched})
    else:
       return render(request,'pages/lecture_search.html',{'search':lecture,'searched':searched})

        
