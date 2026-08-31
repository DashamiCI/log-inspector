def is_valid_email(email):
    """Return True when the email has a basic valid format."""
    return "@" in email and "." in email.split("@")[-1
