---
title: Tanglarity Stability AI
emoji: 🧠
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: "1.45.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# Tanglarity: Stability AI

> An AI assisted stabilization app designed to help overwhelmed users reduce cognitive overload, identify their current phase, and move toward manageable action.

## Table of Contents

* [Pitch](#pitch)
* [Summary](#summary)
* [Live Demo](#live-demo)
* [Demo Preview](#demo-preview)
* [Problem Being Solved](#problem-being-solved)
* [Intended Audience](#intended-audience)
* [How To Use The App](#how-to-use-the-app)
* [Stabilization Phases](#stabilization-phases)
* [Current Features](#current-features)
* [Prompt Engineering](#prompt-engineering)
* [System Prompt](#system-prompt)
* [Grounding](#grounding)
* [Build Log / Development Timeline](#build-log--development-timeline)
* [Evaluation](#evaluation)
* [Honest Limits](#honest-limits)
* [Originality and Ownership](#originality-and-ownership)
* [AI Tools and Technologies Used](#ai-tools-and-technologies-used)
* [Future Improvements](#future-improvements)
* [Final Reflection](#final-reflection)

---

## Pitch

Tanglarity is an AI assisted stabilization app that helps overwhelmed users identify their current phase whether survival, stabilization, organization, growth or somewhere in between to reduce cognitive overload, and move toward realistic action closing the gap between knowing what to do and actually being able to do it.

---

## Summary

Tanglarity is built around the idea that people often know what they should do, but still struggle to act when they are overwhelmed, scattered, frozen, or overloaded.

Stability AI is the first working module inside Tanglarity. It uses a calming interface, structured inputs, stabilization phases, progress sliders, and constrained AI style responses to help users slow down and identify one manageable next step.

The project is designed to help users understand not only the phases themselves, but how each phase builds upon the next. It intentionally avoids skipping stabilization simply to chase productivity because instability often creates cycles of overwhelm, avoidance, and unfinished systems.

---

## Live Demo

https://huggingface.co/spaces/LindseyB1/tanglarity-stability-ai

---

## Demo Preview

Add GIF or screenshot files to the repository and update filenames below.

![Tanglarity Welcome Experience](tanglarity-demo_2.gif)

![Tanglarity Stability AI Workflow](tanglarity-demo_1.gif)

---

## Problem Being Solved

Many productivity systems assume users already have focus, organization, energy, and emotional bandwidth.

Tanglarity is designed for situations where priorities collide, thoughts feel tangled, and the next step feels unclear.

Instead of pushing users harder, the system attempts to reduce pressure, narrow focus, and support stabilization before optimization.

The project focuses on problems such as:

* cognitive overload
* decision fatigue
* competing priorities
* emotional flooding
* organizational chaos
* overwhelm
* unclear next steps
* difficulty moving from awareness into action

---

## Intended Audience

Tanglarity is designed for users who may feel:

* overwhelmed
* frozen
* emotionally flooded
* mentally scattered
* unable to prioritize
* unsure where to begin

The intended audience is not someone who already feels fully organized and ready to move quickly.

The system is intentionally designed for users who need clarity, stabilization, and reduced pressure first.

---

## How To Use The App

1. Open the live app.
2. Watch the calming welcome screen.
3. Click “Enter Stability AI.”
4. Review the Quick Phase Guide.
5. Complete the overload, clarity, and readiness sliders.
6. Review the suggested stabilization phase.
7. Describe one current pressure point.
8. Choose the type of support needed.
9. Click “Generate Stability Plan.”
10. Review the generated response including next actions, grounding reminders, and pause guidance.

---

## Stabilization Phases

Tanglarity uses four stabilization phases to help match the response to the user’s current level of overwhelm, readiness, and clarity.

### Survival

The user may feel overwhelmed, frozen, reactive, or emotionally flooded.

The system focuses on:

* reducing pressure
* narrowing focus
* reducing input
* identifying one safe next step

### Stabilization

The user may be able to complete small actions but still needs structure.

The system focuses on:

* grounding
* manageable routines
* reduced complexity
* rebuilding consistency

### Organization

The user may be ready to sort tasks, organize schedules, and prioritize responsibilities.

The system focuses on:

* structure
* categorization
* workflow organization
* manageable planning

### Growth

The user may be stable enough to build habits, improve systems, reflect, and plan forward.

The system focuses on:

* consistency
* momentum
* sustainable progress
* long term growth

---

## Current Features

* calming welcome screen
* visual onboarding media
* Quick Phase Guide
* stabilization quiz
* overload, clarity, and readiness sliders
* suggested phase logic
* progress tracking
* pressure point input
* support type selection
* structured Stability AI response
* realistic next actions
* grounding reminders
* reflection prompts
* strategic pause guidance

---

## Prompt Engineering

The app uses deliberate prompt design to avoid generic chatbot behavior.

The goal is not to generate large amounts of advice. The goal is to create calm, structured, phase appropriate guidance.

Prompt engineering techniques used:

* role prompting
* structured outputs
* grounding inputs
* constrained responses
* phase based logic
* output limitation
* plain language prompting
* strategic pause guidance
* iterative refinement

These techniques were chosen to keep the system stabilizing instead of overwhelming.

---

## System Prompt

```text
You are Stability AI, a calm and structured assistant inside the Tanglarity platform.

Your purpose is to help overwhelmed users reduce cognitive overload and move toward one manageable next action.

You do not diagnose, provide therapy, give legal advice, or act as emergency support.

Use plain language.

Keep responses short, structured, grounded, and stabilizing.

Focus on the user's selected phase, pressure point, and support type.

Prioritize stabilization before productivity.

Avoid overwhelming the user with too many recommendations.

Support strategic non action when reducing pressure would be more stabilizing than adding tasks.
```

---

## Grounding

The model is grounded through structured user input rather than unrestricted conversation.

Grounding elements include:

* selected stabilization phase
* overload level
* clarity level
* readiness level
* pressure point input
* support type selection
* predefined response structure
* phase based response logic

These inputs help keep responses focused, manageable, and relevant to the user’s current state.

---

## Build Log / Development Timeline

### Initial Concept

The project originally explored AI systems for emotional overload, organization, workflow management, and decision support.

Early versions were too broad and risked becoming generic chatbot systems.

### Scope Narrowing

The project narrowed into a stabilization focused tool centered around helping users move from overwhelm toward one manageable next action.

This improved clarity, workflow structure, and deployment feasibility.

### Stabilization Phase System Added

The four phase system was added:

1. Survival
2. Stabilization
3. Organization
4. Growth

This improved response consistency and allowed the app to adapt guidance based on user readiness and overload level.

### Constrained Output Structure Added

Early versions generated too much advice and increased cognitive overload.

The response structure was redesigned to intentionally limit output and instead focus on:

* one or two next actions
* grounding reminders
* strategic pause guidance
* manageable movement

### Visual and Progress Features Added

The project later added:

* calming onboarding videos
* progress sliders
* stabilization scoring
* visual grounding elements

These additions improved the emotional tone and made the app feel more intentional and immersive.

---

## Evaluation

### What “Good” Meant

A successful Stability AI response should:

* reduce overwhelm
* stay calm and clear
* avoid cognitive flooding
* generate realistic next actions
* match the user’s stabilization phase
* remain manageable and grounded

### How I Tested

The system was tested using example pressure points such as:

* “I have too many assignments and do not know where to begin.”
* “My house feels overwhelming and I feel frozen.”
* “I feel overloaded and cannot prioritize.”
* “I need structure but not pressure.”

### What I Found

The strongest responses were:

* short
* stabilizing
* realistic
* phase appropriate
* action constrained

The system performed best when users clearly identified the main pressure point.

The constrained response structure improved consistency and reduced overwhelming outputs compared to earlier unrestricted versions.

---

## Honest Limits

Tanglarity is not:

* therapy
* diagnosis
* medical care
* legal advice
* emergency support
* crisis intervention

Current limitations include:

* no long term memory
* no retrieval augmented generation
* limited personalization
* no saved user history
* no user accounts
* depends heavily on user input quality
* cannot replace professional support

---

## Originality and Ownership

Tanglarity intentionally avoids traditional productivity optimization framing.

The system is built around the idea that users often need stabilization before optimization.

The name Tanglarity combines the feeling of being tangled with the goal of clarity.

Stability AI was designed as the first module because stabilization is treated as the foundation before deeper planning, organization, or growth.

The project evolved through repeated experimentation, refinement, prompt engineering, workflow redesign, and testing rather than a single generated output.

---

## AI Tools and Technologies Used

* Python
* Streamlit
* GitHub
* GitHub Codespaces
* Hugging Face Spaces
* GitHub Copilot
* Canva
* OpenAI assisted prompting and development support

---

## Future Improvements

Future versions may include:

* saved progress
* optional journaling
* improved phase scoring
* adaptive stabilization workflows
* ambient grounding audio
* personalized stabilization tracking
* retrieval augmented grounding

---

## Final Reflection

Tanglarity is designed to help overwhelmed users reduce chaos, identify their current phase, and take one manageable next step.

The project demonstrates how prompting, grounding, structure, iteration, and constrained outputs can shape an AI system into something more intentional and stabilizing than a generic chatbot.
