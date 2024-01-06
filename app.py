from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ricardo_Marques_CV.pdf"
profile_pic = current_dir / "assets" / "cv_pic.png"

# --- GENERAL SETTINGS ---

PAGE_TITLE = "Digital CV | Ricardo Marques"
PAGE_ICON = "🚀"
NAME = "Ricardo Marques"
DESCRIPTION = """
Mathematician, aspiring Data Scientist with huge passion for football.
"""
EMAIL = "ricardo.andreom@gmail.com"
SOCIAL_MEDIA = {
    "Linkedin": "https://www.linkedin.com/in/ricardoandreom/",
    "Github": "https://github.com/ricardoandreom",
    "Tableau": "https://public.tableau.com/app/profile/ricardoandreom",
    "Medium": "https://medium.com/@ricardoandreom",
    "Halfspace Analytics Instagram": "https://www.instagram.com/halfspace_analytics/",
    "Linktree": "https://linktr.ee/ricardoandreom"
}

PROJECTS = {
    "🏆 Player Radar charts app": "https://football-player-radar-charts.streamlit.app/",
    "🏆 Player similarities app": "https://player-similarities.streamlit.app/",
    "🏆 Ecommerce Sales Power BI dashboard": "https://app.powerbi.com/groups/me/reports/5fdf93cf-7ee2-402e-80b9-169d25e4ecdc/ReportSection?experience=power-bi",
    "🏆 Stock Price Prediction tool": "https://www.linkedin.com/posts/ricardoandreom_datascience-montecarlo-finance-activity-7030227737415925760-a6-6/?utm_source=share&utm_medium=member_desktop",
    "🏆 Article written for RECORD analysing South Koreal in WC2022": "https://www.record.pt/internacional/competicoes-de-selecoes/mundial/mundial-2022/detalhe/ao-cuidado-de-fernando-santos-como-travar-os-sul-coreanos",
    "🏆 Article written for RECORD analysing Switzerland in WC2022": "https://www.record.pt/internacional/competicoes-de-selecoes/mundial/mundial-2022/detalhe/hora-de-acertar-o-relogio-e-nao-marcar-passo-a-analise-a-selecao-suica?tokenOffer=S3to1NHFyUOqI6pUFW1G0AxtJuKb8zX0W6lInZGlI8ww&utm_source=Partilha_Artigo_Premium",
    "🏆 Article written for RECORD analysing Morroco in WC2022": "https://www.record.pt/internacional/competicoes-de-selecoes/mundial/mundial-2022/marrocos/detalhe/rugir-mais-alto-que-os-leoes-do-atlas-ou-de-como-travar-marrocos-nos-quartos-de-final?ref=HP_2BucketDestaquesPrincipais&fbclid=PAAaYWn5R_FJbw1w1LPT_h6LQ_avnKTRjbY2TZIbwO1ilPgxvkVXleEENEx-E",
    "🏆 Football data scouting - Euclidian player similiarities": "https://medium.com/@ricardoandreom/football-scouting-players-level-of-similarity-88c40fb6e77e",
    "🏆 Football data Scouting — Would Dalot be a good signing for a Real Madrid?": "https://medium.com/@ricardoandreom/football-data-scouting-would-dalot-be-a-good-signing-for-a-real-madrid-a5f51f638ff1",
    "🏆 UCL Final 2003/04 visualized using Statsbomb free data": "https://medium.com/@ricardoandreom/ucl-final-2003-04-visualized-using-statsbomb-free-data-f6f7976d9741",
    "🏆 How bookmakers make the odds of goals and corners in a football match?":"https://github.com/ricardoandreom/Football-Data-Analysis/blob/main/Football_eventing_odds.ipynb",
    "🏆 How far can man jump? - Extreme Value Theory":"https://github.com/ricardoandreom/Extreme-Value-Theory",
    "🏆 How can we describe a team’s style of play using data?":"https://medium.com/@ricardoandreom/how-can-we-describe-a-teams-style-of-play-b14ff359d803",
    "🏆 Predicting the transfer value of a player": "https://medium.com/@ricardoandreom/predicting-the-transfer-value-of-a-player-c988c301255a",
    "🏆 Is Liverpool’s poor performance correlated with the high number of injuries?": "https://medium.com/@ricardoandreom/is-liverpools-poor-performance-correlated-with-the-high-number-of-injuries-f8d870714dcb"
    


}

CERTIFICATES_ONLINE = {
    "📊 Python for Data Science and Machine Learning Bootcamp": "https://www.udemy.com/certificate/UC-cab537f2-9656-4106-ba8b-aa4cfafe3373/",
    "📊 The Business Intelligence Analyst Course": "https://www.udemy.com/certificate/UC-9681db21-054a-41d7-86d3-2adc11605a82/",
    "📊 Data Science Math Skills": "https://www.coursera.org/account/accomplishments/verify/XN2PJLWC9HNR",
    "📊 Level I CFA Prep Course (2023) - Quantitative Methods": "https://www.udemy.com/certificate/UC-ae2b7cda-d1b1-435e-94ee-e400957eb7bd/",
    "📊 Python and Statistics for Financial Analysis": "https://www.coursera.org/account/accomplishments/verify/BHKY6XVMQF59"
}

CERTIFICATES_FOOTBALL = {
    "⚽ Match analysis - Barça Innovation Hub": "",
    "⚽ Opponent team analysis - Barça Innovation Hub": "",
    "⚽ PFSA Level 1 Performance Analysis in Football": "",
    "⚽ PFSA Level 2 Performance Analysis in Football": "",
    "⚽ PFSA Level 1 Technical Scouting in Football": "",
    "⚽ PFSA Level 2 Technical Scouting in Football": ""
}
                

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



st.title("Hello there!")
#st.markdown("<h1 class='stTitle'>Hello there!</h1>", unsafe_allow_html=True)


# --- HERO SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= "📄 Download Resume",
        data= PDFbyte,
        file_name= resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📩",EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - 📚   BSc in Mathematics - Universidade de Coimbra
    - 📚   MSc in Mathematics with specialization in Statistics, Optimization and Financial Math - Universidade de Coimbra
    - ⚽📊 ️Master in Big Data applied to Football - Universidad Católica San Antonio de Murcia
    - ⚽   Football Scout - Proscout
    """
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard skills")
st.write(
    """
    - 💻 Programming: Python, R, HTML, CSS
    - 📊 Data Visualization: Tableau, PowerBI, Matplotlib, Seaborn, Altair
    - 📚 Machine Learning, ETL processes
    - 💻 Databases: MySQL, BigQuery
    - 💻 Cloud: Google Cloud
    """
)

# --- WORK HISTORY ---
st.write('#')
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---

st.subheader("📈⚽ Data Analyst Intern | Sporting CP")
st.write('05/2022 - 07/2022')
st.write(
    """
    - ⚪ Participated in developing a machine learning model to help the club to decide to which clubs should lend their players. 
    - The goal of this model is minimize the risk of a player have an unsuccessful season in their next club, based on model aproximations of the team style of play and the player style of play.  
    """
)


# --- JOB 2 ---
st.write('#')
st.subheader("📈 Data Analyst Trainee | BNP Paribas")
st.write('09/2022 - 07/2023')
st.write('Internship with rotation on three different teams')
st.write(
    """
    - ⚪ As a member of the Digital team at Risk I2S, my responsibilities encompass the design and development of reporting and analytical features for monitoring counterparty risk.
       Additionally, I am involved in training users on new tools.
   
   - ⚪ As part of the Counterparty Metrics team, I participated in the analysis and production of counterparty metrics.
       
       Additionally, I worked on projects involving the automation of data processing and result production using Python, as well as the creation of Power BI dashboards.
    - ⚪ As a member of the Credit Risk Control team, my primary responsibilities included analyzing counterparty metric exposures that breaching limits and reporting on excesses.
    """

--- JOB 3 ---
st.write('#')
st.subheader("📈 Data Scientist Trainee | BPI AI Center of Excellence")
st.write('09/2023 - Present')
st.write(
)

# --- Projects & Articles ---
st.write("#")
st.subheader("Projects & Articles")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    
    
# --- CERTIFICATES ---
st.write("#")
st.subheader("Certificates - Online courses")
st.write("---")
for project, link in CERTIFICATES_ONLINE.items():
    st.write(f"[{project}]({link})")
    
    
st.write("#")
st.subheader("Certificates - Football")
st.write("No URLs associated.")
st.write("---")
for project, link in CERTIFICATES_FOOTBALL.items():
    st.write(f"[{project}]({link})")

