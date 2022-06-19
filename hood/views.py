from django.shortcuts import render , redirect
from django.contrib import messages
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