const APIURL = "https://glorious-fortnight-5xxrx7jrp7h6rg-8000.app.github.dev"
var currentPiece = null

function init() {
    board = document.querySelector("#boards tbody");
    board.addEventListener("click", clickBoard);
}

function clickBoard(event) {
    target = event.target
    if (currentPiece != null) {
        requestMove(currentPiece.id, target.parentElement.id)
        currentPieceIcon = currentPiece.children[0].innerText
        currentPiece.children[0].innerText = "";
        target.innerText = currentPieceIcon
        currentPiece = null;
        return ;
    }
    if (event.target.innerText != "") {
        currentPiece = event.target.parentElement
    } else {
        currentPiece = null
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

init();
