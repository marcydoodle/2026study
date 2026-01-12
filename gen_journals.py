import os
import json

def generate_daily_journals(roadmap_path):
    # Check if roadmap exists
    if not os.path.exists(roadmap_path):
        print(f"❌ Error: {roadmap_path} not found. Please complete Step 2 first.")
        return

    # Load the full 52-week data
    with open(roadmap_path, 'r') as f:
        data = json.load(f)

    count = 0
    for week_entry in data['weeks']:
        week_num = week_entry['week']
        math_topic = week_entry['math_topic']
        
        # Iterate through each day defined in the JSON
        for day, task in week_entry['math_daily'].items():
            # Create a standardized filename: week_01_mon.md
            filename = f"week_{week_num:02}_{day.lower()}.md"
            filepath = os.path.join("journals", filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# Week {week_num} - {day}\n\n")
                f.write(f"## 📅 Overview\n")
                f.write(f"- **Math Topic:** {math_topic}\n")
                f.write(f"- **Security Module:** {week_entry['security']}\n")
                f.write(f"- **Python Milestone:** {week_entry['python']}\n\n")
                
                f.write(f"## 🔢 Today's Math Task\n")
                f.write(f"{task}\n\n")
                
                f.write(f"---\n\n")
                f.write(f"## 📓 Research & Logic Journal\n")
                f.write(f"### 1. Technical Summary\n")
                f.write(f"*What specific technical steps did you take today?*\n\n")
                
                f.write(f"### 2. The Golden Rule (Math-Security Link)\n")
                f.write(f"*How does the math unit above (e.g., {math_topic}) apply to the security concepts you studied?*\n\n")
                
                f.write(f"### 3. PhD Research Connection\n")
                f.write(f"*How does this topic relate to long-term research or high-level academic theory?*\n")
            
            count += 1
    
    print(f"🚀 Success! Generated {count} daily journal templates in the '/journals' folder.")

if __name__ == "__main__":
    generate_daily_journals('roadmap.json')