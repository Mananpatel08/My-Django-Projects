const form = document.getElementById("liftForm");
const elevator = document.querySelector(".elevator");
const floors = document.querySelectorAll(".elevator div");
let currentFloor = null;
let targetFloor = null;
let passengerCount = null;

function playSound(soundId) {
    const sound = document.getElementById(soundId);
    sound.play(); // Play the sound
}

form.addEventListener("submit", function(event) {
    event.preventDefault(); 

    // get current floor, target floor & passenger count from the form
    currentFloor = parseInt(document.querySelector('[name="current_floor"]').value);
    targetFloor = parseInt(document.querySelector('[name="target_floor"]').value);
    passengerCount = parseInt(document.querySelector('[name="passenger_count"]').value);

    
    // check if current floor and target floor are the same
    if (currentFloor === targetFloor) {
        alert("You are already on your target floor!");
        return;  // stop the function if the floors are the same
    }
    // Check if passenger count exceeds 10
    if (passengerCount > 10) {
        alert("Passenger Capacity is 10 Persons!");
        return;  // stop the function if passenger count is too high
    }
    moveLift(currentFloor, targetFloor);

});

// from lift_position -> current_floor
function moveLift(currentFloor, targetFloor) {

    let greenDiv = document.querySelector('.lift-position'); //current lift position
    let elevatorPosition = parseInt(greenDiv.textContent.trim(), 10); //convert into number
    let current = elevatorPosition; 

    // if lift is allready at user's current floor
    if (current === currentFloor) {
        showMessage(`Lift is at Floor ${currentFloor}`);
        playSound('arrivedSound');
        setTimeout(() => {
            clearMessage();
            moveToTargetFloor(currentFloor, targetFloor); // Proceed to target floor

        }, 3000);
        return; 
    }

    let stepToCurrent = elevatorPosition < currentFloor ? 1 : -1;  //direction using + , -
    const interval1 = setInterval(() => {
        current += stepToCurrent; // Move one step
        updateFloorPosition(current); // Update floor visually

        if (current === currentFloor) {
            clearInterval(interval1); // Stop when it reaches the user's entered current floor

            playSound('arrivedSound');
            //show message when arrived
            showMessage(`Lift has arrived at Floor ${currentFloor}`);
            setTimeout(() => {
                clearMessage();
                moveToTargetFloor(currentFloor, targetFloor); 
            }, 3000 );
            // Now, move to the target floor
        }
    }, 1000);
}

// from current_floor -> target_floor
function moveToTargetFloor(currentFloor, targetFloor) {
    let stepToTarget = currentFloor < targetFloor ? 1 : -1;
    let current = currentFloor;

    const interval2 = setInterval(() => {
        current += stepToTarget; // Move one step
        updateFloorPosition(current); // Update floor visually

        if (current === targetFloor) {
            clearInterval(interval2); // Stop when it reaches the target floor
            
            playSound('arrivedSound');
            //show message when arrived
            showMessage(`Lift has arrived at Floor ${targetFloor}`);
            setTimeout(() => {
                clearMessage();
                submitForm()
            }, 3000 );
        }
    }, 1000);
}

// track lift
function updateFloorPosition(floor) {
    // Reset all floor highlights
    floors.forEach(floorElement => {
        floorElement.classList.remove("lift-position");
        floorElement.style.backgroundColor = ""; // Reset background color
    });

    // Highlight the current floor
    const targetFloorElement = document.querySelector(`.floor${floor}`);
    if (targetFloorElement) {
        targetFloorElement.classList.add("lift-position");
        targetFloorElement.style.backgroundColor = "green"; // highlight in green
    }
}

//for display message
function showMessage(message) {
    const messageDiv = document.createElement("div");
    messageDiv.id = "lift-message";
    messageDiv.textContent = message;
    messageDiv.style.position = "absolute";
    messageDiv.style.top = "10px";
    messageDiv.style.left = "50%";
    messageDiv.style.transform = "translateX(-50%)";
    messageDiv.style.padding = "13px";
    messageDiv.style.backgroundColor = "rgb(255, 255, 255)";
    messageDiv.style.color = "#000000";
    messageDiv.style.fontSize = '13px';
    messageDiv.style.fontFamily = 'Verdana, Geneva, Tahoma, sans-serif';
    messageDiv.style.boxShadow = 'rgba(0, 0, 0, 0.35) 0px 5px 15px';
    document.body.appendChild(messageDiv);
}

//for clear message
function clearMessage() {
    const messageDiv = document.getElementById("lift-message");
    if (messageDiv) {
        messageDiv.remove();
    }
}

function submitForm() {
    form.submit(); // submit form after all animation done
}