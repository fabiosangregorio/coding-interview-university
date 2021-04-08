# How to Pass the Engineering Interview in 2021
you should expect a some combination of a few types of interviews:

-   **Coding interviews.** You’ll be expected to write code to solve a problem during the interview. This demonstrates to the interviewer that you have the necessary skills to solve technical problems. You’ll find more of these in junior and individual contributor roles.
-   **Design/architecture interviews.** These interviews are more open-ended and are designed to be collaborative. You’ll be expected to solve a design problem, generally on a whiteboard and from both conceptual and practical levels, without writing code. You’ll find these in more senior and individual contributor roles.
-   **Behavioral/experience interviews.** In this interview, you’ll discuss your background, recent work experience, and describe how you handle specific situations found in the workplace. You’ll find this in more senior and management roles.

## Before the interview
Get as much information as possible before the interview. The more you know beforehand, the better prepared you’ll be.

It’s important to remember that everyone you’re working with wants you to succeed. If you get an offer, everyone wins.

## Coding interviews
Failing here can sink your chances entirely, so it’s important to be prepared.

Practice deliberatly and be goal-oriented, where you set aside time and focus on improving your skills. What you practice should be informed by everything you know about the upcoming interview. If you’re unsure, then ask your recruiter what you should expect. Will you have to write code that executes? Or will you write pseudocode on the whiteboard? What types of coding questions should be expected? Sometimes the recruiter will provide sample problems and that’s a great place to start.

### Coding interview preparation tips

**ABC (Always Be Coding).** The more code you write, the more prepared you’ll be for your technical interviews

**Be comfortable with at least one dynamic programming language.** Dynamic programming languages like Python and Javascript are both well-known and conducive to writing short, powerful programs with less boilerplate code. That allows you to focus on solving the problem rather than wrestling with the compiler or abstractions.

**Know thy complexities.** Read [this cheat sheet](https://www.bigocheatsheet.com/) and make sure you understand at least 80% of it. Maybe you haven’t ever had to implement a red-black tree, but you should understand when and how it’s useful in various applications. When presenting a solution, interviewers will often follow-up with: “What’s the time complexity of your solution?” Be prepared to speak to it.

**Reinvent the wheel.** Practice by implementing the most common data structures in your language of choice. Do not rely on common libraries. Implement them and write tests for them.

**Solve word problems.** This is one of my favorites and one of the most important activities you can do. Interviewers will often present problems that seem complex but can be reduced down to simple algorithmic solutions. First, read about [competitive programming](https://www.topcoder.com/community/competitive-programming/tutorials/).

During the interview, make sure you are clear on the problem you’re being asked to solve. Sometimes interviewers won’t give you all of the information required for the optimal solution and expect you to ask clarifying questions. Focus on solving it first and optimizing it later. Correctness counts the most, and getting to a suboptimal solution is better than failing to produce a performant one.

After you solve the problem, be prepared for follow-up questions that may require you to write more code. When a problem seems straightforward, you might anticipate there will be follow-up questions that constrain or complicate the problem somehow.

## Design/architecture interviews
Your goal is to produce a design that could realistically be implemented and explain your thought process along the way.
There is no single solution to a design problem, though there are plenty of suboptimal ones. The interviewer will observe how you approach and think through the problem. To do this, you should be more proactive than reactive. Try to think and communicate a couple steps ahead, rather than waiting for the interviewer to ask questions or probe your design.

**Spend the first 5–10 minutes making sure you understand all of the requirements and constraints.** The interviewer won’t lay out all of the constraints and criteria for you immediately, and you’ll be expected to ask clarifying questions.

**Start at a high-level (e.g., box and arrow diagrams) and work your way down from there.** It’s important to not to get too caught up in the details of a particular component before sketching the overall design.

**Ask questions and communicate your thought process along the way.** The interviewer may not intervene immediately to course-correct you, so you should feel comfortable asking questions when in doubt. If you select a piece of technology (e.g., a relational data store), you may explain why you selected that over a key-value storage solution and the tradeoffs you considered. They shouldn’t have to work hard to pull information out of you.

**Be ready to talk about trade-offs.** You should be able to weigh the pros and cons of your design.

### Design interview preparation tips
**Understand service-oriented architecture.** These design problems typically involve drawing “boxes and arrows” to convey how your system works and is coupled together. 

**Read about how some companies built their large-scale systems.** It’s probably a good idea to read a primer on how systems like S3, Google File System, and Google Spanner work.

**Watch YouTube videos on solving design problems.** You can find many useful videos that break-down common problems. Head over to YouTube and search “{FAANG company} design interview questions.”

**Put pencil to paper.** It’s not enough to passively watch some YouTube videos; you should be able to solve them yourself with paper and pencil. You should speak to the overall system design (box diagrams), API design, and database design. Here are some good examples of these sorts of problems:

-   Design a ticket reservation system (like Ticketmaster).
-   Design an app like Twitter, assuming 100M active users. Make sure you cover how a user can post a tweet and also fetch their home timeline.
-   Design an app like WhatsApp, assuming 100M+ active users. Consider end-to-end encryption as a design requirement.
-   Design a distributed web crawler to run on N remote machines that you can run arbitrary software on.

## Behavioral/experience interviews
You may be asked to describe a situation that involves a technical solution. These interviews are used to assess culture fit, work experience, background, and how you handle specific situations.

When answering behavioral questions, consider first explaining how you think about it from a conceptual level. This helps to frame your answer and demonstrate to the interviewer that you can approach handling situations in a systematic way. When describing the situation, you might find the [STAR method](https://www.thebalancecareers.com/what-is-the-star-interview-response-technique-2061629) useful.

### Behavioral interview preparation tips

**Write the script.** Think about the types of questions that you expect in the interview (and ask the recruiter). Then write them down and answer them, ideally with anecdotal examples.

Here are some questions that I would make sure to pre-emptively answer:

-   What are you looking for in your next role? Why this company?
-   Tell me about a time when you had to work with a cross-functional team to solve a problem.
-   Tell me about a time when you demonstrated a bias for action.
-   Tell me about a time when you took ownership of a project or process and improved it.
-   Tell me about a time when you had to deal with ambiguity.
-   Tell me about a time when you disagreed with someone or had to resolve a disagreement.
-   Tell me about a time when you led a project that failed. Why did it fail and what did you learn?
-   What is your management style?
-   How do you know that your team is working optimally?
-   How do you handle low-performers?
-   How do you approach solving complex problems?
-   How do you evaluate buying vs. building technology?
-   What is your approach to recruiting talent?

**Write down your principles.** You should try to enumerate some of your principles or virtues for dealing with common workplace situations. It’s a good exercise to think about how you’ve approached problems and reduce them down to first-order concepts. You can then use these to frame your answers. Here are some examples of my principles:

-   Perceive problems early and often, but don’t tolerate them. Don’t just call out problems without owning them.
-   Be approachable and encourage others to probe by actively soliciting questions and challenges.
-   Escalate when necessary to avoid getting stuck or to resolve a dispute or problem quickly.
-   Act like an owner by putting the best interest of the organization and its people first.
-   Be assertive and open-minded at the same time in controversial discussions or debates.
-   Understand the disagreement in a situation before attempting to find agreement; this often reveals important information worth digging into.
-   Get to the root cause to assess how a process is working, and/or to learn more about the people involved.

## After the interviews
I find it useful to immediately write some of my thoughts on how the overall process went and share them with the recruiter. They find this information invaluable, and they may be more inclined to share more detailed information and provide more feedback to you about the interview results.