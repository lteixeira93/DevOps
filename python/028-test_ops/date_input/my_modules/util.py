from datetime import datetime


def util(input_data: str) -> str:
    input_data = add_time(input_data)
    return f"util: {input_data}"


def add_time(input_data: str) -> str:
    return f"{datetime.now()}: {input_data}"


def get_data(input_data: list[str]) -> str:
    input_data = f"There are {len(input_data)} arguments"
    return add_time(input_data)
