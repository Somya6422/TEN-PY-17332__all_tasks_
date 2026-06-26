print("===== SMART TEMPERATURE ADVISOR =====")
temp = float(input("Enter current temperature in °C: "))

if temp < 0:
    advice = "❄ Freezing! Stay indoors and wear heavy clothing."
elif 0 <= temp <= 15:
    advice = "🧥 Cold weather. A jacket is recommended."
elif 16 <= temp <= 25:
    advice = "🌤 Pleasant weather! Great for outdoor activities."
elif 26 <= temp <= 35:
    advice = "☀ Hot weather. Stay hydrated and use sunscreen."
else:
    advice = "🔥 Extreme heat! Avoid going outside if possible."

print("\nTemperature Advice:")
print(advice)
