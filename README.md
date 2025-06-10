# USA Real Estate Price Prediction

This project uses a machine learning model to predict real estate prices based on features like area.  
The model is deployed with Streamlit.

## Project Structure

- `usa_rea_estate.py`: Streamlit app to interact with the trained model
- `model/`: Folder containing the trained model (`model.pkl`) and Jupyter notebook
- `requirements.txt`: Python dependencies
- `.gitignore`: Files/folders to ignore in Git

## How to Run

```bash
pip install -r requirements.txt
streamlit run usa_rea_estate.py
