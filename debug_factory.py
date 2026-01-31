import os
def check_project():
    print("🔍 جاري فحص مشروع BuildAi...")
    files = os.listdir('.')
    essential = ['main.py', 'buildozer.spec', 'myfont.ttf']
    for f in essential:
        if f in files:
            print(f"✅ ملف {f} موجود.")
        else:
            print(f"❌ خطأ: ملف {f} مفقود!")
check_project()
