'''

Welcome to mohammed khormi GDB Online.


'''
import math
print('مرحبا بكم في خدمة الصراف الآلي في بنك معسكر البايثون')
restart=('نعم')
chances = 3
balance = 670.14
while chances >= 0:
    pin = int(input('الرجاء إدخال رقمك السري والمكون من 4 خانات: '))
    if pin == (1234):
        print('التأكد من صحة الرقم السري للبطاقة\n')
        while restart not in ('n','NO','no','N'):
            print('اضغط 1- للإستعلام عن الرصيد')
            print('اضغط 2- للسحب')
            print ('اضغط 3- للمدفوعات')
            print('اضغط 4- للعودة للقائمة السابقة')
            option = int(input('اختر الخدمة المطلوبة ؟'))
            if option == 1:
                print('رصيدك هو  ريال سعودي',balance,'\n')
                restart = input('هل ترغب في الرجوع ؟')
                if restart in ('n','NO','no','N'):
                    print('شكراً لك')
                    break
            elif option == 2:
                option2 = ('نعم')
                withdrawl = float(input('المبلغ المطلوب للسحب? \n''100 /200 /500 /1000/  5000 \n أو 1 لاختيار مبلغ آخر  : '))
                if withdrawl in [100, 200, 500, 1000, 5000]:
                    balance = balance - withdrawl
                    print ('رصيدك الحالي هو \n',balance)
                    restart = input('هل ترغب بالعودة للقائمة السابقة ؟ ')
                    if restart in ('n','NO','no','N'):
                        print('شكراً لك')
                        break
                elif withdrawl != [100,50, 200, 500, 1000, 5000]:
                    print('المبلغ المطلوب للسحب غير متاح, الرجاء إختيار مبلغ آخر\n')
                    restart = ('نعم')
                elif withdrawl == 1:
                    withdrawl = float(input('الرجاء إختيار المبلغ المطلوب للسحب :'))    

            elif option == 3:
                Pay_in = float(input(' ادخل المبلغ المطلوب للسداد؟ \n '))
                balance = balance + Pay_in
                print ('\nرصيدك الحالي هو ريال سعودي',balance)
                restart = input('هل ترغب بالعودة ؟ ')
                if restart in ('n','NO','no','N'):
                    print('شكراً لك')
                    break
            elif option == 4:
                print('الرجاء الإنتظار لإرجاع بطاقتك \n')
                print('سعدنا بخدمتك شكراً لك')
                break
            else:
                print('الرجاء التأكد من صحة الرقم المدخل.\n')
                restart = ('نعم')
    elif pin != ('1234'):
        print('الرقم السري المخل غير صحيح')
        chances = chances - 1
        if chances == 0:
            print('\n لقد إستنفذت عدد مرات المحاولة ')
            break





#© 2021 GitHub@محمد خرمي , Inc.

