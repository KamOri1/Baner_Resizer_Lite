class ScalingParametersCheck:
    def __init__(self, width_height: int | None = None, b_mb: str = 'on'):
        self.width_height: int | None = width_height
        self.b_mb: str = b_mb

    @property
    def _size_calculated(self) -> list:
        if self.width_height == 650:
            return [650, 490]
        else:
            return [610, 242]

    @property
    def _banner_format_calculated(self) -> str:
        if self.b_mb == 'on':
            if self.width_height == 650:
                return '_mb'
            else:
                return 'b'
        else:
            return ''

    @property
    def image_params(self) -> dict:
        return {
            'width': self._size_calculated[0],
            'height': self._size_calculated[1],
            'b_mb': self._banner_format_calculated
        }
