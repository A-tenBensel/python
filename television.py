class Television:
    """
    A class representing details for a tv object.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        """
        Method to set defult values of tv object.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    def power(self) -> None:
        """
        Method to turn on or off the tv.
        """
        self.__status = not self.__status
    def mute(self) -> None:
        """
        Method to mute or unmute the tv.
        """
        if self.__status:
            self.__muted = not self.__muted
    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)
    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)
    def volume_up(self) -> None:
        """
        Method to increase the tv volume.
        """
        if self.__status:
            self.__muted = False
            self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)
    def volume_down(self) -> None:
        """
        Method to decrease the tv volume.
        """
        if self.__status:
            self.__muted = False
            self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)
    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume * (not self.__muted)}."