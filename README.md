# DeepLearning-LSTM-WebApp-CpG-Detector-DNA-Sequences
The project requires you to build a neural network to count the number of CpGs (consecutive CGs) in given DNA (of N, A, C, G, T) sequences. Example, given “NCACANNTNCGGAGGCGNA”, the corrected output should be 2.
# 🧬 DNA Sequence Predictor Web App

This project provides a **web interface** for testing two pre-trained **PyTorch LSTM models** on DNA sequence data. It includes both a **Streamlit** and a **Flask** implementation for UI interaction.

---

## 📂 Project Structure

dna/
├── flask_app/
│ ├── app.py # Flask web server
│ ├── model_utils.py # Common model loading and inference functions
│ ├── static/ # (Optional) Static files (CSS, JS, etc.)
│ └── templates/
│ └── index.html # Flask HTML template
├── streamlit_app/
│ └── app.py # Streamlit app
├── models/
│ ├── 128dim_model.pt # Model for fixed-length sequences
│ └── 128dim_padding_model.pt# Model for variable-length sequences
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DS-Nikhil-AI/DeepLearning-LSTM-WebApp-CpG-Detector-DNA-Sequences.git
   cd dna
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Flask Web App
   ```bash
   cd flask_app
   python app.py
   ```
4. Run Streamlit Web App

   ```bash
   cd streamlit_app
   streamlit run app.py
   ```

   Open your browser at: http://127.0.0.1:5000

   Enter a DNA sequence like NCACANNTNCGGAGGCGNA
   Choose between:

   Fixed-Length (No Padding) — Uses 128dim_model.pt
   Variable-Length (With Padding) — Uses 128dim_padding_model.pt

   Choose the model type and submit

   Result will be displayed on the page

🧠 Model Details

    Model File Type Notes
    128dim_model.pt Fixed-Length Input DNA sequences of fixed size
    128dim_padding_model.pt Variable-Length (Padded) Handles variable lengths w/ padding

    Both models are implemented using PyTorch LSTM layers and expect encoded DNA sequences.

⚙️ How It Works

    Encoding: A, C, G, T, N → 0, 1, 2, 3, 4

    Padding (optional): Pads shorter sequences to a maximum length

    Model Inference: Loaded using torch.load() and run in eval() mode

✅ Requirements

    Python 3.7+

    PyTorch 2.7.0

    Flask 3.1.1

    Streamlit 1.45.1

📌 Notes

    Ensure model files (.pt) are placed in the /models/ directory

    Update max_len in model_utils.py if using different sequence lengths

📄 License

    MIT License – feel free to use, modify, and share.

🙋‍♂️ Contact

    For questions or collaboration, open an issue or contact the maintainer.

    ---

    Let me know if you'd like to include screenshots or add instructions for Docker deployment or hosting on platforms like Heroku or Streamlit Cloud.

    ---

