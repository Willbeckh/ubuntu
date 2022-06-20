from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from hood.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.forms.models import inlineformset_factory

from django.core.exceptions import PermissionDenied

from hood.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout



# Create your views here.
def Home(request):

    return render ( request ,'hood/home.html')

def LoginPage(request):
    # grab the fields from the form
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')


        #authenitcate if user is in db

        user = authenticate(request, username=username, password=password)

        # if the useer exists log thm in
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.info(request, 'username or password is incorrect')




    



    return render(request ,'hood/login.html',)



def Register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'account was created successfully for ' + user)
            return redirect('login')
    



    return render(request ,'hood/register.html',{"form":form})



def LogoutUser(request):
    logout(request)
    



    return redirect('login')




def profile(request):

    return render(request, 'hood/profile.html')


@login_required()
def edit_user(request , pk):
    user = User.objects.get(pk=pk)

    user_form = UserForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('bio','avatar'))
    formset = ProfileInlineFormset(instance=user)



    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == 'POST':
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)



                if formset.is_valid():

                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('profile')
        return render(request, 'hood/profile_update.html',{"noodle":pk,"noodle_form":user_form,"formset":formset,})
    else:
        raise PermissionDenied  


           



