pingpong_list = ["나영", "예진", "원빈", "현빈"]
def mail(list):
    result = []
    for name in list:
        email = "한국교통대학교 천하제일 탁구대회," + name + "님 탁구 대회에 참여해주셔서 감사합니다." \
                                "행사 일시 : 2023-10-06, 시간 : 10:30 AM, 복장 : 트레이닝복" \
                                "행사 당일에 뵙겠습니다." + name + "님 감사합니다"
        result.append(email)
    return result
mail_result = mail(pingpong_list)
print(mail_result)
