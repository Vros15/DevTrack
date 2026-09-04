from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobApplicationForm, SignUpForm
from .models import JobApplication


def home(request):
    return render(request, "app/home.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        #If the form is valid, save the user and log them in, then redirect to the home page
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "You have successfully signed up and logged in.")
            return redirect("home")
    else:
        form = SignUpForm()

    # If the form is not valid or the request method is not POST, render the signup page with the form
    return render(
        request,
        "app/signup.html",
        {
            "form": form,
        },
    )

def login_user(request):
    # If the request method is POST, get the username and password from the request and authenticate the user
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        # If the user is authenticated, log them in and redirect to the home page
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("home")

    return render(
        request,
        "app/login.html",
        {
            "error": "Invalid username or password" if request.method == "POST" else "",
        },
    )

# Log the user out and redirect to the home page
def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")

@login_required
def application_list(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, "Job application created successfully.")
            return redirect("application_list")
    else:
        form = JobApplicationForm()

    applications = JobApplication.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "app/application_list.html",
        {
            "applications": applications,
            "form": form,
        },
    )

@login_required
def application_create(request):
    # If the request method is POST, create a new job application using the submitted form data
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        # If the form is valid, save the job application and redirect to the application list page
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, "Job application created successfully.")
            return redirect("application_list")

    else:
        form = JobApplicationForm()

    return render(
        request,
        "app/application_form.html",
        {
            "form": form,
        },
    )

@login_required
def application_detail(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user)
    
    return render(
        request,
        "app/application_detail.html",
        {
            "application": application,
        },
    )