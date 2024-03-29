import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## 使用方法\n"
            "1. 键入 [OpenAI API key](https://platform.openai.com/account/api-keys) 🔑，按回车健\n"  # noqa: E501
            "2. 上传文档 pdf, docx, or txt file📄\n"
            "3. 开始提问吧💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="API Key放在这里 (sk-...)",
            help="API Key 获取路径 https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
    
            "📖KnowledgeGPT 允许您询问有关 "
            "文档，并通过即时文档内容提取而获得准确答案。. "
        )

        st.markdown("---")

        
