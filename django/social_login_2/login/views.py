from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_integer
from login.models import Photo, Photo_info

from social_login.settings import *
import os
from datetime import datetime, timedelta
import random
import string

import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = UserForm()
        return render(request, 'memo_app/adduser.html', {'form': form})


def login(request):
    users = User.objects.all()
    #if (request.user.is_authenticated):
     #   sa = request.user.socialaccount_set.all()
        #return redirect('upload')
    if request.method == "POST":
        return redirect('upload/')

    context = {'users':users}
    return render(request, 'login/login.html', context)

def upload(request):
    if request.method=="POST":

        #file = request.FILES.get('img_file')
        #title= request.POST.get('title')
        #msg= request.POST.get('message')
        if not os.path.exists(MEDIA_ROOT):
            os.mkdir(MEDIA_ROOT)
        path = os.path.join(MEDIA_ROOT, 'files')
        if not os.path.exists(path):
            os.mkdir(path)
        path2 = os.path.join(path, str(request.user.pk))
        if not os.path.exists(path2):
            os.mkdir(path2)
        p = Photo.objects.all().last()
        last_upload_num = p.upload_num
        upload_num = last_upload_num+1
        print(f'last_upload_num: {last_upload_num}')
        print(f'upload_num: {upload_num}')
        if 'upload' in request.POST:
            for file in request.FILES.getlist('img_files'):
                LENGTH = 15
                # 숫자 + 대소문자
                string_pool = string.ascii_letters + string.digits

                # 랜덤한 문자열 생성
                url_ran = ""
                for i in range(LENGTH):
                    # 랜덤한 문자열 하나 선택
                    url_ran += random.choice(string_pool)
                print(url_ran)
                p = Photo(photo=file, from_user=request.user, upload_num = upload_num, random_url=url_ran)
                p.save()

            print("redirect delete")

            return redirect('delete', upload_num)

    photos = Photo.objects.filter(from_user=request.user)

    context= {'photos':photos}
    return render(request,'login/upload.html',context)

def delete(request, upload_num):
    if request.method == "POST":
        if 'delete' in request.POST:
            cbox_list = request.POST.getlist('cbox')

            for photo_pk in cbox_list:
                photo = Photo.objects.get(pk=photo_pk)
                photo.delete()

        elif 'next' in request.POST:
            cbox_list = request.POST.getlist('cbox')
            photos = Photo.objects.filter(from_user=request.user, msg_flag=False, upload_num=upload_num).order_by('-pk')
            for photo in photos:
                if str(photo.pk) not in cbox_list:
                    photo.delete()
            return redirect('set_phone_number', upload_num)

    photos = Photo.objects.filter(from_user=request.user,msg_flag=False, upload_num=upload_num).order_by('-pk')

    context = {'photos': photos}
    return render(request, 'login/delete.html', context)

def set_phone_number(request,upload_num):
    photos = Photo.objects.filter(from_user=request.user, msg_flag=False, upload_num=upload_num)
    print(photos)
    if request.method == "POST":
        period = request.POST.get('period')
        from_name = request.POST.get('from')
        phone_from = request.POST.get('phone_from')

        random_day = random.choice(range(0, int(period)+1))
        now = datetime.now()
        td = timedelta(days=random_day, minutes=3)
        random_date = now + td
        print(f'now: {now}, random_day={random_day}, random_date={random_date}')
        print(random_date)
        random_list=list(range(0,len(photos)))
        print(type(random_list))
        for i in range(1,6):
            if request.POST.get(f'phone_to{i}') is not "":
                phone_to = request.POST.get(f'phone_to{i}')
                to_name = request.POST.get(f'to{i}')
                message = request.POST.get(f'message{i}')
                if len(message) > 40:
                    msg = '메시지를 40자 이내로 입력해주세요'
                    context = {'msg': msg}
                    return render(request, 'login/message.html', context)
                photo_info = Photo_info(send_date=random_date, phone_from=phone_from, phone_to=phone_to,from_name=from_name,to_name=to_name, message=message,period=period)
                photo_info.save()
                photos = Photo.objects.filter(from_user=request.user, msg_flag=False, upload_num=upload_num)
                print(f'photos: {len(photos)}')
                rd = random.choice(random_list)
                random_list.remove(rd)
                print(f'rd: {rd}, random_list={random_list}')
                photos[rd].info=photo_info
                #photos[rd].set_flag = True
                # num = range(0, 1000)
                #
                # ran_num = random.sample(num, 5)
                #
                # ran_str = []
                #
                # for i in ran_num:
                #     ran_str.append(str(i))
                #
                # ran_str = "".join(ran_str)
                #
                #photos[rd].msg_flag=True
                photos[rd].save()
                print(photos[rd].info)
                print(photos[rd].info.send_date)
                #send_sms(photos[rd])
        # photos = Photo.objects.filter(from_user=request.user, msg_flag=False)
        # for photo in photos:
        #     photo.delete()
        return redirect('confirm', upload_num)

    return render(request,'login/set_phone_number.html')

def confirm(request, upload_num):
    photos = Photo.objects.filter(from_user=request.user, msg_flag=False, upload_num=upload_num)
    print(photos)
    if request.method == "POST":
        if 'edit' in request.POST:
            return redirect('edit', upload_num)
        elif 'confirm' in request.POST:
            for photo in photos:
                if photo.info is not None:
                    photo.msg_flag = True
                    photo.save()
                    #send_sms(photo)
                else:
                    photo.delete()
            msg = "성공적으로 보내졌습니다."
            context={'msg':msg,}
            print(msg)
            return render(request, 'login/message.html', context)

    info_list = []
    for photo in photos:
        print(photo.info)
        if photo.info is not None:
            info_list.append(photo.info)
    print(f'info_list: {info_list}')
    #info_list = Photo.objects.filter(from_user=request.user, upload_num=upload_num, set_flag=True)
    context={'photos':photos, 'info_list': info_list}
    return render(request,'login/confirm.html',context)

def edit(request, upload_num):
    photos = Photo.objects.filter(from_user=request.user, msg_flag=False, upload_num=upload_num)
    info_list = []
    no_info_list=[]
    for photo in photos:
        print(photo.info)
        if photo.info is not None:
            info_list.append(photo.info)
        else:
            no_info_list.append(photo)
    if request.method =="POST":
        period = request.POST.get('period')
        from_name = request.POST.get('from')
        phone_from = request.POST.get('phone_from')
        random_day = random.choice(range(0, int(period) + 1))
        now = datetime.now()
        td = timedelta(days=random_day, minutes=3)
        random_date = now + td
        print(f'len: {len(info_list)}')
        for i in range(0, len(info_list)):
            if request.POST.get(f'phone_to{i+1}') is not "":
                phone_to = request.POST.get(f'phone_to{i+1}')
                to_name = request.POST.get(f'to{i+1}')
                message = request.POST.get(f'message{i+1}')
                if len(message) > 40:
                    msg = '메시지를 40자 이내로 입력해주세요'
                    context = {'msg': msg}
                    return render(request, 'login/message.html', context)
                info_list[i].phone_to= phone_to
                info_list[i].to_name = to_name
                info_list[i].message = message
                info_list[i].send_date = random_date
                info_list[i].save()

        random_list = list(range(0, len(no_info_list)))
        for j in range(len(info_list)+1,6):
            phone_to = request.POST.get(f'phone_to{i}')
            to_name = request.POST.get(f'to{i}')
            message = request.POST.get(f'message{i}')
            if len(message) > 40:
                msg = '메시지를 40자 이내로 입력해주세요'
                context = {'msg': msg}
                return render(request, 'login/message.html', context)
            photo_info = Photo_info(send_date=random_date, phone_from=phone_from, phone_to=phone_to,from_name=from_name,to_name=to_name, message=message,period=period)
            photo_info.save()
            if random_list is not None:
                rd = random.choice(random_list)
                random_list.remove(rd)
                no_info_list[rd].info = photo_info
                no_info_list[rd].save()
        return redirect('confirm', upload_num)
    context = {'info_list': info_list}
    return render(request,'login/edit.html',context)


def send_sms(photo):
    api_key = "NCSBVGKDO0M3X1SD"
    api_secret = "Y25LHM18WNIS7XNN6MGRXVUIKWCHDHRT"

    print(photo.info)
    date = photo.info.send_date
    print(f'date:{date}')
    dt=date.strftime('%Y%m%d%H%M')
    print(f'dt : {dt}')
    #dt = date.year + datetime.month + datetime.day + datetime.hour + datetime.minute
    #print(dt)

    # 4 params(to, from, type, text)설정
    params = dict()
    params['type'] = 'sms'  # Message type ( sms, lms, mms, ata )
    params['to'] = photo.info.phone_to  # 받는사람번호(,로 추가가능)
    params['from'] = '01074210136'  # 보내는사람번호(coolsms사이트에 등록되어있어야함)
    params['text'] = 'Test Message'  # 보내는 메세지
    params['datetime'] = dt
    cool = Message(api_key, api_secret)

    # error 확인
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])
        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)

def photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    date = photo.created_at
    #save_date = date.strftime('%Y년 %m월 %d일 %H:%M')
    # random_num_list = str(range(1,10))
    # random_num_list = random_num_list + ['A','B','C','D','E']
    # random_str = ''
    # for i in range(0,5):
    #     random_num = random.choice(random_num_list)
    #     random_str = random_str + str(random_num)

    context = {'photo':photo, }
    return render(request, 'login/photo.html', context)