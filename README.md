# 📈 Bank Loan Prediction

This project aims to predict the approval of bank loans based on various input parameters. The prediction model is built using machine learning techniques and can be deployed as a web application.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 🛠️ Prerequisites

- Python 3.8
- Conda package manager

### 📥 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/bank-loan-prediction.git
    cd bank-loan-prediction
    ```

2. **Create and activate a new conda environment:**

    ```bash
    conda create -n bank_loan python=3.8 -y
    conda activate bank_loan
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### ▶️ Running the Application

1. **Set the necessary environment variables:**

    ```bash
    export MONGODB_URL="mongodburl"
    export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
    export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
    ```

2. **Run the application:**

    ```bash
    python app.py
    ```

## 🗂️ Project Structure

The project is organized into the following directories:

- **constant**: Contains constant values used throughout the project.
- **config_entity**: Configuration settings and entities.
- **artifact_entity**: Handles artifacts generated during the machine learning pipeline.
- **component**: Core components of the machine learning pipeline.
- **pipeline**: Manages the execution flow of the machine learning process.
- **app.py / demo.py**: Main application scripts for running the web server and demonstration purposes.

## 💻 Git Commands

Use the following commands to manage your version control with Git:

```bash
git add .
git commit -m "Updated"
git push origin main
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to replace the repository URL and other placeholders (like MongoDB credentials) with actual values relevant to your project.
