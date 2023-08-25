from enum import Enum


class ListenerEvent(Enum):
    MAIN_PROCESS_STOP = "main_process_stop"
    MAIN_PROCESS_START = "main_process_start"

    RELOAD_PROCESS_START = "reload_process_start"
    RELOAD_PROCESS_STOP = "reload_process_stop"

    BEFORE_SERVER_START = "before_server_start"
    AFTER_SERVER_START = "after_server_start"
    BEFORE_SERVER_STOP = "before_server_stop"
    AFTER_SERVER_STOP = "after_server_stop"
