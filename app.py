
import streamlit as st
import pandas as pd

st.set_page_config(page_title="МФКН ВДПУ", layout="wide")

# Сторінки
def home():
    st.title("Факультет математики, фізики і комп’ютерних наук ВДПУ")
    st.image("vdpu_logo.png", width=120)
    st.markdown("## Вітаємо на офіційному порталі факультету МФКН!")
    st.info("Перевірте останні новини, розклад занять або авторизуйтеся для повного доступу.")

def student_portal():
    st.header("Портал студента")
    st.subheader("📄 Розклад занять")
    st.write("👉 [Розклад факультету](https://fmft.vspu.edu.ua/?p=schedule)")
    st.subheader("📚 Навчальні матеріали")
    st.file_uploader("Завантажте матеріал", type=["pdf", "docx"])
    st.subheader("📥 Завантаження завдань")
    st.file_uploader("Надішліть виконане завдання")

def teacher_portal():
    st.header("Портал викладача")
    st.subheader("📋 Списки груп")
    st.write("Наразі дані демонстраційні.")
    data = pd.DataFrame({'Група': ['МФКН-11', 'МФКН-21'], 'Кількість студентів': [18, 22]})
    st.table(data)
    st.subheader("🗂️ Завантаження матеріалів")
    st.file_uploader("Додати файл", type=["pdf", "pptx", "zip"])

def admin_panel():
    st.header("Адміністративна панель")
    st.subheader("👤 Управління користувачами")
    st.write("Реєстрація, редагування профілів")
    st.subheader("📈 Аналітика")
    st.bar_chart([20, 35, 50])
    st.subheader("📅 Розклад занять")
    st.write("👉 [Редагувати розклад](https://fmft.vspu.edu.ua/?p=schedule)")

pages = {
    "🏠 Головна": home,
    "🎓 Студентам": student_portal,
    "👨‍🏫 Викладачам": teacher_portal,
    "⚙️ Адмін": admin_panel,
}

st.sidebar.title("Навігація")
selection = st.sidebar.radio("Перейти до:", list(pages.keys()))
pages[selection]()
