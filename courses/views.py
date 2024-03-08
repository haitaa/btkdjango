from django.http import HttpResponse

def home(request):
    return HttpResponse('Anasayfa')

def courses(request):
    return HttpResponse("Kurs Listesi")