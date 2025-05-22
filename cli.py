# cli.py

from research_engine import run_research

if __name__ == "__main__":
    query = input("What can I help you research? ")
    response = run_research(query)

    print("\n📌 Topic:", response.topic)
    print("\n🧠 Summary:", response.summary)
    print("\n📚 Sources:")
    for src in response.sources:
        print("-", src)
    print("\n🛠️ Tools Used:", ", ".join(response.tools_used))
