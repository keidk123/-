from cx_Freeze import setup, Executable

setup(
    name = "def", # اسم التطبيق
    version = "0.1",
    description = "My Python Application",
    executables = [Executable("def.py")] # اسم ملف بايثون الرئيسي
)
