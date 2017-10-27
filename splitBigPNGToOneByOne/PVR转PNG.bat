@echo off

path %path%;"D:\Program Files (x86)\CodeAndWeb\TexturePacker\bin"

for /f "usebackq tokens=*" %%d in (`dir /s /b *.pvr *.pvr.ccz *.pvr.gz`) do (
TexturePacker.exe "%%d" --sheet "%%~dpnd.png" --data "%%~dpnd.plist" --opt RGBA8888 --allow-free-size --algorithm Basic --no-trim --dither-fs
)

pause