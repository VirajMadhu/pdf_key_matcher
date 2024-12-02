from utils.file_handler import extract_text_from_pdf, load_text_file
from utils.text_processor import preprocess_text
from utils.matcher import calculate_match_percentage

def main():
    print("Welcome to PDF Key Matcher!")
    
    # Load files
    file_text = extract_text_from_pdf("data/file.pdf")
    description = load_text_file("data/description.txt")
    
    # Preprocess text
    file_words = preprocess_text(file_text)
    description_words = preprocess_text(description)
    print(file_words)
    
    # Match keywords
    match_percentage, unmatched_keywords = calculate_match_percentage(file_words, description_words)
    
    # Display results
    print("\nMatch Percentage:")
    print(f"{match_percentage:.2f}%")
    print("\nUnmatched Keywords:")
    print(", ".join(unmatched_keywords))

if __name__ == "__main__":
    main()
