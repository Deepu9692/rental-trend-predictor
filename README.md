
# Rental Trend Predictor

This project predicts future monthly rental prices using Linear Regression. It includes a Streamlit-based web application for interactive visualization and prediction.

## Features

- Uses mock rental data from 5 cities
- Predicts next month's rent using Linear Regression
- Visualizes trends using Matplotlib
- Streamlit app for web-based interface

---

## Dataset

Sample rental data (`rental_data.csv`) includes:
- `City`: City name
- `Month`: Numeric month (1 to 5)
- `Rent`: Monthly rent amount

---

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rental-trend-predictor.git
cd rental-trend-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App Locally
```bash
streamlit run app.py
```

The app will open in your browser at: `http://localhost:8501`

---

## Streamlit Deployment

1. Push your project to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click **"New App"** and connect your GitHub repo
4. Choose `app.py` as the main file
5. Click **Deploy**

---

## Files Included

- `app.py` – Streamlit web app
- `predictor.py` – Standalone script for model training
- `rental_data.csv` – Dataset
- `requirements.txt` – Dependencies
- `README.md` – Project documentation

---

## Sample Output

### Streamlit App Screenshot
> *You can add your screenshot here after deploying.*

---

## Author

L. Deepak Reddy – AI Project on Rental Trend Prediction

---

## License

This project is licensed under the MIT License.
