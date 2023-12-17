import streamlit as st

# Titre de l'application
st.title("Real Time Bike Project")

# Image de Kibana
kibana_image = 'C:/Users/User/Desktop/INDP3_AIM/Big Data/kibana.png'
st.image(kibana_image, caption='Kibana', use_column_width=True)

# Bouton pour Kibana
if st.button("Accéder à Kibana"):
    st.write("Redirection vers http://localhost:5601")

# Saut de ligne pour la mise en forme
st.write("\n")

# Image de Hive
hive_image = 'C:/Users/User/Desktop/INDP3_AIM/Big Data/hive.png'
st.image(hive_image, caption='Hive', use_column_width=True)

# Bouton pour Hive
if st.button("Accéder à Hive"):
    st.write("Redirection vers http://localhost:50070")

# Saut de ligne pour la mise en forme
st.write("\n")

# Bouton pour afficher l'architecture du projet
if st.button("Afficher l'architecture du projet"):
    project_architecture_image = 'C:/Users/User/Desktop/INDP3_AIM/Big Data/pipline.png'
    st.image(project_architecture_image, caption='Architecture du projet', use_column_width=True)
