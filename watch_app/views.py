from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.views import View

# local imports
from .forms import UserForm, CreateUserForm
from .models import Business, Facility, UserProfile, Neighborhood, Post


# Create your views here.
class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        try:
            user = request.user
            profile = UserProfile.objects.get(user=user)
            facilities = Facility.objects.filter(
                neighborhood=profile.neighborhood)
            businesses = Business.objects.filter(
                neighborhood=profile.neighborhood)
            posts = Post.objects.filter(neighborhood=profile.neighborhood).order_by('-timestamp')
            # posts = Post.objects.all().order_by('-timestamp')
            context = {
                'title': 'Home',
                'data': profile,
                'facilities': facilities,
                'businesses': businesses,
                'posts': posts
            }
            return render(request, 'watch/index.html', context)
        except UserProfile.DoesNotExist:
            profile = None
            facilities = None
            businesses = None
        return render(request, 'watch/index.html', context)


# user register view
class RegisterView(View):
    """This class view is used to render the register page and execute user registrations."""
    form = CreateUserForm()
    ctx = {
        'title': 'Register',
        'form': form,
    }

    def get(self, request):
        return render(request, 'watch/register.html', self.ctx)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateUserForm()  # reset form
            messages.success(request, 'User created successfully.')
            return redirect(reverse('watch:login'))
        context = {
            form: form,
        }
        return render(request, 'watch/register.html', context)


class LoginView(View):
    context = {
        'title': 'Login'
    }

    def get(self, request):
        return render(request, 'watch/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('watch:home'))
        else:
            messages.error(request, 'Invalid username or password.')

        return render(request, 'watch/login.html', self.context)


# logout view
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("watch:home")


class ProfileView(LoginRequiredMixin, View):
    login_ur = '/login/'
    """this class view is used to render the profile page and execute user profile updates."""

    def get(self, request):
        user = request.user
        profile = get_object_or_404(UserProfile, user=user)
        context = {
            'title': 'Profile',
            'user_data': user,
            'profile_data': profile,

        }
        return render(request, 'watch/profile.html', context)


@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)

    # prepolate the form with the user's data
    user_form = UserForm(instance=user)

    ProfileInlineFormSet = inlineformset_factory(
        User, UserProfile, fields=('photo', 'bio', 'phone', 'street', 'neighborhood'))
    formset = ProfileInlineFormSet(instance=user)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == 'POST':
            user_form = UserForm(
                request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormSet(
                request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormSet(
                    request.POST, request.FILES, instance=created_user)
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/profile/')

        return render(request, 'watch/edit_profile.html', {
            "pk": pk,
            "user_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
