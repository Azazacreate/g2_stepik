from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import Form_feedback


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Form_feedback(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/done')
    form = Form_feedback()
    print('nothing')
    return render(request, 'feedback/feedback.html', context={'form': form, })

def done(request):
    return render(request, 'feedback/done.html')