const APIURL = "https://effective-spork-wr76pqqq7vvw2g66r-8000.app.github.dev/"
const board = document.querySelector("#boards tbody");
var currentPoint = null

function init() {
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

function removeClicked(targetPoint) {
    elementA = targetPoint.children[0];
    elementA.removeAttribute("href");
    elementA.setAttribute("href", "");
    currentPoint = null;
    deleteMovablePoints();
}

function isSameTeam(currentPoint, targetPoint) {
    return currentPoint.children[0].getAttribute("data-team") === targetPoint.children[0].getAttribute("data-team");
}

function setCurrentPoint(targetPoint) {
    currentPoint = getNonemptyPoint(targetPoint);
    if (currentPoint != null) {
        requestGetMovablePositions();
    }
}

function getNonemptyPoint(targetPoint) {
    targetPiece = targetPoint.children[0];
    if (targetPiece.innerText == "") {
        return null;
    }
    return targetPoint;
}

function requestGetMovablePositions() {
    url = `${APIURL}/api/chess/movable-positions/${currentPoint.id}`;
    method = "GET";
    request(url, method)
    .then((response) => response.json())
    .then((data) => showMovablePoints(data));
}

function showMovablePoints(positions) {
    deleteMovablePoints();
    console.log(positions);
    positions.forEach(position => {
        point = board.querySelector(`#${position}`);
        point.innerHTML = '<a href="" data-movable="true">&#9900;</a>';
    });
}

function deleteMovablePoints() {
    points = board.querySelectorAll("a[data-movable='true']");
    Array.from(points).forEach(point => {
        point.innerHTML = makeEmptyPiece();
    });
}

function movePiece(targetPoint) {
    requestMove(currentPoint.id, targetPoint.id);
    targetPoint.innerHTML = currentPoint.innerHTML;
    currentPoint.innerHTML = makeEmptyPiece();
    removeClicked(targetPoint);
}

function requestMove(currentPosition, targetPosition) {
    url = `${APIURL}/api/chess/move`;
    method = "POST";
    body = JSON.stringify({
        currentPosition: currentPosition,
        targetPosition: targetPosition,
    });
    request(url, method, body)
    .then((response) => response.json())
    .then((data) => console.log(data));
}

function request(url, method, body = null) {
    return fetch(url, {
        method: method, 
        headers: { 
            "Content-Type": "application/json",
        },
        body: body
    });
}

function makeEmptyPiece() {
    return '<a href=""></a>';
}

init();
