"""Cliente de linha de comando para o motor PrintF."""
import argparse
import os
from pathlib import Path
import requests


def main():
    parser = argparse.ArgumentParser(description="Análise remota de STL pela PrintF")
    parser.add_argument("stl", type=Path)
    parser.add_argument("--printer", choices=["A1", "A1 Mini"], default="A1")
    parser.add_argument("--api-url", default=os.getenv("PRINTF_API_URL", "http://127.0.0.1:8000"))
    args = parser.parse_args()
    key = os.getenv("PRINTF_API_KEY")
    if not key:
        parser.error("Defina PRINTF_API_KEY antes de executar")
    if not args.stl.is_file() or args.stl.suffix.lower() != ".stl":
        parser.error("Forneça um arquivo .stl existente")
    with args.stl.open("rb") as f:
        response = requests.post(
            args.api_url.rstrip("/") + "/v1/analyze",
            headers={"X-API-Key": key},
            data={"printer": args.printer},
            files={"file": (args.stl.name, f, "application/octet-stream")},
            timeout=120,
        )
    response.raise_for_status()
    import json
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
