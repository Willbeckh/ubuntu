from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from hood.models import *
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.forms.models import inlineformset_factory

from django.core.exceptions import PermissionDenied

from hood.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout



# Create your views here.
@login_required(login_url='login')
def Home(request):

    # get current user 
    current_user = request.user

    print(current_user.id)

    # get current users neighbourhood


    profile = Profile.objects.filter(user_id=current_user.id).first()
    print(profile)
    print()

    # check if user has neighbourhood
    if profile is None:
        profile = Profile.objects.filter(user_id=current_user.id).first()#get profile
        posts = Post.objects.filter(user_id=current_user.id)
        # get locations 
        locations = Location.objects.all()
        neighbourhood = NeighbourHood.objects.all()
        contacts = Contact.objects.filter(user_id=current_user.id)
        businesses = Business.objects.filter(user_id=current_user.id)

        return render (request ,'hood/home.html' , {"posts":posts,"locations":locations,"neighbourhood":neighbourhood,"contacts":contacts,"businesses":businesses})
    else:
        neighbourhood = profile.neighbourhood

        posts = Post.objects.filter(neighbourhood=neighbourhood).order_by("-created_at")
        return render(request ,'hood/home.html',{'posts':posts})




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

    current_user = request.user
    profile = Profile.objects.filter(user=current_user.id).first()
    posts = Post.objects.filter(user_id=current_user.id)
    # getlocations
    locations = Location.objects.all()
    neighbourhood = NeighbourHood.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    contacts = Contact.objects.filter(user_id=current_user.id)
    return render(request, 'hood/profile.html', {"profile":profile,"posts":posts,"locations":locations,"neighbourhood":neighbourhood,"businesses":businesses,"contacts":contacts})




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


           

# business page 
@login_required()
def Businesses(request):
    # get current user 
    current_user = request.user

    print(current_user.id)

    # get current users neighbourhood


    profile = Profile.objects.filter(user_id=current_user.id).first()
    print(profile)
    print()

    # check if user has neighbourhood
    if profile is None:
        profile = Profile.objects.filter(user_id=current_user.id).first()#get profile
        posts = Post.objects.filter(user_id=current_user.id)
        # get locations 
        locations = Location.objects.all()
        neighbourhood = NeighbourHood.objects.all()
        contacts = Contact.objects.filter(user_id=current_user.id)
        businesses = Business.objects.filter(user_id=current_user.id)

        return render (request ,'hood/business.html' , {"posts":posts,"locations":locations,"neighbourhood":neighbourhood,"contacts":contacts,"businesses":businesses})
    else:
        
        neighbourhood = profile.neighbourhood
        #get all biashara in the hood
        businesses = Business.objects.filter(neighbourhood=profile.neighbourhood) #.order_by("-created_at")
        return render(request ,'hood/business-page.html',{"businesses":businesses})


# profile update function 
@login_required()
def Update_Profile(request):

    if request.method == 'POST':



        current_user = request.user

        profile = Profile.objects.filter(user=current_user).first()
        # neighbourhood = NeighbourHood.objects.filter(user=current_user).first()
        
        print (profile)
        

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        profile_pic = request.FILES['profile_pic']

        # profile.first_name = first_name
        profile.avatar = profile_pic

        profile.save()
        
        name = request.POST["first_name"]+ " " + request.POST["last_name"]

        location = request.POST["location"]
        neighbourhood = request.POST['neighbourhood']


        print(neighbourhood)

        # neighbourhood.name = neighbourhood_loc
        # neighbourhood.location = location
        # neighbourhood.save()


        # proofcheckthelocation

        if location == "":

            location = None
        else:
            location = Location.objects.get(name=location)

        # proofcheck if ithashood

        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = NeighbourHood.objects.get(name=neighbourhood)


        # profile.first_name = first_name
        # profile.avatar = profile_pic

        # profile.save()
        

        user = User.objects.get(id= current_user.id)



        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.profile.neighbourhood = neighbourhood
        print(user.profile.neighbourhood)
       

        user.save()
        user.profile.save()


        return redirect('profile')

    else:
        return render(request, "hood/profile.html", {"danger":"profileupdatefailed"})




@login_required()
def create_post(request):

    if request.method == 'POST':

        current_user = request.user

        title = request.POST["title"]
        content = request.POST["content"]
        location = request.POST["location"]



        poster = request.FILES["image"]





        #get user neighbourhood
        profile = Profile.objects.filter(user_id=current_user.id).first()


        if profile is None:
            profile = Profile.objects.filter(
            user_id=current_user.id).first()  # get profile
            posts = Post.objects.filter(user_id=current_user.id)
            # get all locations
            locations = Location.objects.all()
            neighbourhood = NeighbourHood.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            # redirect to profile with error message
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighbourhood = profile.neighbourhood


         # check if its an instance of location
        if location == "":
            location = None
        else:
            location = Location.objects.get(name=location)

        


        post = Post(user_id=current_user.id,title=title, content=content,image=poster,location=location,neighbourhood=neighbourhood,)
        post.create_post()
        return redirect("/profile", {"success": "Post Created Successfully"})

    else:
        return redirect("/profile", {"success": "Post Created Successfully"})


# create business
@login_required()
def create_business(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST["name"]
        email = request.POST["email"]
        description = request.POST["description"]
        # phone = request.POST["phone"]
        # address = request.POST["address"]
        # location = request.POST["location"]
        # neighbourhood = request.POST["neighbourhood"]

        # check if its an instance of location
        # if location == "":
        #     location = None
        # else:
        #     location = Location.objects.get(name=location)

        # get current user neighbourhood
        profile = Profile.objects.filter(user_id=current_user.id).first()
        # check if user has neighbourhood
        if profile is None:
            profile = Profile.objects.filter(
                user_id=current_user.id).first()  # get profile
            posts = Post.objects.filter(user_id=current_user.id)
            # get all locations
            locations = Location.objects.all()
            neighbourhood = NeighbourHood.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            # redirect to profile with error message
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighbourhood = profile.neighbourhood

        # check if its an instance of neighbourhood
        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = NeighbourHood.objects.get(name=neighbourhood)

        business = Business(
            user_id=current_user.id,
            name=name,
            email=email,
            description=description,

            # phone=phone,
            # address=address,
            # location=location,
            neighbourhood=neighbourhood,
        )
        business.create_business()

        return redirect("/profile", {"success": "Business Created Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Business Creation Failed"})




# viewbusinesses 
@login_required()
def business(request):
    current_user = request.user
    # get current user neighbourhood
    profile = Profile.objects.filter(user_id=current_user.id).first()
    # check if user has neighbourhood
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()  # get profile
        posts = Post.objects.filter(user_id=current_user.id)
        # get all locations
        locations = Location.objects.all()
        neighbourhood = NeighbourHood.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        # redirect to profile with error message
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighbourhood": neighbourhood, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        neighbourhood = profile.neighbourhood
        # get all businesses in the user neighbourhood
        businesses = Business.objects.filter(
            neighbourhood=profile.neighbourhood)
        return render(request, "business.html", {"businesses": businesses})

