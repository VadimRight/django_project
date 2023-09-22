from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


def hard_skills(request):
    hard_skills = Articles.objects.all()
    return render(request, 'hard_skills/hard_skills.html', {'hard_skills': hard_skills})

