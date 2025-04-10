import streamlit as st

# Title of the app
st.title("Power BI Embedded Dashboard")

# Power BI embed URL (your provided embed URL)
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZTg4OGU2MjgtZTI0OC00YzI4LWEwOGYtMzhhYTMxOGIzZjYwIiwidCI6ImI3MTRjMWQzLWVkOGEtNGFlYS1iMDYxLTI3MjVkN2I4ZDBjMyJ9"

# Centering the iframe with a YouTube-like fullscreen size (responsive)
st.markdown(
    f"""
    <style>
        .iframe-container {{
            position: relative;
            padding-bottom: 56.25%; /* Aspect ratio for 16:9 */
            height: 0;
            overflow: hidden;
            max-width: 100%;
            background: #000;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
    <div class="iframe-container">
        <iframe src="{power_bi_url}" title="Power BI Dashboard" allowFullScreen="true"></iframe>
    </div>
    """, 
    unsafe_allow_html=True
)
