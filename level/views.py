from django.shortcuts import render
from .models import Subject
def joiner(request):
    subjects = Subject.objects.all()

    return render(
        request,
        'level/joiner.html',
        {
            'subjects': subjects,
        }
    )
