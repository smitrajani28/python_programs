from docx import Document

doc = Document("E:\STUDY\Python\python_programs\project\word_to_html\Cluster In Charge - Institutional Sales.docx")
for para in doc.paragraphs:
    # print(para.text)
    print(para.style.name)
    # print(para.style.numbering.bullet)
    # print(para.bullet_format)
    # for base in para:
    #     print(base)