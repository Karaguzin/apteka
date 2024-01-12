from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task, Drug, Feedback

# Create your views here.

links = [
    {'link': 'ORVI'}, {'link': 'Painkillers'}, {'link': 'Throat'}, {'link': 'Antipyretics'}, {'link': 'Nose'}
]


def get_link(request, r_slug):
    return redirect(reverse(r_slug), permanent=True)


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Apteka', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def ORVI(request):
    return render(request, 'main/ORVI.html', {'remedies': Drug.objects.filter(purpose='ОРВИ')})


def Antipyretics(request):
    return render(request, 'main/Antipyretics.html', {'remedies': Drug.objects.filter(purpose='Жаропонижающее')})


def Painkillers(request):
    return render(request, 'main/Painkillers.html', {'remedies': Drug.objects.filter(purpose='Обезболивающие')})


def Throat(request):
    return render(request, 'main/Throat.html', {'remedies': Drug.objects.filter(purpose='Горло')})


def Nose(request):
    return render(request, 'main/Nose.html', {'remedies': Drug.objects.filter(purpose='Насморк')})


def product_orvi(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)


def product_antipyretics(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)


def product_painkillers(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)


def product_throat(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)


def product_nose(request, product_slug):
    this = Drug.objects.get(slug=product_slug).__dict__
    return render(request, 'main/product.html', context=this)


def feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'main/feedback.html', context={'title': 'Обратная связь', 'feedbacks' : feedbacks})


def message_ok(request):
    if request.POST:
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')
        Feedback.objects.create(name=name, email=email,phone=phone,message=message)
        return render(request, 'main/message_ok.html', context={'title': 'Сообщение отправлено'})


# Обработка ошибок
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def InternalServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')


def ErrBadRequest(request, exception):
    from django.http import HttpResponseBadRequest
    return HttpResponseBadRequest('<h1>Плохой запрос</h1>')


def feedbacks_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'main/feedback.html', context = {'feedbacks': feedbacks})