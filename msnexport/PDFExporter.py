from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from xml.sax.saxutils import escape


class PDFExporter:

    def export(self, output_file, messages):
        document = SimpleDocTemplate(output_file, )
        flowables = self._get_messages_as_paragraphs(
            messages, getSampleStyleSheet()['BodyText'])
        document.build(flowables)

    def _get_messages_as_paragraphs(self, messages, style):
        paragraphs = []
        for message in messages:
            paragraphs.append(self._get_message_as_paragraph(message, style))
        return paragraphs

    def _get_message_as_paragraph(self, message, style):
        date_time = message["dateTime"].strftime("%d/%m/%Y %H:%M")
        sender = message["sender"]
        text = message["text"]
        return Paragraph(escape(f"{date_time} {sender}: {text}"), style)
