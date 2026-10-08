# exapp.py

# AI휴먼 | 31일차 실습
# Streamlit 앱 제작 및 배포
#
# [실습 과제]
# day31 폴더에 exapp 폴더를 생성합니다.
# exapp폴더에 독립적으로 실행되는 Streamlit 앱을 작성합니다. (주제와 UI구성은 자유)
# .env, .gitignore, README.md, requirements.txt 파일을 작성합니다.
# 환경변수를 2개 이상 생성합니다.
# 새로운 GitHub 원격레파지토리를 생성합니다.
# GIT을 통해 commit과 push를 진행합니다.
# Render Web Service에 배포합니다.
# Render에서 획득한 공개 URL을 단톡방에 제출합니다.

# 로컬 실행
# python -m streamlit run ./python/webservice/day31/ezapp/exapp.py

# Render Cloud 실행 (Start Command)
# streamlit run exapp.py --server.port $PORT --server.address 0.0.0.0

import os
import pandas as pd
import psycopg
import streamlit as st
from dotenv import load_dotenv
from psycopg.rows import dict_row



# .env 파일의 환경변수를 로딩
load_dotenv()

DEFAULT_GREETING = 'AI 휴먼'
APP_GREETING = os.getenv('APP_GREETING', DEFAULT_GREETING)

def get_connection():
    # 환경변수 기반 PostgreSQL Connection을 반환합
    return psycopg.connect(APP_GREETING)

st.set_page_config(
    page_title='맛집 저장 앱',
    page_icon='🍰',
    layout='centered'
)


st.title('맛집 저장 앱')
st.form('bab.form', clear_on_submit=True)
store_name = st.text_input('가게이름')
region = st.text_input('지역')
grade = st.number_input(
    '평점',
    min_value=0.0,
    max_value=5.0,
    value=0.0,
    step=0.5
)
memo = st.text_area("메모")
submitted = st.form_submit_button("저장")

if submitted:
    if not store_name.strip() or not region.strip():
        st.warning("가게이름과 지역을 입력하세요.")
    elif not 0.0 <= grade <= 1.0:
        st.warning("평점는 0.0 ~ 5.0이어야 합니다.")
    else:
        store_name.strip(),
        region.strip(),
        float(grade),
        memo.strip()

        st.success("맛집 정보를 저장했습니다.")

#
# st.subheader('환경변수 설정 확인')
#
# if os.getenv('APP_GREETING'):
#     st.success('APP_GREETING 환경변수를 성공적으로 읽었습니다!')
#     st.write(f'현재 인사말 설정 값: {APP_GREETING}')
# else:
#     st.info(f'APP_GREETING 환경변수가 설정되지 않아 기본값을 사용중입니다!')