# ABOUT Dolist1r:
Dolist1r là một công cụ liệt kê tên miền phụ (subdomain enumeration) đơn giản và hiệu quả, 
được thiết kế để giúp các nhà kiểm thử xâm nhập (penetration testers) và thợ săn lỗi (bug hunters) 
tìm kiếm các tên miền phụ của một trang web mục tiêu bằng phương pháp bruteforce.

# Installation:
```bash
https://github.com/dungkhac111/Dolist1r.git
```
# Recommended Python Version:
Dolist1r hỗ trợ cho Python 2 và Python 3.

# Module:
Dolist1r phụ thuộc vào module của Python dnspython và argpare.

**dnspython Module**
* Install for Windows:
```bash
c:\python27\python.exe -m pip install dnspython
```
* Install for Ubuntu/Debian:
```bash
sudo apt-get install python-dnspython
```
* Install using pip on Linux:
```bash
sudo pip install dnspython
```

**argparse Module**
* Install for Ubuntu/Debian:
```bash
sudo apt-get install python-argparse
```
* Install using pip on Linux:
```bash
sudo pip install argparse
```

#Usage
-d hoặc --domain: Tên miền mục tiêu.
-w hoặc --wordlist: Đường dẫn đến tệp wordlist.

#Examples
*Quét các tên miền mục tiêu từ tệp wordlist:
```bash
python dolist1r.py -d example.com -w wordlist.txt
```
