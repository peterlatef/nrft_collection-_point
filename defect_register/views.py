from django.shortcuts import render, redirect
from .forms import DefectForm
from .models import Defect

# Create your views here.

def defects_list(request):
    context = {'defect_list':Defect.objects.all()}
    return render(request, "defect_register/defect_list.html", context)

def defect_form(request, id=0):
    if request.method == "GET":
        # to identify insert or update operations 
        if id == 0:
            form = DefectForm()

        else:
            defect = Defect.objects.get(pk = id)
            form = DefectForm(instance=defect)
        return render(request, "defect_register/defect_form.html",{'form':form})
    else:
        if id == 0:
            form = DefectForm(request.POST)
        else:
            defect = Defect.objects.get(pk = id)
            form = DefectForm(request.POST, instance=defect)

        for field in form:
            print("Field Error:", field.name,  field.errors)          
        if form.is_valid():
            form.save() 
            return redirect('/defects/list/')
        
def defect_delete(request):
    return
