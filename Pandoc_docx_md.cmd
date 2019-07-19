:: using Pandoc to convert docx to markdown while also extracting the images
@echo off
@echo "----using Pandoc to convert docx to markdown while also extracting the images----"
set /p filename="Please give filename path: "
pandoc -f docx -t markdown  --extract-media="." -o "file.md" %filename%
