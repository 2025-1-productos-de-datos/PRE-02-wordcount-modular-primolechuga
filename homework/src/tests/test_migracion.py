import os
import subprocess


def test_migracion():

    result = subprocess.run(
        ["python", "-m", "homework", "data/input", "data/output"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Error en la ejecución: {result.stderr}"


    if not os.path.exists("data/output/wordcount.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe.")


    results = {}
    with open("data/output/wordcount.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        results[key] = value

    assert results.get("computational", 0) == "3"
    assert results.get("analytics", 0) == "5"