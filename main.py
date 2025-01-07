import streamlit as st

# 페이지 제목
st.title("MBTI 성격 유형 테스트")

# 앱 설명
st.write("""
이 앱은 간단한 설문을 통해 당신의 MBTI 성격 유형을 추정합니다.  
각 질문에 답변하고 결과를 확인하세요!  
MBTI는 16가지 성격 유형으로 나뉘며, 사람들의 성향과 행동 방식을 이해하는 데 도움을 줍니다.
""")

# MBTI 유형별 설명 데이터
mbti_descriptions = {
    "INTJ": "전략가형: 독립적이고 분석적이며 계획적인 성격입니다. 목표를 달성하기 위해 체계적으로 행동합니다.",
    "INTP": "논리술사형: 호기심 많고 창의적이며 아이디어를 탐구하는 데 열정적입니다.",
    "ENTJ": "통솔자형: 리더십이 강하며, 목표 지향적이고 조직적입니다.",
    "ENTP": "변론가형: 창의적이고 에너지가 넘치며 새로운 아이디어를 즐깁니다.",
    "INFJ": "옹호자형: 이상주의적이면서도 계획적이고, 다른 사람들을 돕는 데 열정적입니다.",
    "INFP": "중재자형: 공감 능력이 뛰어나고, 가치와 신념을 중요시합니다.",
    "ENFJ": "선도자형: 타인을 이끄는 데 능숙하며, 따뜻하고 외향적인 성격입니다.",
    "ENFP": "활동가형: 열정적이며 상상력이 풍부하고 자유로운 사고를 선호합니다.",
    "ISTJ": "현실주의자형: 책임감 있고 신뢰할 수 있으며, 체계적인 접근 방식을 선호합니다.",
    "ISFJ": "수호자형: 헌신적이고 배려심이 많으며, 타인을 돕는 것을 좋아합니다.",
    "ESTJ": "경영자형: 실용적이고 조직적인 성격으로, 리더십을 발휘하는 것을 좋아합니다.",
    "ESFJ": "집정관형: 사교적이고 타인을 돕는 데 열정을 가지며, 조화를 중요시합니다.",
    "ISTP": "장인형: 실용적이고 문제 해결 능력이 뛰어나며, 손재주가 좋습니다.",
    "ISFP": "모험가형: 예술적이고 감각적이며, 자유로운 삶을 추구합니다.",
    "ESTP": "사업가형: 에너지가 넘치고 현실적인 문제 해결 능력을 가지고 있습니다.",
    "ESFP": "연예인형: 사교적이고 활발하며, 주변 사람들과 즐거운 시간을 보내는 것을 좋아합니다."
}

# 질문 리스트 (질문, 선택지1, 선택지2)
questions = [
    ("1. 사람들과 함께 시간을 보내는 것을 좋아하나요?", 
     ("E", "외향적 (사교적)"), 
     ("I", "내향적 (혼자 있는 것을 선호)")),
    
    ("2. 결정을 내릴 때 논리와 사실에 기반을 두나요?", 
     ("T", "사고형 (논리적)"), 
     ("F", "감정형 (감정적으로 판단)")),
    
    ("3. 계획을 세우고 따르는 것을 선호하나요?", 
     ("J", "계획형 (체계적으로 행동)"), 
     ("P", "인식형 (융통성과 유연성을 선호)")),
    
    ("4. 상상력과 아이디어에 더 끌리나요?", 
     ("N", "직관형 (아이디어 중심)"), 
     ("S", "감각형 (현실 중심)"))
]

# 사용자 응답 저장
answers = []

# 질문 반복 처리
for question, option_a, option_b in questions:
    st.write(question)
    
    # 체크박스 생성
    selected_a = st.checkbox(f"{option_a[0]}: {option_a[1]}", key=f"{question}_a")
    selected_b = st.checkbox(f"{option_b[0]}: {option_b[1]}", key=f"{question}_b")
    
    # 체크박스 유효성 검사
    if selected_a and selected_b:
        st.warning("두 옵션 중 하나만 선택하세요.")
        answers.append(None)
    elif selected_a:
        answers.append(option_a[0])
    elif selected_b:
        answers.append(option_b[0])
    else:
        answers.append(None)
    
    st.write("---")  # 구분선 추가

# 결과 계산 및 출력
if st.button("결과 보기"):
    if None in answers:
        st.warning("모든 질문에 답해주세요.")
    else:
        mbti_result = "".join(answers)
        st.success(f"당신의 MBTI 유형은 **{mbti_result}** 입니다!")
        
        # MBTI 설명 출력
        description = mbti_descriptions.get(mbti_result, "")
        if description:
            st.write(f"### {mbti_result} 유형 설명")
            st.info(description)
        else:
            st.warning("해당 MBTI 유형에 대한 설명이 없습니다.")
        
        # 추가 정보 제공
        st.write("""
        #### MBTI란?
        MBTI(Myers-Briggs Type Indicator)는 개인의 성격 특성을 4가지 차원으로 나누어 16가지 유형으로 분류하는 심리 검사입니다.
        
        - **외향(E) vs 내향(I)**  
          외향은 사람들과의 상호작용에서 에너지를 얻고, 내향은 혼자만의 시간을 통해 에너지를 얻습니다.
        
        - **감각(S) vs 직관(N)**  
          감각은 현실과 사실에 초점을 맞추고, 직관은 가능성과 아이디어를 중시합니다.
        
        - **사고(T) vs 감정(F)**
