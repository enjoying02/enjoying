from django.shortcuts import render
from .models import Subject, Category
def joiner(request):
    subjects = Subject.objects.all().order_by('-pk')


    return render(
        request,
        'level/joiner.html',
        {
            'subjects': subjects,
        }
    )

def single_post_page(request, pk):
    subject = Subject.objects.get(pk=pk)

    return render(
        request,
        'single_pages/detail.html',
        {
            'subject': subject,
        }
    )