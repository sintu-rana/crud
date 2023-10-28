from django.shortcuts import render, redirect
from app.models import Employee

# Create your views here.

def view_create(request):
        if request.method=='POST':
            data=request.POST

            name=data.get('name')
            age=data.get('age')
            mobile=data.get('mobile')
            city=data.get('city')
            pic=request.FILES.get('pic')

            Employee.objects.create(
                name=name,
                age=age,
                mobile=mobile,
                city=city,
                pic=pic
            )
        
        # return render(request, 'app/Create.html')
            return redirect('/app/table/')
        else:
        
        # Display a form for data input
            return render(request, 'app/create.html')


def view_table(request):
    if request.method == "POST":
        resp=render(request, 'app/table.html')
        return resp
    elif request.method == "GET":
        s=Employee.objects.all()
        d1={'emp':s}
        resp=render(request, 'app/table.html', context=d1)
        return resp

def view_update(request, id):
    queryset=Employee.objects.get(id = id)

    if request.method=="POST":
        data=request.POST

        name=data.get('name')
        age=data.get('age')
        mobile=data.get('mobile')
        city=data.get('city')
        pic=request.FILES.get('pic')

        queryset.name=name
        queryset.age=age 
        queryset.mobile=mobile
        queryset.city=city

        if pic:
            queryset.pic=pic
    
        queryset.save()
        return redirect('/app/table/')
    
    context={'emp':queryset}
    return render(request,'app/update.html', context)



def view_delete(request, id):
    queryset=Employee.objects.get(id = id)
    queryset.delete()
    return redirect('/app/table/')


def view_view(request,eid=None):
    mydict={}
    one_rec = Employee.objects.get(pk=eid)
    mydict['emp']=one_rec
    return render(request,'''app/view.html''',mydict)

    
