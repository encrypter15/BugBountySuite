#!/usr/bin/env python3
# main.py: BugBountySuite’s nerve center—Hunter’s Hub HQ!
import sys
import argparse
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from core.database import init_db
import logging

# Logging—because silent crashes are for chumps
logging.basicConfig(filename='logs/bugbounty_suite.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(description="BugBountySuite: Hunter’s Hub—Bug Hunting Beast")
    parser.add_argument('--target', help="Target domain—gimme the goods!")
    parser.add_argument('--scan', action='store_true', help="Run the full scan")
    parser.add_argument('--notify', action='store_true', help="Scream at me when shit changes")
    return parser.parse_args()

async def run_scan(target):
    logging.info(f"Starting full scan on {target}—hold my whiskey!")
    # Placeholder—real scan logic in recon_tools.py
    return {"status": "scanned"}

async def main():
    args = parse_args()
    init_db()
    if args.scan and args.target:
        changes = await run_scan(args.target)
        logging.info("Scan complete—go cash those bounties!")
    else:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        logging.info("Hunter’s Hub GUI launched—hunt in style!")
        sys.exit(app.exec())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
