# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .models import*
from django.contrib import messages
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def user_list(request):
    quary=CustomUser.objects.all()
    if request.GET.get('search'):
        quary=quary.filter(name__icontains= request.GET.get('search'))
    paginator = Paginator(quary, 5)  # Show 5 contacts per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context={'users': page_obj}
    return render(request,'user_list.html',context)


@login_required(login_url='/user/login/')
def user_create(request): 
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            # Validate the password using Django's built-in validators
            validate_password(password1)
        except ValidationError as e:
            messages.error(request, '\n'.join(e))
            return redirect('/user_create/')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('/user_create/')

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already taken!")
            return redirect('/user_create/')

        # Create user
        user = CustomUser(email=email, name=name)
        user.set_password(password1)
        user.save()
        messages.success(request, "User account Created successfully!")
        return redirect('/user_list/')

    return render(request, 'user_create.html')


@login_required(login_url='/user/login/')
def user_update(request,user_id): 
    quary=CustomUser.objects.get(id=user_id)

    if request.method == "POST":
        try:
            email = request.POST.get('email')
            name = request.POST.get('name')
            
            # Check if email already exists
            quary.email=email
            quary.name=name
            quary.save()
            messages.success(request, "User account updated successfully!")
            return redirect('/user_list/')
        except Exception:
            messages.error(request,'Email address already taken try another email address !!!!!!')
        
    return render(request, 'user_update.html',{'users':quary})

def user_delete(request,user_id):
    quary=CustomUser.objects.get(id=user_id)
    quary.delete()
    return redirect('/user_list/')


@login_required(login_url='/login/')
def change_password(request, user_id):
    # Get the user object or return a 404 response if not found
    user = get_object_or_404(CustomUser, id=user_id)
    
    # Check if the user has permission to change passwords
    if not request.user.is_staff and request.user != user:
        messages.error(request, "You don't have permission to change passwords for this user.")
        

    if request.method == 'POST':
       
        old_password = request.POST.get('old_password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not user.check_password(old_password):
            messages.error(request, "Your old password is incorrect.")
            return redirect('/user/password_change/')

        if password1 != password2:
            messages.error(request, "New Password and Confirm password need to be the same.")
            return redirect('/user/password_change/')

        user.set_password(password1)
        user.save()

        # Update the session authentication hash to prevent log out
        update_session_auth_hash(request, user)

        messages.success(request, 'Password changed successfully!')
        return redirect(f'/profile/{user_id}/')
    

    return render(request, 'change_password.html', {'user': user})

def login_form(request): 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'invaild Email address!!!!!!')
            return redirect('/login/')
        user = authenticate(email=email,password=password)
        if user is None:
            messages.info(request,'invaild Email !!!!!!!')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')

    return render(request, 'login.html')

@login_required(login_url='/login/')
def profile_page(request,user_id):
    user=CustomUser.objects.get(id=user_id)
    context={'user':user}
    return render(request,'profile.html',context)


@login_required(login_url='/login/')
def profile_update(request,user_id):
    try:
        user=CustomUser.objects.get(id=user_id)
        if request.method == 'POST':
            data = request.POST
            name=data.get('name')
            email=data.get('email')
            user.name=name
            user.email=email
            user.save()
            messages.success(request,'Profile Update Successfully!!!!!!')
            return redirect(f'/profile/{user_id}/')
        
    except Exception:
        messages.error(request,'This Email Already Exist please Try Different Email !!!!!!!')

    context={'user':user}
    return render(request,'profile_update.html',context)

def logout_page(request):
    logout(request)
    return redirect('/login/')


