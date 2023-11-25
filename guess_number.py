import logging
from random import randint

# configure logger
logging.basicConfig(filename='msg.log', format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# creating game
def play(N, k=1):
    logger.info("The game was started.")
    random_num = randint(1, N)  # generate a hidden number
    logger.info(f"Generated hidden number is {random_num}.")
    for i in range(k):  # player have k tries to guess the number
        num = int(input("Your guess about the hidden number: "))
        logger.info(f"Player's guess is {num}.")
        # check if player's guess is the hidden number
        if num == random_num:  # player won, end the game
            print(f"Congratulations! {num} is the hidden number!")
            logger.info("Player won.")
            break
        else:
            if i+1 != k:  # tips for next guess
                if num > random_num:
                    print(f"No, {num} is greater than the hidden number. Try again!")
                    logger.info(f"Player have {k-i-1} more tries.")
                else:
                    print(f"No, {num} is lesser than the hidden number. Try again!")
                    logger.info(f"Player have {k-i-1} more tries.")
            else:  # player lost, end the game
                print(f"You lost! You have no more tries. {random_num} was the hidden number.")
                logger.info("Player lost.")
    print("Game over.")
    logger.info("Game over.")

logger.info("Start the programm.")

# input for upper limit of hidden number
while True:
    N = int(input("Write an upper limit for a hidden number: "))
    if N <= 1:  # check input 
        print("The upper limit must be greater than 1.")
        logger.error("Expected number greater than 1 for the upper limit.")
        continue
    else:
        logger.info(f"Upper limit for the hidden number is {N}.")
        break

#input for number of tries
while True:
    k = int(input("Write a number of tries to guess the number: "))
    if k < 1:  # check input
        print("The number of tries must be equal or greater than 1.")
        logger.error("Expected a number equal or greater than 1 for the number of tries.")
        continue
    else:
        logger.info(f"Number of tries is {k}.")
        break

play(N, k)
logger.info("End the programm.")