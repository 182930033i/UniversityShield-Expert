import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from inference_engine import ExpertEngine

# CyberGuard visual system
BG='#08111f'; PANEL='#101d30'; CARD='#15263d'; CARD2='#1b304a'; TEXT='#f1f5fb'; MUTED='#91a4bd'; ACCENT='#39e6a1'; BLUE='#62a8ff'; RED='#ff7188'; AMBER='#ffc857'; LINE='#243b58'

class CyberGuardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('UniversityShield Expert — الجاهزية الرقمية الجامعية')
        self.geometry('1200x780'); self.minsize(960,650); self.configure(bg=BG)
        self.engine=ExpertEngine(); self.answers={}; self.index=0; self.result=None; self.feedback_given=False
        self.setup_style(); self.show_intro()

    def setup_style(self):
        s=ttk.Style(self); s.theme_use('clam')
        s.configure('TButton',font=('Segoe UI',11),padding=(17,10),background=CARD2,foreground=TEXT,borderwidth=0,relief='flat')
        s.map('TButton',background=[('active','#2b486b')],foreground=[('active',TEXT)])
        s.configure('Accent.TButton',background=ACCENT,foreground='#06151a',font=('Segoe UI',11,'bold'),padding=(20,11))
        s.map('Accent.TButton',background=[('active','#75f2bf')])
        s.configure('TProgressbar',troughcolor='#20334d',background=ACCENT,darkcolor=ACCENT,lightcolor=ACCENT)

    def clear(self):
        for w in self.winfo_children(): w.destroy()

    def header(self, subtitle='نظام خبير للجاهزية الرقمية والأمن السيبراني الجامعي', show_home=False):
        bar=tk.Frame(self,bg=BG); bar.pack(fill='x',padx=48,pady=(25,12))
        brand=tk.Frame(bar,bg=BG); brand.pack(side='left')
        tk.Label(brand,text='◈',font=('Segoe UI',25,'bold'),fg=ACCENT,bg=BG).pack(side='left',padx=(0,8))
        tk.Label(brand,text='UNIVERSITYSHIELD',font=('Segoe UI',17,'bold'),fg=TEXT,bg=BG).pack(side='left')
        tk.Label(bar,text=subtitle,font=('Segoe UI',11),fg=MUTED,bg=BG).pack(side='right')
        if show_home: ttk.Button(bar,text='الرئيسية',command=self.show_intro).pack(side='right',padx=18)

    def label(self,parent,text,size=11,color=TEXT,bold=False,**kwargs):
        return tk.Label(parent,text=text,font=('Segoe UI',size,'bold' if bold else 'normal'),fg=color,bg=kwargs.pop('bg',parent.cget('bg')),**kwargs)

    def show_intro(self):
        self.clear(); self.header('منصة تقييم أمني قابلة للتفسير والتعلم')
        area=tk.Frame(self,bg=BG); area.pack(fill='both',expand=True,padx=78,pady=20)
        hero=tk.Frame(area,bg=PANEL); hero.pack(fill='x',pady=(0,18))
        left=tk.Frame(hero,bg=PANEL); left.pack(side='left',fill='both',expand=True,padx=35,pady=36)
        self.label(left,'نظام خبير تكيفي',10,ACCENT,True,bg=PANEL).pack(anchor='w')
        self.label(left,'تقييم الجاهزية الرقمية\nوالأمن السيبراني',30,TEXT,True,bg=PANEL,justify='right').pack(anchor='e',pady=(10,8))
        self.label(left,'نظام خبير جامعي واسع يقيم جاهزية الشبكات والأنظمة والبيانات والحوكمة، يفسر قراراته، ويتعلم من تقييم المستخدم للتوصيات دون تغيير قواعد الخبراء تلقائيًا.',13,MUTED,bg=PANEL,wraplength=580,justify='right').pack(anchor='e')
        ttk.Button(left,text='بدء التقييم  ←',style='Accent.TButton',command=self.start).pack(anchor='e',pady=(24,0))
        art=tk.Frame(hero,bg='#102a3c',width=270,height=220); art.pack(side='right',padx=28,pady=28); art.pack_propagate(False)
        self.label(art,'CAMPUS\nSHIELD',22,ACCENT,True,bg='#102a3c',justify='center').place(relx=.5,rely=.45,anchor='center')
        self.label(art,'FORWARD CHAINING  •  LOCAL LEARNING',8,MUTED,bg='#102a3c',justify='center').place(relx=.5,rely=.78,anchor='center')
        tk.Frame(area,bg=LINE,height=1).pack(fill='x',pady=2)
        self.label(area,'ماذا يقدم النظام؟',16,TEXT,True,bg=BG).pack(anchor='e',pady=(18,10))
        cards=tk.Frame(area,bg=BG); cards.pack(fill='x')
        features=[('01','تحليل جامعي شامل','16 سؤالًا تغطي مجالات الأمن والجاهزية الرقمية.'),('02','قرار قابل للتفسير','كل توصية مرتبطة بقاعدة واضحة ودرجة خطر.'),('03','تعلم تراكمي','تحسين ترتيب التوصيات من تقييمات المستخدم.')]
        for num,title,desc in features:
            c=tk.Frame(cards,bg=CARD); c.pack(side='left',fill='both',expand=True,padx=5)
            self.label(c,num,11,ACCENT,True,bg=CARD).pack(anchor='w',padx=18,pady=(16,4)); self.label(c,title,13,TEXT,True,bg=CARD).pack(anchor='w',padx=18); self.label(c,desc,10,MUTED,bg=CARD,wraplength=235,justify='left').pack(anchor='w',padx=18,pady=(5,18))
        bottom=tk.Frame(area,bg=BG); bottom.pack(fill='x',pady=18); self.label(bottom,f'الحالات المتعلمة محليًا: {self.engine.learning.summary()["cases"]}',10,MUTED,bg=BG).pack(side='left'); ttk.Button(bottom,text='لوحة التعلم',command=self.show_learning).pack(side='right')

    def start(self): self.answers={}; self.index=0; self.show_question()

    def show_question(self):
        self.clear(); q=self.engine.kb['questions'][self.index]; total=len(self.engine.kb['questions']); self.header(q['category'])
        area=tk.Frame(self,bg=BG); area.pack(fill='both',expand=True,padx=110,pady=18)
        top=tk.Frame(area,bg=BG); top.pack(fill='x')
        self.label(top,f'السؤال {self.index+1:02d} / {total:02d}',10,ACCENT,True,bg=BG).pack(side='left')
        self.label(top,f'{round((self.index+1)/total*100)}% مكتمل',10,MUTED,bg=BG).pack(side='right')
        ttk.Progressbar(area,maximum=total,value=self.index+1).pack(fill='x',pady=(10,0))
        box=tk.Frame(area,bg=PANEL); box.pack(fill='x',pady=(72,25))
        self.label(box,q['category'].upper(),10,BLUE,True,bg=PANEL).pack(anchor='e',padx=38,pady=(28,7))
        self.label(box,q['text'],23,TEXT,True,bg=PANEL,wraplength=850,justify='right').pack(anchor='e',padx=38,pady=(0,30))
        self.choice=tk.StringVar(value=self.answers.get(q['id'],'')); choices=tk.Frame(box,bg=PANEL); choices.pack(anchor='e',padx=30,pady=(0,30))
        for value,text in q['options']:
            tk.Radiobutton(choices,text=text,value=value,variable=self.choice,font=('Segoe UI',13,'bold'),fg=TEXT,bg=CARD,selectcolor='#2a4c70',activebackground='#2a4c70',activeforeground=TEXT,indicatoron=0,width=19,pady=14,anchor='e',cursor='hand2',relief='flat').pack(side='right',padx=7)
        nav=tk.Frame(area,bg=BG); nav.pack(fill='x',side='bottom'); ttk.Button(nav,text='← السابق',command=self.previous).pack(side='left'); ttk.Button(nav,text='التالي  →',style='Accent.TButton',command=self.next).pack(side='right')

    def next(self):
        if not self.choice.get(): messagebox.showwarning('إجابة مطلوبة','يرجى اختيار إجابة قبل المتابعة.'); return
        self.answers[self.engine.kb['questions'][self.index]['id']]=self.choice.get()
        if self.index < len(self.engine.kb['questions'])-1: self.index+=1; self.show_question()
        else: self.result=self.engine.infer(self.answers); self.feedback_given=False; self.show_result()

    def previous(self):
        if self.index>0: self.answers[self.engine.kb['questions'][self.index]['id']]=self.choice.get(); self.index-=1; self.show_question()

    def show_result(self):
        self.clear(); self.header('النتيجة والتحليل القابل للتفسير',True); r=self.result; color={'حرج':RED,'مرتفع':RED,'متوسط':AMBER,'منخفض':ACCENT}[r['level']]
        area=tk.Frame(self,bg=BG); area.pack(fill='both',expand=True,padx=55,pady=8)
        summary=tk.Frame(area,bg=PANEL); summary.pack(fill='x'); self.label(summary,'مستوى الخطر الحالي',9,MUTED,True,bg=PANEL).pack(pady=(17,2)); self.label(summary,r['level'],31,color,True,bg=PANEL).pack(); self.label(summary,f'{r["percentage"]}% درجة الخطر   •   {len(r["fired_rules"])} قواعد مفعلة   •   {r["learned"]["cases"]} حالات متعلمة',11,TEXT,bg=PANEL).pack(pady=(0,17))
        canvas=tk.Canvas(area,bg=BG,highlightthickness=0); scroll=ttk.Scrollbar(area,orient='vertical',command=canvas.yview); inner=tk.Frame(canvas,bg=BG); inner.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox('all'))); canvas.create_window((0,0),window=inner,anchor='nw',width=1000); canvas.configure(yscrollcommand=scroll.set); canvas.pack(side='left',fill='both',expand=True,pady=14); scroll.pack(side='right',fill='y',pady=14)
        self.label(inner,'نتائج محرك الاستدلال والتوصيات',16,TEXT,True,bg=BG).pack(anchor='e',pady=(0,7))
        for i,rule in enumerate(r['fired_rules'],1):
            c=tk.Frame(inner,bg=CARD); c.pack(fill='x',pady=4); self.label(c,f'{i:02d}  {rule["finding"]}',11,TEXT,True,bg=CARD,wraplength=830,justify='right').pack(anchor='e',padx=18,pady=(11,2)); self.label(c,f'التوصية: {rule["recommendation"]}',10,ACCENT,bg=CARD,wraplength=830,justify='right').pack(anchor='e',padx=18,pady=2); self.label(c,f'{rule["id"]}   •   مستوى الأولوية: {rule["risk"]}   •   الثقة المتعلمة: {int(rule["learned_confidence"]*100)}%',9,BLUE,bg=CARD).pack(anchor='e',padx=18,pady=(2,11))
        fb=tk.Frame(area,bg=PANEL); fb.pack(fill='x'); self.label(fb,'قيّم التوصيات لتدريب ترتيب النتائج القادمة:',10,MUTED,bg=PANEL).pack(side='right',padx=15,pady=8); ttk.Button(fb,text='مفيدة ✓',command=lambda:self.give_feedback(True)).pack(side='right',pady=4); ttk.Button(fb,text='تحتاج تحسينًا',command=lambda:self.give_feedback(False)).pack(side='right',padx=7,pady=4)
        nav=tk.Frame(area,bg=BG); nav.pack(fill='x',pady=8); ttk.Button(nav,text='الرئيسية',command=self.show_intro).pack(side='left'); ttk.Button(nav,text='تقييم جديد',command=self.start).pack(side='left',padx=8); ttk.Button(nav,text='حفظ التقرير',command=self.save_report).pack(side='right')

    def give_feedback(self,helpful):
        if self.feedback_given: messagebox.showinfo('تم التسجيل','تم تسجيل تقييمك مسبقًا لهذه الحالة.'); return
        s=self.engine.record_feedback(self.result,helpful); self.feedback_given=True; messagebox.showinfo('تم التعلم','تم تحديث الذاكرة المحلية بنجاح.\nالحالات المتعلمة: '+str(s['cases']))

    def show_learning(self):
        self.clear(); self.header('لوحة التعلم والذاكرة المحلية',True); s=self.engine.learning.summary(); area=tk.Frame(self,bg=BG); area.pack(fill='both',expand=True,padx=110,pady=32)
        self.label(area,'لوحة التعلم',28,TEXT,True,bg=BG).pack(anchor='e'); self.label(area,'يتعلم النظام من تقييماتك دون إرسال البيانات إلى الإنترنت.',12,MUTED,bg=BG).pack(anchor='e',pady=(4,24))
        stats=tk.Frame(area,bg=BG); stats.pack(fill='x')
        for value,title in [(s['cases'],'حالة محفوظة'),(s['rules'],'قاعدة تلقت تغذية راجعة'),('محلي','نوع الذاكرة')]:
            c=tk.Frame(stats,bg=CARD); c.pack(side='left',fill='both',expand=True,padx=5); self.label(c,str(value),25,ACCENT,True,bg=CARD).pack(anchor='w',padx=20,pady=(18,2)); self.label(c,title,10,MUTED,bg=CARD).pack(anchor='w',padx=20,pady=(0,18))
        info=tk.Frame(area,bg=PANEL); info.pack(fill='x',pady=28); self.label(info,'كيف يعمل التعلم؟',15,TEXT,True,bg=PANEL).pack(anchor='e',padx=24,pady=(20,7)); self.label(info,'يحتفظ النظام بسجل محلي للتقييمات ويستخدم ملاحظتك لرفع أو خفض ثقة التوصيات. لا تتغير قواعد الخبراء أو حدود الخطر تلقائيًا، لذلك تبقى النتائج قابلة للمراجعة والتفسير.',12,MUTED,bg=PANEL,wraplength=780,justify='right').pack(anchor='e',padx=24,pady=(0,20)); self.label(area,'مسار الذاكرة: '+s['path'],9,MUTED,bg=BG).pack(anchor='e'); ttk.Button(area,text='← العودة للرئيسية',command=self.show_intro).pack(anchor='e',pady=24)

    def save_report(self):
        path=Path.home()/'Desktop'/'CyberGuard_Assessment.txt'; path.parent.mkdir(exist_ok=True); r=self.result
        with open(path,'w',encoding='utf-8') as f:
            f.write('CYBERGUARD EXPERT - ADAPTIVE SECURITY ASSESSMENT\n'+'='*60+'\n\n'); f.write(f'مستوى المخاطر: {r["level"]}\nدرجة المخاطر: {r["percentage"]}%\nالحالات المتعلمة: {r["learned"]["cases"]}\n\n')
            for x in r['fired_rules']: f.write(f'- {x["id"]}: {x["finding"]}\n  التوصية: {x["recommendation"]}\n  الثقة المتعلمة: {int(x["learned_confidence"]*100)}%\n')
        messagebox.showinfo('تم الحفظ','تم حفظ التقرير في:\n'+str(path))

if __name__=='__main__': CyberGuardApp().mainloop()
