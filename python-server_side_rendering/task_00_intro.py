#!/usr/bin/python3
import os

def generate_invitations(template_path, attendees_path, output_dir):
    if not isinstance(template_path, str) or not isinstance(attendees_path, str) or not isinstance(output_dir, str):
        print("Invalid input types.")
        return

    if not os.path.exists(template_path):
        print(f"Template file not found: {template_path}")
        return

    if not os.path.exists(attendees_path):
        print(f"Attendees file not found: {attendees_path}")
        return

    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        if not template_content.strip():
            print("Template is empty.")
            return

        with open(attendees_path, 'r', encoding='utf-8') as f:
            attendees_content = f.read()

        import json
        try:
            data = json.loads(attendees_content)
            attendees = data.get("attendees", []) if isinstance(data, dict) else data
        except Exception:
            import ast
            try:
                data = ast.literal_eval(attendees_content)
                attendees = data.get("attendees", []) if isinstance(data, dict) else data
            except Exception:
                print("Invalid attendees format.")
                return

        if not isinstance(attendees, list):
            print("Attendees should be a list.")
            return

        if not attendees:
            print("No attendees found.")
            return

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for attendee in attendees:
            if not isinstance(attendee, dict) or "name" not in attendee or "event" not in attendee:
                print("Invalid attendee format or missing data.")
                continue

            name = attendee.get("name", "Guest")
            event = attendee.get("event", "Event")

            invitation_text = template_content.replace("{name}", name).replace("{event}", event)

            file_name = f"{name.replace(' ', '_')}_invitation.txt"
            output_file_path = os.path.join(output_dir, file_name)

            if os.path.exists(output_file_path):
                continue

            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(invitation_text)

    except Exception as e:
        print(f"An error occurred: {e}")
