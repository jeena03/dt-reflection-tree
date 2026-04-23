The Daily Reflection Tree
Assignment: DT Fellowship: Deterministic Reflection Agent 

I was in search of an internship, essentially, and found DeepThought on Internshala. What instantly interested me was how the assignment was designed to make applicants grind from day one so they get acquainted with the environment before they even walk through the door. I respected that.
Honestly, I am not an expert in analytics, Python, or data structures. I cannot claim to have strong knowledge in this background. I know I am probably not supposed to say this in a write-up because it might reduce my chances of getting selected. Maybe it will. But I want to be real with you because after doing this assignment, I genuinely wish to work with you. Even a small task would count for me now.
Through this assignment I found something I was not expecting. I understood things that my four years of engineering degree could not teach me. Now I know what trees are and what they actually do. I am getting a clearer picture of data structures. I found depth in something I thought was out of my reach. I cannot fully express how happy that makes me.
I used Claude. Yes. I also used NotebookLM to read and understand "Mindset" by Carol S. Dweck because reading a 300 page book in 48 hours is not something I could do alone. I am genuinely thankful to both. Claude walked me through decision trees, JSON structure, branching logic, psychological frameworks, and even fixed my broken code. The thinking, questions, and choices were totally mine.

Why I chose these questions

I have worked in a real office for two months. I have dealt with customers, colleagues, seniors, and managers. I know what it feels like to come home after a long day. Sometimes we feel happy, sometimes tired and drained, sometimes frustrated and sometimes with mixed feelings. I used my experiences fully while designing the tree.
The most important thing I wanted was for the tree to not feel judgmental. It should not make an employee feel guilty or ashamed about their answers. It should hold up a mirror gently so they can see their own pattern without being told what to think about it.

Axis 1 starts with the best question you can ask someone after work: how was your day? I gave four options that cover the full range of how a working day can feel: productive, smooth and satisfying, tough and frustrating, and mixed. Each of these four answers leads to its own unique follow-up question because a person who had a productive day is in a completely different headspace than someone who had a tough one. Giving them the same follow-up would feel lazy and impersonal. The questions then gradually move inward — from describing what happened, to examining what guided their actions, to reflecting on the role they played in how the day went. This is the Locus of Control axis. Here we will show the employee a mirror without making them feel ashamed. 

Axis 2 focuses on the gap between effort and expectation. I designed three questions that together reveal whether someone is in a giving mindset or a receiving mindset without ever using the word entitlement. The questions ask what mattered most during effort, how they feel looking back, and whether they missed a chance to help someone. That last question is the hardest one. It is difficult to rationalize and forces a moment of real honesty. This is the Contribution vs Entitlement axis.
Axis 3 moves from broad to specific. First, I ask who comes to mind when they think about their most important moment. Then what shaped their reaction. Then whether they actually checked in on anyone. The progression is deliberate — it starts at a distance and slowly brings them closer to a concrete answer about where their attention actually was. This is the Radius of Concern axis.

How I designed the branching

Each answer records a signal: internal or external for Axis 1, contribution or entitlement for Axis 2, self or others for Axis 3. These signals accumulate across all questions in each axis. At the end of every axis a decision node counts which signal appeared more often and routes to the matching reflection. This means one answer does not define the result. The overall pattern across multiple questions does. I felt this was fairer and more accurate to how human behavior actually works.
The main trade-off I made was between depth and size. For Axis 1 I branched deeply — each opening answer leads to its own unique follow-up. This makes the conversation feel personal from the start. Doing this for all three axes would have made the tree very large, so for Axis 2 and Axis 3 I used shared follow-up questions and let the signals carry the personalization. It kept the tree manageable while still feeling thoughtful.

Psychological sources

Axis 1 is grounded in Julian Rotter's Locus of Control theory (1954) and Carol Dweck's Growth Mindset research (2006). Axis 2 draws from Campbell et al.'s work on Psychological Entitlement (2004) and Organ's research on Organizational Citizenship Behavior (1988). Axis 3 is informed by Maslow's later writing on Self-Transcendence (1969) and Batson's work on Perspective-Taking (2011).

What I would improve with more time

I would add deeper branching to Axis 2 and Axis 3 the same way I did for Axis 1 so every opening answer leads to a uniquely matched follow-up. I would also build a daily log that saves each session's results so that after a week the employee can see their own patterns across time. One session is a snapshot. A week of sessions is a story. Finally, I would write more reflection variants per axis so the text feels fresh across repeated use and handles mixed results more precisely.

Total nodes: 30 | Axes covered: 3 | Format: JSON | Agent: Python (CLI)

