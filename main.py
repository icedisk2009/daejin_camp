import openai
import streamlit as st

# Streamlit 앱 제목
st.title("MBTI 대백과사전")

# OpenAI API 키 입력
api_key = st.text_input(
    "OpenAI API 키를 입력하세요",
    placeholder="여기에 OpenAI API 키를 입력하세요.",
    type="password"  # 비밀번호 형태로 숨김 처리
)

# 사용자 질문 입력
question = st.text_input(
    "질문",
    placeholder="MBTI에 대해 궁금한 점을 입력해 주세요."
)

# ChatGPT 프롬프트 템플릿
if api_key and question:
    with st.spinner("ChatGPT가 답변을 작성 중입니다..."):
        # Open
