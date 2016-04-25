from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Alert
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from .forms import RegistrationForm, UpdateImage, Update, AlertForm
from alertbot.scripts import snapdeal, flipkart, amazon, shopclues, rediff#, askmebazar, indiarush, jabong, smartshoppers
from django.http import JsonResponse
from alertbot.utils import util
from alertbot.utils.constants import Constant
import json
from django.core import serializers

#from .templates.email.activated import activated_tmpl
# Create your views here.

def index(request):
    return render(request, 'index.html',{'page':'Home'})

def about(request):
    return render(request, 'about.html', {'page':'About'})


def signup(request):
    if(request.method == 'POST'):
        password = request.POST.get('password','')
        confirmPassword = request.POST.get('confirmPassword','')
        print(password,confirmPassword)
        error = ''
        if(password != confirmPassword):
            error = 'Password did\'nt Match'
        user = RegistrationForm(request.POST)
        if user.is_valid():
            user = user.save()
            request.session['_id'] = user.id
            request.session['_otp_times'] = 0
            request.session['_verify'] = 1
            try:
                util.send_sms(user.mobile,Constant.OTP_MESSAGE.replace('OTP_HERE', user.otp))
            except:
                return render(request, 'signup.html',{'success':"Sorry OTP cannot be Send, Please use forgot password",'page':'Sign up'})
            return HttpResponseRedirect('/verify')
        else:
            return render(request, 'signup.html',{'form': user, 'error':error,'page':'Sign up'})
    else:
        return render(request, 'signup.html',{'page':'Sign up'})


def verify(request):
    if(request.method == 'POST'):
        try:
            userId = request.session.get('_id','')
            otp = request.POST.get('otp','')
            user = User.objects.get(id=userId, otp=otp)
            user.otp = ''
            user.activated = True
            user.save()
            request.session.flush()
            return HttpResponseRedirect('/login')
        except:
            return render(request, 'verify.html',{'error':'Incorrect OTP, please try again','page':'Verify'})
    else:
        try:
            userId = request.session.get('_id','')
            user = User.objects.get(id=userId)
            if(request.session.get('_verify',0) != 1):
                request.session.flush()
                return HttpResponseRedirect('/login')
        except:
            request.session.flush()
            return HttpResponseRedirect('/login')
        return render(request, 'verify.html',{'page':'Verify'})

def resend(request):
    if(request.method == 'GET'):
        try:
            if(request.session.get('_verify',0) != 1):
                request.session.flush()
                return HttpResponseRedirect('/login')
            userId = request.session.get('_id','')
            otpTimes = request.session.get('_otp_times', 0)
            if(otpTimes >= 5):
                return render(request, 'verify.html',{'error':'You exceeded resend otp limit','page':'Verify'})
            user = User.objects.get(id=userId)
            user.otp = util.getotp()
            user.save()
            request.session['_otp_times'] = otpTimes + 1
            util.send_sms(user.mobile,Constant.OTP_MESSAGE.replace('OTP_HERE', user.otp))
            return render(request, 'verify.html',{'success':'Successfully resend OTP','page':'Verify'})
        except:
            return render(request, 'verify.html',{'error':'Couldn\'t resend OTP, please try again','page':'Verify'})
    else:
        return render(request, 'error.html',{'error':'POST method not allowed'})


def done(request):
    return render(request, 'done.html')

def login(request):
    if(request.method == 'POST'):
        try:
            mobile = request.POST['mobile']
            password = request.POST['password']
            user = User.objects.get(mobile = mobile, password= password)
            if not user.activated:
                return render(request, 'login.html',{'error':'Your account is not verified yet','page':'Login'})
            request.session['_id'] = user.id
            request.session['_login'] = 1
            return HttpResponseRedirect('/profile')
        except:
            return render(request, 'login.html',{'error':'Mobile and Password did not match','page':'Login'})
    else:
        return render(request, 'login.html',{'page':'Login'})


def forgot(request):
    if(request.method == 'POST'):
        try:
            mobile = request.POST.get('mobile','')
            user = User.objects.get(mobile=mobile)
            user.otp = util.getotp()
            user.save()
            request.session['_id'] = user.id
            request.session['_update'] = 1
            util.send_sms(user.mobile,Constant.OTP_MESSAGE.replace('OTP_HERE', user.otp))
            return HttpResponseRedirect('/update')
        except:
            return render(request, 'forgot.html',{'error':'Incorrect Mobile Number, please try again','page':'Verify'})
    else:
        return render(request, 'forgot.html',{'page':'Forgot Password'})

def update(request):
    if(request.method == 'POST'):
        try:
            password = request.POST.get('password','')
            confirmPassword = request.POST.get('confirmPassword','')
            otp = request.POST.get('otp','')
            if(password != confirmPassword):
                return render(request, 'updatePassword.html',{'error':'Password did not match, try again','page':'Update Password'})
            userId = request.session.get('_id','')
            user = User.objects.get(id=userId, otp=otp)
            user.otp = ''
            user.activated = True
            user.password = password
            user.save()
            request.session['_id'] = user.id
            request.session['_login'] = 1
            return HttpResponseRedirect('/profile')
        except:
            return render(request, 'updatePassword.html',{'error':'Couldn\'t update password, please try again','page':'Update Password'})
    else:
        try:
            userId = request.session.get('_id','')
            user = User.objects.get(id=userId)
            if(request.session.get('_update',0) != 1):
                request.session.flush()
                return HttpResponseRedirect('/login')
        except:
            request.session.flush()
            return HttpResponseRedirect('/login')
        return render(request, 'updatePassword.html',{'page':'Update Password'})



def profile(request):
    if(request.method == "GET"):
        try:
            if(request.session.get('_login',0) != 1):
                request.session.flush()
                return HttpResponseRedirect('/login')
            id = request.session['_id']
            user = User.objects.get(id = id)
            alertList = Alert.objects.filter(user_id=user.id)
            alerts = []
            print(alerts)
            if(user.image):
                url = user.image.url
            else:
                url =''
            request.session['name'] = user.name
            request.session['email'] = user.email
            request.session['image'] = url
            request.session['id'] = user.id
            request.session['mobile'] = user.mobile
            for a in alertList:
                alerts.append(a.as_json())
            request.session['alerts'] = alerts
            return render(request, 'profile.html')
        except:
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'error.html')

def image(request):
    if(request.method == "POST"):
        try:
            id = request.session.get('_id','')
            user = User.objects.get(id=id)
            imageForm = UpdateImage(request.POST, request.FILES, instance=user)
            if(imageForm.is_valid()):
                imageForm.save()
                return HttpResponseRedirect('/profile')
            else:
                return render(request, 'profile.html', {'form':imageForm})
        except:
            request.session.flush()
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'error.html')


def profileUpdate(request):
    if(request.method == 'POST'):
        try:
            id = request.session.get('_id','')
            user = User.objects.get(id=id)
            form = Update(request.POST, instance=user)
            if(form.is_valid()):
                form.save()
                return HttpResponseRedirect('/profile')
            else:
                return render(request, 'profile.html', {'form':form})
        except:
            request.session.flush()
            return HttpResponseRedirect('/login')


def geturl(request):
    if(request.method == 'POST'):
        site = request.POST['site']
        url = request.POST['url']
        if(site == 'Snapdeal'):
            result = (snapdeal.get(url))
        if(site == 'Flipkart'):
            result = (flipkart.get(url))
        if(site == 'Amazon'):
            result = (amazon.get(url))
        if(site == 'Shopclues'):
            result = (shopclues.get(url))
        if(site == 'Rediff'):
            result = (rediff.get(url))
        print(result)
        if(result == 'failed'):
            return JsonResponse({'error':'Unable to fetch, please try again'}, status=400)
        return JsonResponse({'name':result[0], 'price':result[1]})
    else:
        return render(request, 'error.html')

def logout(request):
    if(request.method == 'GET'):
        request.session['_sid'] = ''
        request.session['_id'] = ''
        return HttpResponseRedirect('/')
    else:
        return render(request, 'error.html')


def alert(request):
    if(request.method == "POST"):
        try:
            id = request.session.get('_id','')
            user = User.objects.get(id=id)
            alert = AlertForm(request.POST)
            if(alert.is_valid()):
                alert.save()
                return HttpResponseRedirect('/profile')
            else:
                print(alert)
                return render(request, 'profile.html', {'alert':alert})
        except:
            return HttpResponseRedirect('/login')
    elif(request.method == "GET"):
        pass

def alertDelete(request, pk):
    Alert.objects.get(id=pk).delete()
    return HttpResponseRedirect('/profile')
