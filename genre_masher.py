#!env python2
import random


genres = {
    "Action": [
        "Platformer",
        "Shooter",
        "Fighting",
        "Beat 'em up",
        "Stealth",
        "Survival",
        "Rhythm" ],

    "Action-adventure": [
        "Survival horror",
        "Metroidvania" ],

    "Adventure": [
        "Text adventures",
        "Graphic adventures",
        "Visual novels",
        "Interactive movie",
        "Real-time 3D adventures" ],

    "Role-playing": [
        "Action RPG",
        "MMORPG",
        "Roguelikes",
        "Tactical RPG",
        "Sandbox RPG",
        "First-person party-based RPG",
        "Cultural differences",
        "Choices",
        "Fantasy" ],

    "Simulation": [
        "Construction and management simulation",
        "Life simulation",
        "Vehicle simulation" ],

    "Strategy": [
        "4X",
        "Artillery",
        "Real-time strategy (RTS)",
        "Real-time tactics (RTT)",
        "Multiplayer online battle arena (MOBA)" ],

    "Tower defense": [
        "Turn-based strategy (TBS)",
        "Turn-based tactics (TBT)" ],

    "War": [
        "Grand strategy war",
        "play-fighting",
        "paintball" ],

    "Sports": [
        "Racing",
        "Sports",
        "Competitive",
        "Sports-based fighting" ],

    "Purpose": [
        "Advertising",
        "Art",
        "Casual",
        "Christian",
        "Educational",
        "Esports",
        "Exer",
        "Personalized",
        "Serious",
        "Casual",
        "Party",
        "Programming",
        "Logic",
        "Trivia",
        "Board  or card" ],
}


num_genres = len(genres)-1
out = []
for i in range(0, 3):
    G = random.choice(genres.values())
    S = random.choice(genres.keys())
    out.append(random.choice(G))

print(" ".join(out[::-1]))
