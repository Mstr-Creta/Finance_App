import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
            .main-title {
                font-size: 32px;
                font-weight: 800;
                color: #4B8BBE;
                margin-top: 10px;
            }
            .section-header {
                font-size: 24px;
                font-weight: 700;
                color: #306998;
                margin-bottom: 8px;
            }
            .budget-alert {
                background-color: #FFDDDD;
                padding: 10px;
                border-radius: 6px;
                font-weight: 600;
                color: #BB0000;
            }
            .success-box {
                background-color: #E0FFEF;
                padding: 10px;
                border-radius: 6px;
                color: #007F5F;
                font-weight: 600;
            }
        </style>
    """, unsafe_allow_html=True)

def render_title(text):
    st.markdown(f"<div class='main-title'>{text}</div>", unsafe_allow_html=True)

def render_header(text):
    st.markdown(f"<div class='section-header'>{text}</div>", unsafe_allow_html=True)

def alert_box(message):
    st.markdown(f"<div class='budget-alert'>{message}</div>", unsafe_allow_html=True)

def success_box(message):
    st.markdown(f"<div class='success-box'>{message}</div>", unsafe_allow_html=True)