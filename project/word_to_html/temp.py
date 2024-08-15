from docx import Document

def convert_paragraph_to_html(paragraph):
    html = ""

    if paragraph.style.name.startswith('Heading'):
        level = paragraph.style.name[-1]
        html += f"<h{level}>{paragraph.text}</h{level}>"
    elif 'List Bullet' in paragraph.style.name:
        html += f"<li>{paragraph.text}</li>"
    else:
        html += "<p>"
        for run in paragraph.runs:
            if run.bold:
                html += f"<strong>{run.text}</strong>"
            elif run.italic:
                html += f"<em>{run.text}</em>"
            else:
                html += run.text
        html += "</p>"

    return html

def convert_docx_to_html(docx_path, html_path):
    doc = Document(docx_path)
    html_content = "<html><body>"

    for para in doc.paragraphs:
        html_content += convert_paragraph_to_html(para)

    html_content += "</body></html>"


    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

#
convert_docx_to_html('E:/STUDY/Python/python_programs/project/word_to_html/Sample.docx', 'output.html')
