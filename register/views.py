from django.shortcuts import render
from django.http import HttpResponseRedirect
from register.models import Email

def get_name(request):
    # if this is a POST request, need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = contact(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/Thanks/')

    # if a GET (or any other method), create a blank form
    else:
        form = contact()

    return render(request, 'register/index.html', {'form': form})

