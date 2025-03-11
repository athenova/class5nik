from simple_blogger import Teacher
from datetime import datetime

class Project(Teacher):
    def __init__(self, **kwargs):
        super().__init__(            
            review_chat_id=-1002374309134,
            first_post_date=datetime(2025, 1, 6),
            send_text_with_image=True,
            topic_word_limit=200,
            last_post_date=datetime(2025, 5, 20),
            **kwargs)
        
    def _system_prompt(self, _):
        return "Ты - блогер с 1000000 подписчиков и целевой аудиторией 12 лет, используешь в разговоре сленг и смайлики"

    def _task_converter(self, idea):
        topic = f"{idea['author']}. {idea['topic']}" if 'author' in idea else idea['topic']
        return { 
                "topic": topic,
                "category": f"{idea['category']}",
                "topic_image": f"Нарисуй картинку, вдохновлённую темой '{topic}' из '{idea['category']}'",
                "topic_prompt": f"Напиши интересный факт по теме '{topic}' из '{idea['category']}', используй менее {self.topic_word_limit} слов",
            }
    
   