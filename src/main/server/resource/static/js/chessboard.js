const APIURL = ".";
const board = document.querySelector("#boards tbody");
const turnLabel = document.querySelector("h1.turn");
const PIECE_ICONS = {
    "white": {
        "King": "&#9812;",
        "Queen": "&#9813;",
        "Rook": "&#9814;",
        "Bishop": "&#9815;",
        "Knight": "&#9816;",
        "Pawn": "&#9817;"
    },
    "black": {
        "King": "&#9818;",
        "Queen": "&#9819;",
        "Rook": "&#9820;",
        "Bishop": "&#9821;",
        "Knight": "&#9822;",
        "Pawn": "&#9823;"
    }
}
const PROMOTION_PIECE_TYPES = ["Queen", "Rook", "Bishop", "Knight"]
const TURN_MESSAGE = {
    "white": "백이 둘 차례",
    "black": "흑이 둘 차례"
}
const undoBtns = document.querySelectorAll(".undo-btn");
var currentPoint
var turn

function init() {
    currentPoint = null;
    turn = "white"
    board.addEventListener("click", clickBoard);
    Array.from(undoBtns).forEach(btn => {
        btn.addEventListener("click", requestUndo);
    });
}

function clickBoard(event) {
    event.preventDefault();
    targetPoint = event.target.parentElement;
    getFunction(targetPoint)(targetPoint);
}

function getFunction(targetPoint) {
    if (currentPoint == targetPoint) {
        return removeClicked;
    }
    if (currentPoint == null || isSameTeam(currentPoint, targetPoint)) {
        return setCurrentPoint;
    }
    if (getPieceAttribute(targetPoint, "data-movable") && isTurn(currentPoint)) {
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
    .then((data) => showMovablePoints(data.positions));
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
        piece = point.children[0];
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

function isTurn(currentPoint) {
    return getPieceAttribute(currentPoint, "data-team") === turn
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

async function movePiece(targetPoint) {
    data = await requestMove(currentPoint.id, targetPoint.id);
    move(currentPoint, targetPoint)
    processAfterMove(data)
    changeTurn();
    requestMovePositionByAi(turn)
}

async function movePieceByAi(currentPosition, targetPosition) {
    currentPoint = board.querySelector(`#${currentPosition}`);
    targetPoint = board.querySelector(`#${targetPosition}`);
    data = await requestMove(currentPoint.id, targetPoint.id);
    move(currentPoint, targetPoint)
    processAfterMove(data)
    changeTurn();
}

function move(currentPoint, targetPoint) {
    targetPoint.innerHTML = currentPoint.innerHTML;
    currentPoint.innerHTML = makeEmptyPiece();
    removeClicked(targetPoint);
}

async function requestMove(currentPosition, targetPosition) {
    url = `${APIURL}/api/chess/move`;
    method = "POST";
    body = JSON.stringify({
        currentPosition: currentPosition,
        targetPosition: targetPosition,
    });
    return request(url, method, body)
    .then((response) => response.json())
    .then((data) => data);
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

function requestMovePositionByAi(team) {
    url = `${APIURL}/api/chess/move-ai/${team}`;
    method = "GET";
    request(url, method)
    .then((response) => response.json())
    .then((data) => movePieceByAi(data.currentPosition, data.targetPosition));
}

function processAfterMove(response) {
    requestCheck("white");
    requestCheck("black");
    promote(response);
    castling(response);
}

function requestCheck(team) {
    url = `${APIURL}/api/chess/check/${team}`;
    method = "GET";
    request(url, method)
    .then((response) => response.json())
    .then((data) => check(data));
}

function check(response) {
    piece = board.querySelector(`#${response.kingPosition}`).children[0];
    message = "";
    if (response.isCheck) {
        piece.classList.add("check");
        message = `${turn} 팀이 체크메이트 당했습니다!`
    } else {
        piece.classList.remove("check")
        message = "스테일메이트 입니다!"
    }
    checkmate(response, message)
}

function checkmate(response, message) {
    if (response.isCheckmate) {
        alert(message);
    }
}

function promote(response) {
    if (response.isPromotion) {
        position = response.targetPosition;
        pieceType = getPromotionPieceType();
        requestPromote(position, pieceType)
        requestCheck(turn);
    }
}

function getPromotionPieceType() {
    pieceType = prompt(`승급 시킬 기물을 입력해주세요 (${PROMOTION_PIECE_TYPES})`, "Queen");
    if (PROMOTION_PIECE_TYPES.includes(pieceType)) {
        return pieceType
    }
    alert(`${pieceType} 이란 기물은 없습니다.\n${PROMOTION_PIECE_TYPES} 중에서 입력해주세요.`)
    return getPromotionPieceType()
}

function requestPromote(position, pieceType) {
    url = `${APIURL}/api/chess/promote`;
    method = "POST";
    body = JSON.stringify({
        position: position,
        pieceType: pieceType,
    });
    request(url, method, body)
    .then((response) => response.json())
    .then((data) => changePiece(data));
}

function changePiece(response) {
    position = response.position;
    piece = board.querySelector(`#${position}`).children[0];
    team = "white";
    if (position[1] == "1") {
        team = "black";
    }
    pieceType = response.pieceType;
    piece.innerHTML = PIECE_ICONS[team][pieceType];
}

function castling(response) {
    if (response.isCastling) {
        position = response.targetPosition;
        positions = getCastlingPositions(position);
        rookPoint = board.querySelector(`#${positions.rookPosition}`);
        movePoint = board.querySelector(`#${positions.movePosition}`);
        move(rookPoint, movePoint);
        requestCheck(turn);
    }
}

function getCastlingPositions(position) {
    file = position[0];
    rank = position[1];
    rookFile = "a";
    moveFile = "d";
    if (file == "g") {
        rookFile = "h";
        moveFile = "f";
    }
    positions = {
        rookPosition: rookFile + rank,
        movePosition: moveFile + rank
    }
    return positions
}

function makeEmptyPiece() {
    return '<a href=""></a>';
}

function changeTurn(team=getEnemy(turn)) {
    turn = team
    turnLabel.innerHTML = `<span class="label label-default turn">${TURN_MESSAGE[team]}</span>`
}

function getEnemy(team) {
    if (team === "white") {
        return "black"
    }
    return "white" 
}

function requestUndo(event) {
    url = `${APIURL}/api/chess/undo`;
    method = "POST";
    team = event.target.getAttribute("data-team");
    body = JSON.stringify({
        team: team
    });
    request(url, method, body)
    .then((response) => response.json())
    .then((data) => undo(data));
}

function undo(response) {
    notations = response.notations;
    notations.forEach(notation => {
        currentPiece = makePiece(notation.currentPiece);
        targetPiece = makePiece(notation.targetPiece);
        setPiece(notation.currentPosition, currentPiece);
        setPiece(notation.targetPosition, targetPiece);
    })
    requestCheck("white");
    requestCheck("black");
    changeTurn(response.team);
}

function makePiece(piece) {
    if (piece.pieceType == "NonePiece") {
        return makeEmptyPiece()
    }
    return `<a href="" data-team="${piece.team}">${PIECE_ICONS[piece.team][piece.pieceType]}</a>`
}

function setPiece(position, piece) {
    point = board.querySelector(`#${position}`);
    point.innerHTML = piece;
}

init();
