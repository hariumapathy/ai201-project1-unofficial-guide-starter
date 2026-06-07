# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

**Domain**: My chosen domain is course and professor reviews of the Computer Science Department at UMass Amherst,
focused on the four required 200-level courses: CS210, CS220, CS230, and CS240.

**Use Case**: These 200-level courses are taught by various professors with different sections, so knowing the
ratings and comments of the professors who frequently teach them can help students make informed decisions
for course registration and which professor to take the desired course with.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Rate My Professor: Andrew Lan | extracted into text file | https://www.ratemyprofessors.com/professor/2445013; extracted text into file 'Andrew_Lan_Rate_My_Professor.txt' |
| 2 | COMPSCI 250 Home Page Spring 2026 | extracted into text file |https://people.cs.umass.edu/~barring/cs250/; extracted text into file 'COMPSCI_250_Home_Page_Spring_2026.txt' |
| 3 | Coursicle CS240 at UMass Amherst Overview Page | extracted into text file | https://www.coursicle.com/umass/courses/COMPSCI/240/; extracted into file 'Coursicle_COMPSCI_240_at_UMass_Website.txt' |
| 4 | CS220 Fall 2025 Course Page | extracted into text file | https://people.cs.umass.edu/~jaimedavila/Courses/220/; extracted into file 'CS220_Fall_2025_Course_Page.txt' |
| 5 | Rate My Professor: David Barrington | extracted into text file | https://www.ratemyprofessors.com/professor/82723; extracted text into file 'David_Barrington_Rate_My_Professor.txt' |
| 6 | Rate My Professor: Jaime Davila | extracted into text file | https://www.ratemyprofessors.com/professor/2596812; extracted text into file 'Jaime_Davila_Rate_My_Professor.txt' |
| 7 | Rate My Professor: Joe Chiu | extracted into text file | https://www.ratemyprofessors.com/professor/2420066; extracted text into file 'Joe_Chiu_Rate_My_Professor.txt' |
| 8 | Rate My Professor: Marius Minea | extracted into text file | https://www.ratemyprofessors.com/professor/2416008; extracted text into file 'Marius_Minea_Rate_My_Professor.txt' |
| 9 | Rate My Professor: Mordecai Golin | extracted into text file | https://www.ratemyprofessors.com/professor/2940693; extracted text into file 'Mordecai_Golin_Rate_My_Professor.txt' |
| 10 | Rate My Professor: Phuthipong Bovornkeeratiroj| extracted into text file | https://www.ratemyprofessors.com/professor/2992114; extracted text into file 'Phuthipong_Bovornkeeratiroj_Rate_My_Professor.txt' |
| 11 | r/umass subreddit post titled 'cs 230 and 250' by user SeatAgile1918 | extracted into text file | https://www.reddit.com/r/umass/comments/1orfe6z/cs_230_and_250/; extracted text into file 'umass_subreddit_post_cs_230_and_cs_250.txt' |


**Note on Rate My Professor Text Extraction**: For the Rate My Professor text files, only select reviews were extracted, since these professors also teach upper-level courses
which is not the primary focus of the stated domain above. Older reviews from multiple semesters ago were also minimized or excluded
since the information might not be relevant for upcoming semesters.

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
