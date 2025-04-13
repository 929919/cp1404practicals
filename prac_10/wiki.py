import wikipediaapi

def main():
    wiki = wikipediaapi.Wikipedia('en')  # inglês

    title = input("Enter page title: ").strip()
    while title != "":
        page = wiki.page(title)
        if not page.exists():
            print(f'Page id "{title}" does not match any pages. Try another id!\n')
        else:
            print(page.title)
            print(page.summary[:500])  # Mostra apenas os primeiros 500 caracteres
            print(page.fullurl)

        title = input("Enter page title: ").strip()

    print("Thank you.")

main()
