import streamlit as st

st.set_page_config(page_title="Sten Design", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: yellow;
        margin: 0;
        padding: 0;
    }

    .typing-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 95vh;
        background: transparent;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        padding: 0 5vw;
    }

    .typing-text {
        font-size: 9vw;
        font-weight: 900;
        overflow: hidden;
        border-right: 4px solid white;
        display: inline-block;
        animation: typing 4s steps(40, end) forwards, blink 0.75s step-end infinite;
        word-wrap: break-word;
        white-space: normal;
        max-width: 100%;
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes blink {
        50% { border-color: transparent }
    }

    .subtitle {
        margin-top: 20px;
        font-size: 4vw;
        font-weight: 500;
        opacity: 0;
        animation: fadeIn 3s ease-in-out 4s forwards;
        max-width: 90vw;
    }

    @keyframes fadeIn {
        from { opacity: 0 }
        to { opacity: 1 }
    }

    .footer {
        margin-top: 40px;
        text-align: center;
        color: gray;
        font-size: 3vw;
    }

    /* For larger screens */
    @media (min-width: 768px) {
        .typing-text {
            font-size: 72px;
        }
        .subtitle {
            font-size: 20px;
        }
        .footer {
            font-size: 14px;
        }
    }
    </style>

    <div class="typing-container">
        <div class="typing-text">WELCOME TO STEN DESIGN</div>
        <div class="subtitle">
            TRANSFORMING COMPLEXITY TO SIMPLICITY – AIMS TO PROVIDE TOOLS AND AI SOLUTIONS THAT BENEFIT CIVIL ENGINEERS IN DAILY LIFE
        </div>
        <div class="footer">© 2025 Sten Design. All rights reserved.</div>
    </div>
    """,
    unsafe_allow_html=True
)
