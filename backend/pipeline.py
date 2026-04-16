import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def parse_syllabus(syllabus_text):
    units = {}
    current_unit = None

    for line in syllabus_text.split("\n"):
        line = line.strip()
        if not line:
            continue

        if "unit" in line.lower():
            current_unit = line
            units[current_unit] = []
        elif current_unit:
            units[current_unit].append(line)

    return units


def simple_match(question, units):
    q_words = set(question.lower().split())

    best_unit = None
    best_score = -1

    for unit, content in units.items():
        text = " ".join(content).lower()
        t_words = set(text.split())

        score = len(q_words & t_words)

        if score > best_score:
            best_score = score
            best_unit = unit

    return best_unit if best_unit else list(units.keys())[0]


def run_pipeline(syllabus_text, questions_text):

    units = parse_syllabus(syllabus_text)

    questions = [q.strip() for q in questions_text.split("\n") if q.strip()]

    mapping = {}

    for q in questions:
        unit = simple_match(q, units)

        if unit not in mapping:
            mapping[unit] = []

        mapping[unit].append(q)

    # Generate PDF
    output_path = "output.pdf"
    generate_pdf(mapping, output_path)

    return output_path


def generate_pdf(mapping, path):
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    content = []

    for unit, questions in mapping.items():
        content.append(Paragraph(f"<b>{unit}</b>", styles["Heading1"]))
        content.append(Spacer(1, 10))

        for i, q in enumerate(questions, 1):
            content.append(Paragraph(f"{i}. {q}", styles["BodyText"]))

        content.append(Spacer(1, 20))

    doc.build(content)