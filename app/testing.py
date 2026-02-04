import time
from datetime import datetime
import random

from rich.live import Live
from rich.table import Table

while True:
    data = {
        "id": f"123",
        "name": f"dfg",
        "entry_time": f"342",
        "exit_time": f"asdf"
    }

    def generate_table() -> Table:
        """Make a new table."""
        table = Table()
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Entry Time")
        table.add_column("Exit Time")
        table.add_column("Date")
        
        table.add_row(
                str(data["id"]),
                data["name"],
                str(data["entry_time"]),
                str(data["exit_time"]),
                str(datetime.now().date())
            )

        return table


    with Live(generate_table(), refresh_per_second=4) as live:
        live.update(generate_table())

