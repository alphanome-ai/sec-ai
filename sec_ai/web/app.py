from __future__ import annotations

import streamlit as st
import streamlit_pills as stp  # type: ignore # noqa: PGH003

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
left, right = st.columns(2)
if selected_demo == demo_options["MDNA_SUMMARIZATION"]:
    with left, st.expander("**SEC EDGAR** INPUT", expanded=True):
        st.write("left")
    with right, st.expander("**SEC-AI** OUTPUT", expanded=True):
        st.write("right")
