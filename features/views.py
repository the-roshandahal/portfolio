from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def home(request):
    about = About.objects.all().order_by('-created').first()
    experience = Experience.objects.all().order_by('order')
    education = Education.objects.all().order_by('order')
    skill = Skills.objects.all().order_by('order')
    project = Project.objects.all().order_by('order')
    testimonial = Testimonials.objects.all().order_by('order')
    context ={
        'about':about,
        'experience':experience,
        'education':education,
        'skill':skill,
        'project':project, 
        'testimonial':testimonial,
    }
    return render (request,'index.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        Contact.objects.create(name=name,email=email,phone=phone,message=message)
        return redirect('home')