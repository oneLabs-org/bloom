class EventFormatter:
    def format_event(event_name: str) -> str:
        return "-".join(event_name.lower().split())

    def unformat_event(event_name: str) -> str:
        return " ".join(word.capitalize() for word in event_name.split("-"))
