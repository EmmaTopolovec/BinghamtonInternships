# BinghamtonInternships
An email service that will send Binghamton students job opportunities. Created for the HackBU 2023 Hackathon.

## Inspiration
When brainstorming ideas for the HackBU 2023 hackathon, I considered different problems that I face in my everyday life. After considering multiple ideas, I finally landed on one that will solve the following problem:

As a computer science student, I am constantly looking for job and internship opportunities. I manually check job sites, including Google, Handshake, and LinkedIn, multiple times a week. This is a tiring and tedious part of my day. I have to comb through job postings, one by one, to find a position I want to actually apply for.

I decided to take it upon myself to solve this problem. Not only did I want to automate the job process for myself, but also for other Binghamton students. While there are tools out there to help with job searching, I felt that a Binghamton-specific service would be able to fill a niche that other services are unable to. The Binghamton Internship Newsletter is a service that can improve the lives of all Binghamton University students.

## What it does
The Binghamton Internship Newsletter is an automated, weekly newsletter. Every week, a bot will scrape the web for Binghamton-specific job and internship opportunities, then compile the opportunities into a newsletter and send it to users who are subscribed.

Users can subscribe to the newsletter or learn more about it at https://binghamton.web.app/.
Users can also unsubscribe via [the link at the bottom of the newsletter](https://binghamton.web.app/unsubscribe.html).

The newsletter will contain every single job posted in the previous week that fit the bot's search criteria. Each position will have the position name, company, location, date posted, and a link to apply, among other useful info.

## How I built it
To allow users to subscribe and unsubscribe, I used HTML, CSS, and JavaScript to create an easy-to-use website. The website also implements Google Firebase. Firebase Hosting hosts the website 24/7 and Firebase Firestore stores the email addresses of subscribers in a secure database. I wrote a JavaScript file to add and remove emails from the database when users interact with the site.

To create and send the newsletter, I coded two Python scripts. The first implements SerpAPI's Google Search API to scrape Google for job postings. It uses specific search criteria to find the best jobs for Binghamton students. Some of these criteria are:
- near Binghamton, NY or remote
- designed for undergraduate college students
- internships or part-time positions
- posted in the last week

The positions are then parsed into a text file, which is then inputted into the second Python script. This Python program parses the opportunities into the format of the newsletter. It inserts each job into a specific HTML format. After formatting the newsletter, the script connects to my Firebase Firestore database to find every subscriber's email. Then, the newsletter is sent out to all emails using Python's built-in _smtplib_ and _email_ packages. The newsletter is sent via a custom email address I made for this project: BinghamtonInternships@gmail.com.

All programming was done using the VSCode IDE. As I worked on the project, I used GitHub to manage my code.

## Challenges I ran into
I have never sent emails through Python before, so it was a challenge to get started. There are a few steps I had to take to grant my code the correct permissions to send emails. I have also never used a database to store user data before. While I was familiar with Firebase, I have never used Firebase Firestore in the way I did for this project. It was a hassle to learn, as Firebase does not provide sample code or much documentation on how to get started. After several Google searches, I was able to find the basics of reading and writing to a Firestore database and complete that part of my code.

Other than the struggles of learning how to use new things, I ran into the challenge of designing a UI. This is something that I have always struggled with. This time around, I decided to plan out a rough sketch of what the newsletter and website would look like before I coded them. This helped me save time, but it unfortunately did not help my UIs look nice. While I am happy with the newsletter design, it is a bit plain. I am less proud of my website design. While it gets the job done and is intuitive, it is not the best looking.

## Accomplishments that I'm proud of
I learned a lot during this hackathon. As stated earlier, I had never made any form of email bot before, or even sent emails through code at all. I also have never created any form of subscription service or a database to store subscriber information. I decided to create this project partly because I knew I would learn something from it, so I am pleased that I was successful in learning these skills.

I am also proud of the technical complexity of my project. It involved multiple coding languages and platforms. Even just last year, I wouldn't have been able to made a project like this one. It is amazing to see how far I have come as a programmer. The Binghamton Internship Newsletter is something I can see actual students using.

## What I learned
I stated previously the technologies I learned how to use. However, I also learned about how to approach a project. I spent a lot of time on planning before I even touched code. The few days before the hackathon, I brainstormed projects until I found one I was truly passionate about creating. Then, in the first hour or two of the hackathon, I researched technologies that I could use to create my project. Then, I mapped out how each component would fit together. Finally, I sketched some visuals for the frontend components of my project. After all that, I started coding.

This led to one of the smoothest coding experiences of my life. The problems I ran into were mostly due to inexperiences with certain technologies. I did not run into errors coordinating the different components of my project nor did I get stumped on what I needed to implement next. After this hackathon, I will be using the project design skills I learned for every future project I create.

## What's next for Binghamton Job Newsletter
As of now, my Python script only finds jobs for undergraduate computer science students at Binghamton. I would love to create a script that lets users enter their own major and job criteria that they are looking for. That way, every student can receive a unique, personalized newsletter each week.

I would also improve the visuals of the website. The front page needs to give users a compelling reason to subscribe to the newsletter. Currently, it lacks in persuasion due to the unpolished look of the site.