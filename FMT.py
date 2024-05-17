def fmt_text(text):
    lines = text.split('\n')
    formatted_lines = []
    current_line = ""
    for line in lines:
        words = line.split()
        for word in words:
            if len(current_line) + len(word) <= 72:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
            else:
                formatted_lines.append(current_line)
                current_line = word
        if current_line:
            formatted_lines.append(current_line)
            current_line = ""
    return "\n".join(formatted_lines)

# Sample text
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""

# Format and print the text
formatted_text = fmt_text(text)
print(formatted_text)
