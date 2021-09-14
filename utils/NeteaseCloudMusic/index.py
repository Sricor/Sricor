# -*- encoding: utf-8 -*-
import os
import action

infos = {
    "phone": os.environ["NETEASE_PHONE"],
    "password": os.environ["NETEASE_PASSWORD"],
    # "sc_key": ["XXXX"],
    # "tg_bot_key": ["XXXX", "XXXXX"],
    "bark_key": os.getenv('BARK'),
    # "wecom_key": ["XXXX", "XXXX", "XXXX"],
    # "push_plus_key": ["XXXX"],
    # "qmsg_key": ["XXXX"],
    # "ding_token": ["XXXX"],
}


def main_handler(event, context):
    action.tasks_pool(infos)


if __name__ == "__main__":
    main_handler("", "")
