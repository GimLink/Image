# 텍스트 데이터 처리 01
import re
text_data = [" Emiya muljomdao. mokmalla motsalgetda",
            "Emiya. Yaga odegaseo jjangbakhiga an naono",
            "Emiya daedap jomhera. mokmaleda anhana."]

strip_whitespace = [string.strip() for string in text_data]
print("공백 제거 >> ", strip_whitespace)

# 마침표 제거
remove_periods = [string.replace(".", "") for string in strip_whitespace]
print("마침표 제거 >> ", remove_periods)

def capitalizer(string: str) -> str: return string.upper() # 대문자 변환
temp = [capitalizer(string) for string in remove_periods]
print(temp)

def replace_letters_with_X(string: str) -> str:
    return re.sub(r"[a-zA-z]", "X", string)

data = [replace_letters_with_X(string) for string in remove_periods]
print(data)