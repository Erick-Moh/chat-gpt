import openai
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from .validators import is_valid_input
from django.contrib.auth.decorators import login_required
from .forms import ChatForm
from .models import Chat


def setUp(prompt):
    try:
        openai.api_key = settings.KEY
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.5,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response.choices[0].text
    except Exception as exec:
        return redirect(reverse('chatting'))

@login_required(login_url='login')
def chatting(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['quiz']
            Chat.objects.create(
                user = request.user,
                quiz = prompt,
            )
            if is_valid_input(prompt):
                response = setUp(prompt)
            else:
                form._errors['quiz'] = form.error_class(['Invalid input'])
                response = ''
            context = {
                'form': form,
                'res': response
            }
            return render(request, 'chat.html', context)
        return render(request, 'chat.html', {'form':form})
    context = {
        'form': ChatForm()
    }
    return render(request, 'chat.html', context)
