const bells = new Audio('bell.mp3'); 
const startBtn = document.querySelector('.btn-start'); 
const pauseBtn = document.querySelector('.btn-pause'); 
const resetBtn = document.querySelector('.btn-reset'); 
const session = document.querySelector('.minutes'); 
const minuteDiv = document.querySelector('.minutes');
const secondDiv = document.querySelector('.seconds');
let myInterval; 
let state = true;
let paused = false;
let totalSeconds;

// How much minutes and seconds left on display
const updateDisplay = () => {
    let minutesLeft = Math.floor(totalSeconds/60);
    let secondsLeft = totalSeconds % 60;
    
    if(secondsLeft < 10) {
        secondDiv.textContent = '0' + secondsLeft;
    } else {
        secondDiv.textContent = secondsLeft;
    }
    minuteDiv.textContent = `${minutesLeft}`;
}

// Checking if there are any seconds left and subtracting seconds
const updateSeconds = () => {
    totalSeconds--;
    updateDisplay();

    if(totalSeconds <= 0) {
        bells.play();
        clearInterval(myInterval);
        state = true;
        paused = false;
    }
}

// Starting app
const appTimer = () => {
    const sessionAmount = Number.parseInt(session.textContent);

    if(state) {
        state = false;
        paused = false;
        totalSeconds = sessionAmount * 60;
        myInterval = setInterval(updateSeconds, 1000);
    } else {
        alert('Session has already started.');
    }
}

// Pausing app
const appPause = () => {
    if (!state) {
        paused = !paused;
        
        if (paused) {
            clearInterval(myInterval);
        } else {
            myInterval = setInterval(updateSeconds, 1000);
        }
    }
}

// Reseting app
const appReset = () => {
    clearInterval(myInterval);
    state = true;
    paused = false;
    const sessionAmount = 25;
    totalSeconds = sessionAmount * 60;
    updateDisplay();
}

startBtn.addEventListener('click', appTimer);
pauseBtn.addEventListener('click', appPause);
resetBtn.addEventListener('click', appReset);