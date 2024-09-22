from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Rois-Céti.pdf"
profile_pic = current_dir / "assets" / "roisceti3.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Rois-Céti"
PAGE_ICON = ":wave:"
NAME = "Rois-Céti DIMBAMBA-LOUFOUA-CETIKOUABO"
DESCRIPTION = """
Actuaire Financier, Data Scientist, Ingenieur Statisticien Economiste (ISE)
"""
EMAIL = "rois.ceti@gmail.com"
SOCIAL_MEDIA = {
    "🤝 LinkedIn" : "https://www.linkedin.com/in/rdimbamba",
    "🐱 GitHub" : "https://github.com/rdimbamba",
    "🐦 Twitter / X" : "https://x.com/CetiRois"
}


st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide"
)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
PIC = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(PIC, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📧", EMAIL)

# --- SOCIAL LINKS ---
st.write("---")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

col1, col2 = st.columns([5, 2])

with col1:
    # --- FORMATIONS ---
    st.write("---")
    st.header("🎓 Formations")
    # --- Form 1 ---
    st.subheader("🏢 **Ingénieur Grande Ecole - Actuariat & Finance, Data Science**")
    st.write("📖", "Ecole Nationale de Statistique et d'Administration Economique (ENSAE)")
    st.write("📅 Septembre 2020 - Novembre 2022")
    st.write("📍", "Paris, France")
    st.write(
        """
        - ✔️ Statistique, Econométrie, Mathématiques financière et actuarielle, 
        Machine et Deep Learning, Actuariat-Vie, Actuariat-Non Vie, Risk Management, ...
        """
    )
    # --- Form 2 ---
    st.subheader("🏢 **Ingénieur Statisticien Economiste (ISE)**")
    st.write("📖", "Institut Sous-régionale de Statistique et d'Economie Appliquée (ISSEA)")
    st.write("📅 Septembre 2018 - Juillet 2020")
    st.write("📍", "Yaoundé, Cameroun")
    st.write(
        """
        - ✔️ Statistique, Econométrie, Analyse des données, Microéconomie, 
        Macroéconomie, Sondage, ...
        """
    )
    # --- Form 3 ---
    st.subheader("🏢 **Master II en Mathématiques**")
    st.write("📖", "Ecole Normale Supérieure (ENS) de l'Université Marien Ngouabi (UMNG)")
    st.write("📅 Octobre 2016 - Juillet 2018")
    st.write("📍", "Brazzaville, Congo")
    st.write(
        """
        - ✔️ Analyse fonctionnelle, Théorie des distributions, Statistique Inférentielle,
        Théorie des Probabilités, Processus Stochastique, ...
        """
    )
    # --- Form 4 ---
    st.subheader("🏢 **Licence en Mathématiques**")
    st.write("📖", "Ecole Normale Supérieure (ENS) de l'Université Marien Ngouabi (UMNG)")
    st.write("📅 Octobre 2013 - Juillet 2016")
    st.write("📍", "Brazzaville, Congo")
    st.write(
        """
        - ✔️ Dénombrement et Calcul des Probabilités, Analyse, Mesure et Intégration,
        Topologie, Algèbre, Géométrie, ...
        """
    )

    # --- EXPERIENCES & QUALIFICATIONS ---
    st.write("---")
    st.header("💼 Expérience Professionnelle")
    # --- Job 1 ---
    st.subheader("🏢 **Cadre Finance, Comptabilité et Gestion | SNPC Group, Projet UG**")
    st.write("📅 Août 2024 - À ce jour")
    st.write("📍", "Brazzaville, Congo")
    st.write(
        """
        - ✔️ Modélisation de la récupération des coûts (CAPEX, OPEX, etc) 
        dans les contrats de partage de production.
        - ✔️ Modélisation du partage de production (Cost Oil, Profit Oil, etc) 
        dans les contrats de partage de production.
        - ✔️ Automatisation de la restitution des données avec RShiny, Streamlit et VBA.
        - ✔️ Visualisation en vue du Reporting avec RShiny et Streamlit.
        """
    )
    # --- Job 2 ---
    st.subheader("🏢 **Actuaire Risque Vie | Abeille Assurances, Production Etude et Analyse Vie**")
    st.write("📅 Novembre 2022 - Mars 2023")
    st.write("📍", "Paris, France")
    st.write(
        """
        - ✔️ Modèle ALM (sous Prophet).
        - ✔️ Solvabilité II, pilier 1 : Calcul des métriques de risque (SCR, Own Funds, Cover Rate).
        - ✔️ Solvabilité II, pilier 2 : ORSA (Sensibilités Marché et Passif).
        - ✔️ Solvabilité II, pilier 3 : Reporting réglementaires (QRT).
        """
    )
    # --- Job 3 ---
    st.subheader("🏢 **Actuaire Risque Financier | Abeille Assurances, Fonction Actuarielle Finance**")
    st.write("📅 Octobre 2021 - Octobre 2022")
    st.write("📍", "Paris, France")
    st.write(
        """
        - ✔️ Risque de Crédit (Spread, Transition, Défaut).
        - ✔️ Calibration Crédit Spread Sovereign & Corporate.
        - ✔️ Calibration matrices de transition.
        - ✔️ Calibration surface T0.
        - ✔️ Calibration matrice de corrélation.
        """
    )
    # --- Job 4 ---
    st.subheader("🏢 **Data Scientist | Ethics and Boards**")
    st.write("📅 Juin 2021 - Octobre 2021")
    st.write("📍", "Paris, France")
    st.write(
        """
        - ✔️ Scoring de Gouvernance.
        - ✔️ Visualisation des données avec ggplot2.
        - ✔️ Automatisation des restitutions de données via une interface RShiny.
        - ✔️ Web-scraping avec rvest & RSelenium.
        """
    )

    # --- CERTIFICATIONS ---
    st.write("---")
    st.header("💻 Certifications")
    # --- Certif 1 ---
    st.subheader("🏢 **Certificat Liguaskill**")
    st.write("📖", "Test d'évaluation en Anglais de Cambridge")
    st.write("📅 Mars 2022")
    st.write(
        """
        - ✔️ Certificat de niveau B2 international en Anglais
        """
    )
    # --- Certif 2 ---
    st.subheader("🏢 **Data Science BootCamp Certificate**")
    st.write("📖", "HI!PARIS (HEC + IP-PARIS)")
    st.write("📅 Août 2021")
    st.write(
        """
        - ✔️ Un voyage de 5 jours dans un rôle de Data Scientist 
        pour mener à bien un projet complet sur la consommation 
        d'énergie des bâtiments, de la compréhension business à la
        préparation des données, l'exploration, la visualisation et 
        le déploiement du projet.
        """
    )

    # --- ENSEIGNEMENT ---
    st.write("---")
    st.header("🧑‍🏫 Expériences d'enseignement")
    # --- Exp 1 ---
    st.subheader("🏢 **Chargé de TDs d'Econométrie Informatique avec R**")
    st.write("📖", "Université Paris Descartes")
    st.write("📅 Octobre 2021 - Novembre 2021")
    st.write("📍", "Paris, France")
    st.write(
        """
        - ✔️ Donner des travaux dirigés déconométrie informatique 
        avec le language R et le logiciel RStudio, aux L3 de 
        l'université Paris Descartes.
        """
    )
    # --- Exp 2 ---
    st.subheader("🏢 **Tuteur Parkours**")
    st.write("📖", "Parkours")
    st.write("📅 Novembre 2020 - Mai 2021")
    st.write("📍", "Paris, France")
    st.write(
        """
        - ✔️ Faire des cours du soir de mise et remise à niveau,
        aux élèves de certains collèges et lycées Parisiens.
        """
    )
    # --- Exp 3 ---
    st.subheader("🏢 **Chargé de cours d'Analyse et d'Algèbre**")
    st.write("📖", """
            Prépa SConsulting, pour les concours des ESA 
            (ENSEA, ENSAE, ISSEA, ENEAM) et celui de l'IFORD
            """)
    st.write("📅 Octobre 2021 - Novembre 2021")
    st.write("📍", "Yaoundé, Cameroun")
    st.write(
        """
        - ✔️ Préparer les étudiants en licence ou master en 
        Analyse et Algèbre L2 et L3, pour affronter les concours
        des Ecoles de Statistiques Africaines (ESA) et celui de l'IFORD.
        """
    )
    # --- Exp 4 ---
    st.subheader("🏢 **Enseignant Stagiaire en classes de Terminale C & A**")
    st.write("📖", "Lycée d'enseignement général 'Chaminade'")
    st.write("📅 Février 2018 - Juin 2018")
    st.write("📍", "Brazzaville, Congo")
    # --- Exp 5 ---
    st.subheader("🏢 **Enseignant Stagiaire en classe de 3ème**")
    st.write("📖", "Collège d'enseignement général 'La Fraternité'")
    st.write("📅 Février 2016 - Juin 2016")
    st.write("📍", "Brazzaville, Congo")
    # --- Exp 6 ---
    st.subheader("🏢 **Enseignant Stagiaire en classe de 4ème**")
    st.write("📖", "Collège d'enseignement général 'La Fraternité'")
    st.write("📅 Février 2015 - Mars 2015")
    st.write("📍", "Brazzaville, Congo")

    # --- PROJETS ACADEMIQUES ---
    st.write("---")
    st.header("📁 Projets académiques")
    # --- Projet 1 ---
    st.subheader("🏢 **Projet d'approfondissement en finance et actuariat**")
    st.write("👨‍💻", "Language et Logiciels de travail : R sur RStudio, Python sur Jupyter")
    st.write("📅 2021 - 2022")
    st.write(
        """
        - ✔️ Thème : Modélisation des arbitrages sur des contrats multi-supports de GENERALI.
        """
    )
    # --- Projet 2 ---
    st.subheader("🏢 **Projet de statistique appliquée**")
    st.write("👨‍💻", "Language et Logiciels de travail : R sur RStudio")
    st.write("📅 Octobre 2020 - Janvier 2021")
    st.write(
        """
        - ✔️ Thème : Analyse de la performance thermique du parc de logements 
        français - Exploitation de la base de données de l'ADEME sur les diagnostics
        de performance énergétique (DPE).
        """
    )
    # --- Projet 3 ---
    st.subheader("🏢 **Projet du cours du language C++**")
    st.write("👨‍💻", "Language et Logiciels de travail : C++ sur Visual Studio Code")
    st.write("📅 Décembre 2020 - Janvier 2021")
    st.write(
        """
        - ✔️ Thème : Créer un programme pour déterminer le prix d'une option financière, 
        ainsi que la stratégie de réplication dans le modèle de Black-Scholes-Merton. 
        Dans la plupart des cas où les formules explicites ne s'appliquent pas, 
        on calculera ces prix par méthode de Monte-Carlo.
        """
    )
    # --- Projet 4 ---
    st.subheader("🏢 **Projet du cours d'économétrie des séries temporelles**")
    st.write("👨‍💻", "Language et Logiciels de travail : R sur RStudio")
    st.write("📅 Mai 2020 - Juin 2020")
    st.write(
        """
        - ✔️ Thème : Modélisation du processus générateur de l'indice harmonisé 
        de la production industrielle - branche d'activité « énergie » - du Bénin
        de 2014 à 2018 & Analyse des relations entre la croissance économique, 
        l'investissement et le commerce extérieur de la Sierra-Léone de 1970 à 2018.
        """
    )

with col2:
    st.write("---")
    st.header("📚 Compétences")
    st.write(
        """ 
        - ⭐ Suite Office, LaTeX
        - ⭐ R, Python, VBA
        - ⭐ C++, Stata, SAS
        """
    )
    st.write("---")
    st.header("🌍 Langues")
    st.write(
        """
        - ⭐ Français : Langue maternelle
        - ⭐ Anglais : Ecrit, lu, parlé moyennement
        """
    )