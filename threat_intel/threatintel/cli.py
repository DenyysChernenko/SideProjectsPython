import typer
from typing import Annotated
from rules.manager import cli_rule_add, cli_rules_list, cli_rule_remove

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
    
    
@app.command()
def rule_remove(rule_name: Annotated[str, typer.Argument()]):
    if cli_rule_remove(rule_name):
        typer.echo("Rule was deleted successfully")
        return
    typer.echo("Rule was not deleted -> because of an error or didn't find a rule to delete")


if __name__ == "__main__":
    app()
