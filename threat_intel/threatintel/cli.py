import typer
from typing import Annotated
from rules.manager import cli_rule_add, cli_rules_list

app = typer.Typer()


@app.command()
def rule_add(file_path: Annotated[str, typer.Argument()]):
    if cli_rule_add(file_path):
        typer.echo("Rule was added successfully")
        return
    typer.echo("Rule was not added koz of an error")


@app.command()
def rules_list():
    cli_rules_list()


if __name__ == "__main__":
    app()
