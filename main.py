import streamlit as st 
import os 
import joblib 


def get_base_dir():
    return os.path.dirname(os.path.abspath(__file__))

@st.cache_resource()
def get_models():
    dir =get_base_dir()
    model = joblib.load(os.path.join(dir,'models','model.pkl'))
    encoder = joblib.load(os.path.join(dir,'models','encoder.pkl'))
    scaler = joblib.load(os.path.join(dir,'models','scaler.pkl'))
 
    return model,encoder,scaler

def predict(tsa,sae,go,fcs,pf,sf,das):
    model,encoder,scaler=get_models()
    sf_code=[0,1]if sf=='yes' else [1,0] 
    das_code= [0,1]if das=='yes' else [1,0]
    features =scaler.transform( [[tsa,sae,go,fcs,pf]+sf_code+das_code])
    print(features)
    pred= model.predict(features)
    prob = model.predict_proba(features)[0][pred[0]]
    prediction =encoder.inverse_transform(pred)[0]

    return pred[0],prob,prediction
    


st.title("Personality Prediction based on machine Learning algorithme")
st.markdown("#### this is a demo application that predict Personality  based on caple of features by using machine learning algorithme")

st.write("")
st.write("")
st.text("fill the boxes and submit to get the answer .")
st.write("")
with st.form('form') :

    tsa = st.number_input("Hours spent alone : ",min_value=0,max_value=24,step=1)
    sae = st.number_input('Frequency of attending social events : ',min_value=0,step=1)
    go = st.number_input('Frequency of going outside : ',min_value=0,max_value=24,step=1)
    fcs = st.number_input('Size of Frends social circle : ',min_value=0,step=1)
    pf = st.number_input('Social media post frequency : ',min_value=0,step=1)
    sf = st.selectbox("Fear of performing on stage : ",options=['yes','no'])
    das = st.selectbox("Feeling drained post-socializing : ",options=['yes','no'])

    submitted = st.form_submit_button("Submit")
    if submitted:
        args = {
            "tsa":tsa,"sae":sae,'go':go,'fcs':fcs,'pf':pf,'sf':sf,'das':das
        }
        st.write("🧾 Input Summary:", args)
        
        idx,probability,prediction=predict(**args)
        
             
        with st.status("Prediction Result", expanded=False) as status:
            if idx:
                st.error(prediction)
                st.metric("Prediction Confidence", f"{probability:.2%}")
            else:
                st.success(prediction)
                st.metric("Prediction Confidence", f"{probability:.2%}")

            status.update(label="Prediction completed", state="complete", expanded=True)

        

