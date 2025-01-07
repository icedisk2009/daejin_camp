import streamlit as st

# 페이지 제목
st.title("MBTI 성격 유형 테스트")

# 설명
st.write("""
이 앱은 간단한 설문을 통해 당신의 MBTI 성격 유형을 추정합니다.  
각 질문에 답변하고 결과를 확인하세요!
""")

# 질문 리스트
questions = [
    ("사람들과 함께 시간을 보내는 것을 좋아하나요?", "E", "I"),
    ("결정을 내릴 때 논리와 사실에 기반을 두나요?", "T", "F"),
    ("계획을 세우고 따르는 것을 선호하나요?", "J", "P"),
    ("상상력과 아이디어에 더 끌리나요?", "N", "S")
]

# 사용자 응답 저장
answers = []

# 질문 반복 처리
for question, option_a, option_b in questions:
    answer = st.radio(question, (option_a, option_b))
    answers.append(answer)

# 결과 계산
if st.button("결과 보기"):
    if len(answers) == len(questions):  # 모든 질문에 답했는지 확인
        mbti_result = "".join(answers)
        st.success(f"당신의 MBTI 유형은 **{mbti_result}** 입니다!")
    else:
        st.warning("모든 질문에 답해주세요.")
