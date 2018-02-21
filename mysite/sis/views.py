from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

from sis.forms import UserForm
from django.template import RequestContext

from django.views.generic import View

def home(request):
    output = "LOL"
    return HttpResponse(output)

# class based views
class UserFormView(View):
    form_class = UserForm
    template_name = 'sis/registration_form.html'
    print("Entered here")
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # create an object from the form
            # without saving it to the database
            user = form.save(commit=False)
            # cleaned (normalized) data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user.set_password(password)
            # save to the database
            user.save()

            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    # now logged in
                    login(request, user)
                    # request.user.
                    return redirect('sis:index')
        return render(request, self.template_name, {'form':form})
