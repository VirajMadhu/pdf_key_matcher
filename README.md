# PDF Key Matcher

**PDF Key Matcher** is an open-source, terminal-based application designed to analyze and compare text from PDF files with a description text file. This tool is especially useful for tailoring CVs to match job descriptions, helping users identify keyword matches and gaps.

---

## 🚀 Features

- **PDF Text Extraction**: Extract text directly from PDF files (e.g., CVs).
- **Description File Support**: Load comparison descriptions from plain text files.
- **Text Preprocessing**: Includes case conversion, special character removal, and stop-word filtering.
- **Keyword Matching**: Compare PDF content with the description and calculate matching percentages.
- **Unmatched Keywords**: Identify keywords in the description that are missing from the PDF.
- **Terminal-Friendly Output**: Visualize results directly in the terminal.
- **Clean and Modular Design**: Easily extensible and maintainable code structure.

---

## 🛠️ Project Structure

```plaintext
pdf_key_matcher/
├── main.py              # Entry point of the app
├── utils/
│   ├── file_handler.py  # Handles file upload and text extraction
│   ├── text_processor.py # Text cleaning, preprocessing, and tokenization
│   ├── matcher.py       # Performs keyword comparison
│   ├── display.py       # Display outputs in User friendly way
├── data/
│   ├── file.pdf         # Example PDF file (e.g., CV)
│   ├── description.txt  # Example description file (e.g., job description)
├── venv/                # Virtual environment directory
├── .gitignore
├── README.md
├── LICENSE
└── requirements.txt     # Required Python libraries
```

## 🧰 Requirements
- Python 3.8 or higher
- Dependencies
    - PyMuPDF (pymupdf) for PDF text extraction.
    - ```re``` for text preprocessing and pattern matching.


## 🖥️ How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pdf-key-matcher.git
cd pdf_key_matcher
```

### 2. Set Up the Virtual Environment
Activate a virtual environment to keep dependencies isolated:

- For Linux/Mac Users
```bash
python -m venv venv
source venv/bin/activate
```

- For Windows Users
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 4. Add Your Files
Place your PDF file (e.g., CV) and the description file (e.g., job description) in the data/ folder:
- Example CV file: data/file.pdf
- Example description: data/description.txt

**NOTE :** pdf file name should be **file.pdf** and text file should be **description.txt**. Using Other names will not work unless you change the code.

### 5. Run the Application
```bash
python main.py
```

## 📂 Example Usage
Input:
- PDF File Content:
```plaintext
Python developer with experience in Django, and SQL.
```

- Description File Content:
```plaintext
Looking for a Python developer skilled in Flask, Django and SQL.
```

Output:
```plaintext
Match Percentage:
75.00%

Unmatched Keywords:
flask
```

- Sample output screenshots
  ![image](https://github.com/user-attachments/assets/540c755b-54dd-45f7-ac18-6afe0ad3b4b6)
  ![image](https://github.com/user-attachments/assets/31889746-ae82-45d4-a04f-606d0a26e076)


## 🌟 Contribution
Contributions are welcome! To get started:

### 1. Fork the repository.
### 2. Create a feature branch:
```bash
git checkout -b feature-name
```
### 3. Commit your changes:
```bash
git commit -m "Add a new feature"
```
### 4. Push to your branch:
```bash
git push origin feature-name
```
### 5. Open a Pull Request.


## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/VirajMadhu/pdf_key_matcher/blob/main/LICENSE) file for more details.
