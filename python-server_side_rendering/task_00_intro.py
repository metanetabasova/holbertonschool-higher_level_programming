#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    # 1. Giriş Tiplərinin Yoxlanılması (Invalid Input Types)
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
        
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # 2. Boş Girişlərin Yoxlanılması (Empty Template & Empty List)
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. İştirakçıların Emal Edilməsi və Faylların Yaradılması
    for index, attendee in enumerate(attendees, start=1):
        try:
            # Şablonun nüsxəsini çıxarırıq
            invitation_text = template

            # Əvəzlənəcək bütün placeholder-lərin siyahısı
            placeholders = ["name", "event_title", "event_date", "event_location"]

            for key in placeholders:
                # Əgər açar yoxdursa və ya dəyəri None-dırsa, "N/A" ilə əvəzlənir
                val = attendee.get(key)
                if val is None:
                    val = "N/A"
                
                # Şablondakı yerliyi ({name}, {event_title} və s.) real dəyərlə dəyişirik
                invitation_text = invitation_text.replace(f"{{{key}}}", str(val))

            # Çıxış faylının adı (output_1.txt, output_2.txt və s.)
            output_filename = f"output_{index}.txt"

            # Təhlükəsizlik: os.path.exists ilə faylın öncədən mövcudluğunu yoxlayırıq
            if os.path.exists(output_filename):
                continue

            # Faylın daxilinə yazılması
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(invitation_text)

        except Exception as e:
            print(f"An error occurred while processing attendee {index}: {e}")
