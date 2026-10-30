def format_inr(value):
    """
    Format a value as Indian Rupees.
    """

    if value is None:
        return "₹0"

    return f"₹{value:,.0f}"


def format_lakhs(value):
    """
    Convert an INR value into Lakhs and format it.
    """

    if value is None:
        return "₹0 L"

    return f"₹{value / 100000:,.2f} L"


def format_number(value):
    """
    Format a numeric value with comma separators.
    """

    if value is None:
        return "0"

    return f"{value:,.0f}"


def format_decimal(value):
    """
    Format a numeric value with two decimal places.
    """

    if value is None:
        return "0.00"

    return f"{value:,.2f}"


def format_area(value):
    """
    Format area in square feet.
    """

    if value is None:
        return "0 sq.ft"

    return f"{value:,.0f} sq.ft"