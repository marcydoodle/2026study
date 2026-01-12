import json
import os

def update_json_with_japanese():
    # The Japanese Learning Plan list provided
    jp_topics_raw = """
    Hiragana A-O
    Hiragana KA-KO
    Hiragana SA-SO
    Hiragana TA-TO
    Hiragana NA-NO
    Writing Practice
    Anki Setup
    Hiragana HA-HO
    Hiragana MA-MO
    Hiragana YA-YO
    Hiragana RA-RO
    Hiragana WA-N
    Dakuten (ga, za)
    Hiragana Test
    Katakana A-NO
    Katakana HA-HO
    Katakana MA-YO
    Katakana RA-N
    Long Vowels
    Loanwords
    Core 2k Deck
    Desu / Da
    Negatives (Janai)
    Past Tense (Datta)
    Past Neg (Janakatta)
    Question Particle
    Particles WA/GA
    Grammar Audit
    Particle MO
    Particle NO
    Particle O
    Particle NI/E
    Particle DE
    All Particles
    Anki Review
    I-Adjectives
    I-Adj Conjugation
    Na-Adjectives
    Na-Adj Conjugation
    Adj Vocabulary
    Adj Sentences
    Adj Review
    Ru-Verbs
    U-Verbs
    Irregular Verbs
    Masu Form
    Dictionary Form
    Polite vs Plain
    Verb Recognition
    Verb Neg (Nai)
    Verb Past (Ta)
    Past Neg (Nakatta)
    SOV Structure
    Counting (1-10)
    High Numbers
    Monthly Review
    Kanji 1-10
    Kanji Days
    Kanji Body
    Adverbs
    Locations
    Interrogatives
    Stroke Order
    Give/Receive
    Desiring (~Tai)
    Tari Tari
    Aru/Iru (Exist)
    Counters (~nin)
    Short Stories
    Desmos Practice
    Te-form (Ru-Verbs)
    Te-form (U-Verbs)
    Te-form (Irregular)
    Te-form Connect
    Te-form Requests
    Te-form States
    Te-form Drill
    ~Mo ii (Permission)
    Prohibition (Dame)
    ~Te kara (After)
    N5 Grammar Rev
    N5 Vocab Test
    N5 Listening
    Phase 3 Exam
    Kanji (Nature)
    Kanji (Directions)
    Kanji (Time)
    Potential Form (Ru)
    Potential Form (U)
    "I can..."
    Potential Drills
    Nouns (Koto/No)
    ~N desu (Explain)
    ~To omou (Think)
    ~To iu (Quote)
    Relative Clauses
    Complex Sentences
    Sentence Mod
    Comparison (Yori)
    Superlatives
    ~Tara (If/When)
    ~Ba (Conditional)
    Volitional Form
    Trans/Intransitive
    Trig Graphs
    Particle SHI
    NAGARA (While)
    NODE/KARA
    ~Kana (Wonder)
    Passive Voice
    Causative Voice
    Phase 4 Exam
    Keigo Intro
    Kenjougo
    Business JP
    Formal Phone
    Giving Advice
    ~Te shimau
    Keigo Audit
    ~Sou desu
    ~Rashii
    ~Deshou
    ~Tame ni
    ~Yasui
    Podcasts
    Continuity Audit
    News Reading
    Journaling
    Lang Exchange
    Slang
    Anime No Subs
    Shadowing
    Derivative Quiz
    N4 Grammar Rev
    Kanji Audit
    Immersion Day
    Monologue
    N3 Planning
    Anki Goals
    Passive Voice (Rareru)
    Passive Sentences
    Causative (Make/Let)
    Causative Practice
    Keigo: Intro
    Keigo: Sonkeigo
    Keigo Audit
    Keigo: Kenjougo
    ~Te oku (Prep)
    ~Te shimau (Regret)
    ~Te miru (Try)
    ~Te kuru/iku
    Adverbial ~Ku/Ni
    Particle Audit
    ~Hazu (Expect)
    ~Kamoshirenai
    ~Tame ni (Purpose)
    ~Youni (Order to)
    ~Tsumori (Intent)
    Potential Rev
    Purpose Grammar
    Nouns (Koto/No)
    ~N desu (Explain)
    ~To omou (Think)
    ~To iu (Quote)
    Relative Clauses
    Complex Sent
    Sentence Mod
    Transitive Verbs
    Intransitive Verbs
    Trans/Intrans Pair
    Appearance (~Sou)
    Hearsay (~Sou)
    Likeness (~You)
    Monthly Review
    Comparison
    Superlatives
    ~Tara (If)
    ~Ba (If)
    Volitional Form
    Let's... (Volitional)
    Conditional Audit
    ~Ba yokatta
    ~Noni (Despite)
    ~Shika (Only)
    ~Dake (Just)
    ~Bakari (Just)
    ~Nagara (While)
    Simultaneous
    ~Mono da
    ~Wake da
    ~Temo (Even if)
    ~To shitemo
    ~Uchi ni
    ~Kagiri
    N3 Monologue
    N3 Kanji
    News Reading
    Journaling
    HelloTalk
    Potential Rev
    Passive Rev
    Output Check
    Causative Rev
    Keigo Rev
    Business Phrases
    Phone Call
    Advice Rev
    Regret Rev
    Keigo Audit
    Hearsay (~Sou)
    Hearsay (~Rashii)
    Guess (~Deshou)
    Purpose
    Difficulty
    Podcast
    Podcast Sum
    News Reading
    N2 Kanji
    Immersion
    Speaking
    Monologue
    Future Plan
    Mastery Audit
    Nominalizers
    Opinions
    Quotes
    Clauses
    Complex Sent
    Monologue
    Grammar Final
    Comparison
    Superlative
    Conditional
    Volitional
    Transitive
    News Audit
    N3 Kanji
    Particle SHI
    NAGARA
    NODE/KARA
    ~Kana
    Passive
    Causative
    Output
    Keigo Rev
    Kenjougo
    Business
    Phone
    Advice
    Regret
    Phone
    ~Sou desu
    ~Rashii
    ~Deshou
    ~Tame ni
    ~Yasui
    Podcast
    Summary
    News
    """
    
    # Clean list
    jp_topics = [line.strip() for line in jp_topics_raw.strip().split('\n') if line.strip()]
    
    # Load current roadmap
    with open('roadmap.json', 'r') as f:
        roadmap = json.load(f)
        
    # Distribute topics across 52 weeks (approx 4 per week)
    chunk_size = len(jp_topics) // 52
    remainder = len(jp_topics) % 52
    
    topic_index = 0
    for i in range(len(roadmap['weeks'])):
        current_chunk_size = chunk_size + (1 if i < remainder else 0)
        week_topics = jp_topics[topic_index : topic_index + current_chunk_size]
        roadmap['weeks'][i]['japanese_topics'] = week_topics
        topic_index += current_chunk_size

    # Save updated roadmap
    with open('roadmap.json', 'w') as f:
        json.dump(roadmap, f, indent=4)
    
    print("✅ Roadmap updated with Japanese Learning Plan!")

if __name__ == "__main__":
    update_json_with_japanese()