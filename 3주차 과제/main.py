#과제1

time = input("시간을 초 단위로 입력하세요:")
sec = int(time) % 60
min = int(time)//60%60
hour = int(time) // 3600
print(time, "초는", hour, "시간",min, "분", sec, "초입니다")


#과제2

data = "2021-05-04 오후 8시 비"

print("날짜 :", data[:10])
print("시간 :", data[11:16])
print("날씨 :", data[-1])

date=data[:10]
time=data[11:16]
weather=data[-1]

print("날짜 :", date)
print("시간 :", time)
print("날씨 :", weather)