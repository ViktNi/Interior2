from __future__ import annotations

from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
            # token=env.str('BOT_TOKEN')
            # token=env(BOT_TOKEN)
            # token='6691110174:AAEVRgqNL5Wp5fzOVjRBl90_blfakuXTzYA'
                     )
    )
