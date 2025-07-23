
---

## 🐧 نبرد دسترسی‌ها – دستورها در فایل `solution.sh`

```bash
#!/bin/bash

# ساخت گروه shared
groupadd shared

# ساخت یوزر user1 و اضافه کردن به گروه shared
useradd -m -G shared user1

# ساخت یوزر user2 و اضافه کردن به گروه shared
useradd -m -G shared user2

# ساخت دایرکتوری shared_files در روت
mkdir /shared_files

# ساخت فایل shared_file درون آن
touch /shared_files/shared_file

# تغییر مالک فایل و دایرکتوری به user1 و گروه shared
chown user1:shared /shared_files
chown user1:shared /shared_files/shared_file

# تنظیم دسترسی: فقط کاربر و گروه بتوانند بخوانند و بنویسند، بقیه هیچ‌گونه دسترسی نداشته باشند
chmod 660 /shared_files/shared_file
chmod 770 /shared_files  # برای دسترسی به دایرکتوری، اجرای آن لازم است

# حذف کاربران و گروه و فایل‌ها (برای پاکسازی نهایی)
userdel user1
userdel user2
groupdel shared
rm -rf /shared_files
```

---

## ⚠️ نکات مهم:

* `useradd -m` باعث ایجاد دایرکتوری خانه برای هر کاربر می‌شود.
* `-G shared` برای افزودن کاربر به گروه `shared`.
* `chmod 660` → فقط owner و group اجازه خواندن و نوشتن دارند.
* `chmod 770` برای دایرکتوری به user1 و shared group اجازه اجرای دایرکتوری را می‌دهد.
* `rm -rf` برای حذف کامل دایرکتوری و فایل‌ها.
* دستور `usermod` و `cd` استفاده نشده‌اند.

---
