import streamlit as st

st.set_page_config(page_title="국어 서논술형 자동 채점 시스템", layout="wide")

st.title("📝 국어 서논술형 답안 자동 채점 시스템")
st.write("1~3세트 모든 문항에 대한 자동 채점 및 모범 답안 검증을 제공합니다.")

# ----------------------------------------------------------------------
# [실전 적용 - 1] 사회적 촉진과 사회적 억제
# ----------------------------------------------------------------------
st.header("1️⃣ [실전 적용 - 1] 사회적 촉진과 사회적 억제")

with st.form("set_1_form"):
    st.subheader("[서·논술형 1] 표 채우기")
    q1_1_1 = st.text_input("1-(1) 쉬운 과제 특성:", key="s1_q1_1")
    q1_1_2 = st.text_input("1-(2) 어려운 과제 환경:", key="s1_q1_2")
    q1_1_3 = st.text_input("1-(3) 심리학 용어:", key="s1_q1_3")

    st.subheader("[서·논술형 2] 조건 적용 설명문 작성")
    st.caption("💡 모범 답안 선택지: [예시] 쉬운 과제는 커피숍에서 공부하는 것이 효율적이다. / [정의] 타인의 존재가 수행 효율을 높이는 현상을 사회적 촉진이라 한다.")
    col1, col2 = st.columns(2)
    with col1:
        q1_2_m1 = st.selectbox("(1) 설명 방법", ["예시", "비교와 대조", "정의", "인과"], key="s1_m1")
        q1_2_a1 = st.text_area("(1) 문장 작성:", key="s1_a1")
    with col2:
        q1_2_m2 = st.selectbox("(2) 설명 방법", ["예시", "비교와 대조", "정의", "인과"], index=2, key="s1_m2")
        q1_2_a2 = st.text_area("(2) 문장 작성:", key="s1_a2")

    st.subheader("[서·논술형 3] 영상 기획안 및 효과 서술")
    q1_3_vis = st.text_area("(1) 시각 요소 효과:", key="s1_vis")
    q1_3_aud = st.text_area("(2) 청각 요소 효과:", key="s1_aud")

    submit_1 = st.form_submit_button("🎯 1세트 채점하기")

if submit_1:
    st.markdown("#### 📊 1세트 채점 결과")
    # 문항 1
    s1 = 100 if any(k in q1_1_1 for k in ["쉬운", "친숙", "노력", "부담"]) and "어려운" not in q1_1_1 else 0
    s2 = 100 if any(k in q1_1_2 for k in ["혼자", "집중", "연습", "차분"]) and "함께" not in q1_1_2 else 0
    s3 = 100 if "사회적 억제" in q1_1_3.replace(" ", "") else 0
    st.write(f"- **1-(1) 표 채우기:** {s1}점 ({'통과' if s1==100 else '재검토: 쉬운/친숙한 과제 의미 필요'})")
    st.write(f"- **1-(2) 표 채우기:** {s2}점 ({'통과' if s2==100 else '재검토: 혼자/차분히 집중 의미 필요'})")
    st.write(f"- **1-(3) 표 채우기:** {s3}점 ({'통과' if s3==100 else '오답: 사회적 억제 정확히 기재'})")

    # 문항 2
    if q1_2_m1 == q1_2_m2:
        st.error("- **2번 설명문:** 오류 (두 문장의 설명 방법은 서로 달라야 합니다.)")
    elif "어려운" in q1_2_a1 and ("함께" in q1_2_a1 or "커피숍" in q1_2_a1):
        st.warning("- **2번 설명문:** 오개념 감지 (어려운 과제는 타인의 존재가 방해가 됨)")
    else:
        st.success("- **2번 설명문:** 조건 및 설명 방법 구조 통과")

    # 문항 3
    c_vis = any(k in q1_3_vis for k in ["혼자", "집중", "익숙", "연습"])
    c_aud = any(k in q1_3_aud for k in ["차분", "정적", "조용", "집중"])
    st.write(f"- **3-(1) 시각 효과:** {'통과' if c_vis else '미통과 (혼자 집중해야 효율이 오른다는 결론 필요)'}")
    st.write(f"- **3-(2) 청각 효과:** {'통과' if c_aud else '미통과 (정적/차분함의 필요성 명시 필요)'}")

st.divider()

# ----------------------------------------------------------------------
# [실전 적용 - 2] 정전기의 특징
# ----------------------------------------------------------------------
st.header("2️⃣ [실전 적용 - 2] 정전기의 특징")

with st.form("set_2_form"):
    st.subheader("[서·논술형 1] 표 채우기")
    q2_1_1 = st.text_input("1-(1) 물의 상태 비유:", key="s2_q1_1")
    q2_1_2 = st.text_input("1-(2) 전하의 상태:", key="s2_q1_2")
    q2_1_3 = st.text_input("1-(3) 위험성:", key="s2_q1_3")

    st.subheader("[서·논술형 2] 조건 적용 설명문 작성")
    st.caption("💡 모범 답안 선택지: [비교/대조] 실생활 전기가 흐르는 물이라면 정전기는 고여 있는 물이다. / [인과] 정전기는 전하가 이동하지 않으므로 위험하지 않다.")
    col1, col2 = st.columns(2)
    with col1:
        q2_2_m1 = st.selectbox("(1) 설명 방법", ["비교와 대조", "정의", "인과", "예시"], key="s2_m1")
        q2_2_a1 = st.text_area("(1) 문장 작성:", key="s2_a1")
    with col2:
        q2_2_m2 = st.selectbox("(2) 설명 방법", ["비교와 대조", "정의", "인과", "예시"], index=2, key="s2_m2")
        q2_2_a2 = st.text_area("(2) 문장 작성:", key="s2_a2")

    st.subheader("[서·논술형 3] 영상 기획안 및 효과 서술")
    q2_3_vis = st.text_area("(1) 시각 요소 효과:", key="s2_vis")
    q2_3_aud = st.text_area("(2) 청각 요소 효과:", key="s2_aud")

    submit_2 = st.form_submit_button("🎯 2세트 채점하기")

if submit_2:
    st.markdown("#### 📊 2세트 채점 결과")
    # 문항 1
    s1 = 100 if ("높은" in q2_1_1 or "높이가" in q2_1_1) and "고여" in q2_1_1 else (50 if "고여" in q2_1_1 else 0)
    s2 = 100 if any(k in q2_1_2 for k in ["이동하지", "머물", "정지"]) and "흐름" not in q2_1_2 else 0
    s3 = 100 if "위험하지" in q2_1_3 or "피해가 없" in q2_1_3 else 0
    st.write(f"- **1-(1) 표 채우기:** {s1}점 ({'통과' if s1==100 else '부분 점수/오답: 높은 곳 + 고여 있음 필수'})")
    st.write(f"- **1-(2) 표 채우기:** {s2}점 ({'통과' if s2==100 else '오답: 전하가 이동하지 않고 머물러 있음 필수'})")
    st.write(f"- **1-(3) 표 채우기:** {s3}점 ({'통과' if s3==100 else '오답: 위험하지 않음 명시'})")

    # 문항 2
    if "자유롭게 흐른" in q2_2_a1 or "자유롭게 흐른" in q2_2_a2:
        st.error("- **2번 설명문:** 오개념 감지 (정전기는 전하가 이동하지 않고 머물러 있음)")
    elif q2_2_m1 == q2_2_m2:
        st.error("- **2번 설명문:** 오류 (두 문장의 설명 방법은 서로 달라야 합니다.)")
    else:
        st.success("- **2번 설명문:** 지문 사실관계 및 논리 구조 통과")

    # 문항 3
    c_vis = "위험하지" in q2_3_vis or "피해" in q2_3_vis or "고여" in q2_3_vis
    c_aud = any(k in q2_3_aud for k in ["대비", "정", "조용", "적막", "움직이지"])
    st.write(f"- **3-(1) 시각 효과:** {'통과' if c_vis else '미통과 (전하가 이동하지 않아 위험하지 않다는 지문 근거 필요)'}")
    st.write(f"- **3-(2) 청각 효과:** {'통과' if c_aud else '미통과 (장면 1과의 대비 및 정적인 성격 서술 필요)'}")

st.divider()

# ----------------------------------------------------------------------
# [실전 적용 - 3] AI 그림과 인간의 예술
# ----------------------------------------------------------------------
st.header("3️⃣ [실전 적용 - 3] AI 그림과 인간의 예술")

with st.form("set_3_form"):
    st.subheader("[서·논술형 1] 표 채우기")
    q3_1_1 = st.text_input("1-(1) 올림픽 비유:", key="s3_q1_1")
    q3_1_2 = st.text_input("1-(2) 예술 여부 판단 및 근거:", key="s3_q1_2")
    q3_1_3 = st.text_input("1-(3) 예술로서의 가치:", key="s3_q1_3")

    st.subheader("[서·논술형 2] 조건 적용 설명문 작성")
    st.caption("💡 모범 답안 선택지: [예시] 에드몽 드 벨라미는 고가에 낙찰되었다. / [비교와 대조] AI와 달리 인간 작품에는 작가의 감정과 경험이 담긴다.")
    col1, col2 = st.columns(2)
    with col1:
        q3_2_m1 = st.selectbox("(1) 설명 방법", ["예시", "비교와 대조", "분류와 구분", "인과"], key="s3_m1")
        q3_2_a1 = st.text_area("(1) 문장 작성:", key="s3_a1")
    with col2:
        q3_2_m2 = st.selectbox("(2) 설명 방법", ["예시", "비교와 대조", "분류와 구분", "인과"], index=1, key="s3_m2")
        q3_2_a2 = st.text_area("(2) 문장 작성:", key="s3_a2")

    st.subheader("[서·논술형 3] 영상 기획안 및 효과 서술")
    q3_3_vis = st.text_area("(1) 시각 요소 효과:", key="s3_vis")
    q3_3_aud = st.text_area("(2) 청각 요소 효과:", key="s3_aud")

    submit_3 = st.form_submit_button("🎯 3세트 채점하기")

if submit_3:
    st.markdown("#### 📊 3세트 채점 결과")
    # 문항 1
    s1 = 100 if "로봇" in q3_1_1 and ("피겨" in q3_1_1 or "실수" in q3_1_1 or "완벽" in q3_1_1) else 0
    s2 = 100 if ("감정" in q3_1_2 or "철학" in q3_1_2 or "이야기" in q3_1_2) and ("어렵" in q3_1_2 or "아니다" in q3_1_2) else 0
    s3 = 100 if any(k in q3_1_3 for k in ["변화", "확장", "범주", "상징"]) else 0
    st.write(f"- **1-(1) 표 채우기:** {s1}점 ({'통과' if s1==100 else '재검토: 로봇의 완벽한 피겨 연기 의미 필요'})")
    st.write(f"- **1-(2) 표 채우기:** {s2}점 ({'통과' if s2==100 else '재검토: 감정/철학 없음 + 부정 결론 필수'})")
    st.write(f"- **1-(3) 표 채우기:** {s3}점 ({'통과' if s3==100 else '재검토: 미술계 변화/범주 확장 의미 필요'})")

    # 문항 2
    if any(k in q3_2_a1 or k in q3_2_a2 for k in ["미드저니", "Midjourney", "달리", "DALL-E"]):
        st.warning("- **2번 설명문:** 조건 위반 (지문 외 외부 지식/사례 사용)")
    elif "AI가 감정을" in q3_2_a1 or "AI가 감정을" in q3_2_a2:
        st.error("- **2번 설명문:** 오개념 감지 (인공지능은 감정을 느끼지 못함)")
    elif q3_2_m1 == q3_2_m2:
        st.error("- **2번 설명문:** 오류 (두 문장의 설명 방법은 서로 달라야 합니다.)")
    else:
        st.success("- **2번 설명문:** 지문 사실관계 및 외부 지식 배제 조건 통과")

    # 문항 3
    c_vis = any(k in q3_3_vis for k in ["감정", "철학", "경험", "관점", "삶"])
    c_aud = any(k in q3_3_aud for k in ["울림", "감동", "따뜻", "대비"])
    st.write(f"- **3-(1) 시각 효과:** {'통과' if c_vis else '미통과 (작가의 감정/철학/경험이 녹아든다는 근거 필요)'}")
    st.write(f"- **3-(2) 청각 효과:** {'통과' if c_aud else '미통과 (마음의 울림/감동 전달 명시 필요)'}")
