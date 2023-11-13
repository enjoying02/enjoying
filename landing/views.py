from django.shortcuts import render
def enjoying(request):

    return render(
        request,
        'landing/Enjoying.html',
    )
