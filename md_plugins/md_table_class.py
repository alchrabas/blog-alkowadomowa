from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


class AddTableClassTreeprocessor(Treeprocessor):
    def run(self, root):
        for table in root.iter("table"):
            existing = table.get("class", "")
            classes = set(existing.split()) if existing else set()
            classes.add("table table-striped table-bordered")
            table.set("class", " ".join(sorted(classes)))


class AddTableClassExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            AddTableClassTreeprocessor(md), "add_table_class", 9
        )


def makeExtension(**kwargs):
    return AddTableClassExtension(**kwargs)