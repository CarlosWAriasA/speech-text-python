import speech_recognition as sr

recognizer = sr.Recognizer()

# Duración de cada segmento en segundos
segment_duration = 30

# Nombre del archivo de salida
output_file = 'texto_reconocido.txt'

with sr.AudioFile('audio.wav') as source:
    total_duration = source.DURATION
    start_time = 0

    # Variable para acumular todo el texto
    full_text = ""

    while start_time < total_duration:
        # Establecer los límites de tiempo para el segmento actual
        end_time = min(start_time + segment_duration, total_duration)

        # Extraer el segmento de audio
        audio = recognizer.record(source, duration=end_time - start_time, offset=start_time)

        try:
            print("Leyendo el segmento...")
            text = recognizer.recognize_google(audio, language='es-ES')
            print(text)

            # Agregar el texto del segmento a la variable de texto completa
            full_text += text + ' '

        except sr.UnknownValueError:
            print("No se pudo entender el segmento.")
        except sr.RequestError as e:
            print("Error en la solicitud:", e)

        # Actualizar el inicio del próximo segmento
        start_time += segment_duration
        print(start_time)

# Dividir el texto en líneas cada 100 caracteres
formatted_text = ''
for i in range(0, len(full_text), 100):
    formatted_text += full_text[i:i + 100] + '\n'

# Escribir todo el texto formateado en el archivo de salida
with open(output_file, 'w') as file:
    file.write(formatted_text)

print("Texto guardado en 'texto_reconocido.txt'.")
