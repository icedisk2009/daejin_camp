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
