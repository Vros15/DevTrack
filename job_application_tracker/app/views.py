from django.contrib.auth import login
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