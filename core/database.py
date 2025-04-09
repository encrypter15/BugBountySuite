# database.py—storing your bounty gold like a pro
import sqlite3
import logging

DB_PATH = "data/hunters_hub.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS targets 
                 (id INTEGER PRIMARY KEY, program TEXT, url TEXT UNIQUE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS vulnerabilities 
                 (id INTEGER PRIMARY KEY, target_id INTEGER, title TEXT, poc TEXT, 
                 severity TEXT, date_found TEXT DEFAULT CURRENT_TIMESTAMP, 
                 status TEXT DEFAULT 'New', notes TEXT, 
                 FOREIGN KEY(target_id) REFERENCES targets(id))''')
    conn.commit()
    conn.close()
    logging.info("DB initialized—ready to roll!")

def add_target_db(program, url):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO targets (program, url) VALUES (?, ?)", (program, url))
    conn.commit()
    conn.close()

def add_vuln_db(target_url, title, poc, severity):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id FROM targets WHERE url = ?", (target_url,))
    target_id = c.fetchone()
    if target_id:
        c.execute("INSERT INTO vulnerabilities (target_id, title, poc, severity) VALUES (?, ?, ?, ?)",
                  (target_id[0], title, poc, severity))
        conn.commit()
    conn.close()

def get_targets():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT program, url FROM targets")
    return c.fetchall()

def get_vulns_by_target(target_url):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT v.title, v.poc, v.severity, v.date_found, v.status, v.notes 
                 FROM vulnerabilities v 
                 JOIN targets t ON v.target_id = t.id 
                 WHERE t.url = ?''', (target_url,))
    return [{"title": r[0], "poc": r[1], "severity": r[2], "date_found": r[3], "status": r[4], "notes": r[5]} 
            for r in c.fetchall()]
