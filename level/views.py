from django.shortcuts import render
from .models import Subject, Category

def joiner(request):
    category = Category.objects.get(slug='joiner')
    subjects = Subject.objects.filter(category=category).order_by('-pk')


    return render(
        request,
        'level/joiner.html',
        {
            'subjects': subjects,
        }
    )

def beginner(request):
    category = Category.objects.get(slug='beginner')
    subjects = Subject.objects.filter(category=category).order_by('-pk')


    return render(
        request,
        'level/joiner.html',
        {
            'subjects': subjects,
        }
    )

def pro(request):
    category = Category.objects.get(slug='professional')
    subjects = Subject.objects.filter(category=category).order_by('-pk')


    return render(
        request,
        'level/joiner.html',
        {
            'subjects': subjects,
        }
    )



def friends(request):
    category = Category.objects.get(slug='friends')
    subjects = Subject.objects.filter(category=category).order_by('-pk')


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
