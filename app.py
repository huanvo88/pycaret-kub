from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('churn_best_1')
threshold = 0.5 #set the threshold to be 0.5

##################################################################

def predict(model, input_df):
    prediction_df = predict_model(estimator=model, data = input_df)
    predictions = prediction_df['Label'][0]
    #predictions = (predictions > threshold)
    return predictions

def run():

    from PIL import Image
    image = Image.open('logo.png')

    st.image(image, use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?",
        ("Online", "Batch")
    )

    st.sidebar.info("This app is created to predict customer churn")
    st.sidebar.success('https://www.pycaret.org')

    st.title("Customer Churn Prediction App")

    if add_selectbox == 'Online':
        gender = st.selectbox("Gender", ("Male", "Female"))
        senior = st.selectbox("Senior Citizen", (True, False))
        if senior:
            senior = 1
        else:
            senior = 0
        partner = st.selectbox("Has Partner", (True, False))
        dependents = st.selectbox("Has Dependents", (True, False))
        tenure = st.slider("Tenure", 0, 100)
        phone = st.selectbox("Phone Service", (True, False))
        mult = st.selectbox("Multiple Lines", ('No', 'Yes', 'No phone service'))
        internet = st.selectbox("Internet Service", ("Fiber optic", "DSL", "No"))
        sec = st.selectbox("Online Security", ("No", "Yes", "No internet service"))
        backup = st.selectbox("Online Backup", ("No", "Yes", "No internet service"))
        protection = st.selectbox("Online Protection", ("No", "Yes", "No internet service"))
        support = st.selectbox("Tech Support", ("No", "Yes", "No internet service"))
        tv = st.selectbox("Streaming TV", ("No", "Yes", "No internet service"))
        movies = st.selectbox("Streaming Movies", ("No", "Yes", "No internet service"))
        contract = st.selectbox("Contract", ("Month-to-month", "Two year", "One year"))
        paperless = st.selectbox("Paperless Billing", (True, False))
        payment = st.selectbox("Payment Method", ("Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"))
        monthly = st.slider("Monthly Charges", 10, 200)
        total = st.slider("Total Charges", 10, 10000)

        input_dict = {'gender': gender,
                      'SeniorCitizen': senior,
                      'Partner': partner,
                      'Dependents': dependents,
                      'tenure': tenure,
                      'PhoneService': phone,
                      'MultipleLines': mult,
                      'InternetService': internet,
                      'OnlineSecurity': sec,
                      'OnlineBackup': backup,
                      'DeviceProtection': protection,
                      'TechSupport': support,
                      'StreamingTV': tv,
                      'StreamingMovies': movies,
                      'Contract': contract,
                      'PaperlessBilling': paperless,
                      'PaymentMethod': payment,
                      'MonthlyCharges': monthly,
                      'TotalCharges': total
        }

        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            st.success(f'Will the customer churn? {output}')

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type = ["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            prediction_df = predict_model(estimator=model, data = data)
            prediction_df.rename(columns = {'Label': 'Churn'}, inplace = True)
            prediction_df.drop('Score', axis = 1, inplace = True)
            st.write(prediction_df)


if __name__ == '__main__':
    run()


