import typer

from bookstore.core.infrastructure.publisher import publish
from bookstore.modules.book_mgt.commands import CreateBook


def main():
    title = typer.prompt("What is the title of book?")
    first_name = typer.prompt("First name of author?")
    last_name = typer.prompt("Last name of author?")
    command = CreateBook(
        title=title,
        author_first_name=first_name,
        author_last_name=last_name,
    )
    publish(command)


if __name__ == "__main__":
    typer.run(main)
