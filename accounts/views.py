from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils import simplejson
from django.contrib.auth.models import User


def ajaxlogout(request):
    logout(request)
    return HttpResponse(simplejson.dumps({"logout": "success"}),
                        content_type='application/json')


@sensitive_post_parameters()
@csrf_protect
@never_cache
def ajaxlogin(request):
    template_name = 'registration/ajaxlogin.html'
    if request.user.is_authenticated():
        return render(request, template_name)

    authentication_form = AuthenticationForm

    if request.method == "POST":
        response_dict = {}
        form = authentication_form(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            response_dict.update({"logged_in": True})
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            user = User.objects.get(username=form.get_user())
            in_controllers = user.groups.filter(name="controllers").exists()
            response_dict.update({"in_controllers": in_controllers})
            response_dict.update({"username": user.username})
        else:
            response_dict.update({"form_errors": True})
        return HttpResponse(simplejson.dumps(response_dict),
                            content_type='application/json')
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()
    return render(request, template_name,
                  {'form': form})


@sensitive_post_parameters()
@csrf_protect
@never_cache
def ajaxregister(request):
    template_name = "registration/ajaxregister.html"
    if request.user.is_authenticated():
        return render(request, template_name)

    registration_form = UserCreationForm
    form = registration_form(request)

    if request.method == "POST":
        response_dict = {}
        form = registration_form(data=request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            user = User.objects.create_user(username, password=password)
            user.is_active = True
            user.save()
            user = authenticate(username=username,
                                password=password)
            login(request, user)
            response_dict.update({"created": True})
            #user = User.objects.get(username=form.get_user())
            #in_controllers = user.groups.filter(name="controllers").exists()
            #response_dict.update({"in_controllers": in_controllers})
        else:
            response_dict.update({"form_errors": form.errors})
        return HttpResponse(simplejson.dumps(response_dict),
                            content_type='application/json')

    else:
        form = registration_form(request)

    return render(request, template_name,
                  {'form': form})
