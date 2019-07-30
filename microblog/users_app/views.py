from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from blog_app.models import Item
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import getmac


class RegistrationView(View):

    def get(self, request):
        template = 'users_app/join.html'
        title = 'Registraion'
        context = {'title': title}
        return render(request, template, context)

    def post(self, request):
        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        re_password = request.POST.get('re_password', '')

        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('users_app:registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('registration')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                    #is_active=False
                )
                user.save()
                messages.info(request, 'User Created!')
        else:
            messages.info(request, 'Password Not Matching')

        return redirect('registration')


class LoginView(RegistrationView):

    def get(self, request):
        template = 'users_app/login.html'
        title = 'Login'
        context = {'title': title}
        return render(request, template, context)

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password, is_superuser=False)

        if user:
            auth.login(request, user)
            return redirect('users_app:dashboard')

        else:
            messages.info(request, 'Invalid Credential! Please try again...')
            return redirect('login')


@login_required
def dashboard(request):
    template = 'users_app/user_dashboard.html'
    title = 'Dashboard | Chocolat'
    mac_id = getmac.get_mac_address()
    #item = Item.objects.filter(Q(create_by=request.user) | Q(mac_address=mac_id))
    item = Item.objects.filter(create_by=request.user)
    context = {
        'title': title,
        'item': item
    }
    return render(request, template, context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
