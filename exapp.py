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

import os
import streamlit as st
from dotenv import load_dotenv

# .env 파일의 환경변수를 로딩
load_dotenv()

DEFAULT_GREETING = 'AI 휴먼'
APP_GREETING = os.getenv('APP_GREETING', DEFAULT_GREETING)

st.set_page_config(
    page_title='맛집 저장 앱',
    page_icon='🍰',
    layout='centered'
)

st.title('맛집 저장 앱')

st.subheader('환경변수 설정 확인')

if os.getenv('APP_GREETING'):
    st.success('APP_GREETING 환경변수를 성공적으로 읽었습니다!')
    st.write(f'현재 인사말 설정 값: {APP_GREETING}')
else:
    st.info(f'APP_GREETING 환경변수가 설정되지 않아 기본값을 사용중입니다!')