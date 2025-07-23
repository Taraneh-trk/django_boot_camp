
---

# یه چیش کمه!

هر زبانی پر از شگفتی است. یکی از این شگفتی‌ها جمله‌ای است که شامل **تمام حروف الفبای** آن زبان باشد.

در این مسئله، می‌خواهیم بررسی کنیم آیا جمله‌ی ورودی شامل **تمام حروف الفبای زبان انگلیسی** هست یا خیر.

### شرایط خروجی:

* اگر جمله‌ی ورودی شامل **تمام ۲۶ حرف الفبای انگلیسی** باشد، خروجی باید به صورت زیر باشد:

  ```
  Contains all letters!
  ```

* اگر جمله‌ی ورودی **شامل تمام حروف نباشد**، خروجی به صورت زیر خواهد بود:

  ```
  Does not contain all letters and n letters are missing!
  ```

که در آن `n` تعداد حروفی است که در جمله وجود ندارند.

---

## ورودی

در تنها سطر ورودی، **یک جمله** دریافت می‌شود.

> (توجه: ورودی ممکن است خالی باشد!)

---

## خروجی

* اگر ورودی یک **پانگرام** باشد:

  ```
  Contains all letters!
  ```

* در غیر این صورت:

  ```
  Does not contain all letters and n letters are missing!
  ```

---

## مثال‌ها

### ورودی نمونه ۱

```
The quick brown fox jumps over a lazy dog.
```

### خروجی نمونه ۱

```
Contains all letters!
```

---

### ورودی نمونه ۲

```
Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. 
```

### خروجی نمونه ۲

```
Does not contain all letters and 4 letters are missing!
```

---

