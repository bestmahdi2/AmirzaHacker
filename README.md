# AmirzaHacker
This is a python program with GUI to examine all answers for Amirza and similar Games

این یک برنامه پایتون با ظاهر گرافیکی برای پیدا کردن تمامی حالت های ممکن جواب بازی هایی مثل آمیرزا است

***
If you're not a developer, download the **AmirzaHacker.rar** in **Release(GitHub)**, extract it and open the *compiler.exe*

اگر برنامه نویس نیستید ، در قسمت **ریلیز** در سایت گیت هاب **فایل رار** رو دانلود کنید و بعد از اسختراج *فایل اجرایی* را باز کنید
****
If you came for only-python-script in Virgool, you can find it in ProgramFile\Amirza_virgool.py

اگر برای قسمت فقط-پایتون مقاله سایت ویرگول آمدید ، در پوشه پروگرام فایل ، آمیرزا_ویرگول را دانلود کنید 
***
Otherwise, translate Persian letters with yours and replace Moin.db with Your-language words database.**/Main directory/**

Compiler.py: a script to connect python to Qt, and a little smarter. Moin.db: Persian words database.**/Programfiles/**

Amirza_ui.ui: GUI designed with PyQt5 designer. Amirza_ui.py: generated from the UI file. Amirza.py: main program. Amirza_virgool.py: a simplified version of Amirza.py (won't work with compiler.py in the main directory) CMD, PowerShell, terminal or similar):pyinstaller --OneFile --noconsole --icon='.\ProgramFile\Pirate Icon 21.ico' .\compiler.py

To convert UI file to py use below: ProgramFile

&gt; Pyuic5 -x -o Amirza_ui.py Amirza_ui.ui

![Program Logo](/ProgramFile/Logo.png)
