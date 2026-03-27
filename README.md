# SBU 102: Simple Motivational Video Generator

## What This Project Does

A Python application that creates motivational videos with AI-generated scripts and voiceovers, then combines them with a background video to produce a finished MP4 file.

## How This Docker Project Works

| Step | What Happens | Command | File Location | Where It Happens | Result |
|------|-------------|---------|---------------|------------------|---------|
| 1 | **Clean Up** | `docker system prune -f` | run.sh | Your Computer | Removes old Docker files |
| 2 | **Build Image** | `docker build -t motivational-video-generator .` | run.sh | Docker Engine | Creates container with Python + AI tools |
| 3 | **Get API Key** | `read -p "API Key:" GEMINI_API_KEY` | run.sh | Terminal Prompt | You enter your Google Gemini key |
| 4 | **Run Container** | `docker run --rm -i -v $(pwd):/app` | run.sh | Inside Docker | Container starts with your files |
| 5 | **Generate Video** | `python main.py` | Dockerfile | Inside Container | AI creates script → audio → video |
| 6 | **Save Files** | Volume mount saves output | run.sh | Your Computer | Output files saved to your folder |
| 7 | **Cleanup** | `docker rmi motivational-video-generator` | run.sh | Docker Engine | Removes container, keeps your files |

**Simple Command:** Just run `./run.sh` and Docker handles everything automatically!

## Learning Goals

- Use an API key safely (environment variables)
- Run a project in a reproducible Docker environment
- Generate content using AI APIs

## Files in This Project

- `main.py` - Main Python application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container build instructions
- `run.sh` - Simple script to build and run the project
- `background.mp4` - Your background video (required)
- `README.md` - This instruction file
- `voiceover.mp3` - Generated audio voiceover  
- `final_video.mp4` - Your finished motivational video

## To-Do List

### Setup Tasks
- [ ] Get your free Google Gemini API key from https://aistudio.google.com/app/apikey
- [ ] Add your `background.mp4` file to the project directory
- [ ] Make sure you have the complete API key (starts with `AIzaSy`)

### Running the Project
- [ ] Make script executable: `chmod +x run.sh`  
- [ ] Run the project: `./run.sh`
- [ ] Enter API key when prompted
- [ ] Enter your motivational topic when asked
- [ ] Check your generated `final_video.mp4`

### Optional Improvements
- [ ] Try different background videos
- [ ] Experiment with different motivational topics
- [ ] Test with shorter/longer topics

---

## Quick Start Guide

### Step 1: Get Your FREE Google Gemini API Key

1. **Visit Google AI Studio**: https://aistudio.google.com/app/apikey
2. **Sign in** with your Google account
3. **Create API key** → "Create API key in new project"
4. **Copy your API key** (starts with `AIzaSy`)

### Step 2: Add Your Background Video

You need a `background.mp4` file in this directory.

**Quick options:**
- Download from [Pixabay](https://pixabay.com/videos/) or [Pexels](https://www.pexels.com/videos/)
- Record a 10-30 second video with your phone
- Use any MP4 video you have (just rename it to `background.mp4`)

**Important:** File must be named exactly `background.mp4` in the same folder as `main.py`

### Step 3: Run the Project

Make the script executable and run it:
```bash
chmod +x run.sh
./run.sh
```

**The script will:**
1. Build the Docker container
2. **Prompt you to enter your API key** (it will be visible when you type)
3. Run the application
4. Ask for your motivational topic
5. Generate your video!

**Important:** When entering your API key, make sure you paste the complete key from Google AI Studio.

### Step 4: Check Your Results

After completion, you'll have:
- `script.txt` - Your AI-generated script
- `voiceover.mp3` - The audio narration
- `final_video.mp4` - Your finished motivational video

**To download:** Right-click on `final_video.mp4` → Download

---


## Troubleshooting

**Docker not found?** Make sure you're in a GitHub Codespace or have Docker installed.

**API key errors?** 
- Double-check your key starts with `AIzaSy` 
- Make sure you copied the complete key from https://aistudio.google.com/app/apikey
- Try generating a new API key if the old one doesn't work

**No background.mp4?** The file must exist and be named exactly `background.mp4`.

**Permission denied on run.sh?** Run: `chmod +x run.sh`

**Docker build issues?** Clean up first: `docker system prune -f` then try again.

**Container errors?** Try rebuilding: `docker build -t motivational-video-generator . && ./run.sh`

## Your Generated Files

After running successfully, you'll have:
- `script.txt` - Your AI-generated motivational script
- `voiceover.mp3` - The AI-generated audio narration  
- `final_video.mp4` - Your finished motivational video

**Tip:** To keep multiple videos, rename them after each run:
```bash
mv final_video.mp4 my_motivation_video_1.mp4
```

---

## Understanding .sh vs .yml: Beginner's Guide

### Quick Comparison: Which Should You Use?

| Feature | Bash Script (.sh) | Docker Compose (.yml) |
|---------|-------------------|----------------------|
| **What Is It?** | Shell commands in a file | Container configuration file |
| **Why Use It?** | Easy to learn, flexible | Industry standard, professional |
| **Where Is Code?** | All in `run.sh` | Split: `docker-compose.yml` + `Dockerfile` |
| **Command to Run** | `./run.sh` | `docker compose up --build` |
| **Best For** | Learning Docker basics | Real projects, teams |
| **Our Project** | ✓ Current approach | → Your homework assignment! |

### Detailed Breakdown for This Project

| Step | What Happens | Bash Script (.sh) | Docker Compose (.yml) |
|------|-------------|-------------------|----------------------|
| **Build** | Create Docker image | `docker build -t myapp .` | `build: .` (in YAML) |
| **Environment** | Set API key | `read -p "API Key:" KEY` | `GEMINI_API_KEY=${GEMINI_API_KEY}` |
| **Run** | Start container | `docker run --rm -i -v $(pwd):/app myapp` | `docker compose up` |
| **Cleanup** | Remove containers | Manual cleanup commands | Automatic with `--rm` |
| **File Location** | Everything in `run.sh` | Configuration in `docker-compose.yml` |

### Code Examples

#### Current Bash Script (run.sh)
```bash
#!/bin/bash
echo "Building image..."
docker build -t motivational-video-generator .
read -p "API Key: " GEMINI_API_KEY
docker run --rm -i -v "$(pwd):/app" -e GEMINI_API_KEY="$GEMINI_API_KEY" motivational-video-generator
```

#### Your Homework: Docker Compose (docker-compose.yml)
```yaml
version: '3.8'
services:
  app:
    build: .
    volumes:
      - .:/app
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    stdin_open: true
    tty: true
```

### Why Learn Both?

| Skill Level | Recommended Approach | Reason |
|-------------|---------------------|---------|
| **Beginner** | Start with `.sh` | Easy to understand, see each command |
| **Intermediate** | Learn `.yml` | Industry standard, more maintainable |
| **Professional** | Use `.yml` | Team collaboration, scalability |

**Your Mission:** Use the `.sh` script first, then complete the homework to convert it to `.yml`!

### Pros and Cons

| Feature | Bash Script | Docker Compose |
|---------|-------------|----------------|
| **Learning Curve** | Easy for beginners | Requires YAML knowledge |
| **Flexibility** | Very flexible, any logic | Structured, container-focused |
| **Team Sharing** | Platform dependent | Works everywhere |
| **Industry Standard** | Good for automation | Standard for containers |
| **Error Handling** | Manual error handling | Built-in container management |
| **Documentation** | Comments in code | Self-documenting structure |

---

## Homework Assignment: Convert from .sh to .yml

**Now that you understand both approaches from the comparison table above, it's time to practice!**

**Your Challenge:** Convert your working `run.sh` script to a professional `docker-compose.yml` file.

**Why This Matters:** 
- Real companies use Docker Compose, not bash scripts
- You'll understand both beginner and professional approaches
- Great for your resume and job interviews

### Your Assignment

Create a `docker-compose.yml` file that replaces `run.sh` completely. Use the code examples from the comparison table above as your starting point.

### What You Need to Convert

Currently `run.sh` does these steps:
1. Clean up old containers: `docker system prune -f`
2. Build image: `docker build -t motivational-video-generator .`
3. Get API key from user input
4. Run container: `docker run --rm -i -v $(pwd):/app -e GEMINI_API_KEY="$API_KEY" motivational-video-generator`
5. Clean up: `docker rmi motivational-video-generator`

### Hints for Your docker-compose.yml

```yaml
version: '3.8'
services:
  app:
    build: .
    volumes:
      - .:/app
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    stdin_open: true
    tty: true
```

### Challenge Requirements

1. **Create** `docker-compose.yml` that builds and runs the app
2. **Test** that `docker compose up --build` works
3. **Compare** the command simplicity:
   - Old way: `./run.sh` (but script has 30+ lines)
   - New way: `GEMINI_API_KEY="your-key" docker compose up --build`

### Bonus Points

- How would you handle the cleanup automatically?
- Can you make the API key input more user-friendly?
- What other Docker Compose features could improve this project?

### Expected Learning Outcomes

After completing this homework, you should understand:
- Docker Compose vs bash scripts for container management
- YAML syntax for defining services
- Environment variable handling in containers
- Volume mounting for file sharing
- When to use Compose vs single containers

**Time Estimate:** 30-60 minutes  
**Difficulty:** Intermediate  
**Submit:** Your working `docker-compose.yml` file

### Solution Testing

Your solution works if:
1. `docker compose up --build` builds the image
2. The container runs and asks for motivational topic
3. Video files are created in your host directory
4. Container stops cleanly after completion

Good luck!
