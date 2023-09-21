from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def soft_skills(request):
    return render(request, 'soft_skills/soft_skills.html')

