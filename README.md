<p align="center">&nbsp;</p>
<p align="center">
  <h1 align="center"><b>sec-ai</b></h1>
</p>
<p align="left">
  <!-- Using &nbsp; for alignment due to GitHub README limitations -->
  <b>Essentials ➔&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b>
  <a href='https://sec-ai.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/sec-ai/badge/?version=latest' alt='Documentation Status' /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/alphanome-ai/sec-ai.svg" alt="Licence"></a>
  <a href="https://project-types.github.io/#federation"><img src="https://img.shields.io/badge/project%20type-federation-brightgreen" alt="Project Type: Federation"></a>
  <!-- NOTE: After changing stability level here, also change it in pyproject.toml -->
  <a href="https://github.com/mkenney/software-guides/blob/master/STABILITY-BADGES.md#experimental"><img src="https://img.shields.io/badge/stability-experimental-orange.svg" alt="Experimental"></a>
  <br>
  <b>Health ➔&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b>
  <a href="https://github.com/alphanome-ai/sec-ai/actions/workflows/ci.yml"><img alt="GitHub Workflow Status: ci.yml" src="https://img.shields.io/github/actions/workflow/status/alphanome-ai/sec-ai/ci.yml?label=ci"></a>
  <a href="https://github.com/alphanome-ai/sec-ai/actions/workflows/cd.yml"><img alt="GitHub Workflow Status: cd.yml" src="https://img.shields.io/github/actions/workflow/status/alphanome-ai/sec-ai/cd.yml?label=cd"></a>
  <a href="https://github.com/alphanome-ai/sec-ai/commits/main"><img alt="Last Commit" src="https://img.shields.io/github/last-commit/alphanome-ai/sec-ai"></a>  
  <br>
  <b>Quality ➔&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b>
  <a href="https://codecov.io/gh/alphanome-ai/sec-ai"><img src="https://codecov.io/gh/alphanome-ai/sec-ai/graph/badge.svg?token=KJLA96CBCN" alt="codecov" /></a>
  <a href="https://mypy-lang.org/"><img src="https://img.shields.io/badge/type%20checked-mypy-blue.svg"></a>
  <a href="https://github.com/psf/black"><img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <br>
  <b>Distribution ➔&nbsp;&nbsp;&nbsp;</b>
  <a href="https://badge.fury.io/py/sec-ai"><img src="https://badge.fury.io/py/sec-ai.svg" alt="PyPI version" /></a>
  <a href="https://pypi.org/project/sec-ai/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/sec-ai"></a>
  <a href="https://pypistats.org/packages/sec-ai"><img src="https://img.shields.io/pypi/dm/sec-ai.svg" alt="PyPI downloads"></a>
  <br>
  <b>Community ➔&nbsp;&nbsp;&nbsp;&nbsp;</b>
  <a href="http://hits.dwyl.com/alphanome-ai/sec-ai"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fhits.dwyl.com%2Falphanome-ai%2Fsec-ai.json%3Fshow%3Dunique" alt="HitCount" /></a>
  <a href="https://twitter.com/alphanomeai"><img alt="X (formerly Twitter) Follow" src="https://img.shields.io/twitter/follow/alphanomeai"></a>
  <a href="https://github.com/alphanome-ai/sec-ai"><img src="https://img.shields.io/github/stars/alphanome-ai/sec-ai.svg?style=social&label=Star us on GitHub!" alt="GitHub stars"></a>


</p>

<div align="left">
  A comprehensive open-source toolkit for AI-powered analysis and interpretation of SEC EDGAR filings, providing valuable insights for investors, fintech developers, and researchers.
</div>
<br>
<div align="center">
  <b>
  <a href="https://sec.app.alphanome.dev">See Demo</a> |
  <a href="https://sec-ai.rtfd.io">Read Docs</a> |
  <a href="https://github.com/orgs/alphanome-ai/discussions">Join Discussions</a> |
  <a href="https://github.com/alphanome-ai/sec-ai/issues">Report Bugs</a>
  </b>
</div>
<br>

# Overview

`sec-ai` is an open-source project designed to provide a comprehensive toolset for analyzing and interpreting data from SEC filings. Utilizing advanced AI technologies, this project aims to serve a wide range of users, from individual investors to researchers and regulatory bodies. 

The project leverages [`alphanome-ai/sec-parser`](https://github.com/alphanome-ai/sec-parser) for its data extraction needs, an essential component that simplifies the parsing of SEC EDGAR HTML documents into a structured and analyzable format.

- Explore the [**Demo**](https://sec.app.alphanome.dev/)
- Read the [**Documentation**](https://sec-ai.rtfd.io)
- Join the [**Discussions**](https://github.com/orgs/alphanome-ai/discussions) to get help, propose ideas, or chat with the community
- Report bugs in [**Issues**](https://github.com/alphanome-ai/sec-ai/issues)
- Stay updated and contribute to our project's direction in [**Announcements**](https://github.com/orgs/alphanome-ai/discussions/categories/announcements) and [**Roadmap**](https://github.com/orgs/alphanome-ai/discussions/categories/roadmap-future-plans)

# Getting Started

To get started, first install the `sec-ai` package:

```bash
pip install sec-ai
```

> **Warning**
We are currently finalizing a few key prerequisites for `sec-ai` within our [**sec-parser**](https://github.com/alphanome-ai/sec-parser) project, as detailed in our [**Roadmap**](https://github.com/orgs/alphanome-ai/discussions/categories/roadmap-future-plans).<br><br>Your anticipation for the launch of `sec-ai` is greatly appreciated. We are working diligently to ensure that `sec-ai` is ready to launch as soon as possible. To stay informed about our progress and to receive notifications when `sec-ai` is ready, please follow our [**Announcements**](https://github.com/orgs/alphanome-ai/discussions/categories/announcements) page.<br><br>**Get Involved**: If you're excited about our project and would like to contribute, we warmly invite you to do so! Check out our [**sec-parser/CONTRIBUTING.md**](https://github.com/alphanome-ai/sec-parser/blob/main/CONTRIBUTING.md) guide for details on how to get started.
<br><br>Thank you for your interest and we look forward to sharing our progress with you soon.

For more examples and advanced usage, you can continue learning how to use `sec-ai` by referring to the [**User Guide**](https://sec-ai.readthedocs.io/en/latest/notebooks/user_guide.html), [**Developer Guide**](https://sec-ai.readthedocs.io/en/latest/notebooks/developer_guide.html), and [**Documentation**](https://sec-ai.rtfd.io).

# Best Practices

### Importing modules

1. Standard: `import sec_ai as sai`
1. Package-Level: `from sec_ai import SomeClass`
1. Submodule: `from sec_ai import sub_module`
1. Submodule-Level: `from sec_ai.sub_module import SomeClass`

> **Note**
The root-level package `sec_ai` contains only the most common symbols. For more specialized functionalities, you should use submodule or submodule-level imports.

> **Warning**
To allow us to maintain backward compatibility with your code during internal structure refactoring for `sec-ai`, avoid deep or chained imports such as `sec_ai.sub_module.internal_utils import SomeInternalClass`.

# Contributing
For information about setting up the development environment, coding standards, and contribution workflows, please refer to our [CONTRIBUTING.md](https://github.com/alphanome-ai/sec-ai/blob/main/CONTRIBUTING.md) guide.

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/alphanome-ai/sec-ai/blob/main/LICENSE) file for details.
