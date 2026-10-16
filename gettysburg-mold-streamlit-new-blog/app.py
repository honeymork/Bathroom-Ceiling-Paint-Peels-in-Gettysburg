"""One-page Gettysburg homeowner article for Streamlit Community Cloud."""
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Peeling Bathroom Ceiling Paint in Gettysburg | Homeowner Guide",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's visible app chrome; the reading page remains accessible.
st.markdown(
    """
    <style>
      [data-testid="stSidebar"],
      [data-testid="stHeader"],
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      footer {display: none !important;}
      .stApp { background: #f7fafb; }
      .block-container {
        max-width: none !important;
        padding: 0 !important;
        margin: 0 !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      div[data-testid="stElementContainer"] { margin: 0 !important; }
      iframe { border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Auto-height HTML embedding avoids clipping and keeps the same plain-blog layout.
# Streamlit 1.66+ supports st.iframe with height='content' for local HTML files.
st.iframe(
    Path(__file__).resolve().with_name("article.html"),
    width="stretch",
    height="content",
    alt="Gettysburg bathroom ceiling peeling paint and mold prevention guide",
)
