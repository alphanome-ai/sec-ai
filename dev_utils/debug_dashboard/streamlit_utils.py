from __future__ import annotations

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


class DemoOption:
    @classmethod
    def get_names(cls, demo_options: dict[str, DemoOption]) -> list[str]:
        return [demo.name for demo in demo_options.values()]

    @classmethod
    def get_icons(cls, demo_options: dict[str, DemoOption]) -> list[str]:
        return [demo.icon for demo in demo_options.values()]

    @classmethod
    def get_by_name(
        cls,
        demo_options: dict[str, DemoOption],
        name: str | None,
    ) -> DemoOption:
        if name is None:
            msg = "Name cannot be None."
            raise ValueError(msg)
        return next(v for _, v in demo_options.items() if v.name == name)

    def __init__(self, icon: str, name: str) -> None:
        self.icon = icon
        self.name = name
