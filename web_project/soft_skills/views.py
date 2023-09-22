from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


def soft_skills(request):
    soft_skills = Articles.objects.all()
    return render(request, 'soft_skills/soft_skills.html', {'soft_skills': soft_skills})

