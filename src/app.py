import gradio as gr
from dotenv import load_dotenv
from crew import VibeCheckCrew

# Load environment variables (SERPER_API_KEY, GEMINI_API_KEY, etc.)
load_dotenv()

# Initialize crew
crew = VibeCheckCrew().crew()

def run_vibecheck(image_url, city):
    """
    Runs the vibecheck pipeline:
    - Vision Analyst analyzes vibe from image URL
    - Venue Finder searches for similar places in the given city
    - Recommender packages the results
    """
    if not image_url:
        return ["Please provide an image URL first."]

    task_input = {"city": city, "image": image_url}
    result = crew.kickoff(inputs=task_input)

    # Normalize output
    venues = []
    if isinstance(result, str):
        venues = [{"name": line, "link": "", "snippet": ""} for line in result.splitlines() if line.strip()]
    elif isinstance(result, dict):
        venues = result.get("venues", [])
    elif isinstance(result, list):
        venues = result
    else:
        venues = [{"name": str(result), "link": "", "snippet": ""}]

    return venues

def display_cards(venues):
    """Convert venue dicts into card-style markdown for display."""
    if isinstance(venues, str):
        return venues

    cards = []
    for v in venues:
        name = v.get("name", "Unknown Venue")
        link = v.get("link", "")
        snippet = v.get("snippet", "")

        if link:
            title = f"### [{name}]({link})"
        else:
            title = f"### {name}"

        card = f"{title}\n\n{snippet}\n"
        cards.append(card)

    return "\n---\n".join(cards)

with gr.Blocks() as demo:
    gr.Markdown("# 🍸 VibeCheck: Find your vibe in the city")
    gr.Markdown("Paste a photo URL of a restaurant/bar you like, and we'll find similar spots nearby.")

    with gr.Row():
        image_url = gr.Textbox(label="Image URL (must be publicly accessible)")
        city = gr.Textbox(value="Chicago", label="City")

    run_btn = gr.Button("Find Similar Places")
    output = gr.Markdown(label="Recommendations")

    run_btn.click(
        fn=lambda url, c: display_cards(run_vibecheck(url, c)),
        inputs=[image_url, city],
        outputs=[output]
    )

if __name__ == "__main__":
    demo.launch()
