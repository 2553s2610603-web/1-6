import streamlit as st
st.title('밥먹고싶다')
st.write('집가고싶다')
st.write("키와 몸무게를 입력하면 BMI를 계산해드립니다.")

# 입력
height = st.number_input("키(cm)를 입력하세요", min_value=100.0, max_value=250.0)
weight = st.number_input("몸무게(kg)를 입력하세요", min_value=20.0, max_value=300.0)

# 버튼
if st.button("BMI 계산하기"):

    # cm -> m 변환
    height_m = height / 100

    # BMI 계산
    bmi = weight / (height_m ** 2)

    # 결과 출력
    st.subheader(f"당신의 BMI는 {bmi:.2f} 입니다.")

    # BMI 판정
    if bmi < 18.5:
        st.warning("저체중입니다.")
    elif bmi < 23:
        st.success("정상 체중입니다.")
    elif bmi < 25:
        st.info("과체중입니다.")
    else:
        st.error("비만입니다.")

    # 비만 예방 팁
    st.markdown("## ✅ 비만 예방 방법")

    st.write("1. 하루 30분 이상 운동하기")
    st.write("2. 탄산음료 줄이기")
    st.write("3. 야식 피하기")
    st.write("4. 채소와 과일 자주 먹기")
    st.write("5. 물 충분히 마시기")
3. 실행 방법

터미널에서 실행:
