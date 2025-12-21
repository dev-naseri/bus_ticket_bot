from pathlib import Path

ROOT = Path(__file__).parent.parent
DATABASE_PATH = ROOT / "data" / "database.db"
BOT_LOGGER = ROOT / "logs" / "bot.log"
SERVICES_LOGGER = ROOT / "logs" / "services.log"
