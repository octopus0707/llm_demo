import streamlit as st

st.title("📄 專利分析展示")

st.markdown("這是示範頁面。")

example = {
    "title": "US20140080537A1",
    "target": "1104111181",
    "llm_result": "### 相似之處分析\n\n兩篇專利聚焦於早期解碼...\n\n**結論：** 都在做低功耗設計。"
}

st.subheader(f"📌 {example['title']} (target: {example['target']})")
st.markdown(example["llm_result"])
