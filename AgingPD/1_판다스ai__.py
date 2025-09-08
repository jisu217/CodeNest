# https://calmmimiforest.tistory.com/125
# https://pypi.org/project/pandas-gpt/

import pandas as pd
import pandas_gpt
import openai


# 코드에 open api key 있을떄, github에 자료 업로드시 이 key가 정지당함
# 별도의 환경변수로 넣어야함. 또는 txt 파일로 만들고 읽기해야함.
OPENAI_API_KEY=''
openai.api_key = OPENAI_API_KEY

import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/pleabargain/e79e39f56d04278d4e7bc64825de5196/raw/7e64971a126093298cd63644aeaec9d3d78d09b2/sample-sales-data.csv')

print(df.head())

#df.ask('일본의 판매량에 대한 막대 그래프를 그려줘')

#df.ask('미국과 일본의 연도별 판매량에 대해 선 그래프를 그려줘', verbose=True)

df.ask('EU 판매량 데이터에서 어느 년도가 가장 적게 판매됐어?, print해줘', verbose=True)

#df.ask('2016년 미국의 판매량을 2015년과 비교해서 막대그래프를 그려주고, 몇 % 증감했는지 설명해줘')

df1 = df.drop(columns='Sales Pct Change')
#df1.ask('2012~2014년도 미국의 연도별 판매량에 대해 막대 그래프를 그려주고, 년도별 증가/감소에 대해 설명해줘', verbose=True)

#df1.ask('2012~2014년도에 대해 미국의 년도별 증감 비율에 대해 설명해서 print해줘')