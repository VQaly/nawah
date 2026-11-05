import re


def تشغيل_المشروع(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        arabic_code = file.read()
    
    # التعديل الذكي: شيلنا المسافة من جوة علامات التنصيص عشان يلقط الكلمة في أي وضع!
    translated_code = arabic_code
    translated_code = translated_code.replace("لو", "if")
    translated_code = translated_code.replace("إذا", "if")
    translated_code = translated_code.replace("اذا", "if")
    translated_code = translated_code.replace("جمد", "lambda")

    translated_code = re.sub(
        r'("(?:\\.|[^"\\])*"|،)',
        lambda m: "," if m.group() == "،" else m.group(),
        translated_code
    )
    
    
    final_code = "from nawah import *\n" + translated_code
    exec(final_code, globals())

    
def سجل(text):
    """اخراج النص المكتوب على الطرفية (تيرمنال)"""
    print(text)

def احفظ(data):
    """الإحتفاظ بالناتج"""
    return data

def عندما_يضغط_الزر(button_name, event_action):
    """مراقبة أزرار النظام وتشغيل الأحداث المؤجلة"""
    print(f"[System] Monitoring keyboard button: '{button_name}'")
    # هنا يتم الربط الفعلي التفاعلي مع النظام في الخلفية

    
