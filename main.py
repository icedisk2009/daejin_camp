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

# API 키 검증 상태
api_key_valid = False

if api_key:
    # API 키 검증
    try:
        openai.api_key = api_key

        # 간단한 테스트 요청으로 API 키 유효성 확인
        openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "API 키 검증 테스트입니다."},
                {"role": "user", "content": "테스트"}
            ]
        )
        st.success("API 키가 유효합니다!")
        api_key_valid = True

    except Exception as e:
        st.error(f"API 키가 유효하지 않습니다. 다시 입력해 주세요. 오류: {e}")

# 질문 입력 필드 (API 키가 유효한 경우에만 표시)
if api_key_valid:
    question = st.text_input(
        "질문",
        placeholder="MBTI에 대해 궁금한 점을 입력해 주세요."
    )

    if question:
        with st.spinner("ChatGPT가 답변을 작성 중입니다..."):
            try:
                # ChatGPT 프롬프트 생성
                prompt = f"""
                당신은 MBTI 전문가입니다. 아래 질문에 대해 MBTI 지식을 기반으로 명확하고 간결하게 답변해 주세요.

                질문: {question}
                """

                # OpenAI ChatCompletion 호출
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # 최신 모델 사용
                    messages=[
                        {"role": "system", "content": "당신은 MBTI 전문가입니다."},
                        {"role": "user", "content": question}
                    ],
                    max_tokens=150,
                    temperature=0.7,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                # 응답 출력
                answer = response['choices'][0]['message']['content'].strip()
                st.markdown(f"### 답변\n{answer}")

            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
