import matplotlib.pyplot as plt
import string
from collections import Counter

class CipherAnalysis:
    def __init__(self, full_name):
        self.full_name = full_name

    def kamasutra_cipher(self):
        key = "w i r l z u b j q y c v f a x d m t e s n p g o k h"
        mapping = dict(zip(string.ascii_lowercase, key.split()))
        encrypted_text = ''.join([mapping.get(char, char) for char in self.full_name.lower()])
        return encrypted_text

    def caesar_cipher(self, shift=11):
        def shift_char(char):
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                return chr((ord(char) - base + shift) % 26 + base)
            return char

        encrypted_text = ''.join([shift_char(char) for char in self.full_name])
        return encrypted_text

    def frequency_analysis(self, text):
        frequencies = Counter(text)
        return frequencies

    def plot_histogram(self, frequencies):
        letters = list(frequencies.keys())
        counts = list(frequencies.values())
        percentages = [(count / len(self.full_name)) * 100 for count in counts]

        plt.bar(letters, percentages)
        plt.xlabel('Letters')
        plt.ylabel('Percentage')
        plt.title('Frequency Analysis')
        plt.show()

# Example usage:
full_name = "Mohamed Afrith Khan"  # Replace with your actual full name
cipher_analysis = CipherAnalysis(full_name)

# Kamasutra Cipher
kamasutra_cipher_text = cipher_analysis.kamasutra_cipher()
print(f"Kamasutra Cipher Text: {kamasutra_cipher_text}")
# Caesar Cipher
caesar_cipher_text = cipher_analysis.caesar_cipher(shift=11)
print(f"Caesar Cipher Text: {caesar_cipher_text}")

# Frequency Analysis
frequency_result = cipher_analysis.frequency_analysis(caesar_cipher_text)
print("Frequency Analysis:")
print(frequency_result)

# Plot Histogram
cipher_analysis.plot_histogram(frequency_result)
