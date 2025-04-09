# report_generator.py—turning bugs into paychecks
import logging
from jinja2 import Environment, FileSystemLoader

def generate_report(target_url, vulnerabilities, output_file):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.md')
    report_content = template.render(target=target_url, vulns=vulnerabilities)
    
    with open(output_file, 'w') as f:
        f.write(report_content)
    logging.info(f"Report dumped to {output_file}—go get that bounty!")
