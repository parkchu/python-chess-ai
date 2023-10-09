const APIURL = "https://glorious-fortnight-5xxrx7jrp7h6rg-8000.app.github.dev"
var currentPoint = null

function init() {
    board = document.querySelector("#boards tbody");
    board.addEventListener("click", clickBoard);
}

function clickBoard(event) {
    event.preventDefault();
    targetPoint = event.target.parentElement;
    getFunction(targetPoint)(targetPoint)
}

function getFunction(targetPoint) {
    if (currentPoint == targetPoint) {
        return removeClicked;
    }
    if (currentPoint == null || isSameTeam(currentPoint, targetPoint)) {
        return setCurrentPoint;
    }
    return movePiece;
}

function isSameTeam(currentPoint, targetPoint) {
    return currentPoint.children[0].getAttribute("data-team") === targetPoint.children[0].getAttribute("data-team");
}

function setCurrentPoint(targetPoint) {
    currentPoint = getNonemptyPoint(targetPoint);
}

function getNonemptyPoint(targetPoint) {
    targetPiece = targetPoint.children[0];
    if (targetPiece.innerText == "") {
        return null;
    }
    return targetPoint;
}

function removeClicked(targetPoint) {
    elementA = targetPoint.children[0];
    elementA.removeAttribute("href");
    elementA.setAttribute("href", "");
    currentPoint = null;
}

function movePiece(targetPoint) {
    requestMove(currentPoint.id, targetPoint.id);
    targetPoint.innerHTML = currentPoint.innerHTML;
    currentPoint.innerHTML = makeEmptyPiece();
    removeClicked(targetPoint);
}

function requestMove(currentPosition, targetPosition) {
    fetch(`${APIURL}/api/chess/move`, {
        method: "POST", 
        headers: { 
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
        currentPosition: currentPosition,
        targetPosition: targetPosition,
        }),
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}

function makeEmptyPiece() {
    return '<a href=""></a>'
}

init();
