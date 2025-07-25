import streamlit as st
import json

with open("./llm_similarity_results.json", 'r') as file:
    data = json.load(file)

st.set_page_config(page_title="LLM 進行專利相似度比對分析", layout="wide")
st.title("專利相似度比對分析")

# 產生 tab 名稱
tab_titles = [f"{item['target']} v.s. {item['id']}" for item in data]

# 建立 tabs
tabs = st.tabs(tab_titles)

# 對應每個 tab 顯示內容
for tab, result in zip(tabs, data):
    with tab:
        st.markdown(f"- 📌 本國專利號：{result['target']}")
        st.markdown(f"- 📌 美國專利號：{result['id']}")
        with st.expander("🔍 查看 LLM 回答"):
            st.markdown(result['llm_result'])
