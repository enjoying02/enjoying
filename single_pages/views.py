from level.models import Subject
from django.shortcuts import render

def single_post_page(request, pk):
    subject = Subject.objects.get(pk=pk)

    return render(
        request,
        'single_pages/detail.html',
        {
            'subject': subject,
        }
    )