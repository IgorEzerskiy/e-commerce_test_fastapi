from app.core.config import config
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def now_local():
    return datetime.now(timezone.utc).astimezone(ZoneInfo(config.system_settings.time_zone))
