from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.views import View
from django.contrib import messages
from django.urls import reverse

# local imports
from .forms import UserForm, CreateUserForm
from .models import UserProfile


# Create your views here.
class HomeView(View):
    def get(self, request):
        context = {
            'title': 'Home',
        }
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
    def get(self, request):
        return render(request, 'watch/login.html')

    def post(self, request):
        pass


@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)

    # prepolate the form with the user's data
    user_form = UserForm(instance=user)

    ProfileInlineFormSet = inlineformset_factory(
        User, UserProfile, fields=('photo', 'bio', 'phone', 'block'))
    formset = ProfileInlineFormSet(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
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
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
