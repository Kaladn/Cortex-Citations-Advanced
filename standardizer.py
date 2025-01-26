import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def standardize_citation(entities, category):
    """
    Standardizes citation entries based on category and extracted entities.

    Args:
        entities (dict): A dictionary of extracted entities (e.g., author, title, year).
        category (str): The category of the citation (e.g., "article", "book").

    Returns:
        str: A standardized citation string.
    """
    try:
        if category == "article":
            standardized = f"{entities['author']} ({entities['year']}). {entities['title']}. {entities['journal']}."
        elif category == "book":
            standardized = f"{entities['author']} ({entities['year']}). {entities['title']}. {entities['publisher']}."
        else:
            standardized = f"{entities['author']} ({entities['year']}). {entities['title']}."
        
        logging.info(f"Standardized Citation: {standardized}")
        return standardized

    except KeyError as e:
        logging.error(f"Missing key in entities for standardization: {e}")
        return ""

if __name__ == "__main__":
    # Example Usage
    entities_article = {
        "author": "Doe, J. and Smith, A.",
        "title": "The Impact of AI on Society",
        "year": "2022",
        "journal": "Journal of Artificial Intelligence"
    }
    category_article = "article"

    entities_book = {
        "author": "Jones, M.",
        "title": "A History of the Internet",
        "year": "2021",
        "publisher": "Tech Publishers"
    }
    category_book = "book"

    # Standardize citations
    standardized_article = standardize_citation(entities_article, category_article)
    standardized_book = standardize_citation(entities_book, category_book)

    print(f"Standardized Article Citation: {standardized_article}")
    print(f"Standardized Book Citation: {standardized_book}")
