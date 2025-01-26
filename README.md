# Validation Module

This module provides functionality to validate extracted entities from citations. It ensures that the data conforms to predefined rules based on the citation type (e.g., article, book). The validation checks include year range validation, category-specific validation, and general validation rules.

## Usage

The `validate_entities` function is the main entry point for validation. It takes a dictionary of entities and the category of the citation as input and returns a list of error messages if any validation rules are violated.

```python
entities = {
    "author": "Doe, J.",
    "title": "Example Title",
    "year": "2023",
    "journal": "Journal of Information Science",
}
category = "article"

errors = validate_entities(entities, category)
if errors:
    print("Validation errors:", errors)
else:
    print("Validation passed.")
```

## Key Features
- **Year Validation**: Ensures the year is within a valid range (1800-2024).
- **Category-Specific Validation**: Checks for required fields based on the citation category (e.g., author, title, journal for articles).
- **General Validation Rules**: Includes checks such as title length and capitalization.

## Future Enhancements
- Extend validation rules for additional citation categories.
- Integrate with a database or API for dynamic rule updates.
- Provide more detailed error messages and suggestions for correction.

# Main Processing Script

This script serves as the central processing pipeline for citations. It integrates various modules to extract, validate, enrich, standardize, and store citations. The script demonstrates how to process a single citation through these steps and provides logging for each stage.

## Usage

The `process_citation` function is the main entry point for processing a citation. It takes a raw citation text as input and processes it through the pipeline. The script includes an example citation for demonstration purposes.

```python
citation_text = "Doe, J. (2022). A study of citations. Journal of Information Science, 10(2), 123-145."
process_citation(citation_text)
```

## Key Features
- **Integration with Modules**: Utilizes modules for entity extraction, validation, enrichment, standardization, and database storage.
- **Logging**: Provides detailed logging at each step for easy debugging and monitoring.
- **Error Handling**: Includes error handling to ensure smooth processing of citations.

## Future Enhancements
- Expand the pipeline to handle different citation categories dynamically.
- Implement parallel processing for handling multiple citations simultaneously.
- Integrate with a user interface for real-time citation processing.
