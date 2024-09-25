from typing import Any
from typing import Dict

from pythonjsonlogger.jsonlogger import JsonFormatter


class CustomJsonFormatter(JsonFormatter):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, rename_fields=self._rename_fields, **kwargs)

    # def add_fields(self, log_record, record, message_dict):
    #     log_record["hostname"] = os.getenv("HOSTNAME", 'hostname')
    #     super().add_fields(log_record, record, message_dict)

    @property
    def _rename_fields(self) -> Dict[str, str]:
        return {
            # "asctime": "Date",
            # "thread": "Thread",
            # "module": "Logger",
            "name": "source",
            "levelname": "severity",
            # "message": "message",
        }
