import logging
import os
import random
import time
from contextlib import contextmanager
from datetime import datetime
from typing import Optional
import functools

import numpy as np
import pytz
import psutil


@contextmanager
def timer(name: str, logger: Optional[logging.Logger] = None):
    """Timer context manager

    Args:
        name (str): name of the timer
        logger (Optional[logging.Logger], optional): A Logger object.

    Usage:
        with timer("process ...", logger):
            process()
    """
    t0 = time.time()
    start_msg = f"[{name}] start..."
    if logger:
        logger.info(start_msg)
    else:
        print(start_msg)
    yield
    end_msg = f"[{name}] done in {time.time()-t0:.0f} s"
    if logger:
        logger.info(end_msg)
    else:
        print(end_msg)


class JSTFormatter(logging.Formatter):
    """JST Formatter for logging"""

    converter = datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created, pytz.timezone("Asia/Tokyo"))
        if datefmt:
            return dt.strftime(datefmt)
        else:
            return dt.strftime("%Y-%m-%d %H:%M:%S %Z%z")


def setup_logger(log_file, jst=False) -> logging.Logger:
    """for setting up logger

    Args:
        log_file (str): A path to a log file

    Returns:
        logging.Logger: Setup logger
    """
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if jst:
        formatter = JSTFormatter("%(asctime)s [%(levelname)s] %(message)s")
    else:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def seed_everything_essential(seed: int) -> None:
    """seed_everything_essential

    Args:
        seed (int): a seed number
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)


def seed_everything_torch(seed: int) -> None:
    """seed_everything (for pytorch)

    Args:
        seed (int): a seed number
    """
    seed_everything_essential(seed)
    import torch

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = False
    torch.backends.cudnn.benchmark = True


def memory_limit_exceeded(limit_gb):
    """
    A decorator to monitor memory consumption.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            memory_before = psutil.virtual_memory().used / (1024**3)
            result = func(*args, **kwargs)
            memory_after = psutil.virtual_memory().used / (1024**3)
            memory_difference = memory_after - memory_before
            if memory_difference > limit_gb:
                raise MemoryError(
                    f"Memory usage exceeded limit of {limit_gb} GB"
                    + " (Used: {memory_difference} GB)"
                )
            return result

        return wrapper

    return decorator
