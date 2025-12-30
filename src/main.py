import shutil
import os
from textnode import TextNode, TextType
from generate_page import generate_pages_recursive

def main():
    textNodeObject = TextNode("This is some anchor text", TextType.LINK , "https://www.boot.dev")
    print(textNodeObject)


main()


def recursive_copy(source_path, destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)
    for file_path in os.listdir(source_path):
        extended_path = os.path.join(source_path, file_path)
        if os.path.isfile(extended_path) == True:
            shutil.copy(extended_path, destination_path)
        else:
            full_source = extended_path
            full_destination = os.path.join(destination_path, file_path)
            recursive_copy(full_source, full_destination)

recursive_copy("static", "public")
generate_pages_recursive("content", "template.html", "public")