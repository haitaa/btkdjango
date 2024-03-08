from django.urls import path
from courses.views import home, courses

urlpatterns = [
    path('', home),
    path('home/', home),
    path('courses/', courses),
]
