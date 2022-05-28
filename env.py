from typing import Dict, Optional

from dotenv import dotenv_values

_env: Dict[str, Optional[str]] = dotenv_values(dotenv_path=".env")


def get(key: str) -> Optional[str]:
    return _env.get(key)


def project_id() -> str:
    return _env.get('PROJECT_ID')


def proejct_region() -> str:
    return _env.get('PROJECT_REGION')


def registry() -> str:
    return _env.get('REGISTRY')


def credential() -> str:
    return _env.get("CREDENTIALS")
