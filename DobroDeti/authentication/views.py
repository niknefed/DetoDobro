from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .models import User, Director, Children
from django.contrib.auth import authenticate, login
from django.urls import reverse


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        context = [

        ]
        return render(request, 'authentication/registration.html', context)

    def post(self, request, *args, **kwargs):
        if User.is_director and User.is_children != False:
            if request.method == "POST":
                context = {'has_error': False, 'data': request.POST}
                email = request.POST.get('email')
                username = request.POST.get('username')
                password = request.POST.get('password')
                passwordrep = request.POST.get('password2')
                name = request.POST.get('name')
                surname = request.POST.get('surname')
                address = request.POST.get('address')
                phone = request.POST.get('phone')
                title = request.POST.get('title')

                if len(password) < 6:
                    messages.add_message(request, messages.ERROR, 'Пароль должен быть больше чем 6 символов')
                    context['has_error'] = True

                if password != passwordrep:
                    messages.add_message(request, messages.ERROR, 'Введённые пароли не совпдают')
                    context['has_error'] = True

                if not username:
                    messages.add_message(request, messages.ERROR, 'Введите логин')
                    context['has_error'] = True

                if User.objects.filter(username=username).exists():
                    messages.add_message(request, messages.ERROR, 'Этот логин уже занят')
                    context['has_error'] = True

                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Этот EMAIL занят')
                    context['has_error'] = True

                if User.objects.filter(address=address).exists():
                    messages.add_message(request, messages.ERROR, 'Аккаунт с таким адресом уже существует')
                    context['has_error'] = True

                if User.objects.filter(phone=phone).exists():
                    messages.add_message(request, messages.ERROR, 'Аккаунт с таким номером телефона уже существует')
                    context['has_error'] = True

                if User.objects.filter(title=title).exists():
                    messages.add_message(request, messages.ERROR, 'Детский дом с таким названием уже сушествует')
                    context['has_error'] = True

                if context['has_error']:
                    return render(request, 'authentication/registration.html', context)

                user = User.objects.create_user(username=username, email=email, first_name=name, last_name=surname,
                                                address=address, phone=phone)
                user.set_password(password)
                user.save()

                return redirect('login')

        return render(request, 'authentication/registration.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'authentication/login.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            context = {'data': request.POST}
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user:

                return render(request, 'authentication/login.html', context)

            if not user:
                messages.add_message(request, messages.ERROR, 'Неверные учётные данные')
                return render(request, 'authentication/login.html', context)
            login(request, user)

            return redirect(reverse('home'))

        return render(request, 'authentication/login.html')
