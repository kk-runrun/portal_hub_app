import json
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
LINKS_PATH = BASE_DIR / "portal_links.json"


def load_links() -> dict:
    with LINKS_PATH.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background: #ffffff;
        }
        .portal-title {
            margin: 0 0 8px 0;
            font-size: 36px;
            font-weight: 700;
            color: #111827;
        }
        .card {
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 16px;
            background: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
            margin-bottom: 12px;
            min-height: 120px;
        }
        .card-title {
            margin: 0 0 12px 0;
            font-size: 20px;
            font-weight: 600;
            color: #111827;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def link_card(title: str, url: str) -> None:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<p class="card-title">{title}</p>', unsafe_allow_html=True)
    if url:
        st.link_button("打开页面", url, use_container_width=True)
    else:
        st.button("打开页面", disabled=True, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


def main() -> None:
    st.set_page_config(page_title="统一工作台门户", page_icon="🧭", layout="wide")
    inject_styles()
    st.markdown('<h1 class="portal-title">统一工作台门户</h1>', unsafe_allow_html=True)

    cfg = load_links()
    apps = cfg.get("apps", [])

    left, right = st.columns(2)
    for i, item in enumerate(apps):
        with (left if i % 2 == 0 else right):
            link_card(item.get("name", "未命名模块"), item.get("url", "").strip())


if __name__ == "__main__":
    main()
