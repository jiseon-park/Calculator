import streamlit as st
import math

# --- 웹앱 제목 및 설정 ---
st.title("🔢 다기능 계산기 웹앱")
st.markdown("---")

# --- 입력 필드 ---
st.header("입력")
col1, col2 = st.columns(2)

with col1:
    # 사용자에게 첫 번째 숫자를 입력받습니다.
    num1 = st.number_input("첫 번째 숫자 (x)", value=0.0, step=0.1)

with col2:
    # 사용자에게 두 번째 숫자를 입력받습니다. (로그 연산의 밑/지수 연산의 지수 등)
    num2 = st.number_input("두 번째 숫자 (y) / 밑 / 지수", value=0.0, step=0.1)

# --- 연산 선택 ---
st.header("연산 선택")
operation = st.radio(
    "수행할 연산을 선택하세요:",
    ('덧셈 (+)', '뺄셈 (-)', '곱셈 (*)', '나눗셈 (/)', 
     '모듈러 연산 (%)', '지수 연산 (x^y)', '로그 연산 (log_y(x))')
)

# --- 계산 및 결과 표시 ---
st.markdown("---")
st.header("결과")
result = None

# 사용자가 선택한 연산에 따라 계산을 수행합니다.
if operation == '덧셈 (+)':
    result = num1 + num2
    st.write(f"**{num1} + {num2} = {result}**")
    
elif operation == '뺄셈 (-)':
    result = num1 - num2
    st.write(f"**{num1} - {num2} = {result}**")
    
elif operation == '곱셈 (*)':
    result = num1 * num2
    st.write(f"**{num1} * {num2} = {result}**")
    
elif operation == '나눗셈 (/)':
    if num2 != 0:
        result = num1 / num2
        st.write(f"**{num1} / {num2} = {result}**")
    else:
        st.error("오류: 0으로 나눌 수 없습니다.")

elif operation == '모듈러 연산 (%)':
    try:
        # 모듈러 연산은 일반적으로 정수에 사용되므로 정수로 변환 시도
        int_num1 = int(num1)
        int_num2 = int(num2)
        if int_num2 != 0:
            result = int_num1 % int_num2
            st.write(f"**{int_num1} % {int_num2} = {result}**")
        else:
            st.error("오류: 0으로 나눌 때 나머지를 구할 수 없습니다.")
    except ValueError:
        st.error("오류: 모듈러 연산은 정수 입력에만 적합합니다.")

elif operation == '지수 연산 (x^y)':
    result = num1 ** num2
    st.write(f"**{num1} ^ {num2} = {result}
