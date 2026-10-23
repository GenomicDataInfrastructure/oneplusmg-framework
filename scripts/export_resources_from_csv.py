#!/usr/bin/env python3
"""
Convert a CSV export of the 1+MG Framework Resource Library to Jekyll YAML.

Expected input:
- CSV exported from the Google Sheet tab "Resources"
- Header row containing field names such as resource_id, include_in_library, title, etc.
- If the CSV includes the two descriptive rows above the real header, use --header-row 3
- If you export only the table starting from the actual header row, use --header-row 1

By default the script:
- reads resources.csv
- assumes the real field names are on row 3
- exports only rows where include_in_library is TRUE
- preserves spreadsheet field names
- converts TRUE/FALSE fields to YAML booleans
- converts pipe-separated multi-value fields to YAML lists
- omits blank fields
- writes _data/resources.yml
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any

import yaml


DEFAULT_INPUT = "resources.csv"
DEFAULT_HEADER_ROW = 3
DEFAULT_OUTPUT = "_data/resources.yml"

BOOLEAN_FIELDS = {
    "include_in_library",
    "featured",
}

MULTI_VALUE_FIELDS = {
    "review_flags",
    "framework_topics",
    "audiences",
}

REQUIRED_WHEN_INCLUDED = {
    "resource_id",
    "title",
    "short_description",
    "framework_topics",
    "audiences",
    "resource_type",
    "framework_recommendation",
    "source_or_publisher",
    "resource_status",
    "access_url_1",
    "catalogue_owner",
    "last_checked",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert the 1+MG Resource Library CSV export to Jekyll YAML."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default=DEFAULT_INPUT,
        help='Input CSV file. Default: "resources.csv".',
    )
    parser.add_argument(
        "--header-row",
        type=int,
        default=DEFAULT_HEADER_ROW,
        help="1-based row containing field names. Default: 3.",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help='Output YAML path. Default: "_data/resources.yml".',
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if an included resource is missing a required field.",
    )
    return parser.parse_args()


def normalise_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value

    text = str(value).strip().lower()

    if text in {"true", "yes", "1"}:
        return True

    if text in {"false", "no", "0", ""}:
        return False

    raise ValueError(f"Unrecognised boolean value: {value!r}")


def split_pipe_values(value: Any) -> list[str]:
    return [
        part.strip()
        for part in str(value).split("|")
        if part.strip()
    ]


def clean_value(field: str, value: Any) -> Any:
    if value is None:
        return None

    if isinstance(value, str):
        value = value.strip()

    if value == "":
        return None

    if field in BOOLEAN_FIELDS:
        return normalise_bool(value)

    if field in MULTI_VALUE_FIELDS:
        values = split_pipe_values(value)
        return values or None

    return value


def read_csv(path: str, header_row: int) -> tuple[list[str], list[list[str]]]:
    csv_path = Path(path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {csv_path}")

    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))

    if len(rows) < header_row:
        raise RuntimeError(
            f"CSV has only {len(rows)} row(s), but --header-row is {header_row}."
        )

    headers = [cell.strip() for cell in rows[header_row - 1]]

    if "resource_id" not in headers:
        raise RuntimeError(
            f"Expected 'resource_id' on row {header_row}, but found: {headers}"
        )

    return headers, rows[header_row:]


def row_to_record(headers: list[str], row: list[str]) -> dict[str, Any]:
    padded = row + [""] * max(0, len(headers) - len(row))
    record: dict[str, Any] = {}

    for field, raw_value in zip(headers, padded):
        if not field:
            continue

        value = clean_value(field, raw_value)

        if value is not None:
            record[field] = value

    return record


def validate_record(record: dict[str, Any]) -> list[str]:
    return [
        field
        for field in sorted(REQUIRED_WHEN_INCLUDED)
        if field not in record or record[field] in (None, "", [])
    ]


def export_resources(
    headers: list[str],
    rows: list[list[str]],
    header_row: int,
    strict: bool = False,
) -> list[dict[str, Any]]:
    resources: list[dict[str, Any]] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()

    for csv_row_number, row in enumerate(rows, start=header_row + 1):
        record = row_to_record(headers, row)

        if not record:
            continue

        resource_id = record.get("resource_id")

        if not resource_id:
            continue

        try:
            include = normalise_bool(record.get("include_in_library", False))
        except ValueError as exc:
            raise ValueError(
                f"CSV row {csv_row_number} ({resource_id}): {exc}"
            ) from exc

        if not include:
            continue

        resource_id = str(resource_id)

        if resource_id in seen_ids:
            raise ValueError(
                f"Duplicate resource_id {resource_id!r} at CSV row {csv_row_number}"
            )

        seen_ids.add(resource_id)

        missing = validate_record(record)

        if missing:
            message = (
                f"CSV row {csv_row_number} ({resource_id}) is included "
                f"but missing required field(s): {', '.join(missing)}"
            )

            if strict:
                raise ValueError(message)

            warnings.append(message)

        resources.append(record)

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    return resources


def write_yaml(resources: list[dict[str, Any]], output_path: str, source_csv: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    generated_header = (
        "# AUTO-GENERATED FILE - DO NOT EDIT BY HAND\n"
        f"# Source CSV: {Path(source_csv).name}\n"
        "# Generated from rows where include_in_library = TRUE.\n\n"
    )

    yaml_text = yaml.safe_dump(
        resources,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=1000,
    )

    path.write_text(generated_header + yaml_text, encoding="utf-8")


def main() -> int:
    args = parse_args()

    headers, rows = read_csv(
        path=args.input,
        header_row=args.header_row,
    )

    resources = export_resources(
        headers=headers,
        rows=rows,
        header_row=args.header_row,
        strict=args.strict,
    )

    write_yaml(
        resources=resources,
        output_path=args.output,
        source_csv=args.input,
    )

    print(f"Exported {len(resources)} resources to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
