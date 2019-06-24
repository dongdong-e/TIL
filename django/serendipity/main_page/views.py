from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_integer
from .models import Photo, Photo_info
from serendipity.settings import *
import os
from datetime import datetime, timedelta
import random
import string

import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException



def index(request):
    return render(request, 'main_page/index.html')



def upload(request):
    if request.method=="POST":
        if not os.path.exists(MEDIA_ROOT):
            os.mkdir(MEDIA_ROOT)
        path = os.path.join(MEDIA_ROOT, 'files')
        if not os.path.exists(path):
            os.mkdir(path)
        path2 = os.path.join(path, str(request.user.pk))
        if not os.path.exists(path2):
            os.mkdir(path2)
        if Photo.objects.all().count()==0:
            upload_num =0
        else:
            p = Photo.objects.all().last()
            last_upload_num = p.upload_num
            upload_num = last_upload_num+1
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
    return render(request,'main_page/upload.html',context)