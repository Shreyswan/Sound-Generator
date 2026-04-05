
# --- SETUP ---
fs = 44100
delay = 0.15

# --- DURATIONS ---
bass_dur = 0.5
song_dur = 0.4

# Frequency Maps
N = {
    'C4': 261.63, 'D4': 293.66, 'E4': 329.63,
    'F4': 349.23, 'G4': 392.00, 'A4': 440.00,
    'B4': 493.88, 'C5': 523.25, 'D5': 587.33,
    'E5': 659.25, 'F5': 698.46, 'A5': 880.00
}

B = {
    'B_C3': 130.81, 'B_D3': 146.83, 'B_E3': 164.81,
    'B_F3': 174.61, 'B_G3': 196.00, 'B_A3': 220.00,
    'B_B3': 246.94, 'B_C4': 261.63, 'B_D4': 293.66,
    'B_E4': 329.63, 'B_F4': 349.23, 'B_A4': 440.00
}

# ================== SAVED MUSIC: ==================
# STARTUP SOUND:
# bass_notes = [B['B_C3'], B['B_A4']]
# bass_samples = []
# for n in bass_notes:
#     # Each bass note lasts 0.8 seconds
#     bass_samples.extend(generate_note(n, duration=bass_dur, volume=0.5, waveform="sine"))

# bass_notes_2 = [0, 0, 0, B['B_F3'], B['B_F4'], 0, 0, 0, B['B_F3'], B['B_F4'], B['B_C3']]
# bass_samples_2 = []
# for n in bass_notes_2:
#     # Each bass note lasts 0.8 seconds
#     bass_samples_2.extend(generate_note(n, duration=0.3, volume=0.5, waveform="sine"))

# melody = [0, 0, 0, N['C4']]


# GAME SOUND:
# melody = [N['C4'], N['D5'], N['A5'], N['F5'], N['D5'], N['C4'], N['D5'], N['F5']]
# melody_2 = [N['C4'], 0, 0, 0, 0, N['C4']]


# THIS IS MELODY FOR INTENSE GAMEPLAY MOMENT (TO BE PLAYED WITH DUR = 0.1)
# melody = [N['A5'], N['A4'], N['C4'], N['B4'], N['C4'], N['A5'], 
#           N['C4'], N['C4'], N['C5'],
#           N['A5'], N['A4'], N['C4'], N['B4'], N['C4'], N['A5']]