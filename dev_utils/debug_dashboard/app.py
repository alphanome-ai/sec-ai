from __future__ import annotations

import rich.traceback
import streamlit as st
import streamlit_pills as stp

from dev_utils.debug_dashboard.config import get_config  # type: ignore # noqa: PGH003
from dev_utils.debug_dashboard.streamlit_utils import DemoOption, st_hide_page_element

rich.traceback.install()
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
We're thrilled to inform you that the `sec-parser` project is the final prerequisite for launching our eagerly anticipated feature, sec-ai. We're diligently working to ensure that it meets all the necessary standards and functionalities.

**Stay Informed**: For detailed information and updates specific to `sec-parser` and to be the first to know when sec-ai is launched, please [follow our Announcements page](https://github.com/orgs/alphanome-ai/discussions/categories/announcements).

**Contribute to sec-parser**: If you're as excited about `sec-parser` and the upcoming sec-ai feature as we are, we warmly invite you to get involved!

 - Join our [Discussions](https://github.com/orgs/alphanome-ai/discussions) and connect with us on [Discord](https://discord.gg/w6bpyBW6).
 - Please review our [Contribution Guide for sec-parser](https://github.com/alphanome-ai/sec-parser/blob/main/CONTRIBUTING.md).
 - Explore the [current Issues](https://github.com/alphanome-ai/sec-parser/issues) or propose new enhancements to the `sec-parser`. 

Our targeted launch for sec-ai is approaching, and we're grateful for your continued anticipation and interest, which are invaluable to our endeavors.
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
