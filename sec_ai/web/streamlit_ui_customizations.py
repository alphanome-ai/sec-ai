import streamlit as st


def st_hide_page_element(*, tag_name: str, key: str, value: str) -> None:
    st.markdown(
        f"""
        <style>
            {tag_name}[{key}="{value}"] {{
                visibility: hidden;
                height: 0%;
                position: fixed;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
