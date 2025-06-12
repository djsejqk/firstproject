import streamlit as t
t.title("나의 첫 홈페이지")
t.write("hello")
t.write("wa! sans!")
import streamlit as st
import random

st.set_page_config(page_title="🎉 가위바위보 게임 🎉", page_icon="✂️", layout="centered")

# 배경색 꾸미기 (html 스타일)
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f5a623, #f76b1c);
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .big-font {
        font-size: 48px !important;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
    }
    .result {
        font-size: 36px;
        margin-top: 20px;
        font-weight: bold;
        text-shadow: 1px 1px 3px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="big-font">✂️🪨📄 가위바위보 게임 🎉</div>', unsafe_allow_html=True)

choices = {"가위": "✂️", "바위": "🪨", "보": "📄"}

user_choice = st.radio("당신의 선택은?", list(choices.keys()), index=0, horizontal=True)

if st.button("결과 보기! 🔥"):
    computer_choice = random.choice(list(choices.keys()))

    # 승부 결정
    if user_choice == computer_choice:
        result = "무승부! 🤝"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "당신이 이겼어요! 🎉🥳"
    else:
        result = "컴퓨터가 이겼어요... 😢"

    st.markdown(f"""
    <div class="result">
    당신: {choices[user_choice]} <br>
    컴퓨터: {choices[computer_choice]} <br><br>
    <span style="font-size:48px;">{result}</span>
    </div>
    """, unsafe_allow_html=True)
