#!/usr/bin/bash

# MySQL istifadeci adini qeyd
USER="istifadeci_adi"

# Şifrəni daxil etmək üçün (-p) skript səndən şifrə istəyəcək
mysql -u $USER -p -e "SHOW DATABASES;"
