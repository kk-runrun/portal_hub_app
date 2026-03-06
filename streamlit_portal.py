import html
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
            background: linear-gradient(115deg, #f4f6f8 0%, #e8edf2 45%, #eef4f5 100%);
        }
        .block-container {
            max-width: 1180px;
            padding-top: 1.7rem;
            padding-bottom: 2rem;
        }
        .portal-title {
            margin: 0 0 14px 0;
            font-size: 48px;
            font-weight: 800;
            color: #000000 !important;
            letter-spacing: 0.5px;
        }
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
        }
        .card {
            background: #ffffff;
            border: 1px solid #e6ebf0;
            border-radius: 14px;
            padding: 16px 14px;
            box-shadow: 0 10px 22px rgba(16, 24, 40, 0.08);
            min-height: 138px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .card-title {
            margin: 0;
            font-size: 34px;
            font-weight: 700;
            color: #000000 !important;
            line-height: 1.2;
            word-break: break-word;
        }
        .open-btn {
            display: inline-block;
            width: fit-content;
            margin-top: 16px;
            background: #184a86;
            color: #ffffff !important;
            text-decoration: none !important;
            border-radius: 10px;
            padding: 9px 16px;
            font-size: 15px;
            font-weight: 600;
            border: 1px solid #184a86;
        }
        .open-btn:hover {
            background: #113a6b;
            border-color: #113a6b;
        }
        .open-btn.disabled {
            background: #d1d9e6;
            border-color: #d1d9e6;
            color: #6b7280 !important;
            pointer-events: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_cards(apps: list[dict]) -> None:
    items = []
    for app in apps:
        name = html.escape(str(app.get("name", "未命名模块")))
        url = str(app.get("url", "")).strip()
        if url:
            btn = f'<a class="open-btn" href="{html.escape(url)}" target="_blank">打开页面</a>'
        else:
            btn = '<span class="open-btn disabled">打开页面</span>'
        items.append(f'<div class="card"><h3 class="card-title">{name}</h3>{btn}</div>')

    st.markdown(f'<div class="cards-grid">{"".join(items)}</div>', unsafe_allow_html=True)


def main() -> None:
    st.set_page_config(page_title="统一工作台门户", page_icon="🧭", layout="wide")
    inject_styles()
    st.markdown('<h1 class="portal-title">统一工作台门户</h1>', unsafe_allow_html=True)
    cfg = load_links()
    render_cards(cfg.get("apps", []))


if __name__ == "__main__":
    main()
