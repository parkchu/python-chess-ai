const APIURL = "https://glorious-fortnight-5xxrx7jrp7h6rg-8000.app.github.dev"
var currentPoint = null

function init() {
    board = document.querySelector("#boards tbody");
    board.addEventListener("click", clickBoard);
}

function clickBoard(event) {
    event.preventDefault();
    targetPoint = event.target.parentElement;
    console.log(event.target.getAttribute("data-team"))
    if (currentPoint == null) {
        if (event.target.innerText != "") {
            currentPoint = targetPoint;
        } else {
            currentPoint = null;
        }
        return ;
    }
    if (currentPoint == targetPoint) {
        currentPoint = null;
        removeClicked(event.target);
        return ;
    }
    currentPiece = currentPoint.children[0];
    if (currentPiece.getAttribute("data-team") === event.target.getAttribute("data-team")) {
        currentPoint = targetPoint;
        return ;
    }
    if (currentPoint != null) {
        requestMove(currentPoint.id, targetPoint.id);
        targetPoint.innerHTML = currentPoint.innerHTML;
        currentPoint.innerHTML = makeEmptyPiece();
        currentPoint = null;
        removeClicked(event.target);
        return ;
    }
}

function requestMove(currentPosition, targetPosition) {
    fetch(`${APIURL}/api/move`, {
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

function removeClicked(elementA) {
    elementA.removeAttribute("href");
    elementA.setAttribute("href", "");
}

init();
