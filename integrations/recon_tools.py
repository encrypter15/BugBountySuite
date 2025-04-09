# recon_tools.py—unleashing the recon beasts from BugBountySuite!
import subprocess
import logging
import asyncio
import json

async def run_bugwatch(target):
    cmd = ["python", "BugWatch/bugwatch.py", "--target", target, "--scan"]
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode() if not stderr else f"BugWatch failed: {stderr.decode()}"

async def run_vuln_voyager(target):
    cmd = ["python", "VulnVoyager/main.py", "--cli", "--target", target]
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode() if not stderr else f"VulnVoyager failed: {stderr.decode()}"

async def run_subsonic(target):
    cmd = ["python", "SubSonic/subsonic.py", "--target", target]
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode() if not stderr else f"SubSonic failed: {stderr.decode()}"

async def run_bugbounty_scraper(target):
    cmd = ["python", "BugBountyScraper/bugbounty_scraper.py", "--target", target]
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode() if not stderr else f"BugBountyScraper failed: {stderr.decode()}"

def run_nmap(target):
    cmd = ["nmap", "-p", "22,80,443", target]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout if not result.stderr else f"Nmap failed: {result.stderr}"

async def run_amass(target):
    cmd = ["amass", "enum", "-d", target]
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    return stdout.decode() if not stderr else f"Amass failed: {stderr.decode()}"

async def run_all_recon(target):
    logging.info(f"Running all recon tools on {target}—hold my beer!")
    tasks = [
        run_bugwatch(target),
        run_vuln_voyager(target),
        run_subsonic(target),
        run_bugbounty_scraper(target),
        asyncio.to_thread(run_nmap, target),
        run_amass(target)
    ]
    results = await asyncio.gather(*tasks)
    return dict(zip(["bugwatch", "vuln_voyager", "subsonic", "bugbounty_scraper", "nmap", "amass"], results))
