from __future__ import annotations

import sec_parser as sp
import streamlit as st

from dev_utils.debug_dashboard.config import get_config


class SecDataRetriever:
    def __init__(self, secapio_api_key: str) -> None:
        self._secapio_api_key = secapio_api_key or get_config().secapio_api_key
        if not self._secapio_api_key:
            msg = (
                "SEC API key is not set. Please set it as the "
                "environment variable SECAPIO_API_KEY."
            )
            raise ValueError(msg)

    @st.cache_data(
        experimental_allow_widgets=True,
        show_spinner="Retrieving SEC EDGAR document...",
    )
    def get_metadata(
        # The prefix _ is used to circumvent a known issue with Streamlit's cache.
        # More details can be found at: https://github.com/streamlit/streamlit/issues/6109
        _self,  # noqa: N805
        *,
        doc: sp.DocumentType | str,
        url: str | None = None,
        latest_from_ticker: str | None = None,
    ) -> dict:
        self = _self  # to avoid false positives from python linters

        retriever = sp.SecapioDataRetriever(api_key=self._secapio_api_key)
        return retriever.retrieve_report_metadata(
            doc,
            url=url,
            latest_from_ticker=latest_from_ticker,
        )

    @st.cache_data(
        experimental_allow_widgets=True,
        show_spinner="Retrieving SEC EDGAR document...",
    )
    def download_html(
        # The prefix _ is used to circumvent a known issue with Streamlit's cache.
        # More details can be found at: https://github.com/streamlit/streamlit/issues/6109
        _self,  # noqa: N805
        *,
        doc: sp.DocumentType | str,
        url: str,
        sections: list[sp.SectionType | str] | None = None,
    ) -> str:
        self = _self  # to avoid false positives from python linters

        retriever = sp.SecapioDataRetriever(api_key=self._secapio_api_key)
        return retriever.get_report_html(doc, url, sections=sections)

    @st.cache_resource
    def get_semantic_elements(
        # The prefix _ is used to circumvent a known issue with Streamlit's cache.
        # More details can be found at: https://github.com/streamlit/streamlit/issues/6109
        _self,  # noqa: N805
        *,
        html: str,
    ) -> list[sp.AbstractSemanticElement]:
        parser = sp.SecParser()
        return parser.parse(html)
