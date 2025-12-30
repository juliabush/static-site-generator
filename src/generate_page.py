import os
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode
from extract_markdown import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        from_contents = f.read()
    with open(template_path, "r") as t:
        template_contents = t.read()
    markdown = markdown_to_html_node(from_contents)
    html_string = markdown.to_html()
    title = extract_title(from_contents)
    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", html_string)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as d:
        d.write(template_contents)