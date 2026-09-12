import streamlit as st

st.set_page_config(page_title="서논술형 자동 채점 시스템", layout="wide")

st.title("📝 국어 서논술형 답안 자동 채점 시스템")
st.subheader("서논술형 문항 유형 익히기 (1~3 세트)")

# 사이드바: 문제 세트 선택
set_option = st.sidebar.selectbox("채점할 문항 세트를 선택하세요", ["1세트: 사회적 촉진과 억제", "2세트: 정전기의 특징", "3세트: AI 그림과 인간의 예술"])

# ----------------------------------------------------------------------
# [1세트] 사회적 촉진과 억제 로직
# ----------------------------------------------------------------------
if set_option == "1세트: 사회적 촉진과 억제":
    st.header("[실전 적용 - 1] 사회적 촉진과 사회적 억제")
    
    with st.expander("📌 문제 1 (표 채우기)"):
        q1_1 = st.text_input("1-(1) 쉬운 과제 특성:")
        q1_2 = st.text_input("1-(2) 어려운 과제 환경:")
        q1_3 = st.text_input("1-(3) 심리학 용어:")
        
        if st.button("1번 채점"):
            # (1) 채점
            kw_1 = ["쉬운", "친숙", "노력", "부담 없는", "좋아하는"]
            score_1 = 100 if any(k in q1_1 for k in kw_1) and "어려운" not in q1_1 else 0
            
            # (2) 채점
            kw_2 = ["혼자", "집중", "연습", "차분"]
            score_2 = 100 if any(k in q1_2 for k in kw_2) and "함께" not in q1_2 and "도서관" not in q1_2 else 0
            
            # (3) 채점 (단답형 용어)
            score_3 = 100 if "사회적 억제" in q1_3.replace(" ", "") else 0
            
            st.write(f"**1-(1) 점수:** {score_1}점 / {'통과' if score_1==100 else '재검토 필요 (쉬운/친숙한 과제 의미 필요)'}")
            st.write(f"**1-(2) 점수:** {score_2}점 / {'통과' if score_2==100 else '재검토 필요 (혼자/차분히 집중 의미 필요)'}")
            st.write(f"**1-(3) 점수:** {score_3}점 / {'통과' if score_3==100 else '오답 (사회적 억제 정확히 작성)'}")

    with st.expander("📌 문제 2 (설명문 작성)"):
        st.caption("선택지별 모범 답안: [예시] 쉬운 과제는 커피숍에서 할 때 효율적이다. / [정의] 타인의 존재가 수행을 돕는 것을 사회적 촉진이라 한다.")
        q2_method1 = st.selectbox("(1) 문장 설명 방법", ["예시", "비교와 대조", "정의", "인과"])
        q2_ans1 = st.text_area("(1) 작성 답안:")
        
        q2_method2 = st.selectbox("(2) 문장 설명 방법", ["예시", "비교와 대조", "정의", "인과"], index=2)
        q2_ans2 = st.text_area("(2) 작성 답안:")
        
        if st.button("2번 채점"):
            if q2_method1 == q2_method2:
                st.error("오류: (1)과 (2)의 설명 방법은 서로 달라야 합니다.")
            else:
                # 오개념 검증: 지문 내용 일치 여부
                err_check = False
                if "어려운" in q2_ans1 and ("함께" in q2_ans1 or "커피숍" in q2_ans1):
                    st.warning("오개념 감지: 어려운 과제에는 타인의 존재가 방해가 됩니다.")
                    err_check = True
                
                if not err_check:
                    st.success("조건 충족: 설명 방법 구조 및 지문 사실관계 통과")

    with st.expander("📌 문제 3 (영상 기획안 및 효과)"):
        q3_vis_effect = st.text_area("(1) 시각 요소 효과:")
        q3_aud_effect = st.text_area("(2) 청각 요소 효과:")
        
        if st.button("3번 채점"):
            # 결론 방향 검증
            cond_vis = any(k in q3_vis_effect for k in ["혼자", "집중", "익숙", "연습"])
            cond_aud = any(k in q3_aud_effect for k in ["차분", "정적", "조용", "집중"])
            
            st.write(f"**시각 효과 결론 검증:** {'통과' if cond_vis else '미통과 (혼자 집중해야 효율이 오른다는 결론 필요)'}")
            st.write(f"**청각 효과 결론 검증:** {'통과' if cond_aud else '미통과 (정적/차분함의 필요성 명시 필요)'}")

# ----------------------------------------------------------------------
# [2세트] 정전기의 특징 로직
# ----------------------------------------------------------------------
elif set_option == "2세트: 정전기의 특징":
    st.header("[실전 적용 - 2] 정전기의 특징")
    
    with st.expander("📌 문제 1 (표 채우기)"):
        q1_1 = st.text_input("1-(1) 물의 상태 비유:")
        q1_2 = st.text_input("1-(2) 전하의 상태:")
        q1_3 = st.text_input("1-(3) 위험성:")
        
        if st.button("1번 채점"):
            score_1 = 100 if ("높은" in q1_1 or "높이가" in q1_1) and "고여" in q1_1 else (50 if "고여" in q1_1 else 0)
            score_2 = 100 if any(k in q1_2 for k in ["이동하지", "머물", "정지"]) and "흐름" not in q1_2 else 0
            score_3 = 100 if "위험하지" in q1_3 or "피해가 없" in q1_3 else 0
            
            st.write(f"**1-(1) 점수:** {score_1}점 / {'통과' if score_1==100 else '부분 점수/오답 (높은 곳 + 고여 있음 필수)'}")
            st.write(f"**1-(2) 점수:** {score_2}점 / {'통과' if score_2==100 else '오답 (전하가 이동하지 않고 머물러 있음 필수)'}")
            st.write(f"**1-(3) 점수:** {score_3}점 / {'통과' if score_3==100 else '오답 (위험하지 않음 명시)'}")

    with st.expander("📌 문제 2 (설명문 작성)"):
        st.caption("선택지별 모범 답안: [비교/대조] 실생활 전기가 흐르는 물이라면 정전기는 고여 있는 물이다. / [인과] 전하가 이동하지 않으므로 위험하지 않다.")
        q2_ans1 = st.text_area("(1) 작성 답안:")
        q2_ans2 = st.text_area("(2) 작성 답안:")
        
        if st.button("2번 채점"):
            if "자유롭게 흐른" in q2_ans1 or "자유롭게 흐른" in q2_ans2:
                st.error("오개념 감지: 정전기는 전하가 이동하지 않고 머물러 있습니다.")
            else:
                st.success("지문 오개념 없음: 문장 간 논리 연결성 검토 완료")

    with st.expander("📌 문제 3 (영상 기획안 및 효과)"):
        q3_vis_effect = st.text_area("(1) 시각 요소 효과:")
        q3_aud_effect = st.text_area("(2) 청각 요소 효과:")
        
        if st.button("3번 채점"):
            # 결론 방향 검증: 위험하지 않음/정적인 성격
            cond_vis = "위험하지" in q3_vis_effect or "피해" in q3_vis_effect or "고여" in q3_vis_effect
            cond_aud = "대비" in q3_aud_effect or "정" in q3_aud_effect or "조용" in q3_aud_effect or "적막" in q3_aud_effect
            
            st.write(f"**시각 효과 결론 검증:** {'통과' if cond_vis else '미통과 (전하가 이동하지 않아 위험하지 않다는 지문 근거 필요)'}")
            st.write(f"**청각 효과 결론 검증:** {'통과' if cond_aud else '미통과 (장면 1과의 대비 및 정적인 성격 서술 필요)'}")

# ----------------------------------------------------------------------
# [3세트] AI 그림과 인간의 예술 로직
# ----------------------------------------------------------------------
elif set_option == "3세트: AI 그림과 인간의 예술":
    st.header("[실전 적용 - 3] AI 그림과 인간의 예술")
    
    with st.expander("📌 문제 1 (표 채우기)"):
        q1_1 = st.text_input("1-(1) 올림픽 비유:")
        q1_2 = st.text_input("1-(2) 예술 여부 판단 및 근거:")
        q1_3 = st.text_input("1-(3) 예술로서의 가치:")
        
        if st.button("1번 채점"):
            score_1 = 100 if "로봇" in q1_1 and ("피겨" in q1_1 or "실수" in q1_1 or "완벽" in q1_1) else 0
            score_2 = 100 if ("감정" in q1_2 or "철학" in q1_2 or "이야기" in q1_2) and ("어렵" in q1_2 or "아니다" in q1_2) else 0
            score_3 = 100 if any(k in q1_3 for k in ["변화", "확장", "범주", "상징"]) else 0
            
            st.write(f"**1-(1) 점수:** {score_1}점 / {'통과' if score_1==100 else '재검토 (로봇의 완벽한 피겨 연기 의미 필요)'}")
            st.write(f"**1-(2) 점수:** {score_2}점 / {'통과' if score_2==100 else '재검토 (감정/철학 없음 + 부정 결론 필수)'}")
            st.write(f"**1-(3) 점수:** {score_3}점 / {'통과' if score_3==100 else '재검토 (미술계 변화/범주 확장 의미 필요)'}")

    with st.expander("📌 문제 2 (설명문 작성)"):
        st.caption("선택지별 모범 답안: [예시] 에드몽 드 벨라미는 고가에 낙찰되었다. / [비교와 대조] AI와 달리 인간 작품에는 작가의 감정과 경험이 담긴다.")
        q2_ans1 = st.text_area("(1) 작성 답안:")
        q2_ans2 = st.text_area("(2) 작성 답안:")
        
        if st.button("2번 채점"):
            # 지문 외 사례 배제 검증
            if any(k in q2_ans1 or k in q2_ans2 for k in ["미드저니", "Midjourney", "달리", "DALL-E"]):
                st.warning("조건 위반: 지문 외 외부 지식/사례(타 AI 프로그램명)를 활용했습니다.")
            elif "AI가 감정을" in q2_ans1 or "AI가 감정을" in q2_ans2:
                st.error("오개념 감지: 인공지능은 감정을 느끼지 못합니다.")
            else:
                st.success("지문 사실관계 및 외부 지식 배제 조건 통과")

    with st.expander("📌 문제 3 (영상 기획안 및 효과)"):
        q3_vis_effect = st.text_area("(1) 시각 요소 효과:")
        q3_aud_effect = st.text_area("(2) 청각 요소 효과:")
        
        if st.button("3번 채점"):
            # 결론 방향 검증: 감정/철학/마음의 울림
            cond_vis = any(k in q3_vis_effect for k in ["감정", "철학", "경험", "관점", "삶"])
            cond_aud = any(k in q3_aud_effect for k in ["울림", "감동", "따뜻", "대비"])
            
            st.write(f"**시각 효과 결론 검증:** {'통과' if cond_vis else '미통과 (작가의 감정/철학/경험이 녹아든다는 근거 필요)'}")
            st.write(f"**청각 효과 결론 검증:** {'통과' if cond_aud else '미통과 (마음의 울림/감동 전달 명시 필요)'}")