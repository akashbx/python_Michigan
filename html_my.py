def generate_html_content(values):
    html_lines = ['<html>']
    font_sizes = [60, 36, 36, 28, 28, 28, 28]

    for i in range(len(values)):
        line = (
            '<P CLASS="western" ALIGN=CENTER STYLE="margin-top: 0.08in; margin-bottom: 0.25in">'
            f'<FONT SIZE=7 STYLE="font-size: {font_sizes[i]}pt"> {values[i]}</FONT></P>'
        )
        html_lines.append(line)

    html_lines.append('</html>')
    return '\n'.join(html_lines)


def main():
    import csv

    filename = input("Enter CSV filename: ")

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) != 7:
                    print(f"Skipping invalid row: {row}")
                    continue

                name_parts = row[0].split()
                last_name = name_parts[-1] if name_parts else "output"
                html_filename = f"{last_name}.html"

                html_content = generate_html_content(row)

                with open(html_filename, 'w', encoding='utf-8') as outfile:
                    outfile.write(html_content)

                print(f"Created file: {html_filename}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
