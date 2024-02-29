from django.shortcuts import render,redirect
from .forms import TeacherForm

# Create your views here.
def teacher_list(request):
    return render(request, "staff/teacher_list.html")

def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "staff/teacher_form.html",{'form':form})
    else:
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/teacher/list')    

def teacher_delete(request):
    return
