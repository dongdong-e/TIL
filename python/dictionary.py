# 1. dict 생성
shop_phone_1 = {
    '중국집': '02-111-1623',
    '한식집': '02-111-1512'
}

# 2. dict item 추가
shop_phone_1['분식집'] = '02-121-9561'

# 3. dict value 호출
shop_phone_1 = {
    '한식집': {
        '경복궁': '02-951-7962'
    }
}

shop_phone_1['한식집']['경복궁']

# 4. dict 내부 자료형
# key값에 가능한 type: string, interger, float, boolean
# value값에 가능한 type: 모든 자료형(list, dict 포함)

# 5. dict 반복문 활용
shop_phone_2 = {
    '일식집': '02-111-1623',
    '중식집': '02-111-1512',
    '분식집': '02-111-1999'
}

# 5-1. 기본
for item in shop_phone_2:
    print(item)

# 5-2. key값 반복
for key in shop_phone_2.keys():
    print(key)

# 5-3. value값 반복
for value in shop_phone_2.values():
    print(value)

# 5-3. key값, value값 동시 출력
for key, value in shop_phone_2.items():
    print(key,':' ,value)