from finalchanges import *


def instState():

    setBackgroundImage("textures/instBoard.PNG")
    instButtons = makeSprite("textures/instBoard.PNG")
    instQuiz = makeSprite("textures/instButtons.png")


def start():

    moveSprite(player, 88, 110)
    showSprite(virus0)
    showSprite(virus1)
    showSprite(virus2)
    showSprite(virus3)
    showSprite(virus4)
    showSprite(virus5)
    showSprite(virus6)
    showSprite(virus7)
    showSprite(virus8)
    showSprite(virus9)
    showSprite(virus10)
    showSprite(virus11)
    showSprite(virus12)
    moveSprite(virus0, xArrayVirus[0], yArrayVirus[0])
    moveSprite(virus1, xArrayVirus[2], yArrayVirus[2])
    moveSprite(virus2, xArrayVirus[3], yArrayVirus[3])
    moveSprite(virus3, xArrayVirus[4], yArrayVirus[4])
    moveSprite(virus4, xArrayVirus[7], yArrayVirus[7])
    moveSprite(virus5, xArrayVirus[8], yArrayVirus[8])
    moveSprite(virus6, xArrayVirus[9], yArrayVirus[9])
    moveSprite(virus7, xArrayVirus[10], yArrayVirus[10])
    moveSprite(virus8, xArrayVirus[12], yArrayVirus[12])
    moveSprite(virus9, xArrayVirus[13], yArrayVirus[13])
    moveSprite(virus10, xArrayVirus[14], yArrayVirus[14])
    moveSprite(virus11, xArrayVirus[17], yArrayVirus[17])
    moveSprite(virus12, xArrayVirus[19], yArrayVirus[19])
    moveSprite(soap0, xArraySoap[0], yArraySoap[0])
    moveSprite(soap1, xArraySoap[2], yArraySoap[2])
    moveSprite(soap2, xArraySoap[5], yArraySoap[5])
    moveSprite(soap3, xArraySoap[7], yArraySoap[7])
    moveSprite(soap4, xArraySoap[6], yArraySoap[6])
    moveSprite(soap5, xArraySoap[12], yArraySoap[12])
    moveSprite(soap6, xArraySoap[16], yArraySoap[16])
    moveSprite(soap7, xArraySoap[17], yArraySoap[17])
    moveSprite(soap8, xArraySoap[19], yArraySoap[19])
    moveSprite(soap9, xArraySoap[21], yArraySoap[21])
    showSprite(soap0)
    showSprite(soap1)
    showSprite(soap3)
    showSprite(soap4)
    showSprite(soap5)
    showSprite(soap6)
    showSprite(soap7)
    showSprite(soap8)
    showSprite(soap9)
    transformSprite(antidote, 0, 0.5)
    showSprite(antidote)
    moveSprite(antidote, 1620, 150)


def hide1():
    hideLabel(playPress)
    hideLabel(logo)
    hideLabel(creds)
    hideLabel(dev)
    setBackgroundImage("textures/baord.png")
    showSprite(player)

    def quizFunc1():

        buttons = makeSprite("textures/buttons_nodisp.png")
        pause(500)

        moveLabel(questionLabel, questionsX[quizDispInd], questionsY[quizDispInd])
        moveLabel(multiAns1Label, ans1X[quizDispInd], ans1Y[quizDispInd])
        moveLabel(multiAns2Label, ans2X[quizDispInd], ans2Y[quizDispInd])
        moveLabel(multiAns3Label, ans3X[quizDispInd], ans3Y[quizDispInd])
        moveLabel(multiAns4Label, ans4X[quizDispInd], ans4Y[quizDispInd])
        pause(200)
        showSprite(buttons)
        showLabel(questionLabel)
        showSprite(multiAns1Label)
        showSprite(multiAns2Label)
        showSprite(multiAns3Label)
        showSprite(multiAns4Label)
        changeLabel(questionLabel, questions[quizDispInd])
        changeLabel(multiAns1Label, multiAns1[quizDispInd])
        changeLabel(multiAns2Label, multiAns2[quizDispInd])
        changeLabel(multiAns3Label, multiAns3[quizDispInd])
        changeLabel(multiAns4Label, multiAns4[quizDispInd])


def back():

    hideAll()
    hideLabel(questionLabel)
    showSprite(virus0)
    showSprite(virus1)
    showSprite(virus2)
    showSprite(virus3)
    showSprite(virus4)
    showSprite(virus5)
    showSprite(virus6)
    showSprite(virus7)
    showSprite(virus8)
    showSprite(virus9)
    showSprite(virus10)
    showSprite(virus11)
    showSprite(virus12)
    showSprite(soap0)
    showSprite(soap1)
    showSprite(soap3)
    showSprite(soap4)
    showSprite(soap5)
    showSprite(soap6)
    showSprite(soap7)
    showSprite(soap8)
    showSprite(soap9)
    showSprite(antidote)

    showSprite(player)
    setBackgroundImage("textures/baord.png")
