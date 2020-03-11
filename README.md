# AmirzaHacker
This is a python program with GUI to examine all possible answers for Amirza and similar Games

این یک برنامه پایتون با ظاهر گرافیکی برای پیدا کردن تمامی حالت های ممکن جواب بازی هایی مثل آمیرزا است

***
If your not a developer just download the **AmirzaHacker.rar** in **Release(Github)**, extract it and open the *compiler.exe*

اگر برنامه نویس نیستید ، در قسمت **ریلیز** در سایت گیت هاب **فایل رار** رو دانلود کنید و بعد از اسختراج *فایل اجرایی* را باز کنید
****
If you came for just-python-script in Virgool , you can find it in ProgramFile\Amirza_virgool.py

اگر برای قسمت فقط-پایتون مقاله سایت ویرگول آمدید ، در پوشه پروگرام فایل ، آمیرزا_ویرگول را دانلود کنید 
***
Otherwise, you may want to translate Persian letters with yours and replace Moin.db with the Your-language words database.

**/Main directory/**

Compiler.py: just a script to connect python to Qt, and a little smarter.

Moin.db: Persian words database.


**/Programfiles/**

Amirza_ui.ui: GUI designed with PyQt5 designer.

Amirza_ui.py: generated from the UI file.

Amirza.py: main program.

Amirza_virgool.py : simplified version of Amirza.py (won't work with compiler.py in main directory) 

## Notice:

To convert py file to executable in windows and linux use these commands (in cmd,powershell,terminal or similar):
> cd Amirza

> pyinstaller --onefile --noconsole --icon='.\ProgramFile\Pirate Icon 21.ico' .\compiler.py

To convert ui file to py use below:
> cd ProgramFile

> Pyuic5 -x -o Amirza_ui.py Amirza_ui.ui

![Program Logo](/ProgramFile/Logo.png)
