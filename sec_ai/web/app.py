from __future__ import annotations

import streamlit as st
import streamlit_pills as stp  # type: ignore # noqa: PGH003
import openai
from sec_ai.web.dashboard_helpers_and_types import DemoOption
from sec_ai.web.streamlit_ui_customizations import (
    st_hide_page_element,
)

# Setup page
st.set_page_config(
    page_title="sec-ai: Advanced AI for SEC EDGAR Filings",
    page_icon="🏦",
)
st_hide_page_element(tag_name="div", key="class", value="stDeployButton")
st_hide_page_element(tag_name="div", key="data-testid", value="stDecoration")
st_hide_page_element(tag_name="span", key="id", value="MainMenu")

# Add page elements

st.markdown(
    (
        "# sec-ai &nbsp;&nbsp;"
        '<a href="https://github.com/alphanome-ai/sec-ai">'
        '<img src="https://img.shields.io/github/stars/'
        'alphanome-ai/sec-ai.svg?style=social&label=Star us on GitHub!" '
        'alt="GitHub stars"></a>'
    ),
    unsafe_allow_html=True,
)


st.write(
    "A comprehensive open-source toolkit for AI-powered analysis and interpretation of "
    "SEC EDGAR filings, providing valuable insights for investors, fintech developers, "
    "and researchers.",
)


demo_options = {
    "MDNA_SUMMARIZATION": DemoOption("🧬", "MD&A Summarization"),
}
selected_demo = DemoOption.get_by_name(
    demo_options,
    stp.pills(
        "Select a demo:",
        options=DemoOption.get_names(demo_options),
        icons=DemoOption.get_icons(demo_options),
    ),
)

def summarize_text_with_gpt4(text, api_key):
    # Create a prompt for GPT-4
    prompt = "Summarize the following text:\n\n" + text

    # Generate a summary
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
        api_key=api_key,
    )

    # Return the summary
    return response.choices[0].text

def summarize_text_with_gpt3_5(text, api_key):
    # Create a prompt for GPT-3.5
    prompt = "Summarize the following text:\n\n" + text

    # Generate a summary
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
        api_key=api_key,
    )

    # Return the summary
    return response.choices[0].text

def summarize_text_with_gpt3(text, api_key):
    # Create a prompt for GPT-3
    prompt = "Summarize the following text:\n\n" + text

    # Generate a summary
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
        api_key=api_key,
    )

    # Return the summary
    return response.choices[0].text

  
left, right = st.columns(2)
with left, st.expander("**SEC EDGAR** INPUT", expanded=True):
    llm_selector = st.selectbox("Select Large Language Model:", ["GPT-4", "GPT-3.5", "GPT-3"])
    
    openai_api_key = st.text_input("Enter your OpenAI API key:")
    
    if openai_api_key:
        text = st.text_area("Enter the text to summarize:")
    
    if openai_api_key and text:
        if st.button("Summarize"):
            if llm_selector == "GPT-4":
                summarized_text = summarize_text_with_gpt4(text, openai_api_key)
            elif llm_selector == "GPT-3.5":
                summarized_text = summarize_text_with_gpt3(text, openai_api_key)
            elif llm_selector == "GPT-3":
                summarized_text = summarize_text_with_gpt3_5(text, openai_api_key)
    with right, st.expander("**SEC-AI** OUTPUT", expanded=True):
        if "summarized_text" in locals():
            st.write("Summarized Text:")
            st.write(summarized_text)
