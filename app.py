import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="JP Martínez Cordeiro | Computational Scientist & Mechanical Engineer", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Hero Section (The Hook)
with st.container():
    col1, col2 = st.columns([3, 1], gap="large")
    
    with col1:
        st.markdown("# Juan Pablo Martínez Cordeiro, Ph.D.")
        st.markdown("## Computational Scientist | Mechanical Engineer")
        st.markdown("### Chasing curiosity and building scalable, rigorous computational models along the way.")
        st.write("""
        __Hi, I'm JP__ - a computational scientist and mechanical engineer taking the next steps in his career 
        after completing his Ph.D. from UT Austin.""")
        st.write("""
        This portfolio contains more information about myself, my papers, 
        my interests, and my projects.
        """)
        st.write("""
        *__Feel free to connect and let me know what you think!__*
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

#st.divider()

# --- Project 2: Tactical Scouting Engine ---
with st.container():
    proj_col3, proj_col4 = st.columns([1, 2], gap="medium")
 
    with proj_col4:
        st.markdown("#### ⚽ Tactical Scouting Engine: Latent-Space Player Replacement")
        st.markdown("""
        **What happens when you strip a player down to pure numbers and ask who else plays the same way?** This engine compresses player performance profiles into a latent space to find suitable replacements.
 
        *Think you know who's truly irreplaceable? Think you could spot the next hidden gem before the market does? Put your inner scout to the test!*
        """)
        st.link_button("🔍 Launch Scouting Engine", "https://futbol-id.streamlit.app")
 
    with proj_col3:
        st.image("assets/football_scout.png", use_container_width=True)
 
st.divider()

# 4.5 Upcoming Projects Section
with st.container():
    st.markdown("### In Progress...")
    st.write("A sneak peek at the computational projects currently cooking in my local development environment.")
    
    # Create two columns for your upcoming projects
    pipe_col1, pipe_col2, pipe_col3 = st.columns(3, gap="large")
    
    with pipe_col1:
        st.markdown("#### 🌡️ OpenFOAM Thermal Surrogate Model")
        st.markdown("""
        **Accelerating heat fin design by replacing heavy CFD loops with rapid machine learning inference.**
        
        * **The Challenge:** Traditional geometric optimization of heat dissipation fins requires computationally expensive fluid dynamics iterations in OpenFOAM.
        * **The Approach:** Training a data-driven surrogate model on a physics-backed dataset to predict thermal profiles in milliseconds.
        
        🚧 *Status: Running CFD Simulations to Train Surrogate Model* 🚧
        """)
        # 🚧 *Status: Architecture Design & Data Collection* 🚧
        
    with pipe_col2:
        st.markdown("#### 🏎️ High-Frequency Telemetry Forecasting")
        st.markdown("""
        **Modeling vehicle sensor streams split-seconds into the future to capture sudden grip loss and system anomalies.**
        
        * **The Challenge:** F1 cars broadcast asynchronous, noisy telemetry across independent channels (Speed, Throttle, Brake, RPM).
        * **The Approach:** Engineering a synchronized time-series pipeline to feed ML models, enabling real-time vehicle state forecasting and instant detection of sudden anomalies like tire lock-ups.
        
        🚧 *Status: Designing Pipeline to Sync Data* 🚧
        """)
        # 🚧 *Status: Pipeline Sync & Architecture Design* 🚧
    
    with pipe_col3:
        st.markdown("#### 🍋 Simulating Adverse Selection")
        st.markdown("""
        **Quantifying the 'Market for Lemons' problem and mitigating buyer risk through dynamic Bayesian updates.**
        
        * **The Challenge:** In markets with asymmetric information, generic or uninformative priors mathematically guarantee expected losses for the buyer over time.
        * **The Approach:** Building a computational probability engine in Python to map market loss distributions and create interactive visualizations of shifting risk surfaces under informed priors.
        
        🚧 *Status: Finalizing Problem Statement* 🚧
        """)
        #🚧 *Status: Engine Dev & Risk Surface Mapping* 🚧

# 5. Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Juan Pablo Martínez Cordeiro. Built with Python and Streamlit.")