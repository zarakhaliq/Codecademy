let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

function generateTarget(){
    return Math.floor(Math.random()*9);
    }
    
    
    function compareGuesses(currentHumanGuess, computerGuess, target){
        //return true if human player wins and false if human player loses and if its a tie then ruturn true if human player wins
    
        let humanDifference=Math.abs(currentHumanGuess-target);
        let computerDifference=Math.abs(computerGuess-target);
        
        let humanWin=humanDifference<=computerDifference;
    
        if(humanWin){
            return true;
        }else{
            return false;
        }
    }
    
    function updateScore(winner){
        if(winner=='human'){
            humanScore++;
        }
        if(winner=='computer'){
            computerScore++;
        }
    }
    function advanceRound(){
      currentRoundNumber++;
    }