import os
import subprocess
import sounddevice as sd
import scipy.io.wavfile as wav

def grabar_audio_mp3(nombre_archivo="mic_audios/audio_5s.mp3", duracion=5, frecuencia=48000, canales=1):
    archivo_temp = "temp.wav"

    print(f"Grabando durante {duracion} segundos...")
    
    # Usamos 1 canal (mono) y 48000 Hz
    audio_datos = sd.rec(int(duracion * frecuencia), samplerate=frecuencia, channels=canales, dtype='int16')
    sd.wait()
    
    print("Grabación finalizada. Convirtiendo a MP3 con FFmpeg...")

    wav.write(archivo_temp, frecuencia, audio_datos)

    # Convertir a MP3 usando FFmpeg
    subprocess.run(
        ["ffmpeg", "-y", "-i", archivo_temp, "-b:a", "192k", nombre_archivo],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )

    if os.path.exists(archivo_temp):
        os.remove(archivo_temp)

    print(f"¡Audio guardado exitosamente como '{nombre_archivo}'!")

if __name__ == "__main__":
    grabar_audio_mp3()
