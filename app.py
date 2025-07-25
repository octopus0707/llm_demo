import streamlit as st
import json

st.markdown("""
<style>
/* 改 expander 標題背景 */
div[role="button"] > div:first-child {
    background-color: #d0f0ff !important;  /* 淺藍色 */
    border-radius: 8px 8px 0 0 !important;
}

/* 改 expander 內容區背景 */
section[aria-expanded="true"] > div[style*="flex-direction: column"] {
    background-color: #e6f7ff !important;  /* 更淺藍 */
    border-radius: 0 0 8px 8px !important;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)

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
            st.markdown(result['llm_result'])
