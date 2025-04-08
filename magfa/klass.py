"""
 * magfa client 
 * author: @alisharify7
 * Under GPL-3.0 license.
 * email: alisharifyofficial@gmail.com
"""

import typing

from requests import Response

from common.http import HttpMethodUtils


class MagfaSMS(HttpMethodUtils):
    """
    main SMS magfa class.
    use object of this class for interacting with magfa
    api service.

    mian doc: https://messaging.magfa.com/ui/?public/wiki/api/http_v2
    error codes doc: https://messaging.magfa.com/ui/?public/wiki/api/http_v2#errors
    """

    error_codes = {
        1: "شماره گيرنده نادرست است",
        2: "شماره فرستنده نادرست است",
        3: "پارامتر encoding نامعتبراست. (بررسی صحت و هم‌خوانی متن پيامک با encoding انتخابی)",
        4: "پارامتر mclass نامعتبر است",
        6: "پارامتر UDH نامعتبر است",
        8: "زمان ارسال پيامک، خارج از باره‌ی مجاز ارسال پيامک تبليغاتی (۷ الی ۲۲) است",
        13: "محتويات پيامک (تركيب UDH و متن) خالی است. (بررسی دوباره‌ی متن پيامک و پارامتر UDH)",
        14: "مانده اعتبار ريالی مورد نياز برای ارسال پیامک کافی نيست",
        15: "سرور در هنگام ارسال پيام مشغول برطرف نمودن ايراد داخلی بوده است. (ارسال مجدد درخواست)",
        16: "حساب غيرفعال است. (تماس با واحد فروش سيستم‌های ارتباطی)",
        17: "حساب منقضی شده است. (تماس با واحد فروش سيستم‌های ارتباطی)",
        18: "نام كاربری و يا كلمه عبور نامعتبر است. (بررسی مجدد نام كاربری و كلمه عبور)",
        19: "درخواست معتبر نيست. (تركيب نام كاربری، رمز عبور و دامنه اشتباه است. تماس با واحد فروش برای دريافت كلمه عبور جديد)",
        20: "شماره فرستنده به حساب تعلق ندارد",
        22: "اين سرويس برای حساب فعال نشده است",
        23: "در حال حاضر امکان پردازش درخواست جديد وجود ندارد، لطفا دوباره سعی كنيد. (ارسال مجدد درخواست)",
        24: "شناسه پيامک معتبر نيست. (ممكن است شناسه پيامک اشتباه و يا متعلق به پيامكی باشد كه بيش از يک روز از ارسال آن گذشته)",
        25: "نام متد درخواستی معتبر نيست. (بررسی نگارش نام متد با توجه به بخش متدها در اين راهنما)",
        27: "شماره گيرنده در ليست سياه اپراتور قرار دارد. (ارسال پيامک‌های تبليغاتی برای اين شماره امكان‌پذير نيست)",
        28: "شماره گیرنده، بر اساس پیش‌شماره در حال حاضر در مگفا مسدود است",
        29: "آدرس IP مبدا، اجازه دسترسی به این سرویس را ندارد",
        30: "تعداد بخش‌های پیامک بیش از حد مجاز استاندارد (۲۶۵ عدد) است",
        31: "فرمت JSON‌ ارسالی صحيح نیست",
        33: "مشترک، دريافت پيامک از اين سرشماره را مسدود نموده است (لغو ۱۱)",
        34: "اطلاعات تایید‌شده برای اين شماره وجود ندارد",
        101: "طول آرايه پارامتر messageBodies با طول آرايه گيرندگان تطابق ندارد",
        102: "طول آرايه پارامتر messageClass با طول آرايه گيرندگان تطابق ندارد",
        103: "طول آرايه پارامتر senderNumbers با طول آرايه گيرندگان تطابق ندارد",
        104: "طول آرايه پارامتر udhs با طول آرايه گيرندگان تطابق ندارد",
        105: "طول آرايه پارامتر priorities با طول آرايه گيرندگان تطابق ندارد",
        106: "آرايه‌ی گيرندگان خالی است",
        107: "طول آرايه پارامتر گيرندگان بيشتر از طول مجاز است",
        108: "آرايه‌ی فرستندگان خالی است",
        109: "طول آرايه پارامتر encoding با طول آرايه گيرندگان تطابق ندارد",
        110: "طول آرايه پارامتر checkingMessageIds با طول آرايه گيرندگان تطابق ندارد",
    }

    def __init__(
        self,
        username: str,
        password: str,
        domain: str,
        endpoint: str = "https://sms.magfa.com/api/http/sms/v2/",
        sender: str | None = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.base_url = endpoint
        self.username = username
        self.password = password
        self.domain = domain
        self.sender = sender
        self.auth = (self.username + "/" + self.domain, self.password)

    def balance(self) -> Response:
        """get account balance.
        doc : https://messaging.magfa.com/ui/?public/wiki/api/http_v2#balance

        `example` JSON response:
            ..code-block:: json

            {
                "status" : 0,
                "balance" : 1000
            }

            {
                "status" : 18,
                "balance" : null
            }
        """
        return self.get(url=self.base_url + "balance", auth=self.auth)

    def send(
        self,
        recipients: typing.List[str],
        messages: typing.List[str],
    ) -> Response:
        """send sms
        doc: https://messaging.magfa.com/ui/?public/wiki/api/http_v2#send
        """

        return self.post(
            url=self.base_url + "send",
            auth=self.auth,
            json={
                "senders": [self.sender] * len(recipients),
                "recipients": recipients,
                "messages": messages,
            },
        )

    def messages(self, count: int = 100) -> Response:
        """get input messages
        doc: https://messaging.magfa.com/ui/public/wiki/api/http_v2#messages
        """
        count = count if count <= 100 else 100
        return self.get(url=self.base_url + f"messages/{count}", auth=self.auth)

    def statuses(self, mid) -> Response:
        """status of send message

        doc: https://messaging.magfa.com/ui/public/wiki/api/http_v2#statuses
        """
        return self.get(url=self.base_url + f"statuses/{mid}", auth=self.auth)

    def mid(self, uid: str) -> Response:
        """
        get
        doc: https://messaging.magfa.com/ui/public/wiki/api/http_v2#mid
        """
        return self.get(url=self.base_url + f"mid/{uid}", auth=self.auth)

    @staticmethod
    def get_error_message(error_code: int) -> str:
        """this method map the error code to error message.
        error docs: https://messaging.magfa.com/ui/?public/wiki/api/http_v2#errors
        """
        return MagfaSMS.error_codes.get(error_code, None)

    def normalize_data(self):
        # TODO: add normalize method
        pass

    def __str__(self):
        return f"<Magfa SMS>"

    def __repr__(self):
        return self.__str__()
