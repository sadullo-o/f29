import datetime

from django.shortcuts import render, HttpResponse, redirect
from .models import OurTeam, AboutUs, News, Contact, TXabar
from .forms import ContactForm

# Create your views here.

def home(request):

    news1 = News.objects.all()[:3]
    news2 = News.objects.all()[3:]

    # Create
    # news = News(rasm='http://127.0.0.1:8000/static/main/assets/img/post-landscape-2.jpg', type='SPORT', title='Test Create')  # datetime  #date
    # news.save()

    context = {
        'news1':news1,
        'news2': news2
    }

    if request.method == 'POST':
        xabar = request.POST.get('xabar')

        x = TXabar(xabar=xabar)
        x.save()

        return redirect('home')



    return render(request, 'main/index.html', context)

def about(request):

    ourteam = OurTeam.objects.all()

    aboutus = AboutUs.objects.first()

    mission = AboutUs.objects.last()


    test = [12,4,4364,65,436,78]

    context = {
        'ourteam': ourteam,
        'aboutus': aboutus,
        'm':mission,
        't': test
    }

    return render(request, 'main/about.html', context)


def contact(request):

    # if request.method == 'POST':
    #     ism = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    #
    #     c = Contact(name=ism, email=email, subject=subject, message=message)
    #     c.save()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')




    return render(request, 'main/contact.html')


def single_post(request):

    return render(request, 'main/single-post.html')


def search(request):

    return render(request, 'main/search-result.html')



# https://getbootstrap.com/

# https://bootstrapmade.com/mentor-free-education-bootstrap-theme/#download

# django-admin startproject nomi


# CRUD - Create, Read, Update, Delete, contact form


# wsssss