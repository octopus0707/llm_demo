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
        # bullet tag + expander
        st.markdown("- **LLM 回答：**")

        with st.expander("點我展開/收合 LLM 回答"):
            # 用 HTML 包一層加背景
            content_html = f"""
            <div style="
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #ddd;
                white-space: pre-wrap;
            ">
            {result['llm_result']}
            </div>
            """
            st.markdown(content_html, unsafe_allow_html=True)
