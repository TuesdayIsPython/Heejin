# def gugudan (a) :
#     if a <10:
#         for i in range(1,10):
#             print(a, "*", i, "=", a*i)
#
#
# b = gugudan(int(input()))
# print(b)

# 왜 마지막에 None이 보이는걸까요....

prompt = """
    ...1. 예금 입금
    ...2. 예금 출금
    ...3. 잔액 조회
    ...4. 업무 종료하기
    ...
    ... 수행하실 업무를 입력하세요 : """
print (prompt)

def bank(a):
    prompt = """
    ...1. 예금 입금
    ...2. 예금 출금
    ...3. 잔액 조회
    ...4. 업무 종료하기
    ...
    ... 수행하실 업무를 입력하세요 : """

    money = 10000000

    while a != 4:
        print(prompt)
        a = int(input())
        print(a)
        if a == 2:
            print("예금 출금하시겠습니까? 현재 출금 가능한 금액은 %d원입니다" % money)
            out = int(input("출금하실 금액을 입력해주세요. "))
            if out > 10000000:
                print("출금 금액이 출금 가능하신 금액을 초과했습니다. 은행 시스템을 재시작합니다.")
            else:
                money = money - out

        elif a == 1:
            print("예금 입급하시겠습니까?")
            inm = int(input("입금하실 금액을 입력해주세요:"))
            print("입금하신 금액은 %d원입니다." % inm)
            money = money + inm

        elif a == 3:
            print("잔액 조회를 도와드리겠습니다. ")
            print("현재 잔액은 %d원입니다. " % money)
        else:
            print("은행 시스템을 종료합니다.")



a=bank(int(input()))
print(a)

#시작하자마자 promopt 창이 어떻게 열리는건지ㅠㅠㅠㅠㅠㅠ