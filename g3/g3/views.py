from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from file.models import student
# from django.views import View

def home(request):
    try:
     if request.method == 'POST':
        stu = request.POST.get('user')
        f = request.FILES.get('img')

        data = student(name=stu,file=f)
        data.save()

        fm = student.objects.all()
     else:
        fm = student.objects.all()
        if request.method == 'GET':
           st = request.GET.get('search')
           if st!= None:
              fm = student.objects.filter(name__icontains = st)
           
       
     return render(request,"index.html",{'di':fm})

    except:
        return render(request,"index.html")
    
def delete(request,id):
   if request.method == 'POST':
      de = student.objects.get(pk = id)
      de.delete()
   return HttpResponseRedirect('/')


# @student
def about(request):
   return render(request,"about.html")


