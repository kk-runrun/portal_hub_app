import json
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
LINKS_PATH = BASE_DIR / "portal_links.json"


def load_links() -> dict:
    with LINKS_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def link_card(title: str, desc: str, url: str) -> None:
    st.markdown(f"### {title}")
    st.caption(desc)
    if url:
        st.link_button("打开页面", url, use_container_width=True)
    else:
        st.warning("尚未配置上线链接")
    st.divider()


def main() -> None:
    st.set_page_config(page_title="统一工作台门户", page_icon="🧭", layout="wide")
    st.title("统一工作台门户")
    st.caption("统一入口访问各模块（外链跳转模式）")

    cfg = load_links()
    apps = cfg.get("apps", [])

    left, right = st.columns(2)
    for i, item in enumerate(apps):
        with (left if i % 2 == 0 else right):
            link_card(
                item.get("name", "未命名模块"),
                item.get("desc", ""),
                item.get("url", "").strip(),
            )

    with st.expander("配置说明"):
        st.code(str(LINKS_PATH), language="text")
        st.write("修改 `portal_links.json` 中的 URL 即可更新跳转地址。")


if __name__ == "__main__":
    main()
