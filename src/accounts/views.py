from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView


from . forms import UserRegistration


class UserRegistrationView(FormView):
    form_class = UserRegistration
    template_name = 'accounts/registration/user_registration.html'

    # if a GET (or any other method) we'll create a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    # if this is a POST request we need to process the form data
    def post(self, request):
        # create a form instance and populate it with data from the request:
        form = self.form_class(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # create a form instance
            user = form.save(commit=False)
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # save user to database
            user.save()
            # return user object if credentials are correct
            user = authenticate(username=username, password=password)
            #validate user
            if user is not None:
                #verify if user is active and not inactive or banned or blocked
                if user.is_active:
                    # login user and initaite sessions
                    login(request, user)
            # redirect to a new URL:
            return HttpResponseRedirect('/#/')

        # if not valid return to blank form
        return render(request, self.template_name, {'form': form})




