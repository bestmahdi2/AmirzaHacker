# AmirzaHacker
Python program with GUI to examine all possible answers for Amirza and similar Games

این یک برنامه گرافیکی برای پیدا کردن تمامی حالت های ممکن جواب بازی هایی مثل آمیرزا است.

***
If your not a developer just download the RAR file, extract it and open the compiler.exe

اگر برنامه نویس نیستید فقط فایل رار رو دانلود کنید و بعد از اسختراج فایل اجرایی رو باز کنید.
****

Otherwise, you may want to translate Persian letters with yours and replace Moin.db with the English words database.

/Main directory/

Compiler.py: just a script to connect python to Qt, and a little smarter.

Moin.db: Persian words database.


/Programfiles/

Amirza_ui.ui: GUI designed with PyQt5 designer.

Amirza_ui.py: generated from the UI file.

Amirza.py: main program.


Rememmber :

To convert py file to executable in windows and linux use command like below (in cmd,powershell,terminal or similar):
> cd Amirza
> pyinstaller --onefile --noconsole --icon='.\ProgramFile\Pirate Icon 21.ico' .\compiler.py

To convert ui file to py use below:
> cd ProgramFile
> Pyuic5 -x -o Amirza_ui.py Amirza_ui.ui

