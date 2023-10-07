from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum

import streamlit as st


class Environment(Enum):
    DEV = "dev"
    CI_CD = "ci_cd"
    PROD = "prod"

    @property
    def is_dev(self) -> bool:
        return self == Environment.DEV

    @property
    def is_prod(self) -> bool:
        return self == Environment.PROD

    @property
    def is_ci_cd(self) -> bool:
        return self == Environment.CI_CD


@dataclass
class Config:
    environment: Environment
    # You can obtain a free API key at https://sec-api.io
    secapio_api_key: str | None


@st.cache_data
def get_config() -> Config:
    return Config(
        environment=Environment(os.environ.get("ENVIRONMENT", Environment.DEV)),
        secapio_api_key=os.environ.get("SECAPIO_API_KEY"),
    )
