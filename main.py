from utils.file_handler import extract_text_from_pdf, load_text_file
from utils.text_processor import preprocess_text
from utils.matcher import calculate_match_percentage
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def main():
    console.rule("[bold blue]PDF Key Matcher[/bold blue]")
    
    # Load files
    console.print("\n[bold yellow]Loading files...[/bold yellow]")
    file_text = extract_text_from_pdf("data/file.pdf")
    description = load_text_file("data/description.txt")
    
    # Preprocess text
    console.print("[bold yellow]Processing text...[/bold yellow]")
    file_words = preprocess_text(file_text)
    description_words = preprocess_text(description)
    
    # Match keywords
    console.print("[bold yellow]Analyzing keywords...[/bold yellow]")
    match_percentage, matched_keywords, unmatched_keywords = calculate_match_percentage(file_words, description_words)
    
    # Display results
    console.rule("[bold green]Results[/bold green]")
    
    # Display match percentage
    console.print(f"[bold cyan]Match Percentage:[/bold cyan] [bold magenta]{match_percentage:.2f}%[/bold magenta]")
    
    # Combined table for matched and unmatched keywords
    keywords_table = Table(title="Keyword Match Analysis", style="blue")
    keywords_table.add_column("Matched Keywords", justify="center", style="green", no_wrap=True)
    keywords_table.add_column("Unmatched Keywords", justify="center", style="red", no_wrap=True)
    
    # Populate table
    max_length = max(len(matched_keywords), len(unmatched_keywords))
    for i in range(max_length):
        matched = matched_keywords[i] if i < len(matched_keywords) else ""
        unmatched = unmatched_keywords[i] if i < len(unmatched_keywords) else ""
        keywords_table.add_row(matched, unmatched)
    
    console.print(keywords_table)
    console.print(Panel("[bold green]Thank you for using PDF Key Matcher![/bold green]"))
    console.rule()

if __name__ == "__main__":
    main()
