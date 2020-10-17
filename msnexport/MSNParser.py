from bs4 import BeautifulSoup
from datetime import datetime


class MSNParser:

    def parse_xml(self, xml_file_path):
        messages = []
        with open(xml_file_path, "r") as xml_file:
            xml_tree = BeautifulSoup(xml_file, "lxml-xml")
            for message_tree in xml_tree.Log.findAll("Message"):
                messages.append(self._message_tree_to_dict(message_tree))
        return messages

    def _message_tree_to_dict(self, message_tree):
        return {
            "dateTime": datetime.strptime(message_tree["DateTime"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            "sender": message_tree.From.User["FriendlyName"],
            "text": message_tree.Text.string
        }
