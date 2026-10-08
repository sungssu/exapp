# exapp.py

# AI휴먼 | 31일차 실습
# Streamlit 앱 제작 및 배포
#
# [실습 과제]
# day31 폴더에 exapp 폴더를 생성합니다.
# exapp폴더에 독립적으로 실행되는 Streamlit 앱을 작성합니다. (주제와 UI구성은 자유)
# .env, .gitignore, README.md, requirements.txt 파일을 작성합니다.
# 새로운 GitHub 원격레파지토리를 생성합니다.
# GIT을 통해 commit과 push를 진행합니다.
# Render Web Service에 배포합니다.
# Render에서 획득한 공개 URL을 단톡방에 제출합니다.

# 로컬 실행
# python -m streamlit run ./python/webservice/day31/exapp/exapp.py

# Render Cloud 실행 (Start Command)
# streamlit run exapp.py --server.port $PORT --server.address 0.0.0.0

import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv


# .env 파일의 환경변수를 로딩
load_dotenv()

DEFAULT_GREETING = 'AI 휴먼'
APP_GREETING = os.getenv('APP_GREETING', DEFAULT_GREETING)


st.set_page_config(
    page_title='동물 사전 앱',
    page_icon='🐾',
    layout='centered'
)

st.title('🐾 동물 사전 앱')
st.write('사이드바에서 종류를 고르거나, 상단 검색창에서 원하는 동물을 직접 찾아보세요!')

# 동물 데이터 정의 (종류당 5개씩, 이미지 URL 수정)
animal_data = {
    '육지': {
        '사자': {
            '영문명': 'Lion',
            '특징': '밀림의 왕이라 불리며, 무리(프라이드)를 지어 생활합니다.',
            '서식지': '아프리카 초원',
            '식성': '육식',
            '이미지': 'https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?w=600'
        },
        '코끼리': {
            '영문명': 'Elephant',
            '특징': '지상에서 가장 큰 포유류이며, 긴 코와 상아가 특징입니다.',
            '서식지': '아프리카, 아시아',
            '식성': '초식',
            '이미지': 'https://images.unsplash.com/photo-1557050543-4d5f4e07ef46?w=600'
        },
        '기린': {
            '영문명': 'Giraffe',
            '특징': '목이 매우 길어 높은 곳의 나뭇잎을 뜯어먹을 수 있습니다.',
            '서식지': '아프리카 사바나',
            '식성': '초식',
            '이미지': 'https://images.unsplash.com/photo-1547721064-da6cfb341d50?w=600'
        },
        '호랑이': {
            '영문명': 'Tiger',
            '특징': '주황색 바탕에 검은 줄무늬가 있으며 단독 생활을 합니다.',
            '서식지': '아시아 (시베리아, 인도 등)',
            '식성': '육식',
            '이미지': 'https://images.unsplash.com/photo-1561731216-c3a4d99437d5?w=600'
        },
        '판다': {
            '영문명': 'Panda',
            '특징': '눈 주변의 검은 털이 특징이며 주로 대나무를 먹습니다.',
            '서식지': '중국 산악 지대',
            '식성': '초식 (주로 대나무)',
            '이미지': 'https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=600'
        }
    },
    '해양': {
        '상어': {
            '영문명': 'Shark',
            '특징': '연골로 이루어진 골격을 가졌으며 바다의 최상위 포식자 중 하나입니다.',
            '서식지': '전 세계 바다',
            '식성': '육식',
            '이미지': 'https://images.unsplash.com/photo-1560275619-4662e36fa65c?w=600'
        },
        '바다거북': {
            '영문명': 'Sea Turtle',
            '특징': '등딱지를 가지고 있으며 수중에서 호흡을 위해 물 위로 올라옵니다.',
            '서식지': '열대 및 아열대 바다',
            '식성': '잡식 (해초, 해파리 등)',
            '이미지': 'https://images.unsplash.com/photo-1437622368342-7a3d73a34c8f?w=600'
        },
        '푸른문어': {
            '영문명': 'Octopus',
            '특징': '8개의 다리와 뛰어난 위장 능력을 가지고 있습니다.',
            '서식지': '바다 밑바닥',
            '식성': '육식 (게, 조개 등)',
            '이미지': 'https://images.unsplash.com/photo-1545671913-b89ac1b4ac10?w=600'
        },
        '범고래': {
            '영문명': 'Killer Whale (Orca)',
            '특징': '돌고래과 중 가장 큰 체구를 가졌으며 강력한 협동 사냥을 합니다.',
            '서식지': '차가운 극지방 및 온대 바다',
            '식성': '육식',
            '이미지': 'https://images.unsplash.com/photo-1568430462989-44163eb1752f?w=600'
        }
    },
    '조류': {
        '독수리': {
            '영문명': 'Eagle',
            '특징': '날카로운 부리와 발톱을 지닌 강력한 맹금류입니다.',
            '서식지': '산악 지역 및 삼림',
            '식성': '육식',
            '이미지': 'https://images.unsplash.com/photo-1611689342806-0863700ce1e4?w=600'
        },
        '펭귄': {
            '영문명': 'Penguin',
            '특징': '날지 못하는 새이지만 물속에서 헤엄을 매우 잘 칩니다.',
            '서식지': '남극 및 남반구',
            '식성': '육식 (크릴새우, 물고기)',
            '이미지': 'https://images.unsplash.com/photo-1598439210625-5067c578f3f6?w=600'
        },
        '홍학 (플라밍고)': {
            '영문명': 'Flamingo',
            '특징': '깃털이 분홍빛을 띠며 한 발로 서서 쉬는 습관이 있습니다.',
            '서식지': '염호, 갯벌',
            '식성': '잡식 (조류, 새우 등)',
            '이미지': 'https://images.unsplash.com/photo-1497206365907-f5e630693df0?w=600'
        },
        '앵무새': {
            '영문명': 'Parrot',
            '특징': '화려한 색상과 사람의 말을 흉내 내는 능력이 뛰어납니다.',
            '서식지': '열대 및 아열대 지역',
            '식성': '초식 (견과류, 과일, 씨앗)',
            '이미지': 'https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=600'
        }
    }
}

# 1. 메인 화면 상단 검색창 배치
search_query = st.text_input('🔍 검색할 동물 이름을 입력하세요 (예: 사자, 돌고래...)', placeholder='여기에 검색어를 입력하세요')

# 사이드바 구성
with st.sidebar:
    st.header('📂 카테고리 탐색')
    selected_category = st.selectbox(
        '동물 종류',
        ['육지', '해양', '조류']
    )

    animals_in_category = list(animal_data[selected_category].keys())
    selected_animal = st.selectbox(
        '세부 동물 선택',
        animals_in_category
    )

st.write("---")


# 공통 정보 출력 함수 정의 (설명이 먼저 나오고 사진이 맨 아래에 오도록 배치)
def display_animal_info(category, name, info):
    st.subheader(f'📖 [{category}] {name} 정보')

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**영문명**: {info['영문명']}")
        st.info(f"**서식지**: {info['서식지']}")

    with col2:
        st.success(f"**식성**: {info['식성']}")
        st.success(f"**대표 특징**: {info['특징']}")

    st.write(f"💡 **상세 설명**: {name}은(는) {info['서식지']}에 주로 서식하며, {info['특징']} 특징을 가진 멋진 동물입니다.")

    # 사진을 맨 밑에 배치 (width=400)
    st.image(info['이미지'], caption=f"{name} ({info['영문명']})", width=400)


# 2. 검색창에 입력이 들어온 경우 처리 (기록에 없는 동물 체크 포함)
if search_query.strip():
    found = False
    matched_category = ""
    matched_name = ""
    matched_info = {}

    for cat, animals in animal_data.items():
        if search_query.strip() in animals:
            found = True
            matched_category = cat
            matched_name = search_query.strip()
            matched_info = animals[matched_name]
            break

    if found:
        st.success(f"'{matched_name}'에 대한 검색 결과입니다.")
        display_animal_info(matched_category, matched_name, matched_info)
    else:
        # 기록에 없는 동물일 때 출력
        st.error(f"'{search_query.strip()}'은(는) 없는 동물입니다. 다른 이름을 검색해 보세요!")

# 3. 검색창에 입력이 없을 때는 사이드바에서 선택한 동물 정보를 기본으로 보여줌
else:
    info = animal_data[selected_category][selected_animal]
    display_animal_info(selected_category, selected_animal, info)