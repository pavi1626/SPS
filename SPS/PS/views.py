from django.shortcuts import render, redirect
from .forms import UserForm, ContactForm
from .models import User, Contact, ParkingSlot
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'Username already exists. Please choose another one.')
            else:
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')  # Ensure the 'login' URL name is correct
    else:
        form = UserForm()
    
    # Render the registration form in case of GET request or validation error
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id  # Setting session for logged-in user
                messages.success(request, f'Welcome, {user.name}!')
                return redirect('firstpage')
            else:
                messages.error(request, 'Invalid username or password.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def firstpage(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                    contact = form.save(commit=False)
                    contact.save()
                    messages.success(request, 'Your message has been submitted successfully.')
                    return redirect('firstpage')
            else:
                form = ContactForm()
            context = {'user': user, 'form': form}
            return render(request, 'firstpage.html', context)
        except User.DoesNotExist:
            pass
    return redirect('login')

def logout_view(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    messages.success(request, 'You have been logged out.')
    return redirect('login')


# Handle complaints (Contact Us)
def contact(request):
    if request.method == 'POST':
        form = contact(request.POST)
        if form.is_valid():
            form.save()  # Save the complaint to the database
            return redirect('thanks')  # Redirect to a thank you page after submission
    else:
        form = contact()
    return render(request, 'contact_us.html', {'form': form})

def status(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)

            # Fetch actual slot data from the database
            slots = ParkingSlot.objects.all()  # Replace with actual model name and query

            context = {
                'user': user,
                'slots': slots,
            }
            return render(request, 'status.html', context)
        except User.DoesNotExist:
            return redirect('login')

    return redirect('login')
 

# Parking/views.py

# from django.shortcuts import render, redirect
# from .forms import UserForm, ComplaintForm
# from .models import User
# from django.contrib import messages
# from django.contrib.auth import authenticate, login

# # Handle user registration
# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new user
#             return redirect('login')  # Redirect to the login page after registration
#     else:
#         form = UserForm()
#     return render(request, 'register.html', {'form': form})

# # Handle user login
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to a homepage after login
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')

# # Handle complaints (Contact Us)
# def contact(request):
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the complaint to the database
#             return redirect('thanks')  # Redirect to a thank you page after submission
#     else:
#         form = ComplaintForm()
#     return render(request, 'contact_us.html', {'form': form})

# def logout_view(request):
#     try:
#         del request.session['user_id']
#     except KeyError:
#         pass
#     messages.success(request, 'You have been logged out.')
#     return redirect('login')

# def firstpage(request):
#     user_id = request.session.get('user_id')
#     if user_id:
#         try:
#             user = User.objects.get(id=user_id)
#             if request.method == 'POST':
#                 form = ContactForm(request.POST)
#                 if form.is_valid():
#                     contact = form.save(commit=False)
#                     contact.save()
#                     messages.success(request, 'Your message has been submitted successfully.')
#                     return redirect('firstpage')
#             else:
#                 form = ContactForm()
#             context = {'user': user, 'form': form}
#             return render(request, 'firstpage.html', context)
#         except User.DoesNotExist:
#             pass
#     return redirect('login')