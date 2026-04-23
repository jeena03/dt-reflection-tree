# Daily Reflection Tree

## Overview
This project is a deterministic end-of-day reflection tool designed to help employees understand how they showed up during their day.

The system guides users through a structured conversation across three psychological axes:
- Locus of Control (Victim vs Victor)
- Contribution vs Entitlement
- Radius of Concern (Self vs Others)

Each question has fixed options, and every path is predefined. The same answers always lead to the same outcome.


## Project Structure

DT assignment/
├── tree/
│     ├── reflection-tree.json
│     └── tree-diagram.png
│
├── agent/
│     └── agent.py
│
├── transcripts/
│     ├── persona-1-transcript.md
│     └── persona-2-transcript.md
│
├── write-up.md
└── README.md


## How the Tree Works

- The system presents questions with fixed options  
- Each option records a signal:
  - Axis 1 → internal / external  
  - Axis 2 → contribution / entitlement  
  - Axis 3 → self / others  

- Signals accumulate across each axis  
- A decision node determines the dominant pattern  
- The user is shown a reflection based on that pattern  

This ensures the system remains fully deterministic — no randomness, no AI at runtime.


## Running the Agent

To run the reflection tool:

python agent/agent.py

Follow the prompts in the terminal to move through the reflection.


## Files Included

- tree/reflection-tree.json  
  → Core reflection tree structure  

- tree/tree-diagram.png  
  → Visual representation of the tree  

- agent/agent.py  
  → CLI-based program to run the reflection  

- transcripts/  
  → Sample runs showing different user paths  

- write-up.md  
  → Design explanation and rationale  


## Notes

- The system is fully deterministic  
- No free-text input is used  
- The focus is on guiding reflection, not evaluating the user  

