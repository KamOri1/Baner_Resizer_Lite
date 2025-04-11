import cv2

# Otwórz plik wideo
video = cv2.VideoCapture('nazwa_pliku_wideo.mp4')  # Zastąp 'nazwa_pliku_wideo.mp4' rzeczywistą nazwą pliku

# Sprawdź, czy wideo zostało otwarte pomyślnie
if not video.isOpened():
    print("Błąd podczas otwierania pliku wideo")
else:
    frame_count = 0  # Inicjalizacja licznika klatek
    desired_frame_number = 8  # Numer klatki, którą chcemy pobrać

    while True:
        ret, frame = video.read()  # Odczytaj klatkę

        if not ret:
            # Jeśli nie można odczytać klatki (np. koniec wideo), zakończ pętlę
            break

        frame_count += 1  # Zwiększ licznik klatek

        if frame_count == desired_frame_number:
            # Jeśli to jest 8 klatka, zapisz ją
            output_filename = 'klatka_8.jpg'
            cv2.imwrite(output_filename, frame)
            print(f"Klatka {desired_frame_number} zapisana jako {output_filename}")
            break  # Zakończ pętlę po zapisaniu klatki

    # Zwolnij obiekt przechwytywania wideo
    video.release()