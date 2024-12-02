# For comparing arrays and calculating matches
def calculate_match_percentage(file_words, description_words):
    file_set = set(file_words)
    desc_set = set(description_words)

    # Find matches
    matches = file_set.intersection(desc_set)
    unmatched = desc_set.difference(file_set)

    # Calculate percentage
    match_percentage = (len(matches) / len(desc_set)) * 100 if desc_set else 0

    return match_percentage, list(matches),  list(unmatched)
