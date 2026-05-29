import streamlit as st

# 제목
st.title("😀 나의 첫 스트림릿 웹앱")

# 설명
st.write("버튼을 누르면 메시지가 나옵니다!")

# 이름 입력
name = st.text_input("이름을 입력하세요")

# 버튼
if st.button("확인"):
    st.success(f"{name}님 안녕하세요!")
