from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
from django.db.models import Q
import json

# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    cur_user_id = request.session['user_id']
    cur_user = models.User.objects.get(id = cur_user_id)
    isdriver = cur_user.driver
    print(isdriver)
    #modify begin
    print(11111111)
    rides = models.Ride.objects.all()
    # owners_ride = models.Ride.objects.get(owner = cur_user)
    # print(owners_ride)
    # drivers_ride = models.Ride.objects.get(driver = cur_user)
    #modify end
    return render(request, 'login/index.html', locals())


def login(request):
    # if request.session.get('is_login', None):  
    #     return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = 'check your input!'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = 'invalid user'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = 'invalid password'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")


def register(request):
    # if request.session.get('is_login', None):
    #     return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "check your input"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = 'diff between your two password'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'exist username'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'exist email'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    pass
    return redirect("/login/")

def driverdetail(request):
    if request.method == 'POST':
        driverdetail_form = forms.CarForm(request.POST)
        message = "check your input"
        if driverdetail_form.is_valid():
            cartype = driverdetail_form.cleaned_data.get('cartype')
            platenumber = driverdetail_form.cleaned_data.get('plateNumber')
            passengersnumber = driverdetail_form.cleaned_data.get('passengersNumber')
            freetext = driverdetail_form.cleaned_data.get('freeText')
            cur_user_id = request.session['user_id']
            cur_user = models.User.objects.get(id = cur_user_id)
            print(cur_user)
            cur_car = models.Car.objects.get(user = cur_user)
            if(cur_car):
                new_car = cur_car
            else:
                new_car = models.Car()
            print(new_car)
            new_car.cartype = cartype
            new_car.plateNumber = platenumber
            new_car.passengersNumber = passengersnumber
            new_car.freeText = freetext
            if(cur_user.driver == False):
                new_car.user = cur_user
                cur_user.driver = True
            new_car.save()
            cur_user.save()
            return redirect('/index/')
        else:
            return render(request, 'login/driverdetail.html', locals())
    driverdetail_form = forms.CarForm()
    return render(request, 'login/driverdetail.html', locals())

def profile(request):
    cur_user_id = request.session['user_id']
    cur_user = models.User.objects.get(id = cur_user_id)
    cur_car = None
    if cur_user.driver:
        cur_car = models.Car.objects.get(user = cur_user)
        print(cur_car)

    
    return render(request, 'login/profile.html', locals())

def editprofile(request):
    cur_user_id = request.session['user_id']
    cur_user = models.User.objects.get(id = cur_user_id)
    cur_car = None
    
    if cur_user.driver:
        cur_car = models.Car.objects.get(user = cur_user)
    if request.method == 'POST':
        message = "check your input"
        username = request.POST.get('username')
        email = request.POST.get("email")
        sex = request.POST.get("sex")
        print(sex)
        if not (username and email and sex):
            return render(request, 'login/editprofile.html', locals())
        if cur_user.driver:
            cartype = request.POST.get("cartype")
            plateNumber = request.POST.get("plateNumber")
            passengersNumber = request.POST.get("passengersNumber")
            freeText = request.POST.get("freeText")
            isdriver = request.POST.get("driver")
            print(isdriver)
            if not (cartype and plateNumber and passengersNumber):
                return render(request, 'login/editprofile.html', locals())
            print(int(passengersNumber))
            if int(passengersNumber) > 99 or int(passengersNumber)<0:
                message = "too many passengers!"
                return render(request, 'login/editprofile.html', locals())
        if not username == cur_user.name:
            same_name_user = models.User.objects.filter(name=username)
            if same_name_user:
                message = 'exist username'
                return render(request, 'login/editprofile.html', locals())
        if not email == cur_user.email:
            same_email_user = models.User.objects.filter(email=email)
            if same_email_user:
                message = 'exist email'
                return render(request, 'login/editprofile.html', locals())
        cur_user.name = username
        cur_user.email = email
        cur_user.sex = sex
        if cur_user.driver:
            cur_car.cartype = cartype
            cur_car.plateNumber = plateNumber
            cur_car.passengersNumber = passengersNumber
            cur_car.freeText = freeText
            cur_user.driver = isdriver=="True"
            cur_car.save()
        cur_user.save()
        return redirect('/index/profile/')
    return render(request, 'login/editprofile.html', locals())

def openride(request):
    if request.method == 'POST':
        owner_form = forms.OwnerForm(request.POST)
        message = "check your input"
        if owner_form.is_valid():
            ownernumber = owner_form.cleaned_data.get('ownernumber')
            share = owner_form.cleaned_data.get('share')
            dest = owner_form.cleaned_data.get('dest')
            earlytime = owner_form.cleaned_data.get('earlytime')
            latetime = owner_form.cleaned_data.get('latetime')
            freetext = owner_form.cleaned_data.get('freeText')
            cartype = owner_form.cleaned_data.get('cartype')
            cur_user_id = request.session['user_id']
            cur_user = models.User.objects.get(id = cur_user_id)
            print(cur_user)
            new_ride = models.Ride()
            new_ride.ownernumber = ownernumber
            new_ride.share = share
            new_ride.dest = dest
            new_ride.arrivaltime = earlytime
            new_ride.endtime = latetime
            new_ride.freeText = freetext
            new_ride.owner = cur_user
            new_ride.cartype = cartype
            new_ride.carspace = ownernumber
            new_ride.status = 0
            new_ride.save()
            print(earlytime)
            
            return redirect('/index/')
        else:
            return render(request, 'login/openride.html', locals())
    owner_form = forms.OwnerForm()
    return render(request, 'login/openride.html', locals())

def shareride(request):
    if request.method == 'POST':
        sharer_form = forms.ShareForm(request.POST)
        message = "check your input"
        if sharer_form.is_valid():
            sharenumber = sharer_form.cleaned_data.get('sharenumber')
            dest = sharer_form.cleaned_data.get('dest')
            earlytime = sharer_form.cleaned_data.get('earlytime')
            latetime = sharer_form.cleaned_data.get('latetime')
            ridelist = models.Ride.objects.filter(Q(status=0) & Q(share=True) & Q(dest = dest) & Q(arrivaltime__gte=earlytime) & Q(arrivaltime__lte=latetime))
            return render(request, 'login/shareresult.html', locals())
        else:
            return render(request, 'login/shareride.html', locals())
    sharer_form = forms.ShareForm()
    return render(request, 'login/shareride.html', locals())

def shareresult(request, sharenumber):
    if request.method == 'POST':
        ride_id = request.POST.get("ride")
        cur_ride = models.Ride.objects.get(id = ride_id)
        cur_user_id = request.session['user_id']
        cur_user = models.User.objects.get(id = cur_user_id)
        new_relationship = models.Relationship(user=cur_user, ride=cur_ride, groupnumber=sharenumber)
        print(sharenumber)
        
        cur_ride.carspace = cur_ride.carspace + sharenumber
        print(cur_ride.carspace)
        cur_ride.save()
        new_relationship.save()
        return redirect('/index/')
    return render(request, 'login/shareresult.html', locals())

def driveride(request):
    if request.method == 'POST':
        driver_form = forms.DriverForm(request.POST)
        message = "check your input"
        if driver_form.is_valid():
            space = driver_form.cleaned_data.get('space')
            cartype = driver_form.cleaned_data.get('cartype')
            freeText = driver_form.cleaned_data.get('freeText')
            if(freeText == ""):
                ridelist = models.Ride.objects.filter(Q(status=0) & Q(carspace__lte=space) & (Q(cartype = "")|Q(cartype = cartype)))
            else:
                ridelist = models.Ride.objects.filter(Q(status=0) & Q(carspace__lte=space) & Q(freeText = freeText) & (Q(cartype = "")|Q(cartype = cartype)))
            return render(request, 'login/driveresult.html', locals())
        else:
            return render(request, 'login/driveride.html', locals())
    driver_form = forms.DriverForm()
    return render(request, 'login/driveride.html', locals())

def driveresult(request, space):
    if request.method == 'POST':
        ridelist = request.POST.getlist("ride")
        # print(ridelist)
        for ride_id in ridelist:
            cur_ride = models.Ride.objects.get(id = ride_id)
            cur_ride.ridedriver = request.session['user_name']
            cur_ride.status = 1
            print(space)
            cur_ride.save()
        return redirect('/index/')
    return render(request, 'login/driveresult.html', locals())