import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_entities(entities, category):
    """
    Validates extracted entities based on citation type and predefined rules.

    Args:
        entities (dict): A dictionary of extracted entities (e.g., author, title, year).
        category (str): The category of the citation (e.g., "article", "book").

    Returns:
        list: A list of error messages. Returns an empty list if no errors are found.
    """
    errors = []

    # --- Year Validation ---
    if "year" in entities:
        try:
            year = int(entities["year"])
            if not (1800 <= year <= 2024):
                errors.append(f"Invalid year: {year}. Year should be between 1800 and 2024.")
        except ValueError:
            errors.append(f"Invalid year format: {entities['year']}. Year should be an integer.")

    # --- Category-Specific Validation ---
    if category == "article":
        if "author" not in entities or not entities["author"]:
            errors.append("Missing author for article.")
        if "title" not in entities or not entities["title"]:
            errors.append("Missing title for article.")
        if "journal" not in entities or not entities["journal"]:
            errors.append("Missing journal for article.")

    elif category == "book":
        if "author" not in entities or not entities["author"]:
            errors.append("Missing author for book.")
        if "title" not in entities or not entities["title"]:
            errors.append("Missing title for book.")
        if "publisher" not in entities or not entities["publisher"]:
            errors.append("Missing publisher for book.")

    # --- General Validation Rules ---
    if "title" in entities:
        if len(entities["title"]) < 5:
            errors.append("Title is too short.")
        if not entities["title"][0].isupper():
            errors.append("Title should start with a capital letter.")

    # Log errors if any
    if errors:
        logging.warning(f"Validation errors found for citation: {entities} - Errors: {errors}")

    return errors

