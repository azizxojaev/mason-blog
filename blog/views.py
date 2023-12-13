from django.shortcuts import render
import requests
from .models import Gallery, Timeline, About, ContactInfo


def home_page(request):
    photos = Gallery.objects.all()
    context = {
        'url_name': 'home',
        'photos': photos
    }
    return render(request, 'index.html', context=context)


def about_page(request):
    about_text = About.objects.get(id=1)
    context = {
        'url_name': 'about',
        'about_text': about_text
    }
    return render(request, 'about.html', context=context)


def timeline_page(request):
    timelines = Timeline.objects.all()
    context = {
        'url_name': 'timeline',
        'timelines': timelines
    }
    return render(request, 'timeline.html', context=context)


def contact_page(request):
    contact_info = ContactInfo.objects.all().first()
    context = {
        'url_name': 'contact',
        'info': contact_info
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        apiToken = '6703829567:AAGFKyK3czwvSltX6MO4C1U9gDn5ZZcSGEg'
        chatID = '-4099543912'
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

        try:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': f"Сообщение от: {name}\nЭмейл: {email}\n\n{message}"})
            print(response.text)
        except Exception as e:
            print(e)
    return render(request, 'contact.html', context=context)
