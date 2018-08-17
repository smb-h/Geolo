from django.shortcuts import render



def home_view(request):

    template = 'home.html'

    meta = request.META
    context = {
        'meta': meta,
    }


    return render(request, template, context)

