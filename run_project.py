import subprocess
import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent

scripts = [
    "database.py",
    "import_sales.py",
    "analysis.py",
    "sql_analysis.py",
    "dashboard.py"
]

for script in scripts:
    print(f"\nRunning {script}...", flush=True)

    subprocess.run(
        [sys.executable, script],
        cwd=project_folder,
        check=True
    )

print("\nFinished! Open dashboard.html to view your dashboard.")