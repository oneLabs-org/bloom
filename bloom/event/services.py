class EventFormatter:
    def format_slug(event_name: str) -> str:
        return "-".join(event_name.lower().split())
