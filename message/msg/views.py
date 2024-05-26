from msg.models import Message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

'''
render(request,'html_file_path',dict)
'''

# Create your views here.
class ContactForm(View):
    def get(self,request,sid):
        return HttpResponse("This is Contact Page"+ sid)
    
def about(request):
    #return HttpResponse("This is about page")
    a=10
    b={'a':10}
    b[a]=a
    return render(request,'about.html',b)

def edit(request,id):
    '''print(id)
    return HttpResponse("This is from edit function"+ eid)'''
    if request.method=='GET':
        m=Message.objects.filter(id=id)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        un=request.POST['uname']
        ue=request.POST['email']
        um=request.POST['mob']
        umsg=request.POST['msg']
        '''print(un)
        print(ue)
        print(um)
        print(umsg)'''
        m=Message.objects.filter(id=id)
        m.update(name=un,email=ue,mob=um,msg=umsg)
        return redirect('/dashboard') 

def hello(request):
    context={}
    context['x']=10
    context['y']=20
    context['z']=30
    context['l']=[10,20,30,40]
    context['product']=[
        {'id':1,'name':'oneplus','price':80000},
        {'id':2,'name':'iphone','price':30000}
    ]
    return render(request,'hello.html',context)
def base(request):
    return render(request,'base.html')

def inheritance(request):
    return render(request,'inheritance.html')

def msg(request):
    '''
    Data  retriving from HTML:
    variable=request.POST['value of name attribute'] 
    '''
    #print(request.method)
    if request.method=='GET':
        return render(request,'message.html')
    else:
        n=request.POST['uname']
        e=request.POST['email']
        m=request.POST['mob']
        msg=request.POST['msg']
        '''  print(n)
        print(e)
        print(m)
        print(msg) '''

        m=Message.objects.create(name=n,email=e,mob=m,msg=msg)
        m.save()
        #return HttpResponse("success")
        return redirect('/dashboard')
def dashboard(request):
    m=Message.objects.all()
    print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
def delete(request,did):
    m=Message.objects.filter(id=did)
    m.delete()
    return redirect('/dashboard')