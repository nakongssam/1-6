import streamlit as st

# 페이지 설정
st.set_page_config(page_title="연애 코칭 앱", page_icon="💖")

# 제목
st.title("💖 연애 코칭 앱")
st.write("연애 고민을 입력하면 간단한 조언을 해드립니다!")

# 사용자 입력
question = st.text_area("고민을 적어보세요")

# 버튼
if st.button("조언 받기"):
    if question.strip() == "":
        st.warning("고민을 입력해주세요!")
    else:
        # 아주 간단한 답변
        if "고백" in question:
            answer = "진심을 담아 천천히 표현해보세요 😊"
        elif "헤어" in question:
            answer = "힘든 시간이지만 자신을 먼저 아껴주세요 💛"
        elif "짝사랑" in question:
            answer = "상대와 자연스럽게 대화를 늘려보세요 🌸"
        else:
            answer = "상대의 마음도 존중하면서 솔직하게 대화해보세요 🙂"

        st.success(answer)
