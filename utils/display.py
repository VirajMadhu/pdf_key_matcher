from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import pyfiglet

def display_heading(title: str, console: Console):
    """Display a large ASCII heading."""
    heading = pyfiglet.figlet_format(title)
    console.print(f"[bold blue]{heading}[/bold blue]")

def display_results(match_percentage: float, matched_keywords: list, unmatched_keywords: list, console: Console):
    """Display the match percentage and initiate table pagination."""
    console.rule("[bold green]Results[/bold green]")
    console.print(Panel(f"[bold cyan]Match Percentage:[/bold cyan] [bold magenta]{match_percentage:.2f}%[/bold magenta]", style="green"))

    if matched_keywords or unmatched_keywords:
        display_table_paginated(matched_keywords, unmatched_keywords, console, page_size=10)
    else:
        console.print("[bold red]No keywords found to display.[/bold red]")

def display_table_paginated(matched_keywords: list, unmatched_keywords: list, console: Console, page_size=10):
    """Display the table with pagination."""
    total_rows = max(len(matched_keywords), len(unmatched_keywords))
    current_page = 0

    while True:
        # Create table
        keywords_table = Table(title="Keyword Match Analysis (Page {}/{})".format(
            current_page + 1, (total_rows // page_size) + (1 if total_rows % page_size else 0)), style="blue")
        keywords_table.add_column("Matched Keywords", justify="center", style="green", no_wrap=True)
        keywords_table.add_column("Unmatched Keywords", justify="center", style="red", no_wrap=True)

        # Add rows for the current page
        start_index = current_page * page_size
        end_index = min(start_index + page_size, total_rows)
        for i in range(start_index, end_index):
            matched = matched_keywords[i] if i < len(matched_keywords) else ""
            unmatched = unmatched_keywords[i] if i < len(unmatched_keywords) else ""
            keywords_table.add_row(matched, unmatched)

        console.print(keywords_table)

        # Display navigation instructions
        console.print("\n[bold cyan]Navigation:[/bold cyan] [green]n[/green] - Next Page | [red]p[/red] - Previous Page | [yellow]q[/yellow] - Quit")

        choice = console.input("[bold magenta]Enter your choice (default: n):[/bold magenta] ").strip().lower() or "n"
        if choice == "n" or choice == "" and end_index < total_rows:
            current_page += 1
        elif choice == "p" and current_page > 0:
            current_page -= 1
        elif choice == "q":
            break
        else:
            console.print("[bold red]Invalid input![/bold red] Please try again.")


def display_ending(title: str, console: Console):
    """Display the end message"""
    console.rule(f"[bold green]{title}[/bold green]")