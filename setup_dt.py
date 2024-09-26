import os
import heroku3

def create_database():
    # الحصول على مفتاح API من متغير البيئة
    heroku_api_key = os.environ.get("HEROKU_API_KEY")  # تأكد من تعيين هذا في إعدادات هيروكو
    if not heroku_api_key:
        raise ValueError("HEROKU_API_KEY environment variable not set.")

    # الاتصال بهيروكو
    heroku_conn = heroku3.from_key(heroku_api_key)

    # الحصول على اسم التطبيق من متغير البيئة
    app_name = os.environ.get("HEROKU_APP_NAME")  # تأكد من تعيين هذا في إعدادات هيروكو
    if not app_name:
        raise ValueError("HEROKU_APP_NAME environment variable not set.")

    # إنشاء قاعدة بيانات PostgreSQL
    app = heroku_conn.apps()[app_name]
    addon = app.add_ons.create(name='heroku-postgresql:hobby-dev')
    print(f"Database {addon.name} created.")

if __name__ == "__main__":
    create_database()