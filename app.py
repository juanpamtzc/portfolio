import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Juan Pablo Martínez Cordeiro, Ph.D. | Computational Scientist & Mechanical Engineer", 
    page_icon="📐", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Hero Section (The Hook)
with st.container():
    col1, col2 = st.columns([3, 1], gap="large")
    
    with col1:
        st.markdown("# Juan Pablo Martínez Cordeiro | Computational Scientist & Mechanical Engineer")
        st.markdown("### Chasing my curiosity by building scalable, mathematically rigorous computational models.")
        st.write("""
        I am a computational scientist and mechanical engineer taking the next steps in my career 
        after completing my Ph.D. from UT Austin. This portfolio contains more information about myself, my papers, 
        my interests, and my projects. Feel free to connect and let me know what you think!
        """)
        
        # Call to Action buttons (Adjusted spacing for 3 buttons)
        cta_col1, cta_col2, cta_col3, cta_col4 = st.columns([1.2, 1.2, 1.5, 2])
        with cta_col1:
            st.link_button("👔 LinkedIn", "https://www.linkedin.com/in/jpmc-143912-/", use_container_width=True)
        with cta_col2:
            st.link_button("💻 GitHub", "https://github.com/juanpamtzc", use_container_width=True)
        with cta_col3:
            # Added your actual Google Scholar link!
            st.link_button("🎓 Google Scholar", "https://scholar.google.com/citations?user=UUroaHgAAAAJ&hl=en", use_container_width=True)

    with col2:
        # Pulls the image directly from your GitHub repository folder
        st.image("assets/profile_pic.jpg", use_container_width=True)

st.divider()

# 3. Core Competencies Section
with st.container():
    st.markdown("### Skills")
    st.write("Bridging the gap between mathematical/statistical modeling and high-performance code.")
    
    skill_col1, skill_col2, skill_col3, skill_col4 = st.columns(4)
    
    with skill_col1:
        st.markdown("#### ⚙️ Engineering")
        st.markdown("""
        * Fluid Dynamics
        * Heat Transfer
        * Thermodynamics/Stat Mech
        * Multiscale and Nonlinear FEA/CFD
        * Nanofluidics/Nanomechanics (MD/DFT)
        """)

    with skill_col2:
        st.markdown("#### 📐 Mathematics")
        st.markdown("""
        * Numerical Methods
        * Stochastic Modeling
        * Statistics
        * Probability
        * Linear Algebra
        """)
        
    with skill_col3:
        st.markdown("#### 💻 Programming")
        st.markdown("""
        * High-Performance Computing
        * Python | C | MATLAB | SQL
        * Vectorization | Parallelization (CUDA)
        * CI/CD
        * Machine Learning
        """)
        
    with skill_col4:
        st.markdown("#### 📊 Analysis")
        st.markdown("""
        * Statistical Inference
        * Hypothesis Testing
        * Model Development/Validation
        * Time-series Analysis
        * Spectral Analysis
        """)
    


st.divider()

# 4. Featured Project Section
with st.container():
    st.markdown("### Featured Work")
    
    proj_col1, proj_col2 = st.columns([1, 2], gap="medium")
    
    with proj_col1:
        # We can update this screenshot later just like we did the profile picture!
        st.image("assets/red_vs_blue_viz.png", use_container_width=True)
        
    with proj_col2:
        st.markdown("#### 🔴 🔵 Blue vs. Red: Expected Utility Optimizer")
        st.markdown("""
        **A late-night bachelor party thought experiment, formalized into a rigorous computational model.** This interactive dashboard computes expected utility under existential risk, balancing self-preservation against the greater good. 
        
        *Try it out! Does the mathematical optimum match your moral intuition?*
        """)
        
        # Link directly to the streamlit app
        st.link_button("Launch Live Simulator", "https://red-vs-blue.streamlit.app")

# 5. Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Juan Pablo Martínez Cordeiro. Built with Python and Streamlit.")