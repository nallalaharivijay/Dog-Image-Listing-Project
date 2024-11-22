from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
import re
from .forms import *
from .models import ImageList

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully!")
            return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('search')  # Redirect to a home page
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')

code2=[]

@login_required
def search(request):
    images = []
    code2 = request.session.get('code2', [])
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            response_code_pattern = form.cleaned_data['response_code']
            url_pattern = f"https://http.dog/{response_code_pattern}.jpg"  # URL for exact match
            code2 = []
            # If it's a pattern (like 2xx, 20x, 3xx), use regex to filter
            try:
                # Check if the response_code is an exact match (e.g., "203")
                if re.match(r'^\d{3}$', response_code_pattern):
                    # Exact match (e.g., 203)
                    url = f"https://http.dog/{response_code_pattern}.jpg"
                    code2.append(response_code_pattern)
                    response = requests.get(url)
                    if response.status_code == 200:
                        images.append(url)
                    else:
                        messages.error(request, "Failed to fetch image")
                else:
                    if response_code_pattern in ['9xx', '99x', '999']:
                        url = f"https://http.dog/999.jpg"
                        code2.append(999)
                        images.append(url)
                    else:
                        # If it's a pattern (e.g., 2xx, 20x, 3xx), find matching response codes
                        response_code_regex = response_code_pattern.replace('x', r'\d')
                        # Loop through all possible HTTP response codes (200 to 599)
                        for code in range(200, 600):
                            # Match against the pattern (e.g., '203' matches '20x')
                            if re.match(response_code_regex, str(code)):
                                url = f"https://http.dog/{code}.jpg"
                                code2.append(code)
                                response = requests.get(url)
                                if response.status_code == 200:
                                    images.append(url)
                    if not images:
                        messages.error(request, "No matching images found for the given pattern")
            except requests.exceptions.RequestException:
                messages.error(request, "Error connecting to external service")
        print(code2)
        request.session['code2'] = code2
            # Optionally save the search filter if the user wants to
        if 'save' in request.POST:
            list_name = request.POST.get('list_name', 'Default List')
            # Prepare a dictionary to save response codes and their image URLs
            response_data = {code: f"https://http.dog/{code}.jpg" for code in request.session.get('code2')}
            print(response_data)
                    # Save the data into the database
            ImageList.objects.create(
                        user=request.user,
                        name=list_name,
                        response_codes=list(response_data.keys()),  # Save the response codes as a list
                        image_links=list(response_data.values())   # Save the image links as a list
                    )
            messages.success(request, "List saved successfully!")
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form, 'images': images})

@login_required
def lists(request):
    lists = ImageList.objects.filter(user=request.user)
    return render(request, 'lists.html', {'lists': lists})

@login_required
def delete_list(request, list_id):
    image_list = ImageList.objects.get(id=list_id, user=request.user)
    image_list.delete()
    messages.success(request, "List deleted successfully!")
    return redirect('lists')

@login_required
def view_list(request, list_id):
    image_list = get_object_or_404(ImageList, id=list_id, user=request.user)
    images = [f"https://http.dog/{code}.jpg" for code in image_list.response_codes]
    return render(request, 'view_list.html', {'images': images, 'list_name': image_list.name})