"""Command-line interface for harbor management."""

import click
from colorama import init

from .ships import ShipManager
from .security import SecurityScanner

init(autoreset=True)

ship_manager = ShipManager()
security_scanner = SecurityScanner()


@click.group()
def main():
    """Harbor Management System CLI."""
    pass


@main.group()
def ships():
    """Manage ships in the harbor."""
    pass


@ships.command()
def list():
    """List all ships."""
    all_ships = ship_manager.list_ships()
    if not all_ships:
        click.echo("No ships registered.")
        return
    
    click.echo("Ships in Harbor:")
    for ship in all_ships:
        click.echo(f"  - {ship.name} ({ship.imo_number}) [{ship.status}]")


@main.group()
def security():
    """Security scanning operations."""
    pass


@security.command()
@click.argument('ship_imo')
def scan(ship_imo):
    """Run security scan for a ship."""
    click.echo(f"Running security scan for {ship_imo}...")
    results = security_scanner.run_compliance_scan(ship_imo)
    passed = sum(1 for r in results if r.passed)
    click.echo(f"Scan complete: {passed}/{len(results)} checks passed")


if __name__ == "__main__":
    main()
