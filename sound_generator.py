import array
import math
import pyaudio
import wave
import struct

from config import *

def export_wav(filename, samples, fs=44100):
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setparams((1, 2, fs, len(samples), 'NONE', 'not compressed'))
        for s in samples:
            s = max(-1.0, min(1.0, s))
            int_sample = int(s * 32767)
            wav_file.writeframes(struct.pack('h', int_sample))

    print(f"File saved successfully as {filename}")

def generate_note(freq, duration, volume=0.1, waveform="square"):
    fs = 44100
    num_samples = int(fs * duration)
    samples = []
    
    for k in range(num_samples):
        # 1. Choose Waveform
        t = 2 * math.pi * k * freq / fs
        if waveform == "sine":
            val = math.sin(t)
        elif waveform == "square":
            val = 1.0 if math.sin(t) > 0 else -1.0
        elif waveform == "saw":
            val = 2.0 * (k * freq / fs - math.floor(0.5 + k * freq / fs))
            
        # 2. Add an Envelope (The secret sauce!)
        # This makes the note fade out so it doesn't "click"
        envelope = (num_samples - k) / num_samples  # Linear fade out
        
        samples.append(val * volume * envelope)
        
    return samples

def get_sequence(melody:list, wave:str, duration:float, volume:float):
    sequence = []
    for note_freq in melody:
        sequence.extend(generate_note(note_freq, 
                                      duration=duration, 
                                      volume=volume, 
                                      waveform=wave))
    
    return sequence

def sampler(tunes:dict):
    for key in tunes:
        p = pyaudio.PyAudio()
        components = list(tunes[key].keys())
        seq_list = []
        for comp in components:
            seq = get_sequence(tunes[key][comp]["tune"], 
                               tunes[key][comp]["wave"], 
                               duration=tunes[key][comp]["duration"],
                               volume=tunes[key][comp]["volume"])
            delay_samples = int(fs * tunes[key][comp]["delay"])
            silence = [0.0] * delay_samples
            seq = silence + seq

            seq_list.append(seq)
        
        mixed_sequence = list(map(sum, zip(*seq_list)))
        print(len(mixed_sequence))
        max_val = max(abs(x) for x in mixed_sequence)
        if max_val > 1.0:
            mixed_sequence = [x / max_val for x in mixed_sequence]

        output_bytes = array.array('f', mixed_sequence).tobytes()
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
        stream.write(output_bytes)
        stream.stop_stream()
        stream.close()
        p.terminate()

        export_wav(key+'.wav', mixed_sequence)

tunes_dict = {
    "startup_tune": {
        "bass_1": {"tune": [B['B_C3'], B['B_A4']],
                   "wave": "sine",
                   "duration": 1.8,
                   "volume": 0.5,
                   "delay": 0},

        "bass_2": {"tune": [0, 0, 0, B['B_F3'], B['B_F4'], 
                            0, 0, 0, B['B_F3'], B['B_F4'], B['B_C3'], B['B_A4']],
                   "wave": "sine",
                   "duration": 0.3,
                   "volume": 0.5,
                   "delay": 0},
    },

    "game_tune":{
        "lead_1": {"tune": [N['C4'], N['D5'], N['A5'], N['F5'], 
                            N['D5'], N['C4'], N['D5'], N['F5'], 0,
                            N['A5'], N['A5'], N['C4'], N['D5'],
                            N['F5'], N['D5'], N['C4'], 0],
                   "wave": "saw",
                   "duration": 0.4,
                   "volume": 0.1,
                   "delay": 0},

        "lead_2": {"tune": [N['C4'], 0, 0, 0, 
                            0, N['C4'], 0, 0, 0,
                            N['A5'], N['A5'], 0, 0,
                            0, 0, 0],
                   "wave": "saw",
                   "duration": 0.4,
                   "volume": 0.1,
                   "delay": 0.2}
    }
}

sampler(tunes=tunes_dict)

