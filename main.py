from re import S
from unittest import result


def smart_calculator():
    print("مرحبا بك في الآلة الحاسبة")
    # طلب ادخال رقمين بي try
    try :
     num1 = float(input("أدخال الرقم الاول (num1):"))
     num2 = float(input("ادخال الرقم الثاني (num2):"))
    except ValueError:
        print("الرجاء إدخال رقم صحيح")
        return

    #إختيار العملية
    print("/n الرجاء إدخال العمليةالمطلوبة :")
    print("الجمع (+)")
    print("الطرح (-)")
    print("الضرب (*)")
    print("القسمة (/)")
    operaion = input("ادخل رمز العملية(+,-,*,/):")
    result = None
    if operaion == "+":
        result = num1 + num2
        operaion_name = "الجمع"
    elif operaion == "-":
        result = num1 - num2
        operaion_name = "الطرح"
    elif operaion == "*":
        result = num1 * num2
        operaion_name = "الضرب"
    elif operaion_name == "/":
        if num2 != 0:
         result = num1 / num2
         operaion_name = "القسمة"

    #معالجة حالة القسمة على صفر
    else:
        print("خطأ:لا يمكن القسمة على صفر")
        return
    # عرض النتيجة 
    print(f"/n---نتائج العملية---")
    print(f" عملية{operaion_name}ل {num1} و { num2} = **{result}**")

    #توضيح العلاقة بين الرقمين
    print("/n---العلاقة بين الرقمبن---")
    if num1 > num2:
        print(f"**{num1}** **اكبر** من **{num2}**.")
    elif num1 < num2:
        print(f"**{num1}** **اصغر**من **{num2}**.")
    else:
        print(f"**{num1}** **يساوي** **{num2}**.") 
    # تشغيل البرنامج
    smart_calculator()