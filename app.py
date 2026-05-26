import streamlit as st

# 1. Page Configuration (Set to 'wide' for a modern website feel)
st.set_page_config(
    page_title="Juan Pablo Martínez Cordeiro, Ph.D. | Computational Scientist and Mechanical Engineer", 
    page_icon="📐", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Hero Section (The Hook)
# Using a container to group the introductory visual elements
with st.container():
    col1, col2 = st.columns([3, 1], gap="large")
    
    with col1:
        st.markdown("# Hi, I'm Juan Pablo Martínez Cordeiro.")
        st.markdown("### I chase my curiosity building scalable, mathematically rigorous computational models along the way.")
        st.write("""
        I am a computational scientist and mechanical engineer transitioning taking the next steps after completing my Ph.D. 
        This portfolio has more information about myself, my papers, my interests, and my projects.
        Feel free to connect and let me know what you think!
        """)
        
        # Call to Action buttons
        cta_col1, cta_col2, cta_col3 = st.columns([1, 1, 3])
        with cta_col1:
            st.link_button("👔 LinkedIn", "https://www.linkedin.com/in/jpmc-143912-/", use_container_width=True)
        with cta_col2:
            st.link_button("💻 GitHub", "https://github.com/juanpamtzc", use_container_width=True)

    with col2:
        # A circular or clean profile image looks much more professional
        st.image("https://placehold.co/400x400?text=Profile+Photo", use_column_width=True)

st.divider()

# 3. Core Competencies Section (The Resume Teaser)
with st.container():
    st.markdown("### Technical Expertise")
    st.write("Bridging the gap between pure mathematics and production-grade software.")
    
    skill_col1, skill_col2, skill_col3 = st.columns(3)
    
    with skill_col1:
        st.markdown("#### 📐 Mathematics")
        st.markdown("""
        * Computational Nanofluidics and Statistical Mechanics
        * Numerical Methods
        * Stochastic Modeling
        * Linear Algebra
        """)
        
    with skill_col2:
        st.markdown("#### ⚙️ Engineering")
        st.markdown("""
        * Python (Advanced)
        * Vectorized Compute (`numpy`, `scipy`)
        * Continuous Integration (GitHub Actions)
        * Streamlit / Web Dashboards
        """)
        
    with skill_col3:
        st.markdown("#### 📊 Analysis")
        st.markdown("""
        * Parameter Space Sweeps
        * Data Visualization (`matplotlib`, `seaborn`)
        * Hypothesis Testing
        * Statistical Inference
        """)

st.divider()

# 4. Featured Project Section
with st.container():
    st.markdown("### Featured Work")
    
    # We create an explicit card-like layout for the project
    proj_col1, proj_col2 = st.columns([1, 2], gap="medium")
    
    with proj_col1:
        # You can replace this with a screenshot of your actual Blue vs Red app later
        st.image("https://placehold.co/600x400?text=App+Screenshot", use_column_width=True)
        
    with proj_col2:
        st.markdown("#### 🔵 Blue vs. Red: Game-Theoretic Optimizer")
        st.write("""
        A high-performance interactive dashboard computing expected utility under existential risk scenarios. 
        Engineered with $O(N)$ computational complexity using pure `numpy` broadcasting, bypassing the need 
        for slow iterative loops, and verified against strict closed-form analytical solutions.
        """)
        
        # Link directly to the Spoke
        st.link_button("Launch Live Simulator", "https://yourname-blue-vs-red.streamlit.app")

# 5. Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2024 Juan Pablo Martínez Cordeiro. Built with Python and Streamlit.")