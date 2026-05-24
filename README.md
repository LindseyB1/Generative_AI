# Tanglarity: Stability AI

> An AI assisted stabilization system designed to help overwhelmed users reduce cognitive overload, identify their current phase, and move toward one manageable next action.

## Table of Contents

* Pitch
* Summary
* Live Demo
* Demo Preview
* Problem Being Solved
* Why This Matters
* Intended Audience
* How To Use The App
* Stabilization Phases
* Current Features
* Prompt Engineering
* System Prompt
* Grounding
* Real AI Model Integration
* Build Log / Development Timeline
* Evaluation
* Honest Limits
* Originality and Ownership
* AI Tools and Technologies Used
* Environment Variables and API Security
* Future Improvements
* Final Reflection

---

# Pitch

Tanglarity is an AI assisted stabilization platform designed to help overwhelmed users reduce cognitive overload, identify their current phase, and move toward realistic action by closing the gap between knowing what to do and actually being able to do it.

Stability AI is the first working module inside the broader Tanglarity system.

Rather than focusing purely on productivity, optimization, or speed, the system prioritizes stabilization, clarity, reduced pressure, and manageable movement.

The goal is not to overwhelm users with large amounts of advice. The goal is to help users slow down, regain clarity, reduce chaos, and identify one realistic next step.

---

# Summary

Tanglarity is built around the idea that many people already know what they should do, but still struggle to act when they feel overloaded, mentally scattered, emotionally flooded, frozen, exhausted, or pulled in too many directions at once.

Many systems assume users already have organization, focus, motivation, and emotional bandwidth. Tanglarity was intentionally designed for moments where those conditions may not exist.

Stability AI uses structured prompting, grounding inputs, stabilization phases, constrained outputs, progress tracking, and calming interface design to generate more manageable and phase appropriate responses.

The project intentionally avoids skipping stabilization simply to chase productivity because instability often creates cycles of overwhelm, avoidance, unfinished systems, cognitive flooding, and unsustainable planning.

The system attempts to reduce pressure before increasing complexity.

---

# Live Demo

https://tanglarity-stabilityai.streamlit.app/

---

# Demo Preview

The application includes a calming onboarding experience and stabilization focused workflow designed to reduce cognitive overload before generating responses.

![Tanglarity Welcome Experience](tanglarity-demo_2.gif)

![Tanglarity Stability AI Workflow](tanglarity-demo_1.gif)

---

# Problem Being Solved

Many productivity systems assume users already have:

* focus
* organization
* energy
* emotional bandwidth
* decision making clarity
* prioritization ability
* stable routines

Tanglarity is designed for situations where priorities collide, thoughts feel tangled, and the next step feels unclear.

Instead of pushing users harder, the system attempts to reduce pressure, narrow focus, stabilize thinking, and support manageable movement before optimization.

The project focuses on problems such as:

* cognitive overload
* decision fatigue
* competing priorities
* emotional flooding
* organizational chaos
* overwhelm
* unclear next steps
* difficulty moving from awareness into action
* avoidance cycles
* over analysis
* instability created by excessive complexity

---

# Why This Matters

Tanglarity was created around the idea that clarity and stabilization are often prerequisites for sustainable action, organization, and long term growth.

The project explores whether AI systems can be intentionally constrained and grounded to reduce overwhelm instead of increasing it.

Rather than maximizing output quantity, the system attempts to improve output appropriateness, pacing, and psychological manageability.

---

# Intended Audience

Tanglarity is designed for users who may feel:

* overwhelmed
* frozen
* emotionally flooded
* mentally scattered
* unable to prioritize
* unsure where to begin
* overloaded by competing responsibilities
* stuck between awareness and action

The intended audience is not someone who already feels fully organized and ready to move quickly.

The system is intentionally designed for users who need stabilization, clarity, reduced pressure, and manageable movement first.

---

# How To Use The App

1. Open the live application.
2. Watch the calming onboarding screen.
3. Enter Stability AI.
4. Review the Quick Phase Guide.
5. Complete the overload, clarity, and readiness sliders.
6. Review the suggested stabilization phase.
7. Describe one current pressure point.
8. Select the type of support needed.
9. Generate the Stability Plan.
10. Review the AI generated stabilization response.

The response may include:

* phase interpretation
* one priority lane
* one or two manageable next actions
* grounding reminders
* pause guidance
* reflection prompts
* stabilization focused recommendations

---

# Stabilization Phases

Tanglarity uses four stabilization phases to help match outputs to the user’s current state, readiness level, clarity, and overload level.

## Survival

The user may feel:

* overwhelmed
* reactive
* frozen
* emotionally flooded
* unable to prioritize

The system focuses on:

* reducing pressure
* narrowing focus
* reducing input
* identifying one safe next step
* minimizing overload

## Stabilization

The user may be able to complete small actions but still needs structure and grounding.

The system focuses on:

* grounding
* manageable routines
* reduced complexity
* rebuilding consistency
* reducing chaos

## Organization

The user may be ready to sort responsibilities, organize systems, and prioritize tasks.

The system focuses on:

* structure
* categorization
* workflow organization
* realistic planning
* prioritization

## Growth

The user may be stable enough to build habits, improve systems, reflect, and plan forward.

The system focuses on:

* sustainable momentum
* consistency
* reflection
* long term planning
* growth oriented systems

---

# Current Features

* calming welcome screen
* visual onboarding media
* Quick Phase Guide
* stabilization quiz
* overload sliders
* clarity sliders
* readiness sliders
* suggested phase logic
* progress tracking
* pressure point input
* support type selection
* dynamically generated AI stabilization responses
* grounding reminders
* reflection prompts
* strategic pause guidance
* constrained response formatting
* stabilization focused response structure

---

# Prompt Engineering

The project uses deliberate prompt engineering to avoid unrestricted chatbot behavior.

The goal is not to generate large amounts of advice. The goal is to generate calm, grounded, structured, phase appropriate guidance.

Prompt engineering techniques used include:

* role prompting
* structured outputs
* grounding inputs
* constrained responses
* phase based logic
* output limitation
* plain language prompting
* stabilization focused prompting
* strategic pause guidance
* iterative refinement
* response structure constraints
* prompt narrowing
* system level behavioral constraints

The system also uses structured prompting patterns to improve response consistency and reduce response drift across different overload conditions and pressure points.

These techniques were intentionally selected to keep outputs stabilizing rather than overwhelming.

---

## Gravity Prompt Critique Method

One refinement technique explored during development was a challenge based prompt called the “Gravity” prompt:

> “Act like gravity for my idea. Your job is to pull it back to reality. Attack the weakest points in my reasoning, challenge my assumptions, and expose what I might be missing. Be tough, specific, and do not sugarcoat your feedback.”

This technique was used to intentionally challenge overly broad ideas, unrealistic scope, excessive complexity, and generic chatbot behavior during development.

The process helped narrow Tanglarity from a broad emotional support concept into a more constrained stabilization focused workflow centered around manageable next actions, reduced overload, and grounded outputs.

This approach improved:

* scope control
* deployment feasibility
* workflow clarity
* response realism
* stabilization focused prompting
* practical implementation

---

# System Prompt

```text
You are Stability AI, a calm and structured assistant inside the Tanglarity platform.

Your purpose is to help users reduce cognitive overload, clarify their current pressure point, and move toward one manageable next action.

You are not a therapist, doctor, attorney, emergency service, or crisis support system. Do not diagnose, provide therapy, give legal advice, or present yourself as professional care.

Use plain language.

Keep responses structured, grounded, calm, concise, and realistic.

Focus on the user’s selected stabilization phase, overload level, clarity level, readiness level, support type, pressure point, and uploaded context if relevant.

Prioritize stabilization before productivity.

Avoid overwhelming the user with too many recommendations or excessive planning.

When the user appears overloaded, reduce complexity before suggesting additional action.

Support strategic non action when reducing input, narrowing focus, gathering information, resting, delaying escalation, or pausing noncritical tasks would be more stabilizing than adding more pressure.

Make the response specific to the user’s actual pressure point. Avoid generic motivational language, excessive reassurance, or placeholder wording.

Do not use dramatic crisis language.

Do not tell the user that “everything will be okay.” Instead, help identify what can be simplified, clarified, paused, organized, or approached next in a manageable way.

When appropriate, provide:
- a brief current phase summary
- one priority lane
- one or two realistic next actions
- what to pause or reduce
- a grounding reminder
- an optional reflection question

Keep recommendations realistic, manageable, and phase appropriate.

Maintain a calm, practical, nonjudgmental tone throughout the interaction.
---

# Grounding

The model is grounded through structured user input rather than unrestricted conversation.

Grounding elements include:

* stabilization phase
* overload level
* clarity level
* readiness level
* pressure point input
* support type selection
* predefined response structure
* phase based logic
* system prompt constraints
* stabilization focused response formatting

These grounded inputs are dynamically injected into the OpenAI model request before generation.

This grounding structure helps keep responses:

* focused
* manageable
* phase appropriate
* realistic
* stabilization oriented

rather than producing unrestricted chatbot outputs.

The application can also optionally accept uploaded `.txt` or `.md` files for additional grounding context.

When documents are uploaded, relevant contextual information is included in the grounded model request before generation.

This allows Stability AI to generate more situationally aware responses tied to the user’s actual pressure point, uploaded context, and stabilization phase rather than relying only on generalized prompting.

---

# Real AI Model Integration

The first deployed version of Tanglarity used structured stabilization logic and constrained response architecture, but initially relied more heavily on predefined response pathways during early prototyping.

The application was later expanded into a fully AI assisted stabilization workflow using real OpenAI model inference.

The application now:

* imports the OpenAI Python library
* securely loads API credentials through environment variables
* dynamically loads the system prompt from `Prompts/system_prompt.md`
* sends grounded stabilization inputs directly to the model
* generates real AI assisted stabilization responses using OpenAI `gpt-4o-mini`
* uses structured grounding inputs to influence generated outputs

The model receives contextual grounding information including:

* stabilization phase
* overload score
* clarity score
* readiness score
* pressure point description
* support type selection

These grounded inputs are injected directly into the model request before generation to create more adaptive, phase appropriate responses rather than relying on static response branches.

This transition moved Tanglarity from a structured prototype into a real AI powered stabilization workflow while maintaining constrained outputs, grounding structure, and stabilization focused design principles.

---
## Simplified Workflow Architecture

```text
User Inputs
↓
Stabilization Phase + Sliders + Pressure Point + Uploaded Context
↓
Grounded User Prompt
↓
System Prompt
↓
OpenAI gpt 4o mini
↓
Structured Stability Plan
---

# Build Log / Development Timeline

## Initial Concept

The project originally explored broader AI systems related to:

* emotional overload
* organization
* workflow management
* decision support
* stabilization systems
* cognitive clarity

Early versions were too broad and risked becoming generic chatbot systems without a clearly constrained purpose.

## Scope Narrowing

The project later narrowed into a stabilization focused workflow centered around helping users move from overwhelm toward one manageable next action.

This significantly improved:

* deployment feasibility
* workflow clarity
* response consistency
* system grounding
* practical implementation

## Stabilization Phase System Added

The four phase system was added:

1. Survival
2. Stabilization
3. Organization
4. Growth

This improved consistency and allowed the app to adapt outputs based on user readiness, clarity, and overload levels.

## Constrained Output Structure Added

Early versions generated too much advice and unintentionally increased cognitive overload.

The response structure was redesigned to intentionally limit outputs and instead focus on:

* one or two next actions
* grounding reminders
* strategic pause guidance
* manageable movement
* stabilization before optimization

## Visual and Progress Features Added

The project later added:

* calming onboarding videos
* stabilization scoring
* progress sliders
* visual grounding elements
* calming interface structure

These additions improved the emotional tone and helped the system feel more intentional, immersive, and stabilizing.

---

# Evaluation

## What “Good” Meant

A successful Stability AI response should:

* reduce overwhelm
* remain calm and clear
* avoid cognitive flooding
* generate realistic next actions
* match the user’s stabilization phase
* remain manageable
* remain grounded
* avoid excessive complexity

## How The System Was Tested

The system was tested using pressure points such as:

* “I have too many assignments and do not know where to begin.”
* “My house feels overwhelming and I feel frozen.”
* “I feel overloaded and cannot prioritize.”
* “I need structure but not pressure.”

## What Was Found

The strongest responses were:

* short
* stabilizing
* realistic
* phase appropriate
* action constrained
* grounded

The system performed best when users clearly identified the main pressure point.

The constrained response structure improved consistency and reduced overwhelming outputs compared to earlier unrestricted versions.

---
---

## Example Live AI Output

Example user pressure point:

> “I need to find affordable housing in my area and it is difficult finding something around $1,000 a month that allows three dogs.”

The generated response successfully:

* identified the user’s likely stabilization phase
* narrowed the problem into one priority lane
* suggested realistic next actions
* incorporated uploaded housing context
* avoided excessive productivity pressure
* maintained a structured stabilization focused tone

This demonstrated that grounded AI generation produced more adaptive and realistic outputs compared to earlier static response prototypes.

---
# Honest Limits

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

The system may become less effective when users provide very limited context, unclear pressure points, or situations requiring professional intervention beyond the intended scope of stabilization support.

---

# Originality and Ownership

Tanglarity intentionally avoids traditional productivity optimization framing.

The system is built around the idea that users often need stabilization before optimization.

The name Tanglarity combines the feeling of being tangled with the goal of clarity.

Stability AI was designed as the first module because stabilization is treated as the foundation before deeper planning, organization, or growth.

The project evolved through repeated experimentation, prompt refinement, workflow redesign, stabilization modeling, iteration, and testing rather than a single generated output.

---

# AI Tools and Technologies Used

* Python
* Streamlit
* GitHub
* GitHub Codespaces
* Streamlit Cloud
* GitHub Copilot
* Canva
* OpenAI API integration
* OpenAI assisted prompting and development support

---

# Environment Variables and API Security

Tanglarity uses environment variables for secure API credential management.

Local development uses a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

The `.env` file is excluded from GitHub through `.gitignore`.

For deployed versions on Streamlit Cloud, the API key should be stored securely in Streamlit secrets.

This approach prevents exposing private API credentials publicly while allowing the application to securely access the OpenAI API during runtime.

The application uses:

* `python-dotenv` for local environment variable loading
* Streamlit Cloud secrets for deployment
* `.gitignore` protections to prevent secret exposure

---

# Future Improvements

Future versions may include:

* saved progress
* optional journaling
* improved phase scoring
* adaptive stabilization workflows
* ambient grounding audio
* personalized stabilization tracking
* retrieval augmented grounding
* longitudinal stabilization tracking
* adaptive pacing systems
* dynamic checkpoint systems

---

# Final Reflection

Tanglarity explores whether AI systems can be intentionally constrained and grounded to reduce cognitive overload rather than increase it.

The project demonstrates how prompting, grounding, stabilization logic, constrained outputs, iteration, and structured workflow design can shape an AI system into something more intentional and stabilizing than a generic chatbot.
