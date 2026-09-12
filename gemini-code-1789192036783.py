import streamlit as st

st.set_page_config(page_title="국어 서논술형 자동 채점 및 개념 학습 시스템", layout="wide")

st.title("📝 국어 서논술형 답안 자동 채점 & 개념 학습 시스템")
st.write("1~3세트 문항을 풀고 자동 채점을 받아보세요. 틀린 문항은 맞춤형 핵심 개념 복습 카드가 제공됩니다.")

# 세트별 탭 생성
tab1, tab2, tab3 = st.tabs(["1️⃣ [실전 적용 - 1] 사회적 촉진과 억제", "2️⃣ [실전 적용 - 2] 정전기의 특징", "3️⃣ [실전 적용 - 3] AI 그림과 인간의 예술"])

# ======================================================================
# [1세트] 사회적 촉진과 사회적 억제
# ======================================================================
with tab1:
    st.header("1️⃣ 사회적 촉진과 사회적 억제 (PDF 2~3쪽)")

    with st.form("set_1_form"):
        st.subheader("[서·논술형 1] 표 채우기")
        q1_1_1 = st.text_input("1-(1) 쉬운 과제 특성:", key="s1_q1_1")
        q1_1_2 = st.text_input("1-(2) 어려운 과제 환경:", key="s1_q1_2")
        q1_1_3 = st.text_input("1-(3) 심리학 용어:", key="s1_q1_3")

        st.subheader("[서·논술형 2] 조건 적용 설명문 작성")
        st.caption("💡 모범 답안 예시: [예시] 쉬운 과제는 커피숍에서 공부하는 것이 효율적이다. / [정의] 타인의 존재가 수행 효율을 높이는 현상을 사회적 촉진이라 한다.")
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
        st.markdown("---")
        st.markdown("### 📊 1세트 채점 결과")
        need_review_1 = False

        # 문항 1 채점
        s1 = 100 if any(k in q1_1_1 for k in ["쉬운", "친숙", "노력", "부담"]) and "어려운" not in q1_1_1 else 0
        s2 = 100 if any(k in q1_1_2 for k in ["혼자", "집중", "연습", "차분"]) and "함께" not in q1_1_2 else 0
        s3 = 100 if "사회적 억제" in q1_1_3.replace(" ", "") else 0

        st.write(f"- **1-(1) 표 채우기:** {s1}점 ({'통과' if s1==100 else '⚠️ 재검토 필요'})")
        st.write(f"- **1-(2) 표 채우기:** {s2}점 ({'통과' if s2==100 else '⚠️ 재검토 필요'})")
        st.write(f"- **1-(3) 표 채우기:** {s3}점 ({'통과' if s3==100 else '❌ 오답'})")
        if s1 < 100 or s2 < 100 or s3 < 100: need_review_1 = True

        # 문항 2 채점
        q2_pass = True
        if q1_2_m1 == q1_2_m2:
            st.error("- **2번 설명문:** ❌ 오류 (두 문장의 설명 방법은 서로 달라야 합니다.)")
            q2_pass = False
        elif "어려운" in q1_2_a1 and ("함께" in q1_2_a1 or "커피숍" in q1_2_a1):
            st.warning("- **2번 설명문:** ⚠️ 오개념 감지 (어려운 과제는 타인의 존재가 방해가 됨)")
            q2_pass = False
        else:
            st.success("- **2번 설명문:** ✅ 조건 및 설명 방법 구조 통과")
        if not q2_pass: need_review_1 = True

        # 문항 3 채점
        c_vis = any(k in q1_3_vis for k in ["혼자", "집중", "익숙", "연습"])
        c_aud = any(k in q1_3_aud for k in ["차분", "정적", "조용", "집중"])
        st.write(f"- **3-(1) 시각 효과:** {'✅ 통과' if c_vis else '⚠️ 미통과 (혼자 집중해야 효율이 오른다는 결론 필요)'}")
        st.write(f"- **3-(2) 청각 효과:** {'✅ 통과' if c_aud else '⚠️ 미통과 (정적/차분함의 필요성 명시 필요)'}")
        if not c_vis or not c_aud: need_review_1 = True

        # 오답 시 개념 복습 카드 노출
        if need_review_1:
            st.info("💡 **[1세트 핵심 개념 복습 노트]**\n\n"
                    "* **사회적 촉진**: 쉬운 취미나 친숙한 과제는 다른 사람과 함께하거나 백색소음이 있는 곳(도서관, 카페)에서 할 때 효율이 높아짐.\n"
                    "* **사회적 억제**: 지나치게 어렵거나 도전적인 과제는 타인의 존재가 방해가 되므로 혼자 차분하게 집중할 수 있는 독립된 공간이 효율적임.\n"
                    "* **복합양식성 연출**: 어려운 과제 연출 시 시각(독립된 개인 공간 클로즈업), 청각(정적 및 연필/초침 소리)을 사용하여 차분함과 집중을 강조해야 함.")


# ======================================================================
# [2세트] 정전기의 특징
# ======================================================================
with tab2:
    st.header("2️⃣ 정전기의 특징 (PDF 4~5쪽)")

    with st.form("set_2_form"):
        st.subheader("[서·논술형 1] 표 채우기")
        q2_1_1 = st.text_input("1-(1) 물의 상태 비유:", key="s2_q1_1")
        q2_1_2 = st.text_input("1-(2) 전하의 상태:", key="s2_q1_2")
        q2_1_3 = st.text_input("1-(3) 위험성:", key="s2_q1_3")

        st.subheader("[서·논술형 2] 조건 적용 설명문 작성")
        st.caption("💡 모범 답안 예시: [비교/대조] 실생활 전기가 흐르는 물이라면 정전기는 고여 있는 물이다. / [인과] 정전기는 전하가 이동하지 않으므로 위험하지 않다.")
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
        st.markdown("---")
        st.markdown("### 📊 2세트 채점 결과")
        need_review_2 = False

        # 문항 1 채점
        s1 = 100 if ("높은" in q2_1_1 or "높이가" in q2_1_1) and "고여" in q2_1_1 else (50 if "고여" in q2_1_1 else 0)
        s2 = 100 if any(k in q2_1_2 for k in ["이동하지", "머물", "정지"]) and "흐름" not in q2_1_2 else 0
        s3 = 100 if "위험하지" in q2_1_3 or "피해가 없" in q2_1_3 else 0

        st.write(f"- **1-(1) 표 채우기:** {s1}점 ({'통과' if s1==100 else '⚠️ 감점/재검토: 높은 곳 + 고여 있음'})")
        st.write(f"- **1-(2) 표 채우기:** {s2}점 ({'통과' if s2==100 else '❌ 오답: 전하가 이동하지 않고 머물러 있음'})")
        st.write(f"- **1-(3) 표 채우기:** {s3}점 ({'통과' if s3==100 else '❌ 오답: 위험하지 않음 명시'})")
        if s1 < 100 or s2 < 100 or s3 < 100: need_review_2 = True

        # 문항 2 채점
        q2_pass = True
        if "자유롭게 흐른" in q2_2_a1 or "자유롭게 흐른" in q2_2_a2:
            st.error("- **2번 설명문:** ❌ 오개념 감지 (정전기는 전하가 이동하지 않고 머물러 있음)")
            q2_pass = False
        elif q2_2_m1 == q2_2_m2:
            st.error("- **2번 설명문:** ❌ 오류 (두 문장의 설명 방법은 서로 달라야 합니다.)")
            q2_pass = False
        else:
            st.success("- **2번 설명문:** ✅ 지문 사실관계 및 논리 구조 통과")
        if not q2_pass: need_review_2 = True

        # 문항 3 채점
        c_vis = "위험하지" in q2_3_vis or "피해" in q2_3_vis or "고여" in q2_3_vis
        c_aud = any(k in q2_3_aud for k in ["대비", "정", "조용", "적막", "움직이지"])
        st.write(f"- **3-(1) 시각 효과:** {'✅ 통과' if c_vis else '⚠️ 미통과 (전하가 이동하지 않아 위험하지 않다는 지문 근거 필요)'}")
        st.write(f"- **3-(2) 청각 효과:** {'✅ 통과' if c_aud else '⚠️ 미통과 (장면 1과의 대비 및 정적인 성격 서술 필요)'}")
        if not c_vis or not c_aud: need_review_2 = True

        # 오답 시 개념 복습 카드 노출
        if need_review_2:
            st.info("💡 **[2세트 핵심 개념 복습 노트]**\n\n"
                    "* **실생활 전기 vs 정전기**: 실생활 전기는 '흐르는 물(전하가 이동함)', 정전기는 '높은 곳에 고여 있는 물(전하가 이동하지 않고 머물러 있음)'에 비유됨.\n"
                    "* **정전기의 위험성**: 전압은 매우 높지만 전하가 이동하지 않기 때문에 감전 등의 실질적 위험성이 없음.\n"
                    "* **설명 방법(인과)**: '전하가 머물러 있기 때문에(원인) 위험하지 않다(결과)'의 구조를 가짐.")


# ======================================================================
# [3세트] AI 그림과 인간의 예술
# ======================================================================
with tab3:
    st.header("3️⃣ AI 그림과 인간의 예술 (PDF 6~7쪽)")

    with st.form("set_3_form"):
        st.subheader("[서·논술형 1] 표 채우기")
        q3_1_1 = st.text_input("1-(1) 올림픽 비유:", key="s3_q1_1")
        q3_1_2 = st.text_input("1-(2) 예술 여부 판단 및 근거:", key="s3_q1_2")
        q3_1_3 = st.text_input("1-(3) 예술로서의 가치:", key="s3_q1_3")

        st.subheader("[서·논술형 2] 조건 적용 설명문 작성")
        st.caption("💡 모범 답안 예시: [예시] 에드몽 드 벨라미는 고가에 낙찰되었다. / [비교와 대조] AI와 달리 인간 작품에는 작가의 감정과 경험이 담긴다.")
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
        st.markdown("---")
        st.markdown("### 📊 3세트 채점 결과")
        need_review_3 = False

        # 문항 1 채점
        s1 = 100 if "로봇" in q3_1_1 and ("피겨" in q3_1_1 or "실수" in q3_1_1 or "완벽" in q3_1_1) else 0
        s2 = 100 if ("감정" in q3_1_2 or "철학" in q3_1_2 or "이야기" in q3_1_2) and ("어렵" in q3_1_2 or "아니다" in q3_1_2) else 0
        s3 = 100 if any(k in q3_1_3 for k in ["변화", "확장", "범주", "상징"]) else 0

        st.write(f"- **1-(1) 표 채우기:** {s1}점 ({'통과' if s1==100 else '⚠️ 재검토: 완벽한 로봇의 피겨 연기'})")
        st.write(f"- **1-(2) 표 채우기:** {s2}점 ({'통과' if s2==100 else '⚠️ 재검토: 감정/철학 없음 + 부정 결론 필수'})")
        st.write(f"- **1-(3) 표 채우기:** {s3}점 ({'통과' if s3==100 else '⚠️ 재검토: 미술계 변화/범주 확장'})")
        if s1 < 100 or s2 < 100 or s3 < 100: need_review_3 = True

        # 문항 2 채점
        q2_pass = True
        if any(k in q3_2_a1 or k in q3_2_a2 for k in ["미드저니", "Midjourney", "달리", "DALL-E"]):
            st.warning("- **2번 설명문:** ⚠️ 조건 위반 (지문 외 외부 지식/사례 사용)")
            q2_pass = False
        elif "AI가 감정을" in q3_2_a1 or "AI가 감정을" in q3_2_a2:
            st.error("- **2번 설명문:** ❌ 오개념 감지 (인공지능은 감정을 느끼지 못함)")
            q2_pass = False
        elif q3_2_m1 == q3_2_m2:
            st.error("- **2번 설명문:** ❌ 오류 (두 문장의 설명 방법은 서로 달라야 합니다.)")
            q2_pass = False
        else:
            st.success("- **2번 설명문:** ✅ 지문 사실관계 및 외부 지식 배제 조건 통과")
        if not q2_pass: need_review_3 = True

        # 문항 3 채점
        c_vis = any(k in q3_3_vis for k in ["감정", "철학", "경험", "관점", "삶"])
        c_aud = any(k in q3_3_aud for k in ["울림", "감동", "따뜻", "대비"])
        st.write(f"- **3-(1) 시각 효과:** {'✅ 통과' if c_vis else '⚠️ 미통과 (작가의 감정/철학/경험이 녹아든다는 근거 필요)'}")
        st.write(f"- **3-(2) 청각 효과:** {'✅ 통과' if c_aud else '⚠️ 미통과 (마음의 울림/감동 전달 명시 필요)'}")
        if not c_vis or not c_aud: need_review_3 = True

        # 오답 시 개념 복습 카드 노출
        if need_review_3:
            st.info("💡 **[3세트 핵심 개념 복습 노트]**\n\n"
                    "* **인간 예술의 특징**: 작가의 고유한 감정, 독자적인 철학, 삶의 경험, 세상을 보는 관점이 담겨 있어 감상자에게 '마음의 울림'을 줌.\n"
                    "* **AI 그림의 한계 및 가치**: 감정이 없고 철학과 스토리가 없어 완전한 예술로 보기 어렵지만, 미술계에 큰 변화를 유발하고 예술의 범주를 확장하는 상징적 가치가 있음.\n"
                    "* **조건 유의 사항**: 지문 기반 문제에서는 외부 사례(Midjourney 등)를 쓰지 않고 지문 내 사례(「에드몽 드 벨라미」)만 활용해야 함.")
