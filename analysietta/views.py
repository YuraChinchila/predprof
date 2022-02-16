from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Users
import base64

def index(request, alert=None):
    try:
        enc_uid = request.session['uid']
        uid = base64.b64decode(enc_uid.encode("utf8")).decode("utf8")[6:-5]
        if len(Users.objects.filter(id=uid).values_list()) != 0:
            return render(request, 'analysietta/index.html', {'alert': alert, 'reg': 1})
        else:
            return render(request, 'analysietta/index.html', {'alert': alert, 'reg': 0})
    except KeyError:
        return render(request, 'analysietta/index.html', {'alert': alert, 'reg': 0})

def register(request):
    if request.method == "POST":
        post = request.POST.dict()
        if "email_reg" in post and "password_reg" in post:
            if len(Users.objects.filter(email=post["email_reg"]).values_list()) == 0:
                Users(email=post["email_reg"], password=make_password(post["password_reg"])).save()
                return redirect('index', alert="reg")
            else:
                return redirect('index', alert="email")
    return redirect('index', alert="error")

def auth(request):
    if request.method == "POST":
        post = request.POST.dict()
        if "email_auth" in post and "password_auth" in post:
            try:
                uid, email, password = Users.objects.filter(email=post["email_auth"]).values_list()[0]
                if check_password(post["password_auth"], password):
                    str_uid = "1&n2eT" + str(uid) + "1y82u"
                    enc_uid = base64.b64encode(str_uid.encode("utf8")).decode("utf8")
                    request.session['uid'] = enc_uid
                    return redirect('index')
                else:
                    return redirect('index', alert="auth")
            except IndexError:
                return redirect('index', alert="auth")
    return redirect('index')
