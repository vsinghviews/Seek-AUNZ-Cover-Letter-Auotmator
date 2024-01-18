#Fill out later - inserted template to use. 

How the project idea came about

The idea came about as I was using a Firefox extesnion called oneTab which collates all you're tabs from specific windows, tabs themselves and or the like in one place like a directory. While I was learning Python via ATBS the extension crashed when Firefox closed when restarting my PC. Which I would do on the odd occasion when it will run slow, after which it will re-open all my windows and tabs. However, on this occasion that was not the case and I lost all my saved tabs and the orders they were set in. Through Various Googlefu and the like I tried the measures I could find but could not restore my lost data and if I could the files I needed were replaced with new ones and my PC backup was quite old. I even reached out to the development team and they could not help much. I think I should suggest they create this as a function with thier extension as well as I came across various people whom this had also happened to.

Now after finishing ATBS I came to learn how to use Pyautogui and thought I could use this to create my own backup's by programing (If I could even call it that) or create a script, which when run will export my saved tabs in a .txt format. This would be useful because, I could now store, save, share my tabs as well as re-upload them into oneTab if the same thing happened again.
Problems I faced and how I overcame them

    Image not being found using either Snipping Tool, Windows Screenshot or Pyautogui ScreenShot

    Googled my way around and found that I could not use the Snipping Tool and then crop the image as it distorts the pixels or the like. Making it very difficult for Pyautogui to find an exact or similar match. So found that I can use Windows Screenshot (Windows button + Shift + S) to crop the area I need Pyautogui to find and this worked wonderfully. Also found that I can use an argument called confidence with a range of 0 to 1, 1 being an exact match that would help filter other content on my webpage that looks the simliar to the image I am trying to find. Same thing applies to Grayscale, which I could enable being True or False to help aid in finding my image. However did not need to use this as my images were in color.

    The oneTab dropdown buttons could not be found on repeated occasions

    I decided to stick with their mouse locations on my screen as I had them in the begining.

    oneTab would open but couldn't find or click on the export link buton

    So oneTab would open but either freeze or misclick a different section. I then ran the program through Pythons IDLE and ran it step by step and that solved my issue, which lead me to belive the program needed to pause before it re-attempted the next command. I then Googled how I could implment a pause state in my program which lead me to including the time module. After which my program runs perfectly.

    Saving the contents to notepad

    I manage to get Python to open notepad.exe and Pyautogui to paste the contents into notepad and after that my brain just frooze as to what to do next. I then recalled I could just get Pyautogui to find images of the save button and repeat the saving procedure using images but found that to be tedious and or stupid if I could make it simplier. So I asked my question online and got conflicting answers and or very aggresive help, which was not fun being a new guy and trying to learn. So I took a break and watched some Youtube videos. One of the suggested videos was how to learn programming using AI, watched the video and was like let's try this thing out and asked it how I could automate the saving file section where it would not replace the old file. *I found the solutions online but didin't know how to compile it all together. So the only solution I got from AI was the counter funtion, the filename section under the while statment and the with statment.

    Facing errors running the program

    I kept facing an error at the end and could not figure out why. Being exhasuted researching all these things and being stressed and just eager to complete my first project that I entered my error into AI LOL! and BOOM! it gave me my answer and explained that due to how Windows default encoding structure works, not all content is being saved and that I need to use the encoding="utf-8" encoding to capture the emoji's that oneTab saves into the tab's name. As I use another extenstion to hang tabs not being used which uses Emoji's to signal that a tab is in a paused state.

Improvments that can be made

1. Having everything done by finding images alone, instead of using mouse locations but I encountered problems doing so. May try again to solve why this issue is occuring or images not being found. Fixed this by tinkering with the pixel parameters to ensure the confidence level matches that of the image found.

    As I am using a dual monitor setup, figure out why Pyautogui priortizies one monitor over the other and if it finds the first prompt image on the second monitor to run the program as normal. This may be a simple fix as just finding the location of my mouse on the second monitor and implmenting "try" and or "else" statements.

    Have the program automatically run at set schedules, by the time you are reading this I may have already implmented this on my own system using Windows Tasks Schedular.

If you want to use this program

    Use Pyautogui in CMD and find the location of you're mouse for the "#Opening onetab user interface" sections.
    Take you're own screenshots using Windows, reason being display monitor, make, model and size affects pixel resolution.
    Rename the file to be saved to whatever you want it to be under "#Exporting saved tabs to notepad to be saved as file".

