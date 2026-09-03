from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import SignUpForm


def home(request):
    return render(request, "app/home.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        #If the form is valid, save the user and log them in, then redirect to the home page
        if form.is_valid():
            user = form.save()
            login(request, user)

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
    return redirect("home")