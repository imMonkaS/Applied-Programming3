import re


def read_correct_filename_from_console():
    while True:
        filename = input("Enter your html file: ")
        if 'html' not in filename:
            print("It should be an html file. Try again.")
            continue

        try:
            with open(filename):
                break
        except FileNotFoundError:
            print("Looks like this file was not found. Try again")

    return filename


def read_file(filename: str):
    text = ""
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    return text


def print_to_file(links: list, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        for link in links:
            f.write(link + '\n')


def find_links(text: str):
    regular_expression_pattern = r'<a[^>]* href="([^"]*)"[^>]*>'
    links = re.findall(regular_expression_pattern, text)
    return links


def main():
    filename = read_correct_filename_from_console()
    html_raw_text = read_file(filename)
    links = find_links(html_raw_text)
    print_to_file(links, "output.txt")
    print(*links, sep='\n')


if __name__ == "__main__":
    main()
