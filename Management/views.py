from .telegramBot import TelegramBot
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import QueryDetail, GetInTouch

chat_id = '-1002078539468'  # for testing channel
access_token = '7027505705:AAHMl9A5G4JnbLQj6m9vG_SMoO_QOPIcS-g'  # for testing channel


# Create your views here.

def index(request):
    return render(request, 'index.html')


def queryDetail(request):
    import datetime
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        datetime = datetime.datetime.now()
        my_instance = QueryDetail(name=name, email=email, subject=subject, message=message, querydatetime=datetime)
        message = (
            f"name: {name}\n"
            f"email: {email}\n"
            f"subject: {subject}\n"
            f"message: {message}"
        )

        TelegramBot(chat_id, access_token).sendMessage(message)
        # Save the instance to insert the data into the database
        my_instance.save()
        return redirect('/')
    else:
        return redirect('/')


def get_in_touch(request):
    import datetime
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        datetime = datetime.datetime.now()
        my_instance = GetInTouch(name=name, email=email, phone=phone, message=message, current_datetime=datetime)
        message = (
            f"name: {name}\n"
            f"email: {email}\n"
            f"phone: {phone}\n"
            f"message: {message}"
        )

        TelegramBot(chat_id, access_token).sendMessage(message)
        # Save the instance to insert the data into the database
        my_instance.save()
        return redirect('/')
    else:
        return redirect('/')


def about(request):
    return render(request, 'about.html')


def service_details(request):
    return render(request, 'service-details.html')


def project_details(request):
    return render(request, 'project-details.html')
