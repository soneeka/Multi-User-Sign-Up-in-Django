from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from .models import Staff,Doctor,Patient
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect
#from django.views.generic import CreateView,UpdateView
from django.utils.decorators import method_decorator
#from ..decorators import doctor_required
# from django.urls import reverse_lazy
from .forms import PostForm
from django import forms
from .models import Post
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

def home(request):
	return render(request,'home.html')
def aboutus(request):
	return render(request,template_name='aboutus.html')
def department(request):
	return render(request,template_name='department.html')
def forgetpw(request):
	return render(request,template_name='forgetpw.html')
def resetpw(request):
	return render(request,template_name='resetpw.html')
def profiles(request):
	args={'form':PostForm}
	return render(request,'profile.html',args)
def user(request):
	if(request.method == "POST"):
		body = request.POST.dict()
		print body['userType']
		if(body['userType'] == "patient"):
			patient = Patient(	username= body['username'],
								password=body['password'],
								name=body['name'])
			patient.save()
		if(body['userType'] == "doctor"):
			doctor = Doctor(	username= body['username'],
								password=body['password'],
								name=body['name'])
			doctor.save()
		if(body['userType'] == "staff"):
			staff = Staff(	username= body['username'],
								password=body['password'],
								name=body['name'])
			staff.save()


	return render(request,template_name='home.html')
class HomeView(TemplateView):
	Medicines=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Medicines'}))
	post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Write a post...'}))
	Documents = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control','placeholder': 'upload a file'}))
	class Meta:
		model = Post
		fields = ('post','Documents','Medicines',)



'''def slideshow(request):
	images = Image.objects.all()
    return render(request, "home.html", {'images': images})
'''
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

    