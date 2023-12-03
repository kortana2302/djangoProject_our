from django.views.generic import ListView, TemplateView
from .models import Post, Users, Users_Auth
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['username'] = Users_Auth.objects.get(authorized=1)
        except:
            context['username'] = ''
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['username'] = Users_Auth.objects.get(authorized=1)
        except:
            context['username'] = ''
        return context


class ImputPageView(TemplateView):
    template_name = 'imput.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['username'] = Users_Auth.objects.get(authorized=1)
        except:
            context['username'] = ''
        return context

class ModelPageView(TemplateView):
    template_name = 'model.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['username'] = Users_Auth.objects.get(authorized=1)
        except:
            context['username'] = ''
        return context

class ExamplePageView(TemplateView):
    template_name = 'example.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['username'] = Users_Auth.objects.get(authorized=1)
        except:
            context['username'] = ''
        return context

class EnterForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=100)
    password = forms.CharField(label="Пароль", max_length=100)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=100)
    password = forms.CharField(label="Пароль", max_length=100)
    first_name = forms.CharField(label="Имя", max_length=100)
    last_name = forms.CharField(label="Фамилия", max_length=100)
def get_enter(request):
    data = Users_Auth.objects.values_list()
    if len(data) > 0:
        username = data[0][0]
    else:
        username = ''
    if request.method == "POST":
        form = EnterForm(request.POST)
        if form.is_valid():
            try:
                data = Users.objects.get(user_name=form.cleaned_data['username'])
                password = data.password
                if password!=form.cleaned_data['password']:
                    error = 'Неверный пароль'
                    return render(request, "enter.html", {"form": form, "username": username, 'error': error})
            except:
                error = 'Такого логина нет'
                return render(request, "enter.html", {"form": form, "username": username, 'error':error})
            Users_Auth.objects.all().delete()
            b = Users_Auth(user_name=form.cleaned_data['username'],
                      authorized=1)
            b.save()
            return HttpResponseRedirect('/')
    else:
        form = EnterForm()
    return render(request, "enter.html", {"form": form,"username":username})
def get_register(request):
    data = Users_Auth.objects.values_list()
    if len(data) > 0:
        username = data[0][0]
    else:
        username = ''
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                data = Users.objects.get(user_name=form.cleaned_data['username'])
                error = 'Такой логин уже существует'
                return render(request, "register.html", {"form": form, "username": username, 'error':error})
            except:
                b = Users(user_name=form.cleaned_data['username'],
                          password=form.cleaned_data['password'],
                          first_name=form.cleaned_data['first_name'],
                          last_name=form.cleaned_data['last_name'])
                b.save()
                return HttpResponseRedirect('/enter')
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form,"username":username})

def get_logout(request):
    data = Users_Auth.objects.values_list()
    if len(data) > 0:
        username = data[0][0]
    else:
        username = ''
    if request.method == "POST":
        Users_Auth.objects.all().delete()
        return HttpResponseRedirect('/')
    return render(request, "logout.html", {"username":username})


