from docx import Document
import os
import re
import datetime

def is_bullet_point(paragraph):
    """Check if a paragraph is part of a bullet list."""
    return True if ('List Paragraph' in paragraph.style.name) else False
def convert_run_to_html(run):
    """Convert a Run object to HTML."""
    html = ""
    if run.bold:
        html += f"<strong>{run.text}</strong>"
    elif run.italic:
        html += f"<em>{run.text}</em>"
    else:
        html += run.text
    return html

def convert_paragraph_to_html(paragraph):
    """Convert a Paragraph object to HTML."""
    html = ""
    if is_bullet_point(paragraph):
        return f"<li>{''.join(convert_run_to_html(run) for run in paragraph.runs)}</li>"
    else:
        html += "<p>"
        for run in paragraph.runs:
            html += convert_run_to_html(run)
        html += "</p>"
    return html

def convert_list_to_html(doc):
    """Convert the lists in a Word document to HTML."""
    html_content = ""
    in_bullet_list = False

    for para in doc.paragraphs:
        if is_bullet_point(para):
            if not in_bullet_list:
                html_content += "<ul>"
                in_bullet_list = True
            html_content += convert_paragraph_to_html(para)
        else:
            if in_bullet_list:
                html_content += "</ul>"
                in_bullet_list = False
            
            html_content += convert_paragraph_to_html(para)

    if in_bullet_list:
        html_content += "</ul>"

    return html_content

def convert_docx_to_html(docx_path, html_path):
    """Main function to convert DOCX to HTML with list handling and text formatting."""
    doc = Document(docx_path)
    html_content = "<html><body>"
    html_content += convert_list_to_html(doc)
    html_content += "</body></html>"
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)



enter_path = input("Enter a path of folder where .txt files are located : ")
print("getting files from given location...")
allfiles = os.listdir(f"{enter_path}")
fname = [f for f in allfiles if f.endswith('.docx')]
print("extracting text from files...")
for i in range(len(fname)):
    filename = fname[i]
    filename = re.sub(r'\.docx$', '.html', filename)
    datetime1 = datetime.datetime.now()
    today = f"{datetime1.year}-{datetime1.month}-{datetime1.day}"
    if not os.path.exists(f"{enter_path}/{today}"):
        os.mkdir(f"{enter_path}/{today}")
    convert_docx_to_html(f"{enter_path}/{fname[i]}",f"{enter_path}/{today}/{filename}")
