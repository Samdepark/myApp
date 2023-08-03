from django.shortcuts import redirect, render
from Authentication.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages



def Register(request):
    if request.method == "POST" :
        form  = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success('request', 'Created successfully')
            new_user = authenticate(username = form.cleaned_data['email'], 
                                    password = form.clean_data['password1']
                                    )
            login(request, new_user)
            return redirect('FullStock_traders:index')
    
    else:
        print("Registration failed")
    
    
#The context helps us to display the form
    context = {
        'form' : form,
    }

#have to create a template with the Authentication/SignUP.html
    return render(request, 'Authentication/signUp.html', context)