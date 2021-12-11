import streamlit as st
from PIL import Image
from pages.classify import machine_classification

def app():
    st.header("Image Classification for Batik ")
    st.text("Upload a batik Image for image classification")

    uploaded_file = st.file_uploader("Choose a batik image ...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded MRI.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label_index = machine_classification(image, 'model/modelBatikClassification_v2.0_a62va54.h5')
        
        label_list = ['Batik Bali', 'Batik Betawi', 'Batik Cendrawasih', 'Batik Dayak', 
                    'Batik Geblek Renteng', 'Batik Ikat Celup', 'Batik Insang', 'Batik Kawung', 
                    'Batik Lasem',  'Batik Megamendung', 'Batik Pala', 'Batik Parang', 
                    'Batik Poleng', 'Batik Sekar Jagad', 'Batik Tambal']
        
        st.write(label_list[label_index])