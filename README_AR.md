# UniversityShield Expert — دليل التشغيل العربي

## التشغيل النهائي

شغّل `UniversityShield_Expert.exe` بالنقر المزدوج على Windows. لا يحتاج جهاز التشغيل إلى Python أو Internet.

## مكونات النظام

- `knowledge_base.json`: قاعدة المعرفة والأسئلة والقواعد.
- `inference_engine.py`: محرك الاستدلال الأمامي والتعلم المحلي.
- `main.py`: الواجهة الرسومية العربية.
- `test_engine.py`: اختبارات المحرك.

## بناء EXE

ارفع المشروع إلى GitHub، وضع `build-windows.yml` داخل `.github/workflows/`، ثم افتح Actions وشغّل **Build UniversityShield Expert for Windows**. نزّل Artifact باسم `UniversityShield_Expert-Windows` وفك ضغطه.

## ملاحظة

التعلم محلي وقابل للتفسير، ولا يغير قواعد الخبراء تلقائيًا. النظام أداة أكاديمية للتقييم الأولي.
