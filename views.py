from django.shortcuts import render
from detection.models import *
from cryptography.fernet import Fernet, InvalidToken
from datetime import datetime,timedelta
import numpy as np
import base64,traceback,logging
import pandas as pd
from geopy.geocoders import Nominatim
from .tokens import generate_token
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse

from django.contrib.auth.models import User
from StressandAnxiety import settings
from django.contrib.auth import authenticate,login,logout
import random,time,json
from agora_token_builder import RtcTokenBuilder
from django.contrib import messages
from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
import opencage.geocoder
import os
# from django.conf import settings
# Define your API key
API_KEY = '83b6679a30b34c1b98c648658fd363f8'
def home(request):
    return render(request,"authentication/Home.html")
def register(request):
    #TODO
# - validate password
# -  create django user and get the user object
# - then add the user object in new profile
# - and create the profile
    if request.method == 'POST':
        name = request.POST['name']
        name=encrypt(name)
        age = request.POST['age']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['cpassword']
        door = request.POST['door']
        street = request.POST['street']
        
        city = request.POST['city']
        state = request.POST['state']
        date = request.POST['date']
        
        phone = request.POST['phone']
        phone=encrypt(phone)
        select = request.POST['select']
        print(select)
        if password == password2:
            
            if User.objects.filter(email=email).exists():
                    messages.info(request,"Email already exists. Kindly login...")
                    return redirect('register')
            elif Profile.objects.filter(phone=phone).exists():
                    messages.info(request,"Phone number already exists.")
                    return redirect('register')
            elif Counselor.objects.filter(phone=phone).exists():
                    messages.info(request,"Phone number already exists.")
                    return redirect('register')
            elif Doctor.objects.filter(phone=phone).exists():
                    messages.info(request,"Phone number already exists.")
                    return redirect('register')
            else:
                if select=='User':
                    user = User.objects.create_user(email, email, password)
                    #user.is_active = False
                    Profile(name=name,age=age,email=email,door=door,street=street,city=city,state=state,date=date,phone=phone,user=user).save()
                    
                    messages.success(request,"Your account has been successfully created!")
                    subject ='Confirmation mail'
                    message = f'Hi {user.username},\n Thank you for registering to Stress and Anxiety Detection System. Your account has been successfully created.We have sent you a confirmation mail.Please confirm to activate your account\nRegards,\n Admin'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email, ]
                    send_mail( subject, message, email_from, recipient_list )
                    current_site = get_current_site(request)
                    email_subject = "Confirm your Email @Stress and Anxiety Detection System!!"
                    message2 = render_to_string('authentication/email_confirmation.html',{
                
                'name': user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
                    email = EmailMessage(
                    email_subject,
                    message2,
                    settings.EMAIL_HOST_USER,
                    [user.email],
            )
                    email.fail_silently = True
                    email.send()
                    
            
                    return redirect('begin')
                elif select == 'Counsellor':
                    user = User.objects.create_user(email, email, password)
                    print("yes")
                    Counselor(name=name,age=age,email=email,door=door,street=street,city=city,state=state,date=date,phone=phone,user=user).save()
                    messages.success(request,"Your account has been successfully created!")
                    subject ='Confirmation mail'
                    message = f'Hi {user.username},\n Thank you for registering to Stress and Anxiety Detection System. Your account has been successfully created.We have sent you a confirmation mail.Please confirm to activate your account\nRegards,\n Admin'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email, ]
                    send_mail( subject, message, email_from, recipient_list )
                    current_site = get_current_site(request)
                    email_subject = "Confirm your Email @Stress and Anxiety Detection System!!"
                    message2 = render_to_string('authentication/email_confirmation.html',{
                
                'name': user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
                    email = EmailMessage(
                    email_subject,
                    message2,
                    settings.EMAIL_HOST_USER,
                    [user.email],
            )
                    email.fail_silently = True
                    email.send()
                    
            
                    return redirect('begin')
                elif select == 'Doctor':
                    geocoder = opencage.geocoder.OpenCageGeocode(API_KEY)
                    address = f'{street}, {city}, {state}'
                    result = geocoder.geocode(address)
                    if result and len(result):
                        latitude = result[0]['geometry']['lat']
                        longitude = result[0]['geometry']['lng']
                    user = User.objects.create_user(email, email, password)
                    Doctor(name=name,age=age,email=email,door=door,street=street,city=city,state=state,date=date,phone=phone,latitude=latitude,longitude=longitude,user=user).save()
                    messages.success(request,"Your account has been successfully created!")
                    subject ='Confirmation mail'
                    message = f'Hi {user.username},\n Thank you for registering to Stress and Anxiety Detection System. Your account has been successfully created.We have sent you a confirmation mail.Please confirm to activate your account\nRegards,\n Admin'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email, ]
                    send_mail( subject, message, email_from, recipient_list )
                    current_site = get_current_site(request)
                    email_subject = "Confirm your Email @Stress and Anxiety Detection System!!"
                    message2 = render_to_string('authentication/email_confirmation.html',{
                
                'name': user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
                    email = EmailMessage(
                    email_subject,
                    message2,
                    settings.EMAIL_HOST_USER,
                    [user.email],
            )
                    email.fail_silently = True
                    email.send()
                    
            
                    return redirect('begin')
        else:
                messages.info(request,"Password not matching..")
                return redirect('register')
                
        
        
    else:
        return render(request,'authentication/Register.html')
    
def activate(request,uid64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user,token):
        user.is_active = True
        # user.profile.signup_confirmation = True
        user.save()
        login(request,user)
        messages.success(request, "Your Account has been activated!!")
        return redirect('begin')
    else:
        return render(request,'activation_failed.html')

def begin(request):
    
    if request.method == 'POST':
    
        email = request.POST.get('email')
        password = request.POST.get('password')
        select = request.POST['select']
        sample = authenticate(username=email,password=password)
        if sample is not None:
            if select=='User':
                login(request,sample)
                
                print(request.user)
                
                return redirect('stage0')
            elif select=='Counsellor':
                login(request,sample)
                return redirect('counsellor/')
            elif select=='Doctor':
                login(request,sample)
                return redirect('doctor/')
                
            else:
                messages.error(request,"Email or Password incorrect..")
                return redirect('begin')
    
    
    return render(request,'authentication/login.html')
def out(request):
    logout(request)
    return redirect('/')
def contact(request):
    return render(request,'pages/Contact.html')
def stage0(request):
    attempt = Profile.objects.get(user=request.user)
    if(Stage0.objects.filter(Profile_id=attempt.id).exists()):
        res = True
        return render(request, 'pages/stage0.html',{'blur':res})
    else:
        return render(request, 'pages/stage0.html') 
def stage1(request):
    attempt = Profile.objects.get(user=request.user)
    
    if(Stageone.objects.filter(Profile_id=attempt.id).exists()):
        print("came")
        res = True
        return render(request, 'pages/stage1.html',{'blur':res})
    else:
        return render(request, 'pages/stage1.html')
    
def logout_h(request):
    return render(request,'authentication/happy.html')
def logout_s(request):
    return render(request,'authentication/sad.html')

def anxiety_Stag2(request):
    attempt = Profile.objects.get(user=request.user)
    
    if(Answers.objects.filter(profile_id=attempt.id,stage="stage2").exists()):
        print("came")
        res = True
        return render(request, 'pages/stage1.html',{'blur':res})
    else:
        
            if request.method == 'POST':
                q1 = request.POST.get('ques1',"off")
                q2 = request.POST.get('ques2',"off")
                q3 = request.POST.get('ques3',"off")
                q4 = request.POST.get('ques4',"off")
                q5 = request.POST.get('ques5',"off")
                q6 = request.POST.get('ques6',"off")
                q7 = request.POST.get('ques7',"off")
                data=[]
                if q1=="0":
                    data.append(1)
                    data.append(0)
                    data.append(0)
                    data.append(0)
                if q1 =="1":
                    data.append(0)
                    data.append(1)
                    data.append(0)
                    data.append(0)
                if q1 =="2":
                    data.append(0)
                    data.append(0)
                    data.append(1)
                    data.append(0)
                if q1=="3":
                    data.append(0)
                    data.append(0)
                    data.append(0)
                    data.append(1)   
                if q2=="0":
                    data.append(1)
                    data.append(0)
                    data.append(0)
                    data.append(0)
                if q2 =="1":
                    data.append(0)
                    data.append(1)
                    data.append(0)
                    data.append(0)
                if q2 =="2":
                    data.append(0)
                    data.append(0)
                    data.append(1)
                    data.append(0)
                if q2=="3":
                    data.append(0)
                    data.append(0)
                    data.append(0)
                    data.append(1)
                if q3=="0":
                    data.append(1)
                    data.append(0)
                    data.append(0)
                    data.append(0)
                if q3 =="1":
                    data.append(0)
                    data.append(1)
                    data.append(0)
                    data.append(0)
                if q3 =="2":
                    data.append(0)
                    data.append(0)
                    data.append(1)
                    data.append(0)
                if q3=="3":
                    data.append(0)
                    data.append(0)
                    data.append(0)
                    data.append(1)
                if q4=="0":
                    data.append(1)
                    data.append(0)
                    data.append(0)
                    data.append(0)
                if q4 =="1":
                    data.append(0)
                    data.append(1)
                    data.append(0)
                    data.append(0)
                if q4 =="2":
                    data.append(0)
                    data.append(0)
                    data.append(1)
                    data.append(0)
                if q4=="3":
                    data.append(0)
                    data.append(0)
                    data.append(0)
                    data.append(1)
                if q5=="0":
                    data.append(1)
                    data.append(0)
                    data.append(0)
                    data.append(0)
                if q5 =="1":
                    data.append(0)
                    data.append(1)
                    data.append(0)
                    data.append(0)
                if q5 =="2":
                    data.append(0)
                    data.append(0)
                    data.append(1)
                    data.append(0)
                if q5=="3":
                    data.append(0)
                    data.append(0)
                    data.append(0)
                    data.append(1)
                if q6=="0":
                    data.append(1)
                    data.append(0)
                    data.append(0)
                    data.append(0)
                if q6 =="1":
                    data.append(0)
                    data.append(1)
                    data.append(0)
                    data.append(0)
                if q6 =="2":
                    data.append(0)
                    data.append(0)
                    data.append(1)
                    data.append(0)
                if q6=="3":
                    data.append(0)
                    data.append(0)
                    data.append(0)
                    data.append(1)
                if q7=="0":
                    data.append(1)
                    data.append(0)
                    data.append(0)
                    data.append(0)
                if q7 =="1":
                    data.append(0)
                    data.append(1)
                    data.append(0)
                    data.append(0)
                if q7 =="2":
                    data.append(0)
                    data.append(0)
                    data.append(1)
                    data.append(0)
                if q7=="3":
                    data.append(0)
                    data.append(0)
                    data.append(0)
                    data.append(1)
                
                prof = Profile.objects.get(user=request.user)
                ObjList = [
                        Answers(
                        ques_id = "ques1",
                        ans_id = q1,
                        profile = prof,
                        ques_category = "anxiety_questions",
                        stage = "stage2"
                        ),
                        Answers(
                        ques_id = "ques2",
                        ans_id = q2,
                        profile = prof,
                        ques_category = "anxiety_questions",
                        stage = "stage2"
                        ),
                        Answers(
                        ques_id = "ques3",
                        ans_id = q3,
                        profile = prof,
                        ques_category = "anxiety_questions",
                        stage = "stage2"
                        ),
                        Answers(
                        ques_id = "ques4",
                        ans_id = q4,
                        profile = prof,
                        ques_category = "anxiety_questions",
                        stage = "stage2"
                        ),
                        Answers(
                        ques_id = "ques5",
                        ans_id = q5,
                        profile = prof,
                        ques_category = "anxiety_questions",
                        stage = "stage2"
                        ),
                        Answers(
                        ques_id = "ques6",
                        ans_id = q6,
                        profile = prof,
                        ques_category = "anxiety_questions",
                        stage = "stage2"
                        ),
                        Answers(
                        ques_id = "ques7",
                        ans_id = q7,
                        profile = prof,
                        ques_category = "anxiety_questions",
                        stage = "stage2"
                        )
                        ]
                Answers.objects.bulk_create(ObjList)
                model = pd.read_pickle('final_anxiety.pkl')
                data = np.array(data).reshape(1, -1)
                res=model.predict(data)
                if(res==[1]):
                    return redirect('social')
                elif(res==[0]):
                    return redirect('gad')
                else:
                    return redirect('panic')
            return render(request,'pages/stage2_anxiety.html',{'questions':questions['stage2']['anxiety_questions'],'keys':questions['stage2']['anxiety_questions'].keys()})
            

    
def stress_Stag2(request):
    attempt = Profile.objects.get(user=request.user)
    
    if(Answers.objects.filter(profile_id=attempt.id,stage="stage2").exists()):
        print("came")
        res = True
        return render(request, 'pages/stage1.html',{'blur':res})
    else:
        data=[]
        if request.method == 'POST':
            q1 = request.POST.get('ques1',"off")
            q2 = request.POST.get('ques2',"off")
            q3 = request.POST.get('ques3',"off")
            q4 = request.POST.get('ques4',"off")
            q5 = request.POST.get('ques5',"off")
            if q1=="0":
                data.append(1)
                data.append(0)
                data.append(0)
                data.append(0)
                print("yes")
            if q1 =="1":
                data.append(0)
                data.append(1)
                data.append(0)
                data.append(0)
            if q1 =="2":
                data.append(0)
                data.append(0)
                data.append(1)
                data.append(0)
            if q1=="3":
                data.append(0)
                data.append(0)
                data.append(0)
                data.append(1)   
            if q2=="0":
                data.append(1)
                data.append(0)
                data.append(0)
                data.append(0)
            if q2 =="1":
                data.append(0)
                data.append(1)
                data.append(0)
                data.append(0)
            if q2 =="2":
                data.append(0)
                data.append(0)
                data.append(1)
                data.append(0)
            if q2=="3":
                data.append(0)
                data.append(0)
                data.append(0)
                data.append(1)
            if q3=="0":
                data.append(1)
                data.append(0)
                data.append(0)
                data.append(0)
            if q3 =="1":
                data.append(0)
                data.append(1)
                data.append(0)
                data.append(0)
            if q3 =="2":
                data.append(0)
                data.append(0)
                data.append(1)
                data.append(0)
            if q3=="3":
                data.append(0)
                data.append(0)
                data.append(0)
                data.append(1)
            if q4=="0":
                data.append(1)
                data.append(0)
                data.append(0)
                data.append(0)
            if q4 =="1":
                data.append(0)
                data.append(1)
                data.append(0)
                data.append(0)
            if q4 =="2":
                data.append(0)
                data.append(0)
                data.append(1)
                data.append(0)
            if q4=="3":
                data.append(0)
                data.append(0)
                data.append(0)
                data.append(1)
            if q5=="0":
                data.append(1)
                data.append(0)
                data.append(0)
                data.append(0)
            if q5 =="1":
                data.append(0)
                data.append(1)
                data.append(0)
                data.append(0)
            if q5 =="2":
                data.append(0)
                data.append(0)
                data.append(1)
                data.append(0)
            if q5=="3":
                data.append(0)
                data.append(0)
                data.append(0)
                data.append(1)
            print(data)
            prof = Profile.objects.get(user=request.user)
            ObjList = [
                    Answers(
                    ques_id = "ques1",
                    ans_id = q1,
                    profile = prof,
                    ques_category = "stress_questions",
                    stage = "stage2"
                    ),
                    Answers(
                    ques_id = "ques2",
                    ans_id = q2,
                    profile = prof,
                    ques_category = "stress_questions",
                    stage = "stage2"
                    ),
                    Answers(
                    ques_id = "ques3",
                    ans_id = q3,
                    profile = prof,
                    ques_category = "stress_questions",
                    stage = "stage2"
                    ),
                    Answers(
                    ques_id = "ques4",
                    ans_id = q4,
                    profile = prof,
                    ques_category = "stress_questions",
                    stage = "stage2"
                    ),
                    Answers(
                    ques_id = "ques5",
                    ans_id = q5,
                    profile = prof,
                    ques_category = "stress_questions",
                    stage = "stage2"
                    )
            ]
            Answers.objects.bulk_create(ObjList)
            model = pd.read_pickle('final_stress.pkl')
            data = np.array(data).reshape(1, -1)
            print(data.shape)
            res=model.predict(data)
            if(res==[1]):
                return redirect('acute')
            elif(res==[0]):
                return redirect('ptsd')
            else:
                return redirect('adjust')
            
        return render(request,'pages/stage2_stress.html',{'questions':questions['stage2']['stress_questions'],'keys':questions['stage2']['stress_questions'].keys()})
def stage3(request):
    return render(request,'pages/stage3.html')
def panic(request):
    attempt = Profile.objects.get(user=request.user)
    
    if(Answers.objects.filter(profile_id=attempt.id,stage="stage3").exists()):
        print("came")
        res = True
        return render(request, 'pages/Panic.html',{'blur':res})
    else:
        if request.method == 'POST':
            q1 = request.POST.get('ques1',"off")
            q2 = request.POST.get('ques2',"off")
            q3 = request.POST.get('ques3',"off")
            q4 = request.POST.get('ques4',"off")
            q5 = request.POST.get('ques5',"off")
            q6 = request.POST.get('ques6',"off")
            q7 = request.POST.get('ques7',"off")
            q8 = request.POST.get('ques8',"off")
            q9 = request.POST.get('ques9',"off")
            q10 = request.POST.get('ques10',"off")
            prof = Profile.objects.get(user=request.user)
            ObjList = [
                    Answers(
                    ques_id = "ques1",
                    ans_id = q1,
                    profile = prof,
                    ques_category = "panic_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques2",
                    ans_id = q2,
                    profile = prof,
                    ques_category = "panic_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques3",
                    ans_id = q3,
                    profile = prof,
                    ques_category = "panic_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques4",
                    ans_id = q4,
                    profile = prof,
                    ques_category = "panic_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques5",
                    ans_id = q5,
                    profile = prof,
                    ques_category = "panic_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques6",
                    ans_id = q6,
                    profile = prof,
                    ques_category = "panic_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques7",
                    ans_id = q7,
                    profile = prof,
                    ques_category = "panic_questions",
                    stage = "stage3"
                    )
                    ]
            Answers.objects.bulk_create(ObjList)
            total = int(q1)+int(q2)+int(q3)+int(q4)+int(q5)+int(q6)+int(q7)+int(q8)+int(q9)+int(q10)
            result =""
            if total>=0 and total<=7:
                result += "Border line Panic Disorder"
            elif total>=8 and total<=10:
                result += "Slightly ill Panic Disorder"
            elif total>=11 and total<=15:
                result += "Moderately ill Panic Disorder"
            elif total>=16 and total<=40:
                result += "Markedly ill Panic Disorder"
            prof = Profile.objects.get(user=request.user)
            risks=""
            if result=="Border line Panic Disorder" or result=="Slightly ill Panic Disorder":
                risks+="low"
            else:
                risks+="high"
            Outcome(stage3="Panic",risk=risks,Profile_id=prof.id).save()
            Severity(res=risks,profile_id=prof.id).save()
            return redirect('logout_s')
        return render(request,'pages/panic.html',{'questions':questions['stage3']['panic_questions'],'keys':questions['stage3']['panic_questions'].keys()})
def gad(request):
    attempt = Profile.objects.get(user=request.user)
    
    if(Answers.objects.filter(profile_id=attempt.id,stage="stage3").exists()):
        print("came")
        res = True
        return render(request, 'pages/gad.html',{'blur':res})
    else:
        if request.method == 'POST':
            
            q1 = request.POST.get('ques1',"off")
            q2 = request.POST.get('ques2',"off")
            q3 = request.POST.get('ques3',"off")
            q4 = request.POST.get('ques4',"off")
            q5 = request.POST.get('ques5',"off")
            q6 = request.POST.get('ques6',"off")
            q7 = request.POST.get('ques7',"off")
            prof = Profile.objects.get(user=request.user)
            ObjList = [
                    Answers(
                    ques_id = "ques1",
                    ans_id = q1,
                    profile = prof,
                    ques_category = "gad_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques2",
                    ans_id = q2,
                    profile = prof,
                    ques_category = "gad_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques3",
                    ans_id = q3,
                    profile = prof,
                    ques_category = "gad_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques4",
                    ans_id = q4,
                    profile = prof,
                    ques_category = "gad_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques5",
                    ans_id = q5,
                    profile = prof,
                    ques_category = "gad_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques6",
                    ans_id = q6,
                    profile = prof,
                    ques_category = "gad_questions",
                    stage = "stage3"
                    ),
                    Answers(
                    ques_id = "ques7",
                    ans_id = q7,
                    profile = prof,
                    ques_category = "gad_questions",
                    stage = "stage3"
                    )
                    ]
            Answers.objects.bulk_create(ObjList)
            total = int(q1)+int(q2)+int(q3)+int(q4)+int(q5)+int(q6)+int(q7)
            result =""
            if total>=0 and total<=4:
                result += "Minimal Generalized anxiety"
            elif total>=5 and total<=9:
                result += "Mild Generalized anxiety"
            elif total>=10 and total<=14:
                result += "Moderate Generalized anxiety"
            elif total>=15 and total<=21:
                result += "Severe Generalized anxiety"
            
            prof = Profile.objects.get(user=request.user)
            
            risks=""
            if result=="Minimal Generalized anxiety" or result=="Mild Generalized anxiety":
                risks+="low"
            else:
                risks+="high"
                
            Outcome(stage3="Generalized anxiety",risk=risks,Profile_id=prof.id).save()
            Severity(res=risks,profile_id=prof.id).save()
            return redirect('logout_s')
        
        
        return render(request,'pages/gad.html',{'questions':questions['stage3']['gad_questions'],'keys':questions['stage3']['gad_questions'].keys()})
def social(request):
    attempt = Profile.objects.get(user=request.user)
    
    if(Answers.objects.filter(profile_id=attempt.id,stage="stage3").exists()):
        print("came")
        res = True
        return render(request, 'pages/SIAS.html',{'blur':res})
    else:
        if request.method == 'POST':
            q1 = request.POST.get('ques1',"off")
            q2 = request.POST.get('ques2',"off")
            q3 = request.POST.get('ques3',"off")
            q4 = request.POST.get('ques4',"off")
            q5 = request.POST.get('ques5',"off")
            q6 = request.POST.get('ques6',"off")
            q7 = request.POST.get('ques7',"off")
            q8 = request.POST.get('ques8',"off")
            q9 = request.POST.get('ques9',"off")
            q10 = request.POST.get('ques10',"off")
            q11 = request.POST.get('ques11',"off")
            q12 = request.POST.get('ques12',"off")
            q13 = request.POST.get('ques13',"off")
            q14 = request.POST.get('ques14',"off")
            q15 = request.POST.get('ques15',"off")
            q16 = request.POST.get('ques16',"off")
            q17 = request.POST.get('ques17',"off")
            q18 = request.POST.get('ques18',"off")
            q19 = request.POST.get('ques19',"off")
            q20 = request.POST.get('ques20',"off")
            prof = Profile.objects.get(user=request.user)
            ObjList = [
            Answers(
            ques_id = "ques1",
            ans_id = q1,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques2",
            ans_id = q2,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques3",
            ans_id = q3,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques4",
            ans_id = q4,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques5",
            ans_id = q5,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques6",
            ans_id = q6,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques7",
            ans_id = q7,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques8",
            ans_id = q8,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques9",
            ans_id = q9,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques10",
            ans_id = q10,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),Answers(
            ques_id = "ques11",
            ans_id = q11,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques12",
            ans_id = q12,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques13",
            ans_id = q13,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques14",
            ans_id = q14,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques15",
            ans_id = q15,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques16",
            ans_id = q16,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques17",
            ans_id = q17,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques18",
            ans_id = q18,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques19",
            ans_id = q19,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            ),
            Answers(
            ques_id = "ques20",
            ans_id = q20,
            profile = prof,
            ques_category = "sias_questions",
            stage = "stage3"
            )
            ]
            Answers.objects.bulk_create(ObjList)
            total = int(q1)+int(q2)+int(q3)+int(q4)+int(q5)+int(q6)+int(q7)+int(q8)+int(q9)+int(q10)+int(q11)+int(q12)+int(q13)+int(q14)+int(q15)+int(q16)+int(q17)+int(q18)+int(q19)+int(q20)
            result =""
            if total>43:
                result +="High Social Anxiety Disorder"
            else:
                result +="Low Social Anxiety Disorder"
            prof = Profile.objects.filter(email=request.user)
            risks=""
            if result=="Low Social Anxiety Disorder":
                risks+="low"
            else:
                risks+="high"
            Outcome(stage3="Social phobia",risk=risks,Profile_id=prof.id).save()
            Severity(res=risks,profile_id=prof.id).save()
            return redirect('logout_s')
            
        
        
        return render(request,'pages/SIAS.html',{'questions':questions['stage3']['sias_questions'],'keys':questions['stage3']['sias_questions'].keys()})

def ptsd(request):
        attempt = Profile.objects.get(user=request.user)
    
        if(Answers.objects.filter(profile_id=attempt.id,stage="stage3").exists()):
            print("came")
            res = True
            return render(request, 'pages/PTSD.html',{'blur':res})
        else:
            if request.method == 'POST':
                q1 = request.POST.get('ques1',"off")
                q2 = request.POST.get('ques2',"off")
                q3 = request.POST.get('ques3',"off")
                q4 = request.POST.get('ques4',"off")
                q5 = request.POST.get('ques5',"off")
                q6 = request.POST.get('ques6',"off")
                q7 = request.POST.get('ques7',"off")
                q8 = request.POST.get('ques8',"off")
                q9 = request.POST.get('ques9',"off")
                q10 = request.POST.get('ques10',"off")
                q11 = request.POST.get('ques11',"off")
                q12 = request.POST.get('ques12',"off")
                q13 = request.POST.get('ques13',"off")
                q14 = request.POST.get('ques14',"off")
                q15 = request.POST.get('ques15',"off")
                q16 = request.POST.get('ques16',"off")
                q17 = request.POST.get('ques17',"off")
                q18 = request.POST.get('ques18',"off")
                q19 = request.POST.get('ques19',"off")
                q20 = request.POST.get('ques20',"off")
                prof = Profile.objects.get(user=request.user)
                ObjList = [
                Answers(
                ques_id = "ques1",
                ans_id = q1,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques2",
                ans_id = q2,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques3",
                ans_id = q3,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques4",
                ans_id = q4,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques5",
                ans_id = q5,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques6",
                ans_id = q6,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques7",
                ans_id = q7,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques8",
                ans_id = q8,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques9",
                ans_id = q9,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques10",
                ans_id = q10,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),Answers(
                ques_id = "ques11",
                ans_id = q11,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques12",
                ans_id = q12,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques13",
                ans_id = q13,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques14",
                ans_id = q14,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques15",
                ans_id = q15,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques16",
                ans_id = q16,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques17",
                ans_id = q17,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques18",
                ans_id = q18,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques19",
                ans_id = q19,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques20",
                ans_id = q20,
                profile = prof,
                ques_category = "ptsd_questions",
                stage = "stage3"
                )
                ]
                Answers.objects.bulk_create(ObjList)
                total = int(q1)+int(q2)+int(q3)+int(q4)+int(q5)+int(q6)+int(q7)+int(q8)+int(q9)+int(q10)+int(q11)+int(q12)+int(q13)+int(q14)+int(q15)+int(q16)+int(q17)+int(q18)+int(q19)+int(q20)
                result =""
                if total>33:
                    result +="High Post Traumatic Stress Disorder"
                else:
                    result +="Low Post Traumatic Stress Disorder"
                prof = Profile.objects.get(user=request.user)
                risks=""
                if result=="Low Post Traumatic Stress Disorder":
                    risks+="low"
                else:
                    risks+="high"
                Outcome(stage3="Post traumatic stress",risk=risks,Profile_id=prof.id).save()
                Severity(res=risks,profile_id=prof.id).save()
                return redirect('logout_s')
            return render(request,'pages/PTSD.html',{'questions':questions['stage3']['ptsd_questions'],'keys':questions['stage3']['ptsd_questions'].keys()})
def acute(request):
        attempt = Profile.objects.get(user=request.user)
    
        if(Answers.objects.filter(profile_id=attempt.id,stage="stage3").exists()):
            print("came")
            res = True
            return render(request, 'pages/Acute.html',{'blur':res})
        else:
            if request.method == 'POST':
                
                    q1 = request.POST.get('ques1',"off")
                    q2 = request.POST.get('ques2',"off")
                    q3 = request.POST.get('ques3',"off")
                    q4 = request.POST.get('ques4',"off")
                    q5 = request.POST.get('ques5',"off")
                    q6 = request.POST.get('ques6',"off")
                    q7 = request.POST.get('ques7',"off")
                    prof = Profile.objects.get(user=request.user)
                    ObjList = [
                            Answers(
                            ques_id = "ques1",
                            ans_id = q1,
                            profile = prof,
                            ques_category = "acute_questions",
                            stage = "stage3"
                            ),
                            Answers(
                            ques_id = "ques2",
                            ans_id = q2,
                            profile = prof,
                            ques_category = "acute_questions",
                            stage = "stage3"
                            ),
                            Answers(
                            ques_id = "ques3",
                            ans_id = q3,
                            profile = prof,
                            ques_category = "acute_questions",
                            stage = "stage3"
                            ),
                            Answers(
                            ques_id = "ques4",
                            ans_id = q4,
                            profile = prof,
                            ques_category = "acute_questions",
                            stage = "stage3"
                            ),
                            Answers(
                            ques_id = "ques5",
                            ans_id = q5,
                            profile = prof,
                            ques_category = "acute_questions",
                            stage = "stage3"
                            ),
                            Answers(
                            ques_id = "ques6",
                            ans_id = q6,
                            profile = prof,
                            ques_category = "acute_questions",
                            stage = "stage3"
                            ),
                            Answers(
                            ques_id = "ques7",
                            ans_id = q7,
                            profile = prof,
                            ques_category = "acute_questions",
                            stage = "stage3"
                            )
                            ]
                    Answers.objects.bulk_create(ObjList)
                    total = int(q1)+int(q2)+int(q3)+int(q4)+int(q5)+int(q6)+int(q7)
                    result =""
                    if total>=0 and total<=4:
                        result += "Minimal Acute Disorder"
                    elif total>=5 and total<=9:
                        result += "Mild Acute Disorder"
                    elif total>=10 and total<=14:
                        result += "Moderate Acute Disorder"
                    elif total>=15 and total<=21:
                        result += "Severe Acute Disorder"
                    prof = Profile.objects.get(user=request.user)
                    risks=""
                    if result=="Minimal Acute Disorder" or result=="Mild Acute Disorder":
                        risks+="low"
                    else:
                        risks+="high"
                    Outcome(stage3="Acute stress reaction",risk=risks,Profile_id=prof.id).save()
                    Severity(res=risks,profile_id=prof.id).save()
                    return redirect('logout_s')
            return render(request,'pages/Acute.html',{'questions':questions['stage3']['acute_questions'],'keys':questions['stage3']['acute_questions'].keys()})
def adjust(request):
        attempt = Profile.objects.get(user=request.user)
    
        if(Answers.objects.filter(profile_id=attempt.id,stage="stage3").exists()):
            print("came")
            res = True
            return render(request, 'pages/adjust.html',{'blur':res})
        else:
            if request.method == 'POST':
                q1 = request.POST.get('ques1',"off")
                q2 = request.POST.get('ques2',"off")
                q3 = request.POST.get('ques3',"off")
                q4 = request.POST.get('ques4',"off")
                q5 = request.POST.get('ques5',"off")
                q6 = request.POST.get('ques6',"off")
                q7 = request.POST.get('ques7',"off")
                q8 = request.POST.get('ques8',"off")
                q9 = request.POST.get('ques9',"off")
                q10 = request.POST.get('ques10',"off")
                prof = Profile.objects.get(user=request.user)
                ObjList = [
                Answers(
                ques_id = "ques1",
                ans_id = q1,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques2",
                ans_id = q2,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques3",
                ans_id = q3,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques4",
                ans_id = q4,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques5",
                ans_id = q5,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques6",
                ans_id = q6,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques7",
                ans_id = q7,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques8",
                ans_id = q8,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques9",
                ans_id = q9,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                ),
                Answers(
                ques_id = "ques10",
                ans_id = q10,
                profile = prof,
                ques_category = "adjust_questions",
                stage = "stage3"
                )
                ]
                Answers.objects.bulk_create(ObjList)
                result =""
                if (q1>=2 or q2>=2 or q3>=2) and (q4>=2 or q5>=2 or q6>=2) and (q7>=2 or q8>=2 or q9>=2 or q10>=2):
                    result += "Maximum Adjustment Disorder"
                
                else: 
                    result += "Minimum Adjustment Disorder"
                op = ["Never", "Occasionally", "Half of the time","Most of the time","All of the time"]
                prof = Profile.objects.get(user=request.user)
                risks=""
                if result=="Minimum Adjustment Disorder":
                    risks+="low"
                else:
                    risks+="high"
                Outcome(stage3="Adjustment",risk=risks,Profile_id=prof.id).save()
                Severity(res=risks,profile_id=prof.id).save()
                return redirect('logout_s')
            
            return render(request,'pages/adjust.html',{'questions':questions['stage3']['adjust_questions'],'keys':questions['stage3']['adjust_questions'].keys()})
def getToken(request):
    appId = '9b97b1ccfdcf4936a58e428f0a687224'
    appCertificate ='3da4717235344fd98112ee26b52293b9'
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600*24
    currentTimeStamp = time.time()
    privilegeExpiredTs = expirationTimeInSeconds+currentTimeStamp
    role =1
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token,'uid':uid},safe=False)
def lobby(request):
    return render(request,'pages/lobby.html')
def user_lobby(request):
    return render(request,'pages/user_lobby.html')
def chatroom(request):
    return render(request,'pages/chatroom.html')
@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    print(request.body)
    print(data)
    request.session['room_name'] = data['room_name']
    request.session['select'] = data['select']
    request.session['name'] = data['name']
    member,created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid = data['UID'],
        room_name=data['room_name'],
        select = data['select'],
        
    )
    return JsonResponse({'name':data['name']},safe=False)
def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)
@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)
def counsellor(request):
    nm = Counselor.objects.get(user=request.user)
    if request.method=='POST':
        op = request.POST.get('options')
        if op == "low":
            return redirect('low')
        elif op=="high":
            return redirect('high')
        else:
            return redirect('coun_app')
    return render(request,'pages/counsellor_home.html')
def counsellor_profile(request):
    counsellors = Counselor.objects.get(user=request.user)
    return render(request,'pages/counsellor_profile.html',{'user':request.user,'counsel':counsellors})
def doctor(request):
    doc = Doctor.objects.get(user=request.user)
    find = Appoint.objects.filter(doctor=doc.id)
    list=[]
    for i in find:
        list.append(Profile.objects.filter(id=i.Profile_id))
    print(list)
    return render(request,'pages/doctor_home.html',{'pa':list})
def doctor_profile(request):
    doctors = Doctor.objects.filter(email=request.user).all()
    return render(request,'pages/doctor_profile.html',{'user':request.user,'doc':doctors})
def low(request):
    out = Outcome.objects.filter(risk="low")
    op =[]
    name=[]
    for p in out:
        prof =Profile.objects.filter(id=(p.Profile_id))
        op.append(prof)
    for a in Profile.objects.filter(id=(p.profile_id)):
            name.append(decrypt(a.name))
    return render(request, 'pages/lowrisk.html',{'res':op,'name':name})
    
def high(request):
    out = Severity.objects.filter(res="high")
    op =[]
    name=[]
    for p in out:
        prof =Profile.objects.filter(id=(p.profile_id))
        op.append(prof)
        for a in Profile.objects.filter(id=(p.profile_id)):
            name.append(decrypt(a.name))
    print(name)       
    for na in name:
        
            print(na)
    return render(request, 'pages/highrisk.html',{'res':op,'name':name})

def document(request,obj):
    prof = Profile.objects.get(id=obj)
    res = Outcome.objects.get(Profile_id=obj)
    stage0 = Stage0.objects.get(Profile_id=obj)
    stage1 = Stageone.objects.get(Profile_id=obj)
    out = Outcome.objects.get(Profile_id=obj)
    
    
    responses3 = Answers.objects.filter(profile_id=obj,stage="stage3")
    responses2 = Answers.objects.filter(profile_id=obj,stage="stage2")
    return render(request,'pages/document.html',{'name':decrypt(prof.name),'phone':decrypt(prof.phone),'i':obj,'prof':prof,'res':res,'zero':stage0,'one':stage1,'resu2':responses2,'resu3':responses3,'out':out,'questionjson2':questions['stage2'],'questionjson3':questions['stage3']})
def invite(request):
    select=request.session['select']
    room_name=request.session['room_name']
    name = request.session['name']
    if Counselor.objects.filter(name=name).exists():
        recipient_list = []
        res = Outcome.objects.filter(risk="low",stage3=select)
        for a in res:
            prof = Profile.objects.filter(id=a.Profile_id)
            for em in prof:
                print(em.email)
                recipient_list.append(em.email)
        subject ='Check out session details'
        message = f'Hi buddy,\n Thank you for trusting Stress and Anxiety Detection System. Your session is arranged by Counsellor {name}. Kindly join the session\n\n Steps:\n 1.Login to Stress and Anxiety Detection System using your credentials\n 2.Click to Join room \n Fill personal details and enter room name- {room_name}\n\n Regards,\n Admin'
        email_from = settings.EMAIL_HOST_USER
        send_mail( subject, message, email_from, recipient_list )
        return redirect('chatroom')
    else:
        vv="yes"
        return render(request,'pages/chatroom.html',{"chk":vv})
def personal(request):
    P = Profile.objects.get(user=request.user)
    
    
    
    return render(request,'pages/personal.html',{'user':request.user,'name':decrypt(P.name),'phone':decrypt(P.phone),'counsel':P})
@csrf_exempt
def response(request):
        print("view")
        jsonData = json.loads(request.body)
        print(jsonData)
        prof = Profile.objects.get(user=request.user)
        Stage0.objects.get_or_create(
        Greetings=jsonData['Greetings'],
        Wellbeing = jsonData['How are you doing?'],
        About=jsonData['Tell me about yourself?'],
        Strengths = jsonData['Say me your strengths?'],
        Reason=jsonData['What brings you here?'],
        Therapy = jsonData['Have you been to therapy before? If so, what was your impression of it?'],
        Magical_Wish=jsonData['If you had a magical wish, what would you wish for?'],
        Favourite_Food = jsonData['What is your favorite food for breakfast?'],
        Friend_Characteristics = jsonData['What makes someone a friend to you?'],
        Last_Angry=jsonData['Why and When were you last angry?'],
        Not_like_to_do_at_home = jsonData['What do you not like to do at home?'],
        Profile_id = prof.id,
        
    )
        return JsonResponse({'name':'hi'}, safe=False)
def get_lat_long(request,obj):
    prof = Profile.objects.get(id=obj)
    # Get the street name and city name from the request
    street = prof.street
    city = prof.city
    state =prof.state
    prof_id=prof.id
    
    geocoder = opencage.geocoder.OpenCageGeocode(API_KEY)
    address = f'{street}, {city}, {state}'
    result = geocoder.geocode(address)
    distance=10
    if result and len(result):
        distance =10
        geolocator = Nominatim(user_agent="detection")
        location = geolocator.geocode(f"{street}, {city}, {state}")
        latitude = location.latitude
        longitude = location.longitude
        if Doctor.objects.filter(latitude__range=(latitude - distance, latitude + distance),
                                    longitude__range=(longitude - distance, longitude + distance)).exists():
            doctors = Doctor.objects.filter(latitude__range=(latitude - distance, latitude + distance),
                                longitude__range=(longitude - distance, longitude + distance)).order_by('latitude', 'longitude')
            
            print(doctors)
            #Appoint(doctor=doctors.id,Profile_id=prof_id).save()
            # objs_to_delete = Severity.objects.filter(profile_id=obj)
            # objs_to_delete.delete()
            return render(request, 'pages/doctors.html', {'doctors': doctors,'prof':prof_id})
        else:
            distance=30
            if Doctor.objects.filter(latitude__range=(latitude - distance, latitude + distance),
                                    longitude__range=(longitude - distance, longitude + distance)).exists():
                doctors = Doctor.objects.filter(latitude__range=(latitude - distance, latitude + distance),
                                    longitude__range=(longitude - distance, longitude + distance)).order_by('latitude', 'longitude')
                
                #Appoint(doctor=doctors.id,Profile_id=prof_id).save()
                # objs_to_delete = Severity.objects.filter(profile_id=obj)
                # objs_to_delete.delete()
                print(doctors)
                return render(request, 'pages/doctors.html', {'doctors': doctors,'prof':prof_id})
            else:
                distance = 50
                if Doctor.objects.filter(latitude__range=(latitude - distance, latitude + distance),
                                    longitude__range=(longitude - distance, longitude + distance)).exists():
                    doctors = Doctor.objects.filter(latitude__range=(latitude - distance, latitude + distance),
                                    longitude__range=(longitude - distance, longitude + distance)).order_by('latitude', 'longitude')
                    
                    #Appoint(doctor=doctors.id,Profile_id=prof_id).save()
                    # objs_to_delete = Severity.objects.filter(profile_id=obj)
                    # objs_to_delete.delete()
                    print(doctors)
                    return render(request, 'pages/doctors.html', {'doctors': doctors,'prof':prof_id})
                else:
                        distance = 70
                        if Doctor.objects.filter(latitude__range=(latitude - distance, latitude + distance),
                                            longitude__range=(longitude - distance, longitude + distance)).exists():
                            doctors = Doctor.objects.filter(latitude__range=(latitude - distance, latitude + distance),
                                            longitude__range=(longitude - distance, longitude + distance)).order_by('latitude', 'longitude')
                            
                            #Appoint(doctor=doctors.id,Profile_id=prof_id).save()
                            # objs_to_delete = Severity.objects.filter(profile_id=obj)
                            # objs_to_delete.delete()
                            print(doctors)
                            return render(request, 'pages/doctors.html', {'doctors': doctors})
                        else:
                            return HttpResponse("no")
                            
                    
    return JsonResponse({'error': 'Unable to geocode address'})
def doctors(request):
    return render(request,'pages/doctors.html')
    
def find_nearby_doctors(request,prof,doc):
    Appoint(doctor_id=doc,Profile_id=prof).save()
    objs_to_delete = Severity.objects.filter(profile_id=prof)
    objs_to_delete.delete()
    return render(request,'pages/highrisk.html')
def appoint(request,obj):
    doc = Doctor.objects.get(user=request.user)
    prof = Profile.objects.get(id=obj)
    doc_id=doc.id
    name=doc.name
    street=doc.street
    city=doc.city
    state=doc.state
    user_id=prof.id
    email=prof.email
    user_name=prof.name
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        session = request.POST['session']
        print("in")
    
        Past_Appoint(profile_id=user_id,doctor_id=doc_id,date=date,time=time,session=session).save()
        subject ='Appointment Details'
        message = f'Hi {user_name},\n Thank you for trusting Stress and Anxiety Detection System. This mail is to inform you about confirmation of Psychologist appointment. Kindly visit Psychologist\n Your id:{user_id}\n Psychologist name:{name} \n Street name:{street}\nCity:{city}\nState:{state}\nDate:{date}\nTime:{time}\nRegards,\n Admin'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('doctor')
    return render(request,'pages/appoint.html',{'id':obj})  
def docum_doc(request,obj):
    prof = Profile.objects.get(id=obj)
    res = Outcome.objects.get(Profile_id=obj)
    treat = Treatment.objects.filter(profile=obj)
    stage0 = Stage0.objects.get(Profile_id=obj)
    stage1 = Stageone.objects.get(Profile_id=obj)
    out = Outcome.objects.get(Profile_id=obj)
    responses3 = Answers.objects.filter(profile_id=obj,stage="stage3")
    responses2 = Answers.objects.filter(profile_id=obj,stage="stage2")
    return render(request,'pages/docum_doc.html',{'name':decrypt(prof.name),'phone':decrypt(prof.phone),'i':obj,'prof':prof,'res':res,'zero':stage0,'one':stage1,'resu2':responses2,'resu3':responses3,'out':out,'questionjson2':questions['stage2'],'questionjson3':questions['stage3'],'treats':treat})
    
def coun_app(request):
    app = Past_Appoint.objects.all()
    
    prof=[]
    doc=[]
    name=[]
    phone=[]
    for i in app:
        prof.append(Profile.objects.filter(id=i.profile_id))
        for a in Profile.objects.filter(id=i.profile_id):
            name.append(decrypt(a.name))
        for a in Profile.objects.filter(id=i.profile_id):
            name.append(decrypt(a.phone))   
        doc.append(Doctor.objects.filter(id=i.doctor_id))
        
        # a=Profile.objects.filter(id=i.profile_id)
        print(name)
    
    return render(request,'pages/counsellor_appoint.html',{'app':app,'prof':prof,'doc':doc,'name':name,'phone':phone})
def addcolumn(request,obj):
    if request.method == "POST":
        session = request.POST['Head']
        treat = request.POST['Prescription']
        
        
        objs_to_delete = Past_Appoint.objects.filter(profile_id=obj,session=session)
        objs_to_delete.delete()
            
        Treatment(profile_id=obj,session=session,treat=treat).save()
        return redirect('doctor')
    return render(request,"pages/addcolumn.html")
def terms(request):
    return render(request,'pages/terms.html')
def PasswordResetCompleteView(request):
    return render(request,'authentication/password_reset_complete.html')
def PasswordResetConfirmView(request):
    return render(request,'authentication/password_reset_confirm.html')
def PasswordResetDoneView(request):
    return render(request,'authentication/password_reset_done.html')
def PasswordResetView(request):
    return render(request,'authentication/password_reset_form.html')
@csrf_exempt
def resone(request):
        print("view")
        jsonData = json.loads(request.body)
        print(jsonData['stress'])
        stress = jsonData['stress']
        anxiety = jsonData['anxiety']
        
        stress=2
        anxiety=5
        
        request.session['stress'] = stress
        request.session['anxiety'] = anxiety
        prof = Profile.objects.get(user=request.user)
        request.session['id'] = prof.id
        Stageone.objects.get_or_create(
        greetings=jsonData['Greetings'],
        readiness = jsonData['Ready to start'],
        ques1=jsonData['Do you sometimes have trouble falling asleep? Say yes or no'],
        ques2=jsonData['Do you worry about the future?.Say yes or no'],
        ques3=jsonData['Do you often reach for a cigarette, a drink, or a tranquilizer in order to reduce tension? .Say yes or no'],
        ques4=jsonData['Do you become irritated over basically insignificant matters ?.Say yes or no'],
        ques5=jsonData['Do you have less energy than you seem to need or would like to have?.Say yes or no'],
        ques6=jsonData['Do you have too many things to do and not enough time to do them? .Say yes or no'],
        ques7=jsonData['Do you have headaches or stomach problems?.Say yes or no'],
        ques8=jsonData['Do you feel pressure to accomplish or to get things done?.Say yes or no'],
        
        ques9=jsonData['Do you find it hard to stop worrying?'],
        ques10=jsonData['Do you experience feelings of restlessness?'],
        ques11=jsonData['Do you have feelings of tiredness easily?'],
        ques12=jsonData['Do you have difficulty concentrating?'],
        ques13=jsonData['Do you feel irritable?'],
        ques14=jsonData['Do you experience muscle pain?'],
        
        stress=jsonData['stress'],
        anxiety=jsonData['anxiety'],
        Profile_id = prof.id)
        print("in view"+stress)
        print(anxiety)
        
        
        return JsonResponse({'name':'hi'}, safe=False)
        
    
def navi(request):
    print("in navi")
    stress=request.session['stress']
    anxiety=request.session['anxiety']
    
    id=request.session['id']
   
    print("heyyyy")
    print(stress)
    print(anxiety)
    print(id)
    
    if stress<=2 and  anxiety<=2:
            
            return redirect('logout_h')
    elif stress>anxiety:
        print("vanten da")
        
        return redirect('Stress_Stag2')
    elif anxiety>stress:
        
        return redirect('Anxiety_Stag2')
    else:
        return redirect('Stress_Stag2')
    

# key = Fernet.generate_key()
key=b'Cp-AAWHWkXClIJS-XokS9KTOtMxaw0pJWDh2lJqM1X4='

# Create a Fernet object with the key
fernet = Fernet(key)

def encrypt(plain_text):
    # Encrypt the plain text
    cipher_text = fernet.encrypt(plain_text.encode())

    # Return the cipher text
    return cipher_text.decode()

def decrypt(cipher_text):
    # Decrypt the cipher text
    print(key)
    plain_text = fernet.decrypt(cipher_text.encode())

    # Return the plain text
    return plain_text.decode()


def password_reset_view(request):
    if request.method == 'POST':
        # Get the user's email address
        email = request.POST.get('email')

        # Look up the user by email address
        user = User.objects.filter(email=email).first()

        # If the user exists, generate a password reset token and send an email
        if user:
            # Generate a token
            
            token = default_token_generator.make_token(user)

            # Construct the password reset URL
            reset_url = request.build_absolute_uri('password_reset_confirm', kwargs={
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token
            })

            # Send the email
            send_mail(
                'Password reset request',
                f'Please follow this link to reset your password: {reset_url}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

        # Always display a success message to avoid giving away which email addresses exist in the system
        messages.success(request, 'Password reset email sent')

    return render(request, 'authentication/password_reset.html')
def password_reset_confirm(request, uidb64, token):
    user_id = force_str(urlsafe_base64_decode(uidb64))
    user = get_object_or_404(User, pk=user_id)

    # Check that the token is valid
    if not default_token_generator.check_token(user, token):
        messages.error(request, 'Invalid or expired token')
        return redirect('password_reset')

    # Check that the token hasn't expired
    # if user.password_reset_token_created_at < datetime.now() - timedelta(days=settings.PASSWORD_RESET_TIMEOUT_DAYS):
    #     messages.error(request, 'Invalid or expired token')
    #     return redirect('password_reset')

    if request.method == 'POST':
        # Validate the new password
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
        elif len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters')
        else:
            # Set the new password and clear the password reset token
            user.set_password(password)
            user.password_reset_token = None
            user.password_reset_token_created_at = None
            user.save()
            messages.success(request, 'Password reset successfully')

            return redirect('login')

    return render(request, 'authentication/password_reset_confirm.html')
