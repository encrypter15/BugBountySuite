# target_manager.py—herding targets like a slick cowboy
import logging
from core.database import add_target_db

def add_target(program, url):
    try:
        add_target_db(program, url)
        logging.info(f"Target {url} added to {program}—locked and loaded!")
    except Exception as e:
        logging.error(f"Target add failed: {e}")
        raise
