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
    if (getPieceAttribute(targetPoint, "data-movable")) {
        return movePiece;
    }
    deleteMovablePoints();
    return setCurrentPoint;
}

function removeClicked(targetPoint) {
    elementA = targetPoint.children[0];
    elementA.removeAttribute("href");
    elementA.setAttribute("href", "");
    currentPoint = null;
    deleteMovablePoints();
}

function isSameTeam(currentPoint, targetPoint) {
    return getPieceAttribute(currentPoint, "data-team") === getPieceAttribute(targetPoint, "data-team");
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
        showMovablePoint(position);
    });
}

function showMovablePoint(position) {
    point = board.querySelector(`#${position}`);
    if (isEmptyPiece(point)) {
        point.innerHTML = '<a href="" data-movable="true">&#9900;</a>';
    } else {
        piece = point.children[0]
        piece.classList.add("highlight");
        piece.setAttribute("data-movable", "true");
    }
}

function isEmptyPiece(point) {
    return getPieceAttribute(point, "data-team") == null;
}

function getPieceAttribute(point, attribute) {
    return point.children[0].getAttribute(attribute);
}

function deleteMovablePoints() {
    pieces = board.querySelectorAll("a[data-movable=true], a.highlight");
    Array.from(pieces).forEach(piece => {
        deleteMovablePoint(piece);
    });
}

function deleteMovablePoint(piece) {
    point = piece.parentElement;
    if (isEmptyPiece(point)) {
        point.innerHTML = makeEmptyPiece();
    } else {
        piece.classList.remove("highlight");
        piece.removeAttribute("data-movable");
    }
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
