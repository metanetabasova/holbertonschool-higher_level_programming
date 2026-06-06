#!/usr/bin/python3
import os

def create_report(template_text, output_filename, user_name, date_str):
    try:
        updated_text = template_text.replace("{NAME}", user_name)
        updated_text = updated_text.replace("{DATE}", date_str)
        
        if os.path.exists(output_filename):
            print(f"Xəta: '{output_filename}' adlı fayl artıq mövcuddur.")
            return False
            
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(updated_text)
        
        print(f"Uğurlu: Hesabat '{output_filename}' faylına yazıldı.")
        return True

    except PermissionError:
        print("Xəta: Fayla yazmaq üçün kifayət qədər icazəniz yoxdur.")
    except TypeError as e:
        print(f"Tip xətası baş verdi: {e}")
    except Exception as e:
        print(f"Gözlənilməz bir xəta baş verdi: {e}")
        
    return False
