from __future__ import annotations

import streamlit as st
import streamlit_pills as stp

from dev_utils.debug_dashboard.config import get_config  # type: ignore # noqa: PGH003
from dev_utils.debug_dashboard.streamlit_utils import DemoOption, st_hide_page_element

# Setup page
st.set_page_config(
    page_title="sec-ai: Advanced AI for SEC EDGAR Filings",
    page_icon="🏦",
)
st_hide_page_element(tag_name="div", key="data-testid", value="stDecoration")

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

if True:
    st.info(
        """
### 🚧 Under Construction 🚧
We are currently finalizing a few key prerequisites for `sec-ai` within our [**sec-parser**](https://github.com/alphanome-ai/sec-parser) project, as detailed in our [**Roadmap**](https://github.com/orgs/alphanome-ai/discussions/categories/roadmap-future-plans).

Your anticipation for the launch of `sec-ai` is greatly appreciated. We are working diligently to ensure that `sec-ai` is ready to launch as soon as possible. To stay informed about our progress and to receive notifications when `sec-ai` is ready, please follow our [**Announcements**](https://github.com/orgs/alphanome-ai/discussions/categories/announcements) page.

**Get Involved**: If you're excited about our project and would like to contribute, we warmly invite you to do so! Check out our [**sec-parser/CONTRIBUTING.md**](https://github.com/alphanome-ai/sec-parser/blob/main/CONTRIBUTING.md) guide for details on how to get started.

Thank you for your interest and we look forward to sharing our progress with you soon.
""",
    )
else:
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

footer = f"v{get_config().sec_ai_version}"
if not get_config().environment.is_prod:
    footer = f"[{get_config().environment.value}] {footer}"
st.markdown(
    f"""
    <div style="position: fixed; left: 6px; bottom: 0; width: 100%; text-align: left; color: lightgrey;">
        {footer}
    </div>
    """,
    unsafe_allow_html=True,
)
