"""
Emails
Estimate: 20 minutes
Actual:
"""
def extract_name(email):
    """Extract a formatted name from the email address."""
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name
