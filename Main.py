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
            f.write(str(link + '\n'))


def find_links(text: str):
    find_links_pattern = r'<a[^>]* href="([^"]*)"'
    links = re.findall(find_links_pattern, text)
    return links


def main():
    validate_link_pattern = r"(https|http|ftp)://([a-zA-Z0-9-]{0,63}?\.?[a-zA-Z0-9-]{2,63}\.[a-zA-Z0-9]{2,63})(/?[a-zA-Zа-яА-Я0-9$_.+! *'\(\),-]{0,2048})"
    find_local_links_pattern = r"([a-zA-Zа-яА-Я0-9$_.+! *'\(\),/-]{1,2048})"

    filename = read_correct_filename_from_console()
    html_raw_text = read_file(filename)
    links = find_links(html_raw_text)

    valid_links = []
    for link in links:
        if re.match(validate_link_pattern, link):
            valid_links.append(link)

    for link in valid_links:
        if link in links:
            links.remove(link)

    local_links = []
    for link in links:
        if re.match(find_local_links_pattern, link):
            local_links.append(link)

    for link in local_links:
        if link in links:
            links.remove(link)

    print("valid_links:", *valid_links, sep='\n')
    print()
    print("local_links:", *local_links, sep='\n')
    print()
    print("other_links:", *links, sep='\n')

    print_to_file(valid_links, "valid_links.txt")
    print_to_file(local_links, "local_links.txt")
    print_to_file(links, "other_links.txt")


if __name__ == "__main__":
    main()
