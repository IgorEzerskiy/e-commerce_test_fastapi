import logging
import sys
import json
from pathlib import Path
from logging.handlers import WatchedFileHandler
from pythonjsonlogger.jsonlogger import JsonFormatter
from typing import Optional
from app.core.config import config, ROOT_DIR


class UnicodeJsonFormatter(JsonFormatter):
    def jsonify_log_record(self, log_record):
        return json.dumps(log_record, ensure_ascii=False)

def setup_logging(
    level: int = logging.DEBUG,
    log_file: str = f"{ROOT_DIR}/logs/e-commerce_test_fastapi.log",
) -> None:
    """Setup logging configuration"""

    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.touch(exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(level)

    fmt = "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s"
    formatter = logging.Formatter(fmt)

    # console_h = logging.StreamHandler(sys.stdout)
    # console_h.setLevel(level)
    # console_h.setFormatter(formatter)
    # logger.addHandler(console_h)

    # JSON output to console
    json_h = logging.StreamHandler(sys.stderr)
    json_h.setLevel(level)
    json_h.setFormatter(UnicodeJsonFormatter(fmt))
    logger.addHandler(json_h)

    # JSON output to file, rotated daily
    file_h = WatchedFileHandler(
        filename=log_file,
        encoding="utf-8",
    )
    file_h.setLevel(level)
    file_h.setFormatter(UnicodeJsonFormatter(fmt))
    logger.addHandler(file_h)

    if not config.system_settings.debug:
        for name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
            lg = logging.getLogger(name)
            lg.handlers.clear()
            lg.propagate = True


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Get logger instance"""
    return logging.getLogger(name)
