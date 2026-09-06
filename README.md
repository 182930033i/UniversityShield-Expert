# UniversityShield Expert

نظام خبير جامعي لتقييم **الجاهزية الرقمية والأمن السيبراني في الجامعات**. هذا الموضوع مناسب لمجموعة طلاب لأنه يجمع الشبكات، إدارة الأنظمة، حماية البيانات، الحوكمة، التوعية، التطوير الآمن، والتوثيق.

## الأجزاء البرمجية المطلوبة

1. **Knowledge Base:** ملف `knowledge_base.json` ويضم 16 سؤالًا و16 قاعدة وتوصية.
2. **Inference Engine:** ملف `inference_engine.py` ويطبق Forward Chaining مع تفسير القواعد والتعلم التراكمي من التغذية الراجعة.
3. **User Interface:** ملف `main.py` ويعرض الأسئلة والنتائج ولوحة التعلم بواجهة رسومية.

## ملفات التسليم الثلاثة

| التسليم | الملفات |
|---|---|
| Source Code | `main.py`, `inference_engine.py`, `knowledge_base.json`, `test_engine.py` |
| Executable | `CyberGuard_Expert.exe` الناتج من GitHub Actions أو `build_exe.bat` |
| Report / README | `report_short.md` وملف PDF النهائي |

## التشغيل

لا يحتاج المستخدم النهائي إلى Python إذا استخدم ملف EXE. شغّل `CyberGuard_Expert.exe` بالنقر المزدوج على Windows. الذاكرة المحلية تحفظ في `~/.cyberguard_expert/learning_data.json`.

## بناء EXE عبر GitHub Actions

ارفع ملفات المصدر إلى مستودع GitHub، وضع `build-windows.yml` في `.github/workflows/`، ثم افتح Actions وشغّل `Build UniversityShield Expert for Windows`. بعد النجاح نزّل Artifact باسم `UniversityShield_Expert-Windows`.

## تقسيم العمل المقترح لمجموعة من ستة طلاب

| الطالب | المسؤولية |
|---|---|
| 1 | تحليل الأمن الجامعي وجمع المتطلبات والمراجع |
| 2 | تصميم قاعدة المعرفة والأسئلة والقواعد والأوزان |
| 3 | تطوير محرك Forward Chaining والتعلم والاختبارات |
| 4 | تصميم الواجهة وتجربة المستخدم |
| 5 | اختبار الحالات والتغليف وإنشاء EXE |
| 6 | التقرير ودليل التشغيل والتوثيق والعرض النهائي |

## حدود المشروع

النظام أداة أكاديمية للتوعية والتقييم الأولي، ولا يمثل تدقيقًا أمنيًا احترافيًا أو ضمانًا للامتثال.
