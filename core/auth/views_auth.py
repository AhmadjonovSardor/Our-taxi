import random
import uuid

from django.conf import settings
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import render,redirect


from core.base.helper import code_decoder, generate_key
from core.models.models_auth import User, OTP


def register(request):
    ctx = {}
    if request.POST:
        data = request.POST
        phone = data.get('phone', None),
        username = data.get('username', None),
        password = data.get('email',None)
        password_conf = data.get('email', None),
        if None in [phone,password,username,password_conf] or '' in [phone,password,username,password_conf]:
            ctx['error'] = 'Hamma polyani tuldiring'
            return render(request, 'register.html', ctx)

        phone = phone[0].replace('+', '').replace(' ', '')
        user = User.objects.filter(phone=phone).first()

        if user:
            ctx['error'] = 'Bunaqa yuzur mavjut'
            return render(request, 'register.html', ctx)

        if pass != pas_conf:
            print('ikkinchi')
            ctx['error'] = "Parollar bir xil emas"
            return render(request, 'user/register.html', ctx)

        # OTP ->

        number = random.randint(100_000, 999_999)


        hash = f'{generate_key(15)}${number}${uuid.uuid4().__str__()}'
        hashed = code_decoder(hash, decode=False, l=settings.HASH_LENGTH)
        print(hash)
        print(hashed)
        otp = OTP.objects.create(
            kalit=hashed,
            mobile=phone,
            extra = {"username":username, 'email':email, 'password':code_decoder(password)},
            step = 'regis'
        )

        request.session['key'] = otp.kalit
        request.session['otp'] = number  # bu narsa bumedi

        return redirect('step_two')

    return render(request,'user/register.html',ctx)

def step_two(request):
    ctx={}
    key = request.session.get("key", None)
    if key is None:
        return  redirect('register')

    if request.POST:
        otp = request.POST.get('otp','')
        otp_base = OTP.objects.filter(kalit=key).first()
        if otp_base is None:
            ctx['error'] = 'Kalit Topilmadi Intimos Boshqatdan Ruyxatdan Uting!'
            return render(request,'user/otp.html',ctx)

        if otp_base.is_verified or otp_base.is_expired:
            ctx['error'] = 'Bu token allaqachon eskirdi'
            return render(request, 'user/otp.html', ctx)

        if not otp_base.check_expire_date():
            ctx['error'] = 'Bu Tokinga Ajratilgan Vaqt Tugadi!'
            return render(request, 'user/otp.html', ctx)

        decode = code_decoder(key, decode=True, l=settings.HASH_LENGTH)
        code = decode.split("$")[1]
        print(code)
        if str(otp) != str(code):
            otp_base.tries += 1
            otp_base.save()
            ctx['error'] = 'Kod Xato'
            return render(request, 'user/otp.html', ctx)
        if otp_base.step == 'regis':
            extra = otp_base.extra
            password = extra.pop('password')
            user = User.objects.create_user(
                phone =otp_base.mobile,
                password = code_decoder(password, decode=True),
                **extra
            )

            login(request, user)
            authenticate(request)
            otp_base.is_verified = True
            otp_base.is_expired = True
            otp_base.step = "conf_regis"
            otp_base.save()
            try:
                del request.session['otp']
                del request.session['key']
            except:
                pass

            return redirect('home')
    else:
        pass

    return render(request,'user/otp.html',ctx)


def log_in(request):
    ctx = {}
    if request.POST:
        data = request.POST
        phone = data.get('phone', None),
        email = data.get('email', None),

        if None in [phone, email] or '' in [phone,email]:
            ctx['error'] = 'Hamma polyani tuldiring'
            return render(request, 'register.html', ctx)
        user = User.objects.filter(phone=phone).first()
        if user:
            ctx['error'] = 'Bunaqa yuzur mavjut emas'
            return render(request, 'register.html', ctx)

    return render(request,'user/login.html')

@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('register')



