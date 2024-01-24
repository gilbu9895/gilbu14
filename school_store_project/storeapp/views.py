from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    is_authenticated = request.user.is_authenticated
    return render(request, 'index.html', {'is_authenticated': is_authenticated})


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            #return redirect('/')
            return redirect('new_page.html')
        else:
            #messages.info(request, "invalid credential")
            messages.info(request, "username or password not match")
            return redirect('login.html')

    return render(request, "login.html")

#def register(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']
        #confirmpassword = request.POST['password1']
        #if password == confirmpassword:
            #if User.objects.filter(username=username).exists():
                    #messages.info(request, "Username Taken")
                    #return redirect('register.html')
            #else:
                #user = User.objects.create_user(username=username, password=password)
                #user.save();
                #return redirect('login.html')
        #else:
            #messages.info(request, "password not matching")
            #return redirect('register.html')
        #return redirect('/')
    #return render(request, "register.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # Provide a default value if username is not present
        password = request.POST.get('password', '')
        confirmpassword = request.POST.get('password1', '')

        if not username or not password or not confirmpassword:
            messages.error(request, "All fields are required")
        elif password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Taken")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('login.html')
        else:
            messages.error(request, "Password not matching")

    return render(request, "register.html")
def new_page(request):
    #if not request.user.is_authenticated:
        #return redirect('login')
    return render(request, "new_page.html")
#def form_page(request):
    #if request.method == 'POST':
        # Retrieve form data
        #name = request.POST.get('name')
        #dob = request.POST.get('dob')
        #age = request.POST.get('age')
        #gender = request.POST.get('gender')
        #phone = request.POST.get('phone')
        #email = request.POST.get('email')
        #address = request.POST.get('address')
        #department = request.POST.get('department')
        #courses = request.POST.get('courses')
        #purpose = request.POST.get('purpose')


        # After processing, you may redirect to a success page or render a confirmation template
        #return render(request, 'login.html', {'name': name, 'purpose': purpose, 'dob': dob, 'age': age,
                                              #'gender': gender, 'phone': phone, 'email': email, 'address': address,
                                              #'department': department, 'courses': courses})

        # If the request method is not POST, render the form page
    #return render(request, 'form_page.html')
def form_page(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        courses = request.POST.get('courses')
        purpose = request.POST.get('purpose')

        # Check if any required field is empty
        required_fields = [name, dob, age, gender, phone, email, address, department, courses, purpose]
        if any(not field for field in required_fields):
            messages.error(request, "PLEASE FILL ALL SECTIONS")
            return render(request, 'form_page.html')

        # After processing, you may redirect to a success page or render a confirmation template
        return render(request, 'confirm.html', {'name': name, 'purpose': purpose, 'dob': dob, 'age': age,
                                                     'gender': gender, 'phone': phone, 'email': email,
                                                     'address': address, 'department': department,
                                                     'courses': courses})

    # If the request method is not POST, render the form page
    return render(request, 'form_page.html')

def confirm(request):
    return render(request, 'confirm.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

