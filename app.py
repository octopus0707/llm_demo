import streamlit as st
import json

# 在側邊欄選擇模型
model_option = st.sidebar.selectbox(
    "選擇 prompt 結果",
    ("原始 prompt", "修正 prompt")
)

# 根據選擇載入不同的檔案
if model_option == "原始 prompt":
    file_path = "./llm_similarity_results.json"
else:
    file_path = "./llm_similarity_results_0805.json"

with open(file_path, 'r') as file:
    data = json.load(file)

st.set_page_config(page_title="LLM 進行專利相似度比對分析", layout="wide")
st.title("專利相似度比對分析")

nums = len(data)

tab_titles = [f"example {i+1}" for i in range(nums)]

# 建立 tabs
tabs = st.tabs(tab_titles)

# 對應每個 tab 顯示內容
for tab, result in zip(tabs, data):
    with tab:
        st.markdown(f"- 本國專利號：{result['target']}")
        st.markdown(f"- 美國專利號：{result['id']}")
        # bullet tag + expander
        st.markdown("- LLM 回答：")

        with st.expander("點我展開/收合 LLM 回答", expanded=True):
            st.markdown(result['llm_result'])
