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
        # OpenAI API 키 설정
        openai.api_key = api_key

        prompt = f"""
        당신은 MBTI 전문가입니다. 아래 질문에 대해 MBTI 지식을 기반으로 명확하고 간결하게 답변해 주세요.

        질문: {question}
        """

        try:
            # OpenAI API 호출
            response = openai.Completion.create(
                engine="text-davinci-003",  # GPT-3.5 모델
                prompt=prompt,
                max_tokens=150,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # 응답 출력
            answer = response.choices[0].text.strip()
            st.markdown(f"### 답변\n{answer}")

        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
