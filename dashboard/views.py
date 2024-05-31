#
from django.shortcuts import render


def index(request):
    context = {
        'name': 'newappuser'  # nameをindex.htmlへ送る
    }
    return render(request, 'accounts/login.html', context)


def about(request):
    return render(request, 'accounts/login.html')
