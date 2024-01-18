**#How the project idea came about:**</br>
I have been unemployed and employed throughtout recent years. I have my standard C.V but most employers want a cover letter customisted for that particular job. Having over 40+ jobs a week I save and apply to, I thought I could automate this. Come last year when I taught myself how to code in Python, I learnt the skills required to automate this particular problem I was facing. Saving me time and improving my effeincy in applying. I created this script/program to scrap SEEK.co.nz and Seek.co.au which are the job boards I use to find jobs. I created the program so that based on the catgeory of the job it would alter my existing cover letter templates for those industires while changing the advertiser and the job title.</br>

You still have to manually apply for jobs either through Seek or through the advertisers own careers page. However, what this program basically does is, automate customizing cover letters for specific jobs you have saved and want to apply for.</br>

**#Problems I faced and or how I overcame them:**</br>
1.The main problem I faced was once I learnt how to obtain the CSS Selectors, Seek decided to change how they structered thier web pages and how the customer interacts with it. I tried a few times and was succesfull however, sometimes was not and in those instances used the code from the webpages and inserted into ChatGPT to find the CSS Selectors I was looking for as they started to bury the functions deeply into the code. So if in the future you run this code and it does not work, try and find the CSS Selector's via ChatGPT and that should solve the problem most of the time.</br>

2. Finding the delete button. ChatGPT can also help with teaching how to find code when it is buried, e.g., before the site revision, the delete button was in each jobs box'd section. After the revision the delete button was turned into a popup which you had to press 2 buttons to get to. As easy and dumb as this sounds I had to automate this because Seek decided to remove the funciallity of hiding expired jobs, so say for exmaple you had over 100+ jobs saved and in no paritulcar order, they expired at an interval not known to you. You then get a saved job list that has jobs you can apply for and others that you can't and when you run the automation script, you run into errors like I did and or re-program the script to skip expired jobs but then you have a list of expired jobs in you're saved jobs list. Insert (Seek Expired Ejecto) I have added the file to this repoistery which deletes all jobs in you're saved job list. I would recomend only running it after you have applied for the jobs in youre list. This give you a) Incentive to apply for all the jobs you saved and b) Can give you mini project to script/code to skip all active jobs and delete just expired jobs. You could even merge this into one document like I should of have done but my main goal was to get something funcationing that I could use and show. 

**#Improvments that can be made:</br>**
Have the program automatically run at set schedules, however I find it's easier to just run it once you have saved all the jobs you're looking to apply for and then run the script.</br>

**#If you want to use this program:</br>**
You just have to have Python installed and inserted into you're system variables. Also need to know how to use the IDLE interface and or how to run code once you have written it. I would advise learning Python by watching Automate the Boring Stuff on Udemy. Which is how I learnt how to create this and the creator gives out a free code every month on Reddit which is for a lifetime :D. 

