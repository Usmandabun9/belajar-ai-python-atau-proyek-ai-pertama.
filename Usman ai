import random

class SimpleAI:
    def __init__(self):
        self.knowledge_level = 1
        self.experience_points = 0

    def learn(self):
        # Simulasi AI belajar hal baru
        gain = random.randint(10, 30)
        self.experience_points += gain
        print(f"🤖 AI sedang belajar... Mendapat {gain} poin pengalaman.")
        
        if self.experience_points >= 100:
            self.knowledge_level += 1
            self.experience_points = 0
            print(f"🌟 Evolusi! AI sekarang berada di Level {self.knowledge_level}")

# Jalankan simulasi
my_ai = SimpleAI()
for i in range(5):
    my_ai.learn()

print(f"\nStatus Akhir: AI Usmandabun9 berada di Level {my_ai.knowledge_level}")
