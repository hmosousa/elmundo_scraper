import argparse


def setup_parser() -> argparse.ArgumentParser:
    """Setup CLI parser."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--start_date",
        help="The date to start scrapping. Format: \"YYYY-MM-DD\""
    )

    parser.add_argument(
        "--end_date",
        help="The date to end scrapping. Format: \"YYYY-MM-DD\""
    )

    parser.add_argument(
        "--output_file",
        help="A .csv file name to store the scrapped news."
    )

    return parser
