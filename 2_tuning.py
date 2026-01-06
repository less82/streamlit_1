import streamlit as st
import time
import random
import pandas as pd

st.title("하이퍼파라미터 튜닝 시뮬레이터")

# [Session State] 실험 기록 저장소 초기화
# 페이지가 새로고침 되어도 리스트가 사라지지 않고 유지됩니다.

if 'history' not in st.session_state:
    st.session_state.history = []

with st.form("training_form"):
    st.subheader("모델 파라미터 설정")

    col1, col2 = st.columns(2)

    with col1:
        learning_rate = st.slider("Learning Rate", 0.001, 0.1, 0.01)
    with col2:
        epochs = st.slider("Epochs", 1, 100, 10)

    submitted = st.form_submit_button("학습시작")

if submitted:
    st.write(f"학습시작 LR:{learning_rate}, Epochs:{epochs}")

    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i+1)
        status_text.text(f"Progress: {i+1}%")
    
    accuracy = random.uniform(0.70, 0.99)
    loss = random.uniform(0.1, 0.5)

    st.success(f"학습 완료 Accuracy:{accuracy:.4f}")

    st.session_state.history.append({
        "Learning Rate": learning_rate,
        "Epochs": epochs,
        "Accuracy": accuracy,
        "Loss": loss
    })

if len(st.session_state.history) > 0:
    st.markdown("---")
    st.subheader("실험 기록(Session State 유지)")
    st.dataframe(pd.DataFrame(st.session_state.history))