import django
from django.conf import settings
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.urls import reverse

from .models import Profile, User
from .forms import CreateUserForm
from .utils import generate_token
# Create your views here.


def send_action_email(user, request):
    """Retrieve user model and send email to user and return status 200.

    Args:
        user (Profile): extended model from user
    """
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('users/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )
    email.send()


def home(request):
    """Render home page."""
    return render(request, "users/temp_home.html")


def index(request):
    """Render index page."""
    return render(request, "users/index.html")


def register(request):
    """Add user to database.

    Returns:
        Httprequest: return register page with status 403 if registeration fail
                     and return login page with status 200 if registeration success
    """
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Profile.objects.create(
                user=user,
                username=username,
            )
            send_action_email(user, request)
            return redirect('login')
        return render(request, "users/register.html", {'form': form}, status=403)

    return render(request, "users/register.html", {'form': form})


def loginPage(request):
    """Send user to home page if user put right username and password.

    Returns:
        Httprequest: return home page with status 302 if user put right username and password.
                     And return login page with status 401 if use put wrong
    """
    context = {
        'has_error': False
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if not user.profile.is_email_verified:
                messages.info(
                    request, 'Email is not verified, please check your email inbox')
                context['has_error'] = True
            else:
                login(request, user)
                return redirect('temphome')
        else:
            messages.info(
                request, 'Username or Password is incorrect')
            context['has_error'] = True

    if context['has_error']:
        return render(request, "users/login.html", status=401)

    return render(request, "users/login.html")


def logoutUser(request):
    """Logout user.

    Returns:
        Httprequest: return login page after logout
    """
    logout(request)
    return redirect('login')


def activate_user(request, uidb64, token):
    """Change is_email_verified to true if token are right.

    Retrieve uidb64 and token from activation link. which uidb64
    is encoded.

    Args:
        uidb64 (string): encoded user id(uid)
        token (string): string of token

    Returns:
        Httprequest: return login page if user verified success with statuss 302 and
                     return activate-fail with status 401 if user verified fail
    """
    try:
        # decode uid
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    # check user and token
    if user and generate_token.check_token(user, token):
        user.profile.is_email_verified = True
        user.profile.save()
        messages.info(request, 'Email verified')
        return redirect(reverse('login'))
    return render(request, "users/activation-fail.html", {"user": user}, status=401)
