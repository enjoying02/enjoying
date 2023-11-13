from django.shortcuts import render
from .models import Subject
def joiner(request):
    subjects = Subject.objects.all().order_by('-pk')

    return render(
        request,
        'level/joiner.html',
        {
            'subjects': subjects,
        }
    )
