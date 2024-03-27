from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'iRiseup.html')


def about(request):
    return render(request, 'about.html')


def editing(request):
    return render(request, 'editing.html')


def publishing(request):
    return render(request, 'publishing.html')


def design(request):
    return render(request, 'design.html')


def marketing(request):
    return render(request, 'marketing.html')


def blog(request):
    return render(request, 'bloglist.html')


def contact(request):
    return render(request, 'contact.html')
