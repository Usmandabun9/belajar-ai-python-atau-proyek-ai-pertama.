import random
import json
from typing import Tuple

class SimpleAI:
    def __init__(
        self,
        knowledge_level: int = 1,
        experience_points: int = 0,
        level_threshold: int = 100,
        min_gain: int = 10,
        max_gain: int = 30,
        seed: int | None = None,
    ) -> None:
        if seed is not None:
            random.seed(seed)
        self.knowledge_level = knowledge_level
        self.experience_points = experience_points
        self.level_threshold = level_threshold
        self.min_gain = min_gain
        self.max_gain = max_gain

    def learn(self) -> Tuple[int, int]:
        """
        Simulate learning once.
        Returns a tuple (gain, levels_gained).
        """
        gain = random.randint(self.min_gain, self.max_gain)
        self.experience_points += gain

        levels_gained = 0
        # Handle multiple level-ups if experience exceeds multiple thresholds
        while self.experience_points >= self.level_threshold:
            self.knowledge_level += 1
            self.experience_points -= self.level_threshold
            levels_gained += 1

        return gain, levels_gained

    def to_dict(self) -> dict:
        return {
            "knowledge_level": self.knowledge_level,
            "experience_points": self.experience_points,
            "level_threshold": self.level_threshold,
            "min_gain": self.min_gain,
            "max_gain": self.max_gain,
        }

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls, path: str) -> "SimpleAI":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(**data)

    def __repr__(self) -> str:
        return (
            f"SimpleAI(level={self.knowledge_level}, xp={self.experience_points}/"
            f"{self.level_threshold})"
        )


if __name__ == "__main__":
    ai = SimpleAI(seed=42)  # seed untuk reproducibility saat testing
    for i in range(5):
        gain, leveled = ai.learn()
        if leveled:
            print(f"🤖 Belajar... +{gain} XP -> naik {leveled} level! Sekarang Level {ai.knowledge_level}")
        else:
            print(f"🤖 Belajar... +{gain} XP -> Level tetap {ai.knowledge_level} (XP {ai.experience_points}/{ai.level_threshold})")

    print(f"\nStatus Akhir: {ai}")
    # contoh simpan:
    # ai.save("ai_state.json")
