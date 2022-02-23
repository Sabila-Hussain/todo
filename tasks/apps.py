from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'


class FirestoreDB:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    todo_collection = db.collection("todos")
