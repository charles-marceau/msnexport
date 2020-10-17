import click
from .MSNParser import MSNParser
from .PDFExporter import PDFExporter


@click.command()
@click.argument('input_file_path')
@click.argument('output_file_path')
def export(input_file_path, output_file_path):
    msn_parser = MSNParser()
    messages = msn_parser.parse_xml(input_file_path)

    exporter = PDFExporter()
    exporter.export(output_file_path, messages)
