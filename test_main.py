"""
Test goes here

"""

from mylib.calculator import add
from click.testing import CliRunner
from main import add_cli


def test_add():
    assert add(1, 2) == 3


def test_help():
    """Tests the command-line interface help message."""
    runner = CliRunner()
    result = runner.invoke(add_cli, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


# write a test for the add_cli function that calls the add_cli function with the arguments 1 and 2 and checks that the output is 3.

def test_add_cli():
    """Tests the add_cli command-line interface for adding two numbers."""
    runner = CliRunner()

    # Test adding two positive integers
    result = runner.invoke(add_cli, ["3", "4"])
    assert result.exit_code == 0
    assert "7" in result.output  # Output should be the result of 3 + 4

    
    # Test with zero
    result = runner.invoke(add_cli, ["0", "5"])
    print(result.output)  # Print output for debugging
    assert result.exit_code == 0
    assert "5" in result.output  # Output should be 0 + 5
