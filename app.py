import streamlit as st

# 模擬你的分析結果資料
example_results = [
    {
        "target": "1104111181",
        "id": "US20140080537A1",
        "llm_result": """
### 專利一與專利二的相似之處分析

兩篇專利都聚焦於「早期解碼」技術，以降低功率消耗...

1. **比較點一**  
   - 專利一內容
   - 專利二內容
   - 原因說明

2. **比較點二**
   ...
"""
    },
    {
        "target": "1104111181",
        "id": "US20130250785A1",
        "llm_result": """
### 專利比對說明

**專利一（裝置）段落：**
- 裝置內容

**專利二（方法）段落：**
- 方法內容

**總結：**
兩篇專利都處理早期解碼與功率管理...
"""
    }
]

st.set_page_config(page_title="專利比對展示", layout="wide")
st.title("📄 多筆專利比對分析")

# 產生 tab 名稱
tab_titles = [f"{item['id']} (target: {item['target']})" for item in example_results]

# 建立 tabs
tabs = st.tabs(tab_titles)

# 對應每個 tab 顯示內容
for tab, result in zip(tabs, example_results):
    with tab:
        st.subheader(f"📌 專利編號：{result['id']}")
        st.markdown(result["llm_result"], unsafe_allow_html=True)
