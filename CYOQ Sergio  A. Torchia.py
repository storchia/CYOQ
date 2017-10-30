song_easy = "***1*** there is no heaven, It is ***2*** if you try, No hell below us, Above us only sky, ***1*** all the people living for today, ***1*** there is no ***3***, It is not hard to do, Nothing to kill or die for, And no religion too, ***1*** all the people living life in ***4***."
easy_ans = ['imagine', 'easy', 'heaven', 'peace']
song_med = "It s been a ***1*** day's night, and I ve been working like a ***2***, It's been a ***1*** day's night, I should be ***3*** like a log, But when I get ***4*** to you I find the things that you do, Will make me feel alright."
med_ans = ['hard', 'dog', 'sleeping', 'home']
song_hard = "He wear no ***1***, he's got toe-jam football, He got ***2*** finger, he shoot Coca-Cola, He say, I ***3*** you, you ***3*** me, One thing I can tell you is you got to be ***4***"
hard_ans = ['shoeshine', 'monkey', 'know', 'free']
blanks = ['***1***', '***2***', '***3***', '***4***']    
attempt = 1

def level():
    """
    Function will welcome user and request level. Based on the answer will determine which song will use.
    """
    print 'Welcome to The Beatles fill in the blanks game!'
    print 'Please select Level? (Easy / Medium / Hard)'
    global level_ans
    level_ans = raw_input().lower()
    if level_ans == 'easy':
        return song(level_ans)
    if level_ans == 'medium':
        return song(level_ans)
    if level_ans == 'hard':
        return song(level_ans)
    else :
        print 'Invalid option'
        print '\n'
        return level()
    
def song(level_ans):
    """
    Function will match level with song and blanks answers for the song.
    """
    global song
    global song_ans
    if level_ans == 'easy':
        song = song_easy
        song_ans = easy_ans
        return attempts()
    if level_ans == 'medium':
        song = song_med
        song_ans = med_ans
        return attempts()
    if level_ans == 'hard':
        song = song_hard
        song_ans = hard_ans
        return attempts()
    
def attempts():
    """
    Function will ask for attempts and store a variable with that information to be used later.
    """
    print 'How many attempts will you need?'
    global numberofatt
    numberofatt = raw_input()
    print '\n'
    try:
        float(numberofatt)
    except ValueError:
        print "Please enter a number for attempts"
        return attempts()
    numberofatt = int(numberofatt)
    if numberofatt <= 0 :
        print 'Please enter a positive number'
        return attempts()
    else :
        return quiz_intro(level_ans)
    
def quiz_intro(level):
    """
    Function will start game and print the attempts chosen.
    """
    global blank_pos
    blank_pos = 0
    print 'Please fill in the blanks, you have ' + str(numberofatt) + ' attempts' + '\n'
    print song + '\n'
    return quiz_cont(level)

def quiz_cont(level):
    """
    Function will evaluate answers. If correct will continue on the loop, if false will go to wrong function.
    """
    global blank_pos
    global attempt
    global user_ans
    while blank_pos < len(blanks):
        print 'Fill in blank ' + blanks[blank_pos]
        user_ans = raw_input().lower()
        print '\n'
        if user_ans != song_ans[blank_pos] :
            return wrong()
        if user_ans == song_ans[blank_pos]:
            global song
            song = song.replace(blanks[blank_pos], user_ans)
            print "Correct!" + '\n'
            print song + '\n'
            blank_pos = blank_pos + 1
    else :    
        return 'Great Job!'
    
def wrong():
    """
    Function will work with wrong answers until the answer is correct or will finish game if no more attempts available.
    """
    global user_ans
    global attempt
    global blank_pos
    if attempt == numberofatt :
            return 'Game Finished'
    while user_ans != song[blank_pos]:
        attempt = attempt + 1
        print 'Try Again' + '\n'
        print song + '\n'
        return quiz_cont(level)
    else:
        blank_pos = blank_pos + 1
        print "Correct!" + '\n'
        return quiz_cont(level)
    
print level()

