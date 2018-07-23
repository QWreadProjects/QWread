import logging

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from QWreadProjects import settings
from users.forms import RegisterForm


@csrf_exempt
def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            email = request.POST.get('email')
            print(email)
            send_mail(
                subject='注册成功！',
                message='恭喜{}注册成功！'.format(username),
                from_email=settings.EMAIL_FROM,
                recipient_list=[email, ],
                fail_silently=False,
            )
        if redirect_to:
            return redirect(redirect_to)
        else:
            return redirect('qwread/index/')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html',
                  context={'form': form, 'next': redirect_to})
