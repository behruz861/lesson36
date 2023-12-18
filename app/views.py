from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from app.forms import FeedbackForm


def index_view(request):

    # cookie_data = request.COOKIES.get('sessio', 'something')
    # response = render(request,
    #               'app/index.html')
    # response.set_cookie('my_cookie', '12345')
    #
    # return response
    # context = {'cookie_data': cookie_data}
    # return render(request,
    #               'app/index.html',
    #               context)

    session_data = request.session.get('my_var', 'something')

    return render(request, 'app/index.html')


def second_view(request):

    # Create session var
    request.session['my_var'] = 'my_var_value'

    # context = {'session_data': session_data}
    return render(request,
                  'app/second.html')


class FeedbackFormView(SuccessMessageMixin, FormView):
    template_name = 'app/form.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('form')
    success_message = 'Successful form sending!'


def form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            context = {'name': name, 'text': text,
                       'form': FeedbackForm()}

            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Successful form sending!')

            return render(request, 'app/form.html', context)
    context = {'form': FeedbackForm()}
    return render(request, 'app/form.html', context)


