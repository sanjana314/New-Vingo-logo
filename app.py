
import base64

import streamlit as st

st.set_page_config(page_title="Vingo", layout="centered")

LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="100 215 1240 520">
<defs>
<linearGradient id="w" gradientUnits="userSpaceOnUse" x1="130" y1="330" x2="1040" y2="690">
<stop offset="0" stop-color="#5B21B6"/><stop offset="1" stop-color="#8B2BE2"/>
</linearGradient>
<linearGradient id="o" gradientUnits="userSpaceOnUse" x1="1085" y1="360" x2="1290" y2="580">
<stop offset="0" stop-color="#5B21B6"/><stop offset="0.5" stop-color="#7C3AED"/><stop offset="1" stop-color="#A855F7"/>
</linearGradient>
<mask id="gm">
<ellipse cx="912" cy="466" rx="125" ry="120" fill="#fff"/>
<rect x="958" y="351" width="79" height="215" fill="#fff"/>
<path d="M1037 540 C1037 640 980 684 913 684 C850 684 805 655 798 606 H873 C880 625 895 630 913 630 C945 630 958 610 958 570 Z" fill="#fff"/>
<ellipse cx="912" cy="466" rx="48" ry="59" fill="#000"/>
</mask>
</defs>
<rect x="100" y="215" width="1240" height="520" rx="28" fill="#EEE9FE"/>
<g fill="url(#w)">
<polygon points="132,351 215,351 263,515 311,351 391,351 305,588 220,588"/>
<rect x="410" y="351" width="77" height="237"/>
<path d="M526 351 H602 V385 C625 358 650 346 680 346 C730 346 758 380 758 440 V588 H681 V470 C681 430 665 410 640 410 C614 410 602 428 602 455 V588 H526 Z"/>
</g>
<circle cx="448" cy="296" r="34" fill="url(#w)"/>
<rect x="780" y="340" width="260" height="350" fill="url(#w)" mask="url(#gm)"/>
<circle cx="1186" cy="470" r="124" fill="url(#o)"/>
<circle cx="1186" cy="470" r="59" fill="#F5F3FF"/>
<path d="M1160 488 L1186 453 L1212 488" fill="none" stroke="#6D28D9" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

encoded = base64.b64encode(LOGO_SVG.encode()).decode()

st.markdown(
    f'<div style="text-align:center;padding:20px 0;">'
    f'<img src="data:image/svg+xml;base64,{encoded}" width="260"/>'
    f"</div>",
    unsafe_allow_html=True,
)



