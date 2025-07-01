# https://calmmimiforest.tistory.com/125

import pandas as pd
import pandas_gpt
import openai


# 다음사이트로 접속해서 api_key받으세요
# https://drive.google.com/drive/folders/1q0Qf5c4GEKx3EtZSqznAK2nuQ2Sj1m1q?usp=sharing
OPENAI_API_KEY=''



import pandas as pd
import pandas_gpt

# 여기에 본인의 OpenAI API 키를 직접 입력하세요.
# !!!주의!!! 실제 서비스 배포 시에는 이 방법을 사용하지 않는 것이 좋습니다.
# 보안상의 이유로 환경 변수를 사용하는 것을 강력히 권장합니다.
#OPENAI_API_KEY = "YOUR_ACTUAL_OPENAI_API_KEY" # "sk-..." 와 같은 형식의 키를 여기에 붙여넣으세요.

# OpenAI completer 설정
pandas_gpt.completer = pandas_gpt.OpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

# 1. 샘플 DataFrame 생성
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'Price': [1200, 25, 75, 300, 50],
    'Stock': [10, 50, 30, 8, 20],
    'Category': ['Electronics', 'Peripherals', 'Peripherals', 'Electronics', 'Peripherals']
}
df = pd.DataFrame(data)

print("원본 DataFrame:")
print(df)
print("\n" + "="*30 + "\n")

# 2. 자연어 쿼리를 사용하여 데이터 분석
# 가격이 100보다 높은 제품만 필터링
print("가격이 100을 초과하는 제품 필터링:")
high_value_products = df.ask('show products where price is greater than 100')
print(high_value_products)
print("\n" + "="*30 + "\n")

# 재고가 가장 많은 카테고리 찾기
print("재고가 가장 많은 카테고리는 무엇인가요?")
most_stocked_category = df.ask('which category has the highest total stock?')
print(most_stocked_category)
print("\n" + "="*30 + "\n")

# 'Value' 컬럼 추가: Price * Stock
print("새로운 컬럼 'Value' 추가 (Price * Stock):")
df_with_value = df.ask('add a new column named "Value" which is Price multiplied by Stock')
print(df_with_value)
print("\n" + "="*30 + "\n")