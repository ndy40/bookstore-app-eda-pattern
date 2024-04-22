from pathlib import Path

import typer

import sys

path = Path().joinpath().joinpath('..')
sys.path.append(str(path))


from bookstore.modules.book_mgt.services.create_new_book import create_new_book


def main():
    title = typer.prompt("What is the title of book?")
    first_name_author = typer.prompt("First name of author?")
    last_name_author = typer.prompt("Last name of author?")
    create_new_book(title, first_name_author, last_name_author)


if __name__ == "__main__":
    typer.run(main)




