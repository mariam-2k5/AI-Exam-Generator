import streamlit as st

st.set_page_config(
    page_title="AI Exam Generator",
    layout="wide"
)

# ---------- GLOBAL CSS ----------

st.markdown("""
<style>

.main {
background: linear-gradient(120deg,#0f172a,#111827);
}

.title {
font-size:50px;
font-weight:800;
text-align:center;
background: linear-gradient(90deg,#38bdf8,#22c55e);
-webkit-background-clip:text;
color:transparent;
margin-bottom:10px;
}

.subtitle{
text-align:center;
font-size:20px;
color:#cbd5f5;
margin-bottom:40px;
}

.feature-card{
background:#1e293b;
padding:35px;
border-radius:12px;
border:1px solid #334155;
transition:0.3s;
}

.feature-card:hover{
transform:translateY(-5px);
box-shadow:0px 6px 25px rgba(0,0,0,0.4);
}

.feature-title{
font-size:24px;
font-weight:600;
color:#f1f5f9;
margin-bottom:10px;
}

.feature-text{
color:#cbd5e1;
font-size:16px;
}

.section-title{
font-size:30px;
font-weight:700;
text-align:center;
margin-top:20px;
margin-bottom:25px;
color:#e2e8f0;
}

.step-card{
background:#1e293b;
padding:25px;
border-radius:10px;
border:1px solid #334155;
}

.step-card h4{
color:#38bdf8;
}

.step-card p{
color:#cbd5e1;
}

.footer{
text-align:center;
margin-top:40px;
color:#94a3b8;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)


# ---------- TITLE ----------

st.markdown('<div class="title">AI Exam Generator</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Generate exam papers and enable adaptive learning using Artificial Intelligence</div>',
unsafe_allow_html=True
)

st.divider()

# ---------- FEATURES ----------

st.markdown('<div class="section-title">Platform Features</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
    <div class="feature-title">Teacher Mode</div>
    <div class="feature-text">
    Automatically generate structured exam papers from study material.
    </div>
    <br>

    • MCQ Question Generation  
    • Theory Question Generation  
    • Bloom's Taxonomy Levels  
    • Adjustable Marks  
    • Custom Question Count  
    • Optional Answer Key  

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <div class="feature-title">Student Mode</div>
    <div class="feature-text">
    Adaptive learning system that evaluates answers and increases difficulty.
    </div>
    <br>

    • One Question at a Time  
    • AI Answer Evaluation  
    • Bloom's Level Progression  
    • Strength & Improvement Feedback  
    • Session Completion Summary  

    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------- HOW SYSTEM WORKS ----------

st.markdown('<div class="section-title">How the System Works</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="step-card">

    <h4>Teacher Mode</h4>

    1. Open Teacher Mode from sidebar  
    2. Paste study material  
    3. Choose Bloom's taxonomy level  
    4. Select question type (MCQ or Theory)  
    5. Set marks and number of questions  
    6. Generate the exam paper  

    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="step-card">

    <h4>Student Mode</h4>

    1. Open Student Mode  
    2. Start adaptive practice  
    3. Answer AI generated questions  
    4. Get evaluation feedback  
    5. Progress through Bloom's levels  
    6. Complete the adaptive session  

    </div>
    """, unsafe_allow_html=True)

st.markdown(
"""
<div class="footer">
AI Based Exam Generation and Adaptive Learning System
</div>
""",
unsafe_allow_html=True
)