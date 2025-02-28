from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self) -> None:
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def find_category(self, category_id) -> "Category":
        category_to_find = next((c for c in self.categories if c.id == category_id), None)
        return category_to_find

    def find_topic(self, topic_id) -> "Topic":
        topic_to_find = next((t for t in self.topics if t.id == topic_id), None)
        return topic_to_find

    def find_document(self, document_id) -> "Document":
        document_to_find = next((d for d in self.documents if d.id == document_id), None)
        return document_to_find

    def edit_category(self, category_id: int, new_name: str) -> None:
        category_to_edit = self.find_category(category_id)
        category_to_edit.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic_to_edit = self.find_topic(topic_id)
        topic_to_edit.topic = new_topic
        topic_to_edit.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document_to_edit = self.find_document(document_id)
        document_to_edit.file_name = new_file_name

    def delete_category(self, category_id: int) -> None:
        category_to_delete = self.find_category(category_id)
        self.categories.remove(category_to_delete)

    def delete_topic(self, topic_id: int) -> None:
        topic_to_delete = self.find_topic(topic_id)
        self.topics.remove(topic_to_delete)

    def delete_document(self, document_id: id) -> None:
        document_to_delete = self.find_document(document_id)
        self.documents.remove(document_to_delete)

    def get_document(self, document_id: int) -> "Document":
        document_to_find = self.find_document(document_id)
        return document_to_find

    def __repr__(self):
        result = list(document.__repr__() for document in self.documents)
        return '\n'.join(result)
