import streamlit as st
from translations import TEXT

# 1. Page Configuration
st.set_page_config(
    page_title="JP Martínez Cordeiro | Portfolio", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1.1 Language Toggle
lang = st.sidebar.radio("Language / Idioma", ["en", "es"], horizontal=True)
def t(key):
    return TEXT[lang].get(key, f"Missing: {key}")

# 2. Hook
with st.container():
    col1, col2 = st.columns([3, 1], gap="large")
    
    with col1:
        st.markdown("# Juan Pablo Martínez Cordeiro, Ph.D.")
        st.markdown(t("role"))
        st.markdown(t("hook"))
        st.write(t("intro_1"))
        st.write(t("intro_2"))
        st.write(t("intro_3"))
        
        # Call to Action buttons (Adjusted spacing for 3 buttons)
        cta_col1, cta_col2, cta_col3, cta_col4 = st.columns([1.2, 1.2, 1.2, 1.2])
        with cta_col1:
            st.link_button(t("intro_button_1"), "https://www.linkedin.com/in/jpmc-143912-/", use_container_width=True)
        with cta_col2:
            st.link_button(t("intro_button_2"), "https://github.com/juanpamtzc", use_container_width=True)
        with cta_col3:
            st.link_button(t("intro_button_3"), "https://scholar.google.com/citations?user=UUroaHgAAAAJ&hl=en", use_container_width=True)
        with cta_col4:
            st.link_button(t("intro_button_4"), "https://jp-portfolio-agent.streamlit.app", use_container_width=True)

    with col2:
        st.image("assets/profile_pic.jpg", use_container_width=True)

st.divider()

# 3. Core Competencies Section
with st.container():
    st.markdown(t("skills_header"))
    st.write(t("skills_sub"))
    
    skill_col1, skill_col2, skill_col3, skill_col4 = st.columns(4)
    
    with skill_col1:
        st.markdown(t("skill1_header"))
        st.markdown(t("skill1_contents"))

    with skill_col2:
        st.markdown(t("skill2_header"))
        st.markdown(t("skill2_contents"))
        
    with skill_col3:
        st.markdown(t("skill3_header"))
        st.markdown(t("skill3_contents"))
        
    with skill_col4:
        st.markdown(t("skill4_header"))
        st.markdown(t("skill4_contents"))
    


st.divider()

# 4. Featured Project Section
with st.container():
    st.markdown(t("featured_header"))
    
    proj_col1, proj_col2 = st.columns([1, 2], gap="medium")
    
    with proj_col1:
        st.image("assets/red_vs_blue_viz.png", use_container_width=True)
        
    with proj_col2:
        st.markdown(t("feat1_header"))
        st.markdown(t("feat1_text"))
        
        st.link_button(t("feat1_button"), "https://red-vs-blue.streamlit.app")

#st.divider()

# --- Project 2: Tactical Scouting Engine ---
with st.container():
    proj_col3, proj_col4 = st.columns([1, 2], gap="medium")
 
    with proj_col4:
        st.markdown(t("feat2_header"))
        st.markdown(t("feat2_text"))
        st.link_button(t("feat2_button"), "https://futbol-id.streamlit.app")
 
    with proj_col3:
        st.image("assets/football_scout.png", use_container_width=True)
 
#st.divider()

# --- Project 3: Portfolio Fine-Tuned LLM Agent ---
with st.container():
    proj_col3, proj_col4 = st.columns([1, 2], gap="medium")
 
    with proj_col4:
        st.markdown(t("feat3_header"))
        st.markdown(t("feat3_text"))
        st.link_button(t("feat3_button"), "https://jp-portfolio-agent.streamlit.app")
 
    with proj_col3:
        st.image("assets/fine-tuned_llm.png", use_container_width=True)

# --- Project 4: Thermal Surrogate ---
with st.container():
    proj_col3, proj_col4 = st.columns([1, 2], gap="medium")
 
    with proj_col4:
        st.markdown(t("feat4_header"))
        st.markdown(t("feat4_text"))
        st.link_button(t("feat4_button"), "https://thermal-surrogate.streamlit.app")
 
    with proj_col3:
        st.image("assets/thermal_surrogate.png", use_container_width=True)
 
st.divider()

# --- Project 5: Hex Player ---
with st.container():
    proj_col3, proj_col4 = st.columns([1, 2], gap="medium")
 
    with proj_col4:
        st.markdown(t("feat5_header"))
        st.markdown(t("feat5_text"))
        st.link_button(t("feat5_button"), "https://hex-neural-engine.streamlit.app")
 
    with proj_col3:
        st.image("assets/hex_player.png", use_container_width=True)
 
st.divider()

# 4.5 Upcoming Projects Section
with st.container():
    st.markdown(t("future_header"))
    st.write(t("future_text"))
    
    # Create two columns for upcoming projects
    pipe_col1, pipe_col2, pipe_col3 = st.columns(3, gap="large")
    
    with pipe_col1:
        st.markdown(t("fut1_header"))
        st.markdown(t("fut1_text"))
        
    with pipe_col2:
        st.markdown(t("fut2_header"))
        st.markdown(t("fut2_text"))
    
    with pipe_col3:
        st.markdown(t("fut3_header"))
        st.markdown(t("fut3_text"))


st.divider()
# 4.6 Personal Projects and Hobbies
with st.container():
    st.markdown(t("personal_header"))
    st.write(t("personal_text"))
    
    # Create two columns for your upcoming projects
    pipe_col1, pipe_col2, pipe_col3 = st.columns(3, gap="large")
    
    with pipe_col1:
        st.markdown(t("pers1_header"))
        st.markdown(t("pers1_text"))

# 5. Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Juan Pablo Martínez Cordeiro. Built with Python and Streamlit.")