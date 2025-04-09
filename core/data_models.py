# data_models.py—because structure’s sexy, even with AI
class Target:
    def __init__(self, program, url):
        self.program = program
        self.url = url

class Vulnerability:
    def __init__(self, target_url, title, poc, severity, date_found=None, status="New", notes=None, ai_score=0.0):
        self.target_url = target_url
        self.title = title
        self.poc = poc
        self.severity = severity
        self.date_found = date_found
        self.status = status
        self.notes = notes
        self.ai_score = ai_score
