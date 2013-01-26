from django.shortcuts import render_to_response
from django.template.context import RequestContext
from FC.models.User import User
from django.http import HttpResponseRedirect
from FC.core import membership

def login(request):
    if(membership.getUser(request)):
        return HttpResponseRedirect("/account/home/")
    email = "";
    error = ""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = getUsernameByCredentials(email, password)
        if user == None:
            error = "Wrong combination"
        else:
            membership.login(request, user)
            return HttpResponseRedirect("/account/home/")

    return render_to_response('account/login.html', {"email":email, "error":error},
        context_instance = RequestContext(request))

def logout(request):
    membership.logout(request)
    return HttpResponseRedirect("/account/login/")

def getUsernameByCredentials(email, password):
    user = User.objects.get(email = email)
    if user is None:
        return None
    if user.checkPassword(password) == False:
        return None
    return user

def home(request):
    user = membership.getUser(request)
    if user == None:
        return HttpResponseRedirect("/account/login/")
    return render_to_response("account/home.html", {"user":user})
