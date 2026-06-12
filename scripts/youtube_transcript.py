from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path
import sys

if len(sys.argv) < 3:
    print("Usage: python scripts/youtube_transcript.py <video_id> <expert_name>")
    sys.exit(1)

video_id = sys.argv[1]
expert_name = sys.argv[2]

transcript = YouTubeTranscriptApi().fetch(video_id)
output_path = Path(__file__).resolve().parent.parent / "youtube-transcripts" / f"{expert_name}-{video_id}.md"
youtube_url = f"https://www.youtube.com/watch?v={video_id}"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"# {expert_name} YouTube Transcript\n\n")
    f.write(f"**Expert:** {expert_name}\n\n")
    f.write(f"**Video ID:** {video_id}\n\n")
    f.write(f"**YouTube Link:** {youtube_url}\n\n")
    f.write("## Transcript\n\n")

    for item in transcript:
        text = item["text"] if isinstance(item, dict) else item.text
        f.write(text + "\n")

print(f"Saved transcript for {video_id} to {output_path}")
