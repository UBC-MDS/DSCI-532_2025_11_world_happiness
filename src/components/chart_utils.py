def split_label(label):
    """Splits label into two lines based on space count and total length."""
    if len(label) <= 15:
        return label  # No split needed
    
    spaces = [i for i, char in enumerate(label) if char == " "]  # Find space positions
    
    if len(spaces) >= 1:  # Only split if there's at least one space
        split_index = spaces[min(len(spaces) // 2, len(spaces) - 1)]  # Choose split point
        return label[:split_index] + "<br>" + label[split_index + 1:]  # Insert line break

    return label  # Return original if no spaces exist

def convert_legend(label):
    """Inserts zero-width space (\u200B) in country names for legend wrapping."""
    return label.replace(" ", "\u200B ")