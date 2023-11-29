class IllegalMovementException(Exception):
    def __init__(self) -> None:
        super().__init__("움직일 수 없는 위치 입니다.")


class PromotionPositionException(Exception):
    def __init__(self) -> None:
        super().__init__("승급할 수 없는 위치입니다.")


class PromotionSourceException(Exception):
    def __init__(self) -> None:
        super().__init__("승급할 수 없는 기물입니다.")


class PromotionTargetException(Exception):
    def __init__(self) -> None:
        super().__init__("해당 기물로는 승급할 수 없습니다.")
