from utils.file_handler import extract_text_from_pdf, load_text_file
from utils.text_processor import preprocess_text
from utils.matcher import calculate_match_percentage
from utils.display import display_heading, display_results, display_ending
from rich.console import Console

console = Console()

def main():
    # Display heading
    display_heading("PDF Key Matcher", console)

    try:
        # Load and preprocess files
        console.print("\n[bold yellow]Loading files...[/bold yellow]")
        file_text = extract_text_from_pdf("data/file.pdf")
        description = load_text_file("data/description.txt")
        
        console.print("[bold yellow]Processing text...[/bold yellow]")
        file_words = preprocess_text(file_text)
        description_words = preprocess_text(description)

        # Check if files are empty
        if not file_words:
            console.print("[bold red]Error: 'data/file.pdf' is missing or empty.[/bold red]")
            return
        if not description_words:
            console.print("[bold red]Error: 'data/description.txt' is missing or empty.[/bold red]")
            return

    except FileNotFoundError as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        return

    match_percentage, matched_keywords, unmatched_keywords = calculate_match_percentage(file_words, description_words)

    display_results(match_percentage, matched_keywords, unmatched_keywords, console)
    
    display_ending("Thank you for using PDF Key Matcher!", console)

if __name__ == "__main__":
    main()
