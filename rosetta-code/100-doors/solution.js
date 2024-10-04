function getFinalOpenedDoors(numDoors) {
    let doorsState = new Array(numDoors).fill(false);
    for (let every = 1; every <= doorsState.length; every++) {
        for (let indexToOpen = every - 1; indexToOpen < doorsState.length; indexToOpen += every) {
            doorsState[indexToOpen] = !doorsState[indexToOpen];
        }
    }
    let openedDoors = [];
    for (let [index, doorState] of doorsState.entries()) {
        if (doorState) {
            openedDoors.push(index + 1);
        }
    }
    return openedDoors;
}

for (let i = 0; i < 101; i++) {
    console.log(`${i}: ${JSON.stringify(getFinalOpenedDoors(i))}`);
}
